from urllib3 import make_headers
import os

from finbourne_identity import Configuration, ApiClient

from .api_configuration_loader import ApiConfigurationLoader
from .refreshing_token import RefreshingToken


class ApiClientBuilder:
    """
    The ApiClientBuilder is responsible for building a finbourne_identity.ApiClient. This includes obtaining an access token from
    Okta or using the provided token.

    Any validation on the inputs required to build a finbourne_identity.ApiClient is the responsibility of this ApiClientBuilder.
    """

    @staticmethod
    def __check_required_fields(object_to_check, fields):
        """
        This function checks that the provided fields on an object are populated with values other than None

        :param object_to_check: The object to check the fields (a.k.a attributes) of
        :param list[str] fields: The fields to check on the object

        :return: None
        """
        # Check for fields which have a value of None
        missing_fields = [field for field in fields if getattr(object_to_check, field) is None]

        # Raise an error if any fields have a value of None
        if len(missing_fields) > 0:
            raise ValueError(
                f"The fields {str(missing_fields)} on the {object_to_check.__class__.__name__} are set to None, "
                f"please ensure that you have provided them directly, via a secrets file or environment "
                f"variables")

    @classmethod
    def __resolve_api_token(cls, token=None, configuration=None, id_provider_response_handler=None):

        """
        Description:
        This method uses a PAT (Personal Access Token) or secrets to return an API token.
        The method uses the following conditional logic in order of precedence to resolve an
        authentication path:

            1. Use PAT passed into the function
            2. Use secrets files passed into the function
            3. Use environment variables

        PAT are used in preference to supplied credentials.
        secrets files are used in preference to environment variables.

        :param str token: The pre-populated access token to use instead of asking Okta for a token
        :param ApiConfiguration configuration: configuration object containing secrets loaded from env vars
        :param typing.callable id_provider_response_handler: An optional function to handle the Okta response

        :return: str api_token
        """

        # If token is passed in by user, then use that token
        if token is not None:
            cls.__check_required_fields(configuration, ["api_url"])
            api_token = token

        # If there is a token provided use it
        elif configuration.access_token is not None:
            # Check that there is an api_url available
            cls.__check_required_fields(configuration, ["api_url"])
            api_token = configuration.access_token

        # Otherwise generate an access token from Okta and use a RefreshingToken going forward
        else:
            # Check that all the required fields for generating a token exist
            cls.__check_required_fields(configuration, [
                "api_url",
                "password",
                "username",
                "client_id",
                "client_secret",
                "token_url"])

            # Generate an access token
            api_token = RefreshingToken(
                api_configuration=configuration,
                id_provider_response_handler=id_provider_response_handler
            )

        return api_token

    @classmethod
    def build(cls, api_secrets_filename=None, id_provider_response_handler=None, api_configuration=None, token=None, correlation_id=None, tcp_keep_alive=False):
        """
        :param str api_secrets_filename: The full path to the JSON file containing the API credentials and optional proxy details
        :param typing.callable id_provider_response_handler: An optional function to handle the Okta response
        :param finbourne_identity.utilities.ApiConfiguration api_configuration: A pre-populated ApiConfiguration
        :param str token: The pre-populated access token to use instead of asking Okta for a token
        :param str correlation_id: Correlation id for all calls made from the returned ApiClient instance, added as a header to each request

        :return: finbourne_identity.ApiClient: The configured LUSID ApiClient
        """

        # Load the configuration
        configuration = ApiConfigurationLoader.load(api_secrets_filename)

        # If an api_configuration has been provided override the loaded configuration with any properties that it has
        if api_configuration is not None:
            for key, value in vars(api_configuration).items():
                if value is not None:
                    setattr(configuration, key, value)

        api_token = cls.__resolve_api_token(token, configuration, id_provider_response_handler)

        # Initialise the API client using the token so that it can be included in all future requests
        config = Configuration()
        config.access_token = api_token
        config.host = configuration.api_url

        # Set the certificate from the configuration
        config.ssl_ca_cert = configuration.certificate_filename

        # Set the proxy for LUSID if needed
        if configuration.proxy_config is not None:
            config.proxy = configuration.proxy_config.address
            if configuration.proxy_config.username is not None and configuration.proxy_config.password is not None:
                config.proxy_headers = make_headers(
                    proxy_basic_auth=f"{configuration.proxy_config.username}:{configuration.proxy_config.password}"
                )

        # Create and return the ApiClient
        api_client = ApiClient(configuration=config)

        # set the application name if specified
        if configuration.app_name is not None:
            api_client.set_default_header("X-LUSID-Application", configuration.app_name)

        # set a correlation id for all requests initiated with this ApiClient
        corr_id = correlation_id or os.getenv("FBN_CORRELATION_ID")
        if corr_id is not None:
            api_client.set_default_header("CorrelationId", corr_id)

        return api_client

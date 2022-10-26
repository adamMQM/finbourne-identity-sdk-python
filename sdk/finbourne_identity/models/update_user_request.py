# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1959
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_identity.configuration import Configuration


class UpdateUserRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'second_email_address': 'str',
        'login': 'str',
        'roles': 'list[RoleId]'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'second_email_address': 'secondEmailAddress',
        'login': 'login',
        'roles': 'roles'
    }

    required_map = {
        'first_name': 'required',
        'last_name': 'required',
        'email_address': 'required',
        'second_email_address': 'optional',
        'login': 'required',
        'roles': 'optional'
    }

    def __init__(self, first_name=None, last_name=None, email_address=None, second_email_address=None, login=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """UpdateUserRequest - a model defined in OpenAPI"
        
        :param first_name:  (required)
        :type first_name: str
        :param last_name:  (required)
        :type last_name: str
        :param email_address:  (required)
        :type email_address: str
        :param second_email_address: 
        :type second_email_address: str
        :param login:  The user's login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user's email address. (required)
        :type login: str
        :param roles: 
        :type roles: list[finbourne_identity.RoleId]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._second_email_address = None
        self._login = None
        self._roles = None
        self.discriminator = None

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.second_email_address = second_email_address
        self.login = login
        self.roles = roles

    @property
    def first_name(self):
        """Gets the first_name of this UpdateUserRequest.  # noqa: E501


        :return: The first_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateUserRequest.


        :param first_name: The first_name of this UpdateUserRequest.  # noqa: E501
        :type first_name: str
        """
        if self.local_vars_configuration.client_side_validation and first_name is None:  # noqa: E501
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) > 50):
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and len(first_name) < 1):
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                first_name is not None and not re.search(r'^[\s\S]*$', first_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `first_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateUserRequest.  # noqa: E501


        :return: The last_name of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateUserRequest.


        :param last_name: The last_name of this UpdateUserRequest.  # noqa: E501
        :type last_name: str
        """
        if self.local_vars_configuration.client_side_validation and last_name is None:  # noqa: E501
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) > 50):
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and len(last_name) < 2):
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                last_name is not None and not re.search(r'^[\s\S]*$', last_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `last_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this UpdateUserRequest.  # noqa: E501


        :return: The email_address of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UpdateUserRequest.


        :param email_address: The email_address of this UpdateUserRequest.  # noqa: E501
        :type email_address: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address is not None and len(email_address) > 80):
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email_address is not None and len(email_address) < 5):
            raise ValueError("Invalid value for `email_address`, length must be greater than or equal to `5`")  # noqa: E501

        self._email_address = email_address

    @property
    def second_email_address(self):
        """Gets the second_email_address of this UpdateUserRequest.  # noqa: E501


        :return: The second_email_address of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._second_email_address

    @second_email_address.setter
    def second_email_address(self, second_email_address):
        """Sets the second_email_address of this UpdateUserRequest.


        :param second_email_address: The second_email_address of this UpdateUserRequest.  # noqa: E501
        :type second_email_address: str
        """
        if (self.local_vars_configuration.client_side_validation and
                second_email_address is not None and len(second_email_address) > 80):
            raise ValueError("Invalid value for `second_email_address`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                second_email_address is not None and len(second_email_address) < 5):
            raise ValueError("Invalid value for `second_email_address`, length must be greater than or equal to `5`")  # noqa: E501

        self._second_email_address = second_email_address

    @property
    def login(self):
        """Gets the login of this UpdateUserRequest.  # noqa: E501

        The user's login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user's email address.  # noqa: E501

        :return: The login of this UpdateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UpdateUserRequest.

        The user's login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user's email address.  # noqa: E501

        :param login: The login of this UpdateUserRequest.  # noqa: E501
        :type login: str
        """
        if self.local_vars_configuration.client_side_validation and login is None:  # noqa: E501
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                login is not None and len(login) > 80):
            raise ValueError("Invalid value for `login`, length must be less than or equal to `80`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                login is not None and len(login) < 5):
            raise ValueError("Invalid value for `login`, length must be greater than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                login is not None and not re.search(r'^[\s\S]*$', login)):  # noqa: E501
            raise ValueError(r"Invalid value for `login`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._login = login

    @property
    def roles(self):
        """Gets the roles of this UpdateUserRequest.  # noqa: E501


        :return: The roles of this UpdateUserRequest.  # noqa: E501
        :rtype: list[finbourne_identity.RoleId]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UpdateUserRequest.


        :param roles: The roles of this UpdateUserRequest.  # noqa: E501
        :type roles: list[finbourne_identity.RoleId]
        """

        self._roles = roles

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateUserRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserRequest):
            return True

        return self.to_dict() != other.to_dict()

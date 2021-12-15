# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1487
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


class CreateDomainRequest(object):
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
        'domain': 'str',
        'description': 'str',
        'company_name': 'str',
        'owner': 'CreateUserRequest',
        'technical_contact': 'CreateUserRequest',
        'billing_contact': 'CreateUserRequest',
        'signed_agreements': 'list[str]'
    }

    attribute_map = {
        'domain': 'domain',
        'description': 'description',
        'company_name': 'companyName',
        'owner': 'owner',
        'technical_contact': 'technicalContact',
        'billing_contact': 'billingContact',
        'signed_agreements': 'signedAgreements'
    }

    required_map = {
        'domain': 'required',
        'description': 'optional',
        'company_name': 'required',
        'owner': 'required',
        'technical_contact': 'optional',
        'billing_contact': 'optional',
        'signed_agreements': 'optional'
    }

    def __init__(self, domain=None, description=None, company_name=None, owner=None, technical_contact=None, billing_contact=None, signed_agreements=None, local_vars_configuration=None):  # noqa: E501
        """CreateDomainRequest - a model defined in OpenAPI"
        
        :param domain:  The name LUSID domain to create (required)
        :type domain: str
        :param description:  Optional. Free text description of the domain.
        :type description: str
        :param company_name:  The name of the company to which the domain is registered (required)
        :type company_name: str
        :param owner:  (required)
        :type owner: finbourne_identity.CreateUserRequest
        :param technical_contact: 
        :type technical_contact: finbourne_identity.CreateUserRequest
        :param billing_contact: 
        :type billing_contact: finbourne_identity.CreateUserRequest
        :param signed_agreements:  Optional. If Terms and Conditions agreements have been signed during the sign up process
        :type signed_agreements: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._domain = None
        self._description = None
        self._company_name = None
        self._owner = None
        self._technical_contact = None
        self._billing_contact = None
        self._signed_agreements = None
        self.discriminator = None

        self.domain = domain
        self.description = description
        self.company_name = company_name
        self.owner = owner
        if technical_contact is not None:
            self.technical_contact = technical_contact
        if billing_contact is not None:
            self.billing_contact = billing_contact
        self.signed_agreements = signed_agreements

    @property
    def domain(self):
        """Gets the domain of this CreateDomainRequest.  # noqa: E501

        The name LUSID domain to create  # noqa: E501

        :return: The domain of this CreateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateDomainRequest.

        The name LUSID domain to create  # noqa: E501

        :param domain: The domain of this CreateDomainRequest.  # noqa: E501
        :type domain: str
        """
        if self.local_vars_configuration.client_side_validation and domain is None:  # noqa: E501
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                domain is not None and len(domain) > 25):
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                domain is not None and len(domain) < 3):
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                domain is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9-]*$', domain)):  # noqa: E501
            raise ValueError(r"Invalid value for `domain`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-]*$/`")  # noqa: E501

        self._domain = domain

    @property
    def description(self):
        """Gets the description of this CreateDomainRequest.  # noqa: E501

        Optional. Free text description of the domain.  # noqa: E501

        :return: The description of this CreateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDomainRequest.

        Optional. Free text description of the domain.  # noqa: E501

        :param description: The description of this CreateDomainRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 50):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 5):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `5`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def company_name(self):
        """Gets the company_name of this CreateDomainRequest.  # noqa: E501

        The name of the company to which the domain is registered  # noqa: E501

        :return: The company_name of this CreateDomainRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreateDomainRequest.

        The name of the company to which the domain is registered  # noqa: E501

        :param company_name: The company_name of this CreateDomainRequest.  # noqa: E501
        :type company_name: str
        """
        if self.local_vars_configuration.client_side_validation and company_name is None:  # noqa: E501
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) > 50):
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) < 2):
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `2`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and not re.search(r'^[\s\S]*$', company_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `company_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._company_name = company_name

    @property
    def owner(self):
        """Gets the owner of this CreateDomainRequest.  # noqa: E501


        :return: The owner of this CreateDomainRequest.  # noqa: E501
        :rtype: finbourne_identity.CreateUserRequest
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this CreateDomainRequest.


        :param owner: The owner of this CreateDomainRequest.  # noqa: E501
        :type owner: finbourne_identity.CreateUserRequest
        """
        if self.local_vars_configuration.client_side_validation and owner is None:  # noqa: E501
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def technical_contact(self):
        """Gets the technical_contact of this CreateDomainRequest.  # noqa: E501


        :return: The technical_contact of this CreateDomainRequest.  # noqa: E501
        :rtype: finbourne_identity.CreateUserRequest
        """
        return self._technical_contact

    @technical_contact.setter
    def technical_contact(self, technical_contact):
        """Sets the technical_contact of this CreateDomainRequest.


        :param technical_contact: The technical_contact of this CreateDomainRequest.  # noqa: E501
        :type technical_contact: finbourne_identity.CreateUserRequest
        """

        self._technical_contact = technical_contact

    @property
    def billing_contact(self):
        """Gets the billing_contact of this CreateDomainRequest.  # noqa: E501


        :return: The billing_contact of this CreateDomainRequest.  # noqa: E501
        :rtype: finbourne_identity.CreateUserRequest
        """
        return self._billing_contact

    @billing_contact.setter
    def billing_contact(self, billing_contact):
        """Sets the billing_contact of this CreateDomainRequest.


        :param billing_contact: The billing_contact of this CreateDomainRequest.  # noqa: E501
        :type billing_contact: finbourne_identity.CreateUserRequest
        """

        self._billing_contact = billing_contact

    @property
    def signed_agreements(self):
        """Gets the signed_agreements of this CreateDomainRequest.  # noqa: E501

        Optional. If Terms and Conditions agreements have been signed during the sign up process  # noqa: E501

        :return: The signed_agreements of this CreateDomainRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._signed_agreements

    @signed_agreements.setter
    def signed_agreements(self, signed_agreements):
        """Sets the signed_agreements of this CreateDomainRequest.

        Optional. If Terms and Conditions agreements have been signed during the sign up process  # noqa: E501

        :param signed_agreements: The signed_agreements of this CreateDomainRequest.  # noqa: E501
        :type signed_agreements: list[str]
        """

        self._signed_agreements = signed_agreements

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
        if not isinstance(other, CreateDomainRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDomainRequest):
            return True

        return self.to_dict() != other.to_dict()

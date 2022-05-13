# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1648
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


class DomainResponse(object):
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
        'id': 'DomainId',
        'description': 'str',
        'company_name': 'str',
        'owner': 'UserId',
        'billing_contact': 'UserId',
        'technical_contact': 'UserId',
        'created': 'datetime',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'company_name': 'companyName',
        'owner': 'owner',
        'billing_contact': 'billingContact',
        'technical_contact': 'technicalContact',
        'created': 'created',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'description': 'optional',
        'company_name': 'optional',
        'owner': 'optional',
        'billing_contact': 'optional',
        'technical_contact': 'optional',
        'created': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, description=None, company_name=None, owner=None, billing_contact=None, technical_contact=None, created=None, links=None, local_vars_configuration=None):  # noqa: E501
        """DomainResponse - a model defined in OpenAPI"
        
        :param id: 
        :type id: finbourne_identity.DomainId
        :param description:  A description of the domain
        :type description: str
        :param company_name:  The company name for the domain
        :type company_name: str
        :param owner: 
        :type owner: finbourne_identity.UserId
        :param billing_contact: 
        :type billing_contact: finbourne_identity.UserId
        :param technical_contact: 
        :type technical_contact: finbourne_identity.UserId
        :param created:  The
        :type created: datetime
        :param links: 
        :type links: list[finbourne_identity.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._description = None
        self._company_name = None
        self._owner = None
        self._billing_contact = None
        self._technical_contact = None
        self._created = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.description = description
        self.company_name = company_name
        if owner is not None:
            self.owner = owner
        if billing_contact is not None:
            self.billing_contact = billing_contact
        if technical_contact is not None:
            self.technical_contact = technical_contact
        if created is not None:
            self.created = created
        self.links = links

    @property
    def id(self):
        """Gets the id of this DomainResponse.  # noqa: E501


        :return: The id of this DomainResponse.  # noqa: E501
        :rtype: finbourne_identity.DomainId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DomainResponse.


        :param id: The id of this DomainResponse.  # noqa: E501
        :type id: finbourne_identity.DomainId
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this DomainResponse.  # noqa: E501

        A description of the domain  # noqa: E501

        :return: The description of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DomainResponse.

        A description of the domain  # noqa: E501

        :param description: The description of this DomainResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def company_name(self):
        """Gets the company_name of this DomainResponse.  # noqa: E501

        The company name for the domain  # noqa: E501

        :return: The company_name of this DomainResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this DomainResponse.

        The company name for the domain  # noqa: E501

        :param company_name: The company_name of this DomainResponse.  # noqa: E501
        :type company_name: str
        """

        self._company_name = company_name

    @property
    def owner(self):
        """Gets the owner of this DomainResponse.  # noqa: E501


        :return: The owner of this DomainResponse.  # noqa: E501
        :rtype: finbourne_identity.UserId
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DomainResponse.


        :param owner: The owner of this DomainResponse.  # noqa: E501
        :type owner: finbourne_identity.UserId
        """

        self._owner = owner

    @property
    def billing_contact(self):
        """Gets the billing_contact of this DomainResponse.  # noqa: E501


        :return: The billing_contact of this DomainResponse.  # noqa: E501
        :rtype: finbourne_identity.UserId
        """
        return self._billing_contact

    @billing_contact.setter
    def billing_contact(self, billing_contact):
        """Sets the billing_contact of this DomainResponse.


        :param billing_contact: The billing_contact of this DomainResponse.  # noqa: E501
        :type billing_contact: finbourne_identity.UserId
        """

        self._billing_contact = billing_contact

    @property
    def technical_contact(self):
        """Gets the technical_contact of this DomainResponse.  # noqa: E501


        :return: The technical_contact of this DomainResponse.  # noqa: E501
        :rtype: finbourne_identity.UserId
        """
        return self._technical_contact

    @technical_contact.setter
    def technical_contact(self, technical_contact):
        """Sets the technical_contact of this DomainResponse.


        :param technical_contact: The technical_contact of this DomainResponse.  # noqa: E501
        :type technical_contact: finbourne_identity.UserId
        """

        self._technical_contact = technical_contact

    @property
    def created(self):
        """Gets the created of this DomainResponse.  # noqa: E501

        The  # noqa: E501

        :return: The created of this DomainResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DomainResponse.

        The  # noqa: E501

        :param created: The created of this DomainResponse.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def links(self):
        """Gets the links of this DomainResponse.  # noqa: E501


        :return: The links of this DomainResponse.  # noqa: E501
        :rtype: list[finbourne_identity.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DomainResponse.


        :param links: The links of this DomainResponse.  # noqa: E501
        :type links: list[finbourne_identity.Link]
        """

        self._links = links

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
        if not isinstance(other, DomainResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainResponse):
            return True

        return self.to_dict() != other.to_dict()

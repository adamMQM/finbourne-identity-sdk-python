# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1559
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


class UserSummary(object):
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
        'id': 'str',
        'login': 'str',
        'email': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'type': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'login': 'login',
        'email': 'email',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'type': 'type',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'login': 'optional',
        'email': 'optional',
        'first_name': 'optional',
        'last_name': 'optional',
        'type': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, login=None, email=None, first_name=None, last_name=None, type=None, links=None, local_vars_configuration=None):  # noqa: E501
        """UserSummary - a model defined in OpenAPI"
        
        :param id:  The user id
        :type id: str
        :param login:  The user login
        :type login: str
        :param email:  The email address registered for that user
        :type email: str
        :param first_name:  User's first name
        :type first_name: str
        :param last_name:  User's last name
        :type last_name: str
        :param type:  User's type (Personal, Service...)
        :type type: str
        :param links: 
        :type links: list[finbourne_identity.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._login = None
        self._email = None
        self._first_name = None
        self._last_name = None
        self._type = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.login = login
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.links = links

    @property
    def id(self):
        """Gets the id of this UserSummary.  # noqa: E501

        The user id  # noqa: E501

        :return: The id of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSummary.

        The user id  # noqa: E501

        :param id: The id of this UserSummary.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def login(self):
        """Gets the login of this UserSummary.  # noqa: E501

        The user login  # noqa: E501

        :return: The login of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserSummary.

        The user login  # noqa: E501

        :param login: The login of this UserSummary.  # noqa: E501
        :type login: str
        """

        self._login = login

    @property
    def email(self):
        """Gets the email of this UserSummary.  # noqa: E501

        The email address registered for that user  # noqa: E501

        :return: The email of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserSummary.

        The email address registered for that user  # noqa: E501

        :param email: The email of this UserSummary.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def first_name(self):
        """Gets the first_name of this UserSummary.  # noqa: E501

        User's first name  # noqa: E501

        :return: The first_name of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserSummary.

        User's first name  # noqa: E501

        :param first_name: The first_name of this UserSummary.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserSummary.  # noqa: E501

        User's last name  # noqa: E501

        :return: The last_name of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserSummary.

        User's last name  # noqa: E501

        :param last_name: The last_name of this UserSummary.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def type(self):
        """Gets the type of this UserSummary.  # noqa: E501

        User's type (Personal, Service...)  # noqa: E501

        :return: The type of this UserSummary.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserSummary.

        User's type (Personal, Service...)  # noqa: E501

        :param type: The type of this UserSummary.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def links(self):
        """Gets the links of this UserSummary.  # noqa: E501


        :return: The links of this UserSummary.  # noqa: E501
        :rtype: list[finbourne_identity.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserSummary.


        :param links: The links of this UserSummary.  # noqa: E501
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
        if not isinstance(other, UserSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSummary):
            return True

        return self.to_dict() != other.to_dict()

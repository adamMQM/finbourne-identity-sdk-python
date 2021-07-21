# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1305
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UserResponse(object):
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
        'email_address': 'str',
        'login': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'roles': 'list[Role]',
        'type': 'str',
        'status': 'str',
        'external': 'bool',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'email_address': 'emailAddress',
        'login': 'login',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'roles': 'roles',
        'type': 'type',
        'status': 'status',
        'external': 'external',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'email_address': 'required',
        'login': 'required',
        'first_name': 'required',
        'last_name': 'required',
        'roles': 'optional',
        'type': 'required',
        'status': 'required',
        'external': 'required',
        'links': 'optional'
    }

    def __init__(self, id=None, email_address=None, login=None, first_name=None, last_name=None, roles=None, type=None, status=None, external=None, links=None):  # noqa: E501
        """
        UserResponse - a model defined in OpenAPI

        :param id:  The user's system supplied unique identifier (required)
        :type id: str
        :param email_address:  The user's emailAddress address, which must be unique within the system (required)
        :type email_address: str
        :param login:  (required)
        :type login: str
        :param first_name:  The user's first name (required)
        :type first_name: str
        :param last_name:  The user's last name (required)
        :type last_name: str
        :param roles:  The roles that the user has.
        :type roles: list[finbourne_identity.Role]
        :param type:  The type of user (e.g. Personal or Service) (required)
        :type type: str
        :param status:  The status of the user (required)
        :type status: str
        :param external:  Whether or not the user originates from an external identity system (required)
        :type external: bool
        :param links: 
        :type links: list[finbourne_identity.Link]

        """  # noqa: E501

        self._id = None
        self._email_address = None
        self._login = None
        self._first_name = None
        self._last_name = None
        self._roles = None
        self._type = None
        self._status = None
        self._external = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.email_address = email_address
        self.login = login
        self.first_name = first_name
        self.last_name = last_name
        self.roles = roles
        self.type = type
        self.status = status
        self.external = external
        self.links = links

    @property
    def id(self):
        """Gets the id of this UserResponse.  # noqa: E501

        The user's system supplied unique identifier  # noqa: E501

        :return: The id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserResponse.

        The user's system supplied unique identifier  # noqa: E501

        :param id: The id of this UserResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_address(self):
        """Gets the email_address of this UserResponse.  # noqa: E501

        The user's emailAddress address, which must be unique within the system  # noqa: E501

        :return: The email_address of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this UserResponse.

        The user's emailAddress address, which must be unique within the system  # noqa: E501

        :param email_address: The email_address of this UserResponse.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def login(self):
        """Gets the login of this UserResponse.  # noqa: E501


        :return: The login of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._login

    @login.setter
    def login(self, login):
        """Sets the login of this UserResponse.


        :param login: The login of this UserResponse.  # noqa: E501
        :type: str
        """
        if login is None:
            raise ValueError("Invalid value for `login`, must not be `None`")  # noqa: E501

        self._login = login

    @property
    def first_name(self):
        """Gets the first_name of this UserResponse.  # noqa: E501

        The user's first name  # noqa: E501

        :return: The first_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserResponse.

        The user's first name  # noqa: E501

        :param first_name: The first_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserResponse.  # noqa: E501

        The user's last name  # noqa: E501

        :return: The last_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserResponse.

        The user's last name  # noqa: E501

        :param last_name: The last_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def roles(self):
        """Gets the roles of this UserResponse.  # noqa: E501

        The roles that the user has.  # noqa: E501

        :return: The roles of this UserResponse.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserResponse.

        The roles that the user has.  # noqa: E501

        :param roles: The roles of this UserResponse.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

    @property
    def type(self):
        """Gets the type of this UserResponse.  # noqa: E501

        The type of user (e.g. Personal or Service)  # noqa: E501

        :return: The type of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UserResponse.

        The type of user (e.g. Personal or Service)  # noqa: E501

        :param type: The type of this UserResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this UserResponse.  # noqa: E501

        The status of the user  # noqa: E501

        :return: The status of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserResponse.

        The status of the user  # noqa: E501

        :param status: The status of this UserResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def external(self):
        """Gets the external of this UserResponse.  # noqa: E501

        Whether or not the user originates from an external identity system  # noqa: E501

        :return: The external of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this UserResponse.

        Whether or not the user originates from an external identity system  # noqa: E501

        :param external: The external of this UserResponse.  # noqa: E501
        :type: bool
        """
        if external is None:
            raise ValueError("Invalid value for `external`, must not be `None`")  # noqa: E501

        self._external = external

    @property
    def links(self):
        """Gets the links of this UserResponse.  # noqa: E501


        :return: The links of this UserResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserResponse.


        :param links: The links of this UserResponse.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

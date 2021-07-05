# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1277
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class RoleResponse(object):
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
        'role_id': 'RoleId',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'roleId',
        'name': 'name',
        'description': 'description'
    }

    required_map = {
        'id': 'required',
        'role_id': 'required',
        'name': 'required',
        'description': 'optional'
    }

    def __init__(self, id=None, role_id=None, name=None, description=None):  # noqa: E501
        """
        RoleResponse - a model defined in OpenAPI

        :param id:  The role's system supplied unique identifier (required)
        :type id: str
        :param role_id:  (required)
        :type role_id: finbourne_identity.RoleId
        :param name:  The role name, which must be unique within the system. (required)
        :type name: str
        :param description:  The description for this role
        :type description: str

        """  # noqa: E501

        self._id = None
        self._role_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.role_id = role_id
        self.name = name
        self.description = description

    @property
    def id(self):
        """Gets the id of this RoleResponse.  # noqa: E501

        The role's system supplied unique identifier  # noqa: E501

        :return: The id of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleResponse.

        The role's system supplied unique identifier  # noqa: E501

        :param id: The id of this RoleResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def role_id(self):
        """Gets the role_id of this RoleResponse.  # noqa: E501


        :return: The role_id of this RoleResponse.  # noqa: E501
        :rtype: RoleId
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this RoleResponse.


        :param role_id: The role_id of this RoleResponse.  # noqa: E501
        :type: RoleId
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def name(self):
        """Gets the name of this RoleResponse.  # noqa: E501

        The role name, which must be unique within the system.  # noqa: E501

        :return: The name of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleResponse.

        The role name, which must be unique within the system.  # noqa: E501

        :param name: The name of this RoleResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleResponse.  # noqa: E501

        The description for this role  # noqa: E501

        :return: The description of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleResponse.

        The description for this role  # noqa: E501

        :param description: The description of this RoleResponse.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, RoleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1319
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ErrorDetail(object):
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
        'type': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'detail': 'detail'
    }

    required_map = {
        'id': 'optional',
        'type': 'optional',
        'detail': 'optional'
    }

    def __init__(self, id=None, type=None, detail=None):  # noqa: E501
        """
        ErrorDetail - a model defined in OpenAPI

        :param id:  Id of the entity this error relates to
        :type id: str
        :param type:  Error type
        :type type: str
        :param detail:  Human readable description of the error
        :type detail: str

        """  # noqa: E501

        self._id = None
        self._type = None
        self._detail = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.detail = detail

    @property
    def id(self):
        """Gets the id of this ErrorDetail.  # noqa: E501

        Id of the entity this error relates to  # noqa: E501

        :return: The id of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErrorDetail.

        Id of the entity this error relates to  # noqa: E501

        :param id: The id of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ErrorDetail.  # noqa: E501

        Error type  # noqa: E501

        :return: The type of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ErrorDetail.

        Error type  # noqa: E501

        :param type: The type of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def detail(self):
        """Gets the detail of this ErrorDetail.  # noqa: E501

        Human readable description of the error  # noqa: E501

        :return: The detail of this ErrorDetail.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorDetail.

        Human readable description of the error  # noqa: E501

        :param detail: The detail of this ErrorDetail.  # noqa: E501
        :type: str
        """

        self._detail = detail

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
        if not isinstance(other, ErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

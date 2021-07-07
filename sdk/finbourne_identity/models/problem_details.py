# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1285
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ProblemDetails(object):
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
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance',
        'extensions': 'extensions'
    }

    required_map = {
        'type': 'optional',
        'title': 'optional',
        'status': 'optional',
        'detail': 'optional',
        'instance': 'optional',
        'extensions': 'optional'
    }

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, extensions=None):  # noqa: E501
        """
        ProblemDetails - a model defined in OpenAPI

        :param type: 
        :type type: str
        :param title: 
        :type title: str
        :param status: 
        :type status: int
        :param detail: 
        :type detail: str
        :param instance: 
        :type instance: str
        :param extensions: 
        :type extensions: dict(str, object)

        """  # noqa: E501

        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self._extensions = None
        self.discriminator = None

        self.type = type
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance
        self.extensions = extensions

    @property
    def type(self):
        """Gets the type of this ProblemDetails.  # noqa: E501


        :return: The type of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProblemDetails.


        :param type: The type of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this ProblemDetails.  # noqa: E501


        :return: The title of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ProblemDetails.


        :param title: The title of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this ProblemDetails.  # noqa: E501


        :return: The status of this ProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProblemDetails.


        :param status: The status of this ProblemDetails.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this ProblemDetails.  # noqa: E501


        :return: The detail of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ProblemDetails.


        :param detail: The detail of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this ProblemDetails.  # noqa: E501


        :return: The instance of this ProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this ProblemDetails.


        :param instance: The instance of this ProblemDetails.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def extensions(self):
        """Gets the extensions of this ProblemDetails.  # noqa: E501


        :return: The extensions of this ProblemDetails.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this ProblemDetails.


        :param extensions: The extensions of this ProblemDetails.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

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
        if not isinstance(other, ProblemDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

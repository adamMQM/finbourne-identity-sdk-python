# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1714
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


class AccessControlledAction(object):
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
        'description': 'str',
        'action': 'ActionId',
        'limited_set': 'list[IdSelectorDefinition]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'description': 'description',
        'action': 'action',
        'limited_set': 'limitedSet',
        'links': 'links'
    }

    required_map = {
        'description': 'required',
        'action': 'required',
        'limited_set': 'optional',
        'links': 'optional'
    }

    def __init__(self, description=None, action=None, limited_set=None, links=None, local_vars_configuration=None):  # noqa: E501
        """AccessControlledAction - a model defined in OpenAPI"
        
        :param description:  (required)
        :type description: str
        :param action:  (required)
        :type action: finbourne_identity.ActionId
        :param limited_set: 
        :type limited_set: list[finbourne_identity.IdSelectorDefinition]
        :param links: 
        :type links: list[finbourne_identity.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._action = None
        self._limited_set = None
        self._links = None
        self.discriminator = None

        self.description = description
        self.action = action
        self.limited_set = limited_set
        self.links = links

    @property
    def description(self):
        """Gets the description of this AccessControlledAction.  # noqa: E501


        :return: The description of this AccessControlledAction.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessControlledAction.


        :param description: The description of this AccessControlledAction.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def action(self):
        """Gets the action of this AccessControlledAction.  # noqa: E501


        :return: The action of this AccessControlledAction.  # noqa: E501
        :rtype: finbourne_identity.ActionId
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AccessControlledAction.


        :param action: The action of this AccessControlledAction.  # noqa: E501
        :type action: finbourne_identity.ActionId
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def limited_set(self):
        """Gets the limited_set of this AccessControlledAction.  # noqa: E501


        :return: The limited_set of this AccessControlledAction.  # noqa: E501
        :rtype: list[finbourne_identity.IdSelectorDefinition]
        """
        return self._limited_set

    @limited_set.setter
    def limited_set(self, limited_set):
        """Sets the limited_set of this AccessControlledAction.


        :param limited_set: The limited_set of this AccessControlledAction.  # noqa: E501
        :type limited_set: list[finbourne_identity.IdSelectorDefinition]
        """

        self._limited_set = limited_set

    @property
    def links(self):
        """Gets the links of this AccessControlledAction.  # noqa: E501


        :return: The links of this AccessControlledAction.  # noqa: E501
        :rtype: list[finbourne_identity.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this AccessControlledAction.


        :param links: The links of this AccessControlledAction.  # noqa: E501
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
        if not isinstance(other, AccessControlledAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessControlledAction):
            return True

        return self.to_dict() != other.to_dict()

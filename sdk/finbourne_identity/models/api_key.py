# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2164
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


class ApiKey(object):
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
        'display_name': 'str',
        'created_date': 'datetime',
        'deactivation_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'created_date': 'createdDate',
        'deactivation_date': 'deactivationDate'
    }

    required_map = {
        'id': 'required',
        'display_name': 'required',
        'created_date': 'required',
        'deactivation_date': 'optional'
    }

    def __init__(self, id=None, display_name=None, created_date=None, deactivation_date=None, local_vars_configuration=None):  # noqa: E501
        """ApiKey - a model defined in OpenAPI"
        
        :param id:  The unique Id of the API key (required)
        :type id: str
        :param display_name:  The display name of the API key (required)
        :type display_name: str
        :param created_date:  The creation date of the API key (required)
        :type created_date: datetime
        :param deactivation_date:  The deactivation date of the API key
        :type deactivation_date: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._created_date = None
        self._deactivation_date = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.created_date = created_date
        self.deactivation_date = deactivation_date

    @property
    def id(self):
        """Gets the id of this ApiKey.  # noqa: E501

        The unique Id of the API key  # noqa: E501

        :return: The id of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiKey.

        The unique Id of the API key  # noqa: E501

        :param id: The id of this ApiKey.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) > 64):
            raise ValueError("Invalid value for `id`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this ApiKey.  # noqa: E501

        The display name of the API key  # noqa: E501

        :return: The display_name of this ApiKey.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiKey.

        The display name of the API key  # noqa: E501

        :param display_name: The display_name of this ApiKey.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def created_date(self):
        """Gets the created_date of this ApiKey.  # noqa: E501

        The creation date of the API key  # noqa: E501

        :return: The created_date of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ApiKey.

        The creation date of the API key  # noqa: E501

        :param created_date: The created_date of this ApiKey.  # noqa: E501
        :type created_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_date is None:  # noqa: E501
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this ApiKey.  # noqa: E501

        The deactivation date of the API key  # noqa: E501

        :return: The deactivation_date of this ApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this ApiKey.

        The deactivation date of the API key  # noqa: E501

        :param deactivation_date: The deactivation_date of this ApiKey.  # noqa: E501
        :type deactivation_date: datetime
        """

        self._deactivation_date = deactivation_date

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
        if not isinstance(other, ApiKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiKey):
            return True

        return self.to_dict() != other.to_dict()

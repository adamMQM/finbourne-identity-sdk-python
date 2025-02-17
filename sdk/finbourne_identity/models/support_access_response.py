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


class SupportAccessResponse(object):
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
        'duration': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'expiry': 'datetime',
        'created_by': 'str',
        'terminated': 'bool',
        'terminated_at': 'datetime',
        'terminated_by': 'str',
        'permitted_roles': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'duration': 'duration',
        'description': 'description',
        'created_at': 'createdAt',
        'expiry': 'expiry',
        'created_by': 'createdBy',
        'terminated': 'terminated',
        'terminated_at': 'terminatedAt',
        'terminated_by': 'terminatedBy',
        'permitted_roles': 'permittedRoles'
    }

    required_map = {
        'id': 'required',
        'duration': 'required',
        'description': 'optional',
        'created_at': 'required',
        'expiry': 'required',
        'created_by': 'required',
        'terminated': 'optional',
        'terminated_at': 'optional',
        'terminated_by': 'optional',
        'permitted_roles': 'optional'
    }

    def __init__(self, id=None, duration=None, description=None, created_at=None, expiry=None, created_by=None, terminated=None, terminated_at=None, terminated_by=None, permitted_roles=None, local_vars_configuration=None):  # noqa: E501
        """SupportAccessResponse - a model defined in OpenAPI"
        
        :param id:  ID of the support access request (required)
        :type id: str
        :param duration:  The duration for which access is requested (in any ISO-8601 format) (required)
        :type duration: str
        :param description:  The description of why the support access has been granted (i.e. support ticket numbers)
        :type description: str
        :param created_at:  DateTimeOffset at which the access was granted (required)
        :type created_at: datetime
        :param expiry:  DateTimeOffset at which the access will be revoked (required)
        :type expiry: datetime
        :param created_by:  Obfuscated UserId of the user who granted the support access (required)
        :type created_by: str
        :param terminated:  Whether or not that access has been invalidated
        :type terminated: bool
        :param terminated_at:  DateTimeOffset at which the access was invalidated
        :type terminated_at: datetime
        :param terminated_by:  Obfuscated UserId of the user who revoked the access
        :type terminated_by: str
        :param permitted_roles:  A list of permitted roles, valid for support staff to assume, for the duration of the access request
        :type permitted_roles: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._duration = None
        self._description = None
        self._created_at = None
        self._expiry = None
        self._created_by = None
        self._terminated = None
        self._terminated_at = None
        self._terminated_by = None
        self._permitted_roles = None
        self.discriminator = None

        self.id = id
        self.duration = duration
        self.description = description
        self.created_at = created_at
        self.expiry = expiry
        self.created_by = created_by
        if terminated is not None:
            self.terminated = terminated
        self.terminated_at = terminated_at
        self.terminated_by = terminated_by
        self.permitted_roles = permitted_roles

    @property
    def id(self):
        """Gets the id of this SupportAccessResponse.  # noqa: E501

        ID of the support access request  # noqa: E501

        :return: The id of this SupportAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SupportAccessResponse.

        ID of the support access request  # noqa: E501

        :param id: The id of this SupportAccessResponse.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def duration(self):
        """Gets the duration of this SupportAccessResponse.  # noqa: E501

        The duration for which access is requested (in any ISO-8601 format)  # noqa: E501

        :return: The duration of this SupportAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SupportAccessResponse.

        The duration for which access is requested (in any ISO-8601 format)  # noqa: E501

        :param duration: The duration of this SupportAccessResponse.  # noqa: E501
        :type duration: str
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and len(duration) > 50):
            raise ValueError("Invalid value for `duration`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                duration is not None and len(duration) < 3):
            raise ValueError("Invalid value for `duration`, length must be greater than or equal to `3`")  # noqa: E501

        self._duration = duration

    @property
    def description(self):
        """Gets the description of this SupportAccessResponse.  # noqa: E501

        The description of why the support access has been granted (i.e. support ticket numbers)  # noqa: E501

        :return: The description of this SupportAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupportAccessResponse.

        The description of why the support access has been granted (i.e. support ticket numbers)  # noqa: E501

        :param description: The description of this SupportAccessResponse.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this SupportAccessResponse.  # noqa: E501

        DateTimeOffset at which the access was granted  # noqa: E501

        :return: The created_at of this SupportAccessResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SupportAccessResponse.

        DateTimeOffset at which the access was granted  # noqa: E501

        :param created_at: The created_at of this SupportAccessResponse.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def expiry(self):
        """Gets the expiry of this SupportAccessResponse.  # noqa: E501

        DateTimeOffset at which the access will be revoked  # noqa: E501

        :return: The expiry of this SupportAccessResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this SupportAccessResponse.

        DateTimeOffset at which the access will be revoked  # noqa: E501

        :param expiry: The expiry of this SupportAccessResponse.  # noqa: E501
        :type expiry: datetime
        """
        if self.local_vars_configuration.client_side_validation and expiry is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry`, must not be `None`")  # noqa: E501

        self._expiry = expiry

    @property
    def created_by(self):
        """Gets the created_by of this SupportAccessResponse.  # noqa: E501

        Obfuscated UserId of the user who granted the support access  # noqa: E501

        :return: The created_by of this SupportAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SupportAccessResponse.

        Obfuscated UserId of the user who granted the support access  # noqa: E501

        :param created_by: The created_by of this SupportAccessResponse.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def terminated(self):
        """Gets the terminated of this SupportAccessResponse.  # noqa: E501

        Whether or not that access has been invalidated  # noqa: E501

        :return: The terminated of this SupportAccessResponse.  # noqa: E501
        :rtype: bool
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this SupportAccessResponse.

        Whether or not that access has been invalidated  # noqa: E501

        :param terminated: The terminated of this SupportAccessResponse.  # noqa: E501
        :type terminated: bool
        """

        self._terminated = terminated

    @property
    def terminated_at(self):
        """Gets the terminated_at of this SupportAccessResponse.  # noqa: E501

        DateTimeOffset at which the access was invalidated  # noqa: E501

        :return: The terminated_at of this SupportAccessResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._terminated_at

    @terminated_at.setter
    def terminated_at(self, terminated_at):
        """Sets the terminated_at of this SupportAccessResponse.

        DateTimeOffset at which the access was invalidated  # noqa: E501

        :param terminated_at: The terminated_at of this SupportAccessResponse.  # noqa: E501
        :type terminated_at: datetime
        """

        self._terminated_at = terminated_at

    @property
    def terminated_by(self):
        """Gets the terminated_by of this SupportAccessResponse.  # noqa: E501

        Obfuscated UserId of the user who revoked the access  # noqa: E501

        :return: The terminated_by of this SupportAccessResponse.  # noqa: E501
        :rtype: str
        """
        return self._terminated_by

    @terminated_by.setter
    def terminated_by(self, terminated_by):
        """Sets the terminated_by of this SupportAccessResponse.

        Obfuscated UserId of the user who revoked the access  # noqa: E501

        :param terminated_by: The terminated_by of this SupportAccessResponse.  # noqa: E501
        :type terminated_by: str
        """

        self._terminated_by = terminated_by

    @property
    def permitted_roles(self):
        """Gets the permitted_roles of this SupportAccessResponse.  # noqa: E501

        A list of permitted roles, valid for support staff to assume, for the duration of the access request  # noqa: E501

        :return: The permitted_roles of this SupportAccessResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._permitted_roles

    @permitted_roles.setter
    def permitted_roles(self, permitted_roles):
        """Sets the permitted_roles of this SupportAccessResponse.

        A list of permitted roles, valid for support staff to assume, for the duration of the access request  # noqa: E501

        :param permitted_roles: The permitted_roles of this SupportAccessResponse.  # noqa: E501
        :type permitted_roles: list[str]
        """

        self._permitted_roles = permitted_roles

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
        if not isinstance(other, SupportAccessResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportAccessResponse):
            return True

        return self.to_dict() != other.to_dict()

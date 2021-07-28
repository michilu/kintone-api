# coding: utf-8

"""
    Kintone REST API

    Kintone REST API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InlineResponse200(object):
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
    """
    openapi_types = {
        'rights': 'list[Right]',
        'revision': 'int'
    }

    attribute_map = {
        'rights': 'rights',
        'revision': 'revision'
    }

    def __init__(self, rights=None, revision=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._rights = None
        self._revision = None
        self.discriminator = None

        if rights is not None:
            self.rights = rights
        if revision is not None:
            self.revision = revision

    @property
    def rights(self):
        """Gets the rights of this InlineResponse200.  # noqa: E501


        :return: The rights of this InlineResponse200.  # noqa: E501
        :rtype: list[Right]
        """
        return self._rights

    @rights.setter
    def rights(self, rights):
        """Sets the rights of this InlineResponse200.


        :param rights: The rights of this InlineResponse200.  # noqa: E501
        :type: list[Right]
        """

        self._rights = rights

    @property
    def revision(self):
        """Gets the revision of this InlineResponse200.  # noqa: E501


        :return: The revision of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this InlineResponse200.


        :param revision: The revision of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._revision = revision

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()

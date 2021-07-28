# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class ProtobufAny(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type_url=None, value=None):  # noqa: E501
        """ProtobufAny - a model defined in OpenAPI

        :param type_url: The type_url of this ProtobufAny.  # noqa: E501
        :type type_url: str
        :param value: The value of this ProtobufAny.  # noqa: E501
        :type value: bytearray
        """
        self.openapi_types = {
            'type_url': str,
            'value': bytearray
        }

        self.attribute_map = {
            'type_url': 'type_url',
            'value': 'value'
        }

        self._type_url = type_url
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'ProtobufAny':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The protobufAny of this ProtobufAny.  # noqa: E501
        :rtype: ProtobufAny
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_url(self):
        """Gets the type_url of this ProtobufAny.

        A URL/resource name that uniquely identifies the type of the serialized protocol buffer message. This string must contain at least one \"/\" character. The last segment of the URL's path must represent the fully qualified name of the type (as in `path/google.protobuf.Duration`). The name should be in a canonical form (e.g., leading \".\" is not accepted).  In practice, teams usually precompile into the binary all types that they expect it to use in the context of Any. However, for URLs which use the scheme `http`, `https`, or no scheme, one can optionally set up a type server that maps type URLs to message definitions as follows:  * If no scheme is provided, `https` is assumed. * An HTTP GET on the URL must yield a [google.protobuf.Type][]   value in binary format, or produce an error. * Applications are allowed to cache lookup results based on the   URL, or have them precompiled into a binary to avoid any   lookup. Therefore, binary compatibility needs to be preserved   on changes to types. (Use versioned type names to manage   breaking changes.)  Note: this functionality is not currently available in the official protobuf release, and it is not used for type URLs beginning with type.googleapis.com.  Schemes other than `http`, `https` (or the empty scheme) might be used with implementation specific semantics.  # noqa: E501

        :return: The type_url of this ProtobufAny.
        :rtype: str
        """
        return self._type_url

    @type_url.setter
    def type_url(self, type_url):
        """Sets the type_url of this ProtobufAny.

        A URL/resource name that uniquely identifies the type of the serialized protocol buffer message. This string must contain at least one \"/\" character. The last segment of the URL's path must represent the fully qualified name of the type (as in `path/google.protobuf.Duration`). The name should be in a canonical form (e.g., leading \".\" is not accepted).  In practice, teams usually precompile into the binary all types that they expect it to use in the context of Any. However, for URLs which use the scheme `http`, `https`, or no scheme, one can optionally set up a type server that maps type URLs to message definitions as follows:  * If no scheme is provided, `https` is assumed. * An HTTP GET on the URL must yield a [google.protobuf.Type][]   value in binary format, or produce an error. * Applications are allowed to cache lookup results based on the   URL, or have them precompiled into a binary to avoid any   lookup. Therefore, binary compatibility needs to be preserved   on changes to types. (Use versioned type names to manage   breaking changes.)  Note: this functionality is not currently available in the official protobuf release, and it is not used for type URLs beginning with type.googleapis.com.  Schemes other than `http`, `https` (or the empty scheme) might be used with implementation specific semantics.  # noqa: E501

        :param type_url: The type_url of this ProtobufAny.
        :type type_url: str
        """

        self._type_url = type_url

    @property
    def value(self):
        """Gets the value of this ProtobufAny.

        Must be a valid serialized protocol buffer of the above specified type.  # noqa: E501

        :return: The value of this ProtobufAny.
        :rtype: bytearray
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProtobufAny.

        Must be a valid serialized protocol buffer of the above specified type.  # noqa: E501

        :param value: The value of this ProtobufAny.
        :type value: bytearray
        """
        if value is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', value):  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._value = value
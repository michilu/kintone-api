# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.rpc_code import RpcCode
from openapi_server import util


class Protov1Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: RpcCode=None, message: str=None):
        """Protov1Response - a model defined in OpenAPI

        :param code: The code of this Protov1Response.
        :param message: The message of this Protov1Response.
        """
        self.openapi_types = {
            'code': RpcCode,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Protov1Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The protov1Response of this Protov1Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this Protov1Response.


        :return: The code of this Protov1Response.
        :rtype: RpcCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Protov1Response.


        :param code: The code of this Protov1Response.
        :type code: RpcCode
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this Protov1Response.


        :return: The message of this Protov1Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Protov1Response.


        :param message: The message of this Protov1Response.
        :type message: str
        """

        self._message = message
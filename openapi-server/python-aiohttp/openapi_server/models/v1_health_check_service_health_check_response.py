# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model_ import Model
from openapi_server.models.protov1_response import Protov1Response
from openapi_server import util


class V1HealthCheckServiceHealthCheckResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: Protov1Response=None):
        """V1HealthCheckServiceHealthCheckResponse - a model defined in OpenAPI

        :param value: The value of this V1HealthCheckServiceHealthCheckResponse.
        """
        self.openapi_types = {
            'value': Protov1Response
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'V1HealthCheckServiceHealthCheckResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The v1HealthCheckServiceHealthCheckResponse of this V1HealthCheckServiceHealthCheckResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this V1HealthCheckServiceHealthCheckResponse.


        :return: The value of this V1HealthCheckServiceHealthCheckResponse.
        :rtype: Protov1Response
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1HealthCheckServiceHealthCheckResponse.


        :param value: The value of this V1HealthCheckServiceHealthCheckResponse.
        :type value: Protov1Response
        """

        self._value = value
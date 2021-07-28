# coding: utf-8

"""
    Kintone REST API

    Kintone REST API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.right import Right  # noqa: E501
from openapi_client.rest import ApiException

class TestRight(unittest.TestCase):
    """Right unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Right
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.right.Right()  # noqa: E501
        if include_optional :
            return Right(
                record_importable = True, 
                app_editable = True, 
                record_exportable = True, 
                record_addable = True, 
                record_viewable = True, 
                record_editable = True, 
                include_subs = True, 
                record_deletable = True, 
                entity = openapi_client.models.right_entity.Right_entity(
                    code = '0', 
                    type = 'USER', )
            )
        else :
            return Right(
        )

    def testRight(self):
        """Test Right"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

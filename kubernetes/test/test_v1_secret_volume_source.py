# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_secret_volume_source import V1SecretVolumeSource


class TestV1SecretVolumeSource(unittest.TestCase):
    """ V1SecretVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1SecretVolumeSource(self):
        """
        Test V1SecretVolumeSource
        """
        model = kubernetes.client.models.v1_secret_volume_source.V1SecretVolumeSource()


if __name__ == '__main__':
    unittest.main()

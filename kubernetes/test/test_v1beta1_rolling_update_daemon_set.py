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
from kubernetes.client.models.v1beta1_rolling_update_daemon_set import V1beta1RollingUpdateDaemonSet


class TestV1beta1RollingUpdateDaemonSet(unittest.TestCase):
    """ V1beta1RollingUpdateDaemonSet unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1RollingUpdateDaemonSet(self):
        """
        Test V1beta1RollingUpdateDaemonSet
        """
        model = kubernetes.client.models.v1beta1_rolling_update_daemon_set.V1beta1RollingUpdateDaemonSet()


if __name__ == '__main__':
    unittest.main()

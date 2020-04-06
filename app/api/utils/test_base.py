
from api.utils.config import TestingConfig
from api.utils.factory import create_app
import unittest

class BaseTestCase(unittest.TestCase):
    """A base test case"""
    def setUp(self):
        app = create_app(TestingConfig)
        app.app_context().push()
        self.app = app.test_client()

    def tearDown(self):
        pass

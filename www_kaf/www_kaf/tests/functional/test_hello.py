from www_kaf.tests import *

class TestHelloController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='hello', action='index'))
        # Test response...

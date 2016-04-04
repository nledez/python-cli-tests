'''
    The alice.bob module tests
'''

import unittest

import alice.bob
import responses


class TestBob(unittest.TestCase):
    '''
        The bob module test
    '''

    def test_assert_false(self):
        '''
            To check unittest framework
            Uncomment assertion line
        '''
        pass
        # self.assertTrue(False)

    def test_assert_true(self):
        '''
            To check unittest framework
        '''
        pass
        self.assertTrue(True)

    def test_say_hello(self):
        '''
            Test say hello
        '''
        hello_message = alice.bob.say_hello()
        self.assertEqual(hello_message, 'Hello Alice')

        hello_message = alice.bob.say_hello('Bob')
        self.assertEqual(hello_message, 'Hello Bob')

    @responses.activate
    def test_get_json(self):
        responses.add(responses.GET,
                      'http://echo.jsontest.com/key/value/one/two',
                      json='{"one": "two","key": "value"}',
                      status=200,
                      content_type='application/json')

        the_json = alice.bob.get_json()
        expected = u'{"one": "two","key": "value"}'

        self.assertEqual(the_json, expected)

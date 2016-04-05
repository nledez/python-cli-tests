'''
    The alice.cli module tests
'''

import unittest
import mock

import alice.cli
from docopt import DocoptExit


class TestCli(unittest.TestCase):
    '''
        The cli module test
    '''

    @mock.patch('alice.bob.say_hello')
    def test_say_hello(self, mock_bob_hello):
        '''
            Test say hello
        '''
        parameters = ['hello']
        alice.cli.ARGV = parameters
        alice.cli.main()
        mock_bob_hello.assert_called_with()

        parameters = ['hello', '--name', 'Bob']
        alice.cli.ARGV = parameters
        alice.cli.main()
        mock_bob_hello.assert_called_with('Bob')

    @mock.patch('alice.bob.get_json')
    def test_say_json(self, mock_bob_json):
        '''
            Test get json
        '''
        parameters = ['json']
        alice.cli.ARGV = parameters
        alice.cli.main()
        mock_bob_json.assert_called_with()

    @mock.patch('alice.cli.docopt.extras')
    def test_show_help(self, mock_docopt):
        '''
            Test show help
        '''
        with self.assertRaises(DocoptExit):
            alice.cli.ARGV = None
            alice.cli.main()

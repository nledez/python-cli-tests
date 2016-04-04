'''
    lettuce steps
'''

# -*- coding: utf-8 -*-
from lettuce import step, world

import alice.cli

import responses


@step(u'Given I have no parameter')
def given_i_have_no_parameter(step):
    world.parameters = None


@step(u'Given I have \'([^\']*)\'')
def given_i_have_group1(step, name):
    world.parameters = name


@step(u'When I launch command line with hello command')
def when_i_launch_command_line(step):
    world.command_line = ['hello']
    if world.parameters:
        world.command_line += world.parameters.split(' ')

    world.stdout = None

    import iocapture
    with iocapture.capture() as captured:
        alice.cli.test = ''
        alice.cli.ARGV = world.command_line
        alice.cli.main()
        world.stdout = captured.stdout


@step(u'Then I see the string \'([^\']*)\'')
def then_i_see_the_string_group1(step, expected):
    result = world.stdout.rstrip('\n')
    assert result == expected, \
        '\nGot:\t{}\nExpected:\t{}'.format(result, expected)


@step(u'When I launch command line with json command')
@responses.activate
def when_i_launch_command_line_with_json_command(step):
    responses.add(responses.GET,
                  'http://echo.jsontest.com/key/value/one/two',
                  json='{"one": "two","key": "value"}',
                  status=200,
                  content_type='application/json')
    world.command_line = ['json']

    world.stdout = None

    import iocapture
    with iocapture.capture() as captured:
        alice.cli.test = ''
        alice.cli.ARGV = world.command_line
        alice.cli.main()
        world.stdout = captured.stdout
    # import debug


@step(u'Then I see the string "([^"]*)"')
def then_i_see_the_string_group1(step, expected):
    result = world.stdout.rstrip('\n')
    assert result == expected, \
        '\nGot:\t{}\nExpected:\t{}'.format(result, expected)

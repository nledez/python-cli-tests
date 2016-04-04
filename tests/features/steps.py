'''
    lettuce steps
'''

# -*- coding: utf-8 -*-
from lettuce import step, world

import subprocess


@step(u'Given I have no parameter')
def given_i_have_no_parameter(step):
    world.parameters = None


@step(u'Given I have \'([^\']*)\'')
def given_i_have_group1(step, name):
    print name
    world.parameters = name


@step(u'When I launch command line with hello command')
def when_i_launch_command_line(step):
    world.command_line = './alice.py hello'
    if world.parameters:
        world.command_line += ' ' + world.parameters

    p = subprocess.Popen(world.command_line, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         close_fds=True)
    world.stdout, world.stderr = p.communicate()
    print world.stdout


@step(u'Then I see the string \'([^\']*)\'')
def then_i_see_the_string_group1(step, expected):
    result = world.stdout.rstrip('\n')
    assert result == expected, \
        'Got: {}\nExpected: {}'.format(result, expected)

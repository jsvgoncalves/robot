#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function
import robot.robot as t


def run_cmd(cmd, args):
    try:
        {
            'PLACE':
                lambda x: t.place(x) if t.is_valid(x) else print_error(cmd),
            'MOVE': lambda x: t.move(),
            'REPORT': lambda x: t.report(),
            'LEFT': lambda x: t.rotate(t.LEFT),
            'RIGHT': lambda x: t.rotate(t.RIGHT)
        }[cmd](args)
    except KeyError:
        print_error(cmd)


def print_error(cmd):
    print('Invalid command or movement:')
    print('\t{}'.format(cmd))


def parse_cmds(cmds):
    """Parse the received input and returned a list of commands."""
    input = iter(cmds.split())
    parsed = []
    while True:
        cmd = next(input, None)
        if cmd is None:
            break
        elif cmd == 'PLACE':
            parsed.append(('PLACE', next(input, None)))
        else:
            parsed.append((cmd, None))
    return parsed


if __name__ == '__main__':
    while True:
        cmd = raw_input('> ')
        cmds = parse_cmds(cmd)
        for c in cmds:
            run_cmd(c[0], c[1])

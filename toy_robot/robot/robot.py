#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import print_function

robot = [0, 0, '']
placed = False
MAX_X = 5
MAX_Y = 5
LEFT = -1
RIGHT = 1


def rotate(direction):
    """Rotate the robot."""
    if not placed:
        return
    global robot
    robot[2] = {
        'NORTH': lambda x: 'EAST' if direction == RIGHT else 'WEST',
        'EAST': lambda x: 'SOUTH' if direction == RIGHT else 'NORTH',
        'SOUTH': lambda x: 'WEST' if direction == RIGHT else 'EAST',
        'WEST': lambda x: 'NORTH' if direction == RIGHT else 'SOUTH'
    }[robot[2]](direction)


def place(v):
    """Place the robot."""
    global robot
    global placed
    placed = True
    robot = [v[0], v[2], v[4:]]


def move():
    """Move the robot."""
    if not placed:
        return
    global robot
    r = {
        'NORTH': lambda x, y: '{},{}'.format(x, int(y) + 1),
        'SOUTH': lambda x, y: '{},{}'.format(x, int(y) - 1),
        'EAST': lambda x, y: '{},{}'.format(int(x) + 1, y),
        'WEST': lambda x, y: '{},{}'.format(int(x) - 1, y)
    }[robot[2]](robot[0], robot[1])

    if is_valid(r):
        robot[0] = r[0]
        robot[1] = r[2]


def report():
    """Pretty print robot."""
    if not placed:
        print('Robot not placed')
        return
    global robot
    print('OUPUT: {},{},{}'.format(robot[0], robot[1], robot[2]))


def is_valid(cmd):
    """Check whether the position is valid."""
    # Make sure we have integers
    x = int(cmd[0])
    y = int(cmd[2])
    return not (x < 0 or x > MAX_X or y < 0 or y > MAX_Y)

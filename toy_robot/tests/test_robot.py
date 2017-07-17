# a) PLACE 0,0,NORTH MOVE REPORT Output: 0,1,NORTH

# b) PLACE 0,0,NORTH LEFT REPORT Output: 0,0,WEST

# c) PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT Output: 3,3,NORTH
# PLACE 0,0,NORTH MOVE REPORT

# -*- coding: utf-8 -*-
#

"""Module tests."""

from __future__ import absolute_import, print_function
import robot.robot as t


def test_place():
    """Test robot initialization."""
    assert t.placed is False
    assert t.robot == [0, 0, '']

    # The robot doesn't move before it's placed
    t.move()
    assert t.robot == [0, 0, '']

    # Move the robot
    new = '0,0,NORTH'
    t.place(new)
    assert t.robot == ['0', '0', 'NORTH']


def test_rotate():
    """Test all rotations of the robot."""
    assert t.placed is True
    new = '0,0,SOUTH'
    t.place(new)
    t.rotate(t.LEFT)
    assert t.robot[2] == 'EAST'
    t.rotate(t.LEFT)
    assert t.robot[2] == 'NORTH'
    t.rotate(t.LEFT)
    assert t.robot[2] == 'WEST'
    t.rotate(t.LEFT)
    assert t.robot[2] == 'SOUTH'

    t.rotate(t.RIGHT)
    assert t.robot[2] == 'WEST'
    t.rotate(t.RIGHT)
    assert t.robot[2] == 'NORTH'
    t.rotate(t.RIGHT)
    assert t.robot[2] == 'EAST'
    t.rotate(t.RIGHT)
    assert t.robot[2] == 'SOUTH'


def test_move():
    """Test that the robot moves in the correct direction."""
    new = '0,0,NORTH'
    t.place(new)
    t.move()
    assert t.robot[0] == '0'
    assert t.robot[1] == '1'


def test_boundaries():
    """Test that the robot doesn't move beyond the boundaries."""
    new = '4,5,NORTH'
    t.place(new)
    assert t.robot[0] == '4'
    assert t.robot[1] == '5'
    t.move()
    assert t.robot[0] == '4'
    assert t.robot[1] == '5'

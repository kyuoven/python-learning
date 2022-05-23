from nose.tools import *
from memeweb import Room


def test_room():
    gold = Room(
        "GoldRoom",
        """This room has gold in it you can grab.
                This door leads to the North.""",
    )
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    right = Room("Right", "Test room on the right.")
    left = Room("Left", "Test room on the left.")
    middle = Room("Middle", "Test room in the middle.")

    center.add_paths({"right": right, "left": left, "middle": middle})
    assert_equal(center.go("right"), right)
    assert_equal(center.go("left"), left)
    assert_equal(center.go("middle"), middle)


def test_map():
    start = Room("Start", "You can go to the left, middle and right.")
    left = Room("Left", "Djungelskog is here.")
    middle = Room("Middle", "You are trapped here with Elon Musk")
    right = Room("Right", "It's dark, and there is an imposter here")

    start.add_paths({"left": left, "middle": middle, "right": right})
    left.add_paths({"back": start})
    middle.add_paths({"back": start})
    right.add_paths({"back": start})

    assert_equal(start.go("left"), left)
    assert_equal(start.go("middle").go("back"), start)
    assert_equal(start.go("right").go("back"), start)

from um import count

def test_count():
    assert count("") == 0
    assert count(" ") == 0
    assert count("Hey, um, what's up?") == 1
    assert count("Um, do you know how to play the drums?") == 1
    assert count("Um, thanks for the, um...album") == 2

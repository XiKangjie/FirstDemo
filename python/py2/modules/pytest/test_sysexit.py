import pytest

# If you want to assert that some code raises an exception you can use the raises helper:

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()

"""
Run in "quiet" reporting mode:

$ py.test -q test_sysexit.py
.
1 passed in 0.12 seconds
"""

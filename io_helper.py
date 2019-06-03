import sys
from io import StringIO


def set_new(in_str: str):  # pragma: no cover
    temp = [sys.stdin, sys.stdout]

    sys.stdin = StringIO(in_str)
    sys.stdout = StringIO()

    return temp


def set_former(io_streams):  # pragma: no cover
    sys.stdin = io_streams[0]
    sys.stdout = io_streams[1]

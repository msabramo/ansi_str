import re

_ansi_re = re.compile('\033\[((?:\d|;)*)([a-zA-Z])')


def strip_ansi(value):
    return _ansi_re.sub('', value)


class Printable(str):
    """A printable string

    When you call the ``len`` method, it discounts ANSI color escape codes.
    This is beneficial, because ANSI color escape codes won't mess up code
    that tries to do alignment, padding, printing in columns, etc.

    """
    def __init__(self, s):
        self._stripped = strip_ansi(s)

    def __len__(self):
        return len(self._stripped)

# s = Printable('abc')
# print s
# print len(s)

s = Printable(u'\x1b[32m\x1b[1mSUCCESS\x1b[0m')
print s
print len(s)

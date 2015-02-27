import re

_ansi_re = re.compile('\033\[((?:\d|;)*)([a-zA-Z])')


def strip_ansi(value):
    return _ansi_re.sub('', value)


def len_exclude_ansi(value):
    return len(strip_ansi(value))


class ansi_str(str):
    """A str subclass, specialized for strings containing ANSI escapes.

    When you call the ``len`` method, it discounts ANSI color escape codes.
    This is beneficial, because ANSI color escape codes won't mess up code
    that tries to do alignment, padding, printing in columns, etc.

    """
    _stripped = None

    @property
    def stripped(self):
        if self._stripped is None:
            self._stripped = strip_ansi(self[:])
        return self._stripped

    def __len__(self, exclude_ansi=True):
        if exclude_ansi is False:
            return len(self[:])
        return len(self.stripped)

    def ljust(self, width):
        return self.stripped.ljust(width).replace(self.stripped, self)

    def rjust(self, width):
        return self.stripped.rjust(width).replace(self.stripped, self)

    def center(self, width):
        return self.stripped.center(width).replace(self.stripped, self)

    def lstrip(self):
        return ansi_str(super(ansi_str, self).lstrip())

    def rstrip(self):
        return ansi_str(super(ansi_str, self).rstrip())

    def strip(self):
        return ansi_str(super(ansi_str, self).strip())


if __name__ == '__main__':
    # s = ansi_str('abc')
    # print s
    # print len(s)

    s = ansi_str(u'\x1b[32m\x1b[1mSUCCESS\x1b[0m')
    print s
    print len(s)
    print s.__len__()
    print s.__len__(exclude_ansi=False)
    print(len_exclude_ansi(u'\x1b[32m\x1b[1mSUCCESS\x1b[0m'))

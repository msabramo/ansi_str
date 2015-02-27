ansi_str
========

An experimental Python ``str`` subclass, whose ``__len__`` method excludes ANSI
color escape codes

When you call the ``__len__`` method, it discounts ANSI color escape codes.
This is beneficial, because ANSI color escape codes won't mess up code that
tries to do alignment, padding, printing in columns/tables, etc.

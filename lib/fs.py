# encoding=UTF-8

# Copyright © 2009-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

'''filesystem functions'''

import os

_block_size = 1 << 20  # 1 MiB

def copy_file(input_file, output_file):
    length = 0
    while 1:
        block = input_file.read(_block_size)
        if not block:
            break
        length += len(block)
        output_file.write(block)
    return length

def replace_ext(filename, ext):
    return '%s.%s' % (os.path.splitext(filename)[0], ext)

# vim:ts=4 sts=4 sw=4 et

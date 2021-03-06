#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from subprocess import check_output
from sys import argv

if len(argv) > 1:
    with open('sp.log', mode='at',) as f:
        try:
            f.write(check_output(argv[1:]).decode())
        except Exception as e:
            print(e)

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import subprocess

s = subprocess.run('dir', shell=True, capture_output=True)
print(s.stdout)
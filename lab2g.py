#!/usr/bin/env python3

import sys

# Author: Zhaofa Zhang
# Author ID: 142954221
# Date Created: 2024/09/24

if len(sys.argv) != 2:
    timer = 3
else:

    timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print('blast off!')

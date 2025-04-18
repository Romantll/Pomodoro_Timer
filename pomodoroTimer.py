#!/usr/bin/env python3
import time
import sys
import os
from mainMenu import main_menu

#elapsed_time = time.time()
long_work_time = 50 * 60  # 50 minutes in seconds
short_work_time = 25 * 60  # 25 minutes in seconds
five_break_time = 5 * 60  # 5 minutes in seconds
fifteen_break_time = 15 * 60  # 15 minutes in seconds
ten_break_time = 10 * 60  # 10 minutes in seconds
cycles = 0
long_break_after = 4  # Number of cycles before a long break
print("Before main_menu()")
main_menu()
print("After main_menu()")


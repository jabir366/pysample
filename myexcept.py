#!/usr/bin/python3
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except Exception as e:
    print(f"Unexpected error: {e}", sys.exc_info()[0])
    raise

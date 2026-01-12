#!/usr/bin/python3
for d1 in range(10):
    for d2 in range(d1+1, 10):
        print("{:d}{:d}".format(d1, d2), end=", " if d2 < 9 or d1 < 8 else "\n")
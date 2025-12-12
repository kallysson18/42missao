#!/usr/bin/env python3
i = 0
while i <= 10:
    print(f"Table of {i}:", end=" ")
    
    multiplier = 0
    while multiplier <= 10:
        print(i * multiplier , end=" ")
        multiplier += 1
    print()
    i += 1 
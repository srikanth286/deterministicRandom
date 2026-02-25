#!/usr/bin/env python3
"""
Deterministic random number generator that outputs a stream of 1s followed by 0s.
This can be used to replace /dev/urandom for testing purposes.
"""

import sys
import os
import time

def generate_deterministic_random(count=1024):
    """
    Generate a deterministic stream of bytes:
    - First outputs 'count' bytes of 0xAA (pattern 10101010)
    - Repeats indefinitely
    """
    block = bytes([0xAA] * count)
    
    while True:
        try:
            # Write block of 1s n 0s
            sys.stdout.buffer.write(block)
            sys.stdout.buffer.flush()
            time.sleep(1)
        except (BrokenPipeError, KeyboardInterrupt):
            continue


if __name__ == "__main__":
    # You can customize the block sizes via environment variables
    count = int(os.environ.get('COUNT', 1024))
    
    generate_deterministic_random(count)


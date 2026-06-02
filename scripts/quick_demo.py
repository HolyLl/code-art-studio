#!/usr/bin/env python3
"""
Quick demo script for Code Art Studio
Run this to see all art styles in action
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ascii_art import code_to_ascii_portrait, code_to_pixel_art, code_to_braille, code_to_wave

# Sample code for demonstration
SAMPLE_CODE = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

# Main program
calc = Calculator()
print(calc.add(5, 3))
"""


def run_demo():
    """Run all art style demos"""
    print("=" * 70)
    print("CODE ART STUDIO - QUICK DEMO")
    print("=" * 70)
    
    # ASCII Art Portrait
    print("\n[1] ASCII ART PORTRAIT")
    print("-" * 70)
    print(code_to_ascii_portrait(SAMPLE_CODE, width=60, height=15))
    
    # Pixel Art
    print("\n[2] PIXEL ART")
    print("-" * 70)
    print(code_to_pixel_art(SAMPLE_CODE, scale=3))
    
    # Dot Pattern (Braille-style)
    print("\n[3] DOT PATTERN ART")
    print("-" * 70)
    print(code_to_braille(SAMPLE_CODE, width=50, height=12))
    
    # Wave Pattern
    print("\n[4] WAVE PATTERN")
    print("-" * 70)
    print(code_to_wave(SAMPLE_CODE, width=50, height=10))
    
    print("\n" + "=" * 70)
    print("DEMO COMPLETE!")
    print("=" * 70)
    print("\nTo try with your own code:")
    print("  python scripts/main.py --style ascii --file your_code.py")
    print("  python scripts/main.py --style matrix --file your_code.py")
    print("\nFor more options:")
    print("  python scripts/main.py --help")


if __name__ == "__main__":
    run_demo()

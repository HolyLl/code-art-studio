#!/usr/bin/env python3
"""
Code Art Studio - Complete Demo
This script demonstrates all available art styles
"""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ascii_art import code_to_ascii_portrait, code_to_pixel_art, code_to_braille, code_to_wave

# Sample code for demonstration
SAMPLE_CODE = """
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.processed = []
    
    def filter(self, condition):
        return [x for x in self.data if condition(x)]
    
    def transform(self, func):
        self.processed = [func(x) for x in self.data]
        return self.processed
    
    def aggregate(self, func):
        if not self.processed:
            return None
        return func(self.processed)

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])
result = processor.transform(lambda x: x ** 2)
print(f"Squared: {result}")
"""


def display_header(title):
    """Display formatted header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def main():
    """Run complete demonstration"""
    print("CODE ART STUDIO - COMPLETE DEMONSTRATION")
    print("=" * 70)
    print("Transforming sample code into various art styles...")
    
    # ASCII Art Portrait
    display_header("1. ASCII ART PORTRAIT")
    print("Best for: Code visualization, documentation, social media")
    print("-" * 70)
    print(code_to_ascii_portrait(SAMPLE_CODE, width=60, height=15))
    
    # Pixel Art
    display_header("2. PIXEL ART (8-BIT STYLE)")
    print("Best for: Retro aesthetics, game-themed presentations")
    print("-" * 70)
    print(code_to_pixel_art(SAMPLE_CODE, scale=3))
    
    # Dot Pattern Art
    display_header("3. DOT PATTERN ART (BRAILLE-STYLE)")
    print("Best for: High-density visualization, artistic effects")
    print("-" * 70)
    print(code_to_braille(SAMPLE_CODE, width=50, height=12))
    
    # Wave Pattern
    display_header("4. WAVE PATTERN")
    print("Best for: Animated effects, creative presentations")
    print("-" * 70)
    print(code_to_wave(SAMPLE_CODE, width=50, height=10))
    
    # Summary
    display_header("USAGE EXAMPLES")
    print("""
To use these art styles with your own code:

  # ASCII Art
  python scripts/main.py --style ascii --file your_code.py

  # Pixel Art
  python scripts/main.py --style pixel --file your_code.py --scale 2

  # Dot Pattern
  python scripts/main.py --style braille --file your_code.py

  # Wave Pattern
  python scripts/main.py --style wave --file your_code.py

  # Save to file
  python scripts/main.py --style ascii --file your_code.py --output art.txt
    """)
    
    print("=" * 70)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 70)
    print("\nYour code can now be transformed into beautiful visual art!")
    print("Use this skill to create shareable content for social media,")
    print("presentations, or just for fun!\n")


if __name__ == "__main__":
    main()

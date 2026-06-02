#!/usr/bin/env python3
"""
Code Art Studio - Main Entry Point
Transform code into stunning visual art
"""

import argparse
import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from matrix_rain import matrix_rain, generate_sample_code
from ascii_art import (
    code_to_ascii_portrait,
    code_to_pixel_art,
    code_to_braille,
    code_to_wave
)


def main():
    parser = argparse.ArgumentParser(
        description="Code Art Studio - Transform code into visual art",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --style matrix --file mycode.py
  %(prog)s --style ascii --file mycode.py --width 80
  %(prog)s --style pixel --file mycode.py --scale 3
  %(prog)s --style demo
        """
    )
    
    parser.add_argument(
        '--style', '-s',
        choices=['matrix', 'ascii', 'pixel', 'braille', 'wave', 'demo'],
        default='demo',
        help='Art style to apply (default: demo)'
    )
    
    parser.add_argument(
        '--file', '-f',
        help='Input code file'
    )
    
    parser.add_argument(
        '--width', '-W',
        type=int,
        default=60,
        help='Output width (default: 60)'
    )
    
    parser.add_argument(
        '--height', '-H',
        type=int,
        default=20,
        help='Output height (default: 20)'
    )
    
    parser.add_argument(
        '--scale',
        type=int,
        default=2,
        help='Pixel scale factor (default: 2)'
    )
    
    parser.add_argument(
        '--duration', '-d',
        type=float,
        default=5,
        help='Animation duration in seconds (default: 5)'
    )
    
    parser.add_argument(
        '--fps',
        type=int,
        default=20,
        help='Frames per second for animations (default: 20)'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='Output file (default: stdout)'
    )
    
    args = parser.parse_args()
    
    # Load code
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                code = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    else:
        code = generate_sample_code()
    
    # Generate art
    if args.style == 'demo':
        print("Code Art Studio - Demo Mode")
        print("=" * 60)
        
        print("\n[1] Matrix Rain Effect")
        print("-" * 40)
        print("Run with: --style matrix --file <your_code.py>")
        
        print("\n[2] ASCII Art Portrait")
        print("-" * 40)
        print(code_to_ascii_portrait(code, args.width, args.height))
        
        print("\n[3] Pixel Art")
        print("-" * 40)
        print(code_to_pixel_art(code, args.scale))
        
        print("\n[4] Braille Art")
        print("-" * 40)
        print(code_to_braille(code, args.width, args.height))
        
        print("\n[5] Wave Pattern")
        print("-" * 40)
        print(code_to_wave(code, args.width, args.height))
        
        print("\n" + "=" * 60)
        print("Use --style <style> to apply specific art style")
        print("Available styles: matrix, ascii, pixel, braille, wave")
    
    elif args.style == 'matrix':
        print("Starting Matrix Rain Effect...")
        print("Press Ctrl+C to stop\n")
        try:
            matrix_rain(code, args.width, args.height, args.duration, args.fps)
        except KeyboardInterrupt:
            print("\n\nMatrix rain stopped.")
    
    elif args.style == 'ascii':
        result = code_to_ascii_portrait(code, args.width, args.height)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"ASCII art saved to {args.output}")
        else:
            print(result)
    
    elif args.style == 'pixel':
        result = code_to_pixel_art(code, args.scale)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Pixel art saved to {args.output}")
        else:
            print(result)
    
    elif args.style == 'braille':
        result = code_to_braille(code, args.width, args.height)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Braille art saved to {args.output}")
        else:
            print(result)
    
    elif args.style == 'wave':
        result = code_to_wave(code, args.width, args.height)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Wave pattern saved to {args.output}")
        else:
            print(result)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Matrix Code Rain Effect
Transform any code into the iconic falling green characters from The Matrix
"""

import random
import time
import sys
import os

def matrix_rain(code_text, width=80, height=24, duration=10, fps=30):
    """
    Generate Matrix rain effect from source code
    
    Args:
        code_text: Source code to transform
        width: Terminal width
        height: Terminal height
        duration: Animation duration in seconds
        fps: Frames per second
    """
    # Extract characters from code
    chars = list(code_text)
    if not chars:
        chars = list("abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*")
    
    # Matrix green shades
    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[92m"
    RESET = "\033[0m"
    
    # Initialize columns
    columns = []
    for x in range(width):
        columns.append({
            'x': x,
            'y': random.randint(-height, 0),
            'speed': random.uniform(0.3, 1.0),
            'char': random.choice(chars),
            'trail': []
        })
    
    # Animation loop
    frames = int(duration * fps)
    for frame in range(frames):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Build screen buffer
        screen = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Update and render columns
        for col in columns:
            # Update position
            col['y'] += col['speed']
            
            # Reset if off screen
            if col['y'] >= height:
                col['y'] = random.randint(-5, 0)
                col['char'] = random.choice(chars)
            
            # Draw character
            y = int(col['y'])
            if 0 <= y < height:
                screen[y][col['x']] = col['char']
                
                # Draw trail
                for trail_len in range(1, 5):
                    trail_y = y - trail_len
                    if 0 <= trail_y < height:
                        screen[trail_y][col['x']] = col['char']
        
        # Render frame
        print(f"{GREEN}", end='')
        for row in screen:
            print(''.join(row))
        print(f"{RESET}", end='', flush=True)
        
        # Frame delay
        time.sleep(1 / fps)
    
    print(f"\n{BRIGHT_GREEN}Matrix rain complete!{RESET}")


def generate_sample_code():
    """Generate sample code for demonstration"""
    return """
def hello_world():
    print("Hello, World!")
    return 42

class MatrixAgent:
    def __init__(self, name):
        self.name = name
        self.skills = ['code', 'art', 'rain']
    
    def transform(self, code):
        return matrix_rain(code)

if __name__ == "__main__":
    agent = MatrixAgent("Neo")
    agent.transform("print('Follow the white rabbit')")
"""


if __name__ == "__main__":
    # Demo mode
    print("Matrix Code Rain Demo")
    print("=" * 40)
    
    code = generate_sample_code()
    print(f"Transforming {len(code)} characters into Matrix rain...")
    print("Press Ctrl+C to stop\n")
    
    try:
        matrix_rain(code, width=60, height=20, duration=5, fps=20)
    except KeyboardInterrupt:
        print("\n\nMatrix rain stopped.")

#!/usr/bin/env python3
"""
ASCII Art Generator
Transform code into various ASCII art styles
"""

import random

# ASCII art character sets
DENSITY_CHARS = "@%#*+=-:. "
BLOCK_CHARS = "#*=- "
BOX_CHARS = "+-|"

def code_to_ascii_portrait(code_text, width=60, height=20):
    """
    Convert code into ASCII art portrait
    
    Args:
        code_text: Source code to transform
        width: Output width
        height: Output height
    
    Returns:
        ASCII art string
    """
    lines = code_text.split('\n')
    
    # Calculate code metrics
    metrics = []
    for line in lines:
        if not line.strip():
            metrics.append(0)
            continue
        
        # Complexity score
        indent = len(line) - len(line.lstrip())
        length = len(line.strip())
        has_keyword = any(kw in line for kw in ['def', 'class', 'if', 'for', 'while', 'return'])
        has_string = '"' in line or "'" in line
        
        score = (length / 80) * 0.5
        if has_keyword:
            score += 0.3
        if has_string:
            score += 0.2
        score += (indent / 20) * 0.1
        
        metrics.append(min(1.0, score))
    
    # Generate ASCII art
    art_lines = []
    for i, score in enumerate(metrics[:height]):
        if score == 0:
            art_lines.append(" " * width)
            continue
        
        char_idx = int(score * (len(DENSITY_CHARS) - 1))
        char = DENSITY_CHARS[min(char_idx, len(DENSITY_CHARS) - 1)]
        
        # Create pattern
        pattern_length = int(score * width)
        padding = (width - pattern_length) // 2
        
        line = " " * padding + char * pattern_length
        art_lines.append(line[:width].ljust(width))
    
    return '\n'.join(art_lines)


def code_to_pixel_art(code_text, scale=2):
    """
    Convert code into pixel art blocks
    
    Args:
        code_text: Source code to transform
        scale: Pixel size (1-4)
    
    Returns:
        Pixel art string
    """
    lines = code_text.split('\n')
    pixel_art = []
    
    for line in lines:
        if not line.strip():
            pixel_art.append("  " * 20)
            continue
        
        # Analyze line
        indent = len(line) - len(line.lstrip())
        has_keyword = any(kw in line for kw in ['def', 'class', 'if', 'for', 'while', 'return'])
        has_string = '"' in line or "'" in line
        has_comment = '#' in line
        
        # Choose block
        if has_keyword:
            block = "##"
        elif has_string:
            block = "**"
        elif has_comment:
            block = "::"
        else:
            block = "=="
        
        # Create pixel row
        pixels = "  " * (indent // 2) + block * (len(line.strip()) // scale)
        pixel_art.append(pixels)
    
    return '\n'.join(pixel_art)


def code_to_braille(code_text, width=40, height=20):
    """
    Convert code into dot pattern art (braille-style but ASCII compatible)
    
    Args:
        code_text: Source code to transform
        width: Output width
        height: Output height
    
    Returns:
        Dot pattern art string
    """
    lines = code_text.split('\n')
    
    # Create binary pattern from code
    pattern = []
    for y in range(height * 2):
        row = []
        for x in range(width):
            line_idx = y % len(lines)
            char_idx = x % max(len(lines[line_idx]), 1)
            
            if line_idx < len(lines) and char_idx < len(lines[line_idx]):
                char = lines[line_idx][char_idx]
                row.append(1 if char.strip() else 0)
            else:
                row.append(0)
        pattern.append(row)
    
    # Convert to dot pattern
    dot_art = []
    for by in range(height):
        row = ""
        for bx in range(width):
            # Get 2x2 block
            dots = 0
            for dy in range(2):
                for dx in range(1):
                    py = by * 2 + dy
                    px = bx + dx
                    if py < len(pattern) and px < len(pattern[py]):
                        if pattern[py][px]:
                            dots += 1
            
            # Choose character based on density
            if dots == 0:
                row += " "
            elif dots == 1:
                row += "."
            else:
                row += ":"
        dot_art.append(row)
    
    return '\n'.join(dot_art)


def code_to_wave(code_text, width=60, height=15, frequency=0.2):
    """
    Create wave pattern from code
    
    Args:
        code_text: Source code to transform
        width: Output width
        height: Output height
        frequency: Wave frequency
    
    Returns:
        Wave art string
    """
    import math
    
    chars = list(code_text)
    if not chars:
        chars = list("~-~")
    
    frames = []
    for frame in range(1):
        screen = []
        for y in range(height):
            row = ""
            for x in range(width):
                # Calculate wave position
                wave_y = math.sin((x + frame * 5) * frequency) * (height / 4)
                target_y = height // 2 + int(wave_y)
                
                if y == target_y:
                    char_idx = (x + frame * 10) % len(chars)
                    row += chars[char_idx]
                else:
                    row += " "
            screen.append(row)
        frames.append('\n'.join(screen))
    
    return frames[0]


def generate_demo():
    """Generate demo ASCII art"""
    sample_code = """
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
    
    print("=" * 60)
    print("ASCII ART PORTrait")
    print("=" * 60)
    print(code_to_ascii_portrait(sample_code))
    
    print("\n" + "=" * 60)
    print("PIXEL ART")
    print("=" * 60)
    print(code_to_pixel_art(sample_code))
    
    print("\n" + "=" * 60)
    print("BRAILLE ART")
    print("=" * 60)
    print(code_to_braille(sample_code))
    
    print("\n" + "=" * 60)
    print("WAVE PATTERN")
    print("=" * 60)
    print(code_to_wave(sample_code))


if __name__ == "__main__":
    generate_demo()

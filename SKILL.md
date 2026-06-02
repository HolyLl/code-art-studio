---
name: code-art-studio
description: Transform code into stunning visual art styles including ASCII art, Matrix rain, pixel art, and more. Use when user wants to visualize code creatively, generate terminal art, create code-based animations, or make shareable visual content from source code.
---

# Code Art Studio

Transform ordinary code into extraordinary visual art. This skill enables creation of stunning terminal-based visuals, ASCII art reconstructions, and animated code displays that are perfect for social media, presentations, or just pure creative expression.

## Supported Art Styles

### 1. Matrix Code Rain
Convert code into the iconic falling green characters from The Matrix.

**When to use**: User wants "matrix style", "hacker aesthetic", "code rain", "green falling code"

**Implementation**:
```python
# Generate Matrix rain effect from source code
import random
import time

def matrix_rain(code_lines, width=80, height=24):
    """Transform code into Matrix-style falling characters"""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*(){}[]|;:,.<>?"
    
    # Extract meaningful tokens from code
    tokens = []
    for line in code_lines:
        tokens.extend(list(line.strip()))
    
    if not tokens:
        tokens = list(chars)
    
    # Create rain columns
    columns = []
    for x in range(width):
        speed = random.uniform(0.1, 0.5)
        start_y = random.randint(-height, 0)
        columns.append({"x": x, "y": start_y, "speed": speed, "char": random.choice(tokens)})
    
    return columns

def render_frame(columns, width, height, frame):
    """Render a single frame of Matrix rain"""
    screen = [[" " for _ in range(width)] for _ in range(height)]
    
    for col in columns:
        y = int(col["y"] + frame * col["speed"])
        if 0 <= y < height:
            screen[y][col["x"]] = col["char"]
            # Add trail effect
            for trail in range(1, 4):
                trail_y = y - trail
                if 0 <= trail_y < height:
                    brightness = max(0, 255 - trail * 60)
                    screen[trail_y][col["x"]] = col["char"]
    
    return "\n".join(["".join(row) for row in screen])
```

### 2. ASCII Art Portrait
Convert images or code structure into ASCII art portraits.

**When to use**: User wants "ascii art", "text art", "character art", "code portrait"

**Implementation**:
```python
ASCII_CHARS = "@%#*+=-:. "

def code_to_ascii(code_text, width=60):
    """Convert code text into ASCII art representation"""
    # Calculate density from code complexity
    lines = code_text.split('\n')
    density_map = []
    
    for line in lines:
        # Measure line complexity
        complexity = len(line.strip()) / max(len(line), 1)
        indent = len(line) - len(line.lstrip())
        density_map.append((complexity, indent))
    
    # Generate ASCII art
    ascii_art = []
    for i, (complexity, indent) in enumerate(density_map):
        char_idx = int(complexity * (len(ASCII_CHARS) - 1))
        char = ASCII_CHARS[min(char_idx, len(ASCII_CHARS) - 1)]
        
        # Create visual pattern
        pattern = " " * indent + char * int(complexity * 20)
        ascii_art.append(pattern)
    
    return "\n".join(ascii_art)
```

### 3. Pixel Art Generator
Transform code into retro pixel art style blocks.

**When to use**: User wants "pixel art", "retro style", "8-bit", "block art", "minecraft style"

**Implementation**:
```python
PIXEL_BLOCKS = {
    "empty": "  ",
    "light": "░░",
    "medium": "▒▒",
    "dark": "▓▓",
    "solid": "██"
}

def code_to_pixel_art(code_lines, scale=2):
    """Convert code into pixel art block representation"""
    pixel_art = []
    
    for line in code_lines:
        if not line.strip():
            pixel_art.append(PIXEL_BLOCKS["empty"] * 20)
            continue
        
        # Analyze code structure
        indent = len(line) - len(line.lstrip())
        has_keyword = any(kw in line.lower() for kw in ['def', 'class', 'if', 'for', 'while', 'return'])
        has_string = '"' in line or "'" in line
        has_comment = '#' in line
        
        # Choose block style based on code type
        if has_keyword:
            block = PIXEL_BLOCKS["dark"]
        elif has_string:
            block = PIXEL_BLOCKS["medium"]
        elif has_comment:
            block = PIXEL_BLOCKS["light"]
        else:
            block = PIXEL_BLOCKS["solid"]
        
        # Create pixel row
        pixels = " " * indent + block * (len(line.strip()) // scale)
        pixel_art.append(pixels)
    
    return "\n".join(pixel_art)
```

### 4. Syntax Highlighting Art
Create visually stunning syntax-highlighted terminal output.

**When to use**: User wants "syntax highlight", "colorful code", "terminal colors", "pretty print"

**Implementation**:
```python
# ANSI Color codes for syntax highlighting
COLORS = {
    "keyword": "\033[95m",    # Magenta
    "string": "\033[92m",     # Green
    "comment": "\033[90m",    # Gray
    "function": "\033[94m",   # Blue
    "number": "\033[93m",     # Yellow
    "operator": "\033[96m",   # Cyan
    "reset": "\033[0m"
}

KEYWORDS = ['def', 'class', 'if', 'else', 'elif', 'for', 'while', 'return', 'import', 'from', 'try', 'except', 'finally']

def highlight_code(code_line):
    """Apply syntax highlighting to a line of code"""
    result = ""
    i = 0
    
    while i < len(code_line):
        # Check for comments
        if code_line[i] == '#':
            result += COLORS["comment"] + code_line[i:] + COLORS["reset"]
            break
        
        # Check for strings
        if code_line[i] in '"\'':
            quote = code_line[i]
            end = code_line.find(quote, i + 1)
            if end != -1:
                result += COLORS["string"] + code_line[i:end+1] + COLORS["reset"]
                i = end + 1
                continue
        
        # Check for keywords
        word = ""
        j = i
        while j < len(code_line) and (code_line[j].isalnum() or code_line[j] == '_'):
            word += code_line[j]
            j += 1
        
        if word in KEYWORDS:
            result += COLORS["keyword"] + word + COLORS["reset"]
            i = j
            continue
        elif word and word[0].isupper():
            result += COLORS["function"] + word + COLORS["reset"]
            i = j
            continue
        elif word.isdigit():
            result += COLORS["number"] + word + COLORS["reset"]
            i = j
            continue
        
        # Default
        result += code_line[i]
        i += 1
    
    return result
```

### 5. Wave Animation
Create flowing wave patterns from code characters.

**When to use**: User wants "wave effect", "sine wave", "flowing animation", "text animation"

**Implementation**:
```python
import math

def code_wave(code_text, width=60, height=20, frequency=0.3, amplitude=3):
    """Create a wave animation from code text"""
    frames = []
    
    for frame in range(60):  # 60 frames for smooth animation
        screen = []
        
        for y in range(height):
            row = ""
            for x in range(width):
                # Calculate wave position
                wave_y = math.sin((x + frame * 2) * frequency) * amplitude
                char_y = height // 2 + int(wave_y)
                
                if y == char_y:
                    # Get character from code
                    char_idx = (x + frame * 10) % len(code_text)
                    row += code_text[char_idx]
                else:
                    row += " "
            
            screen.append(row)
        
        frames.append("\n".join(screen))
    
    return frames
```

### 6. Fractal Tree
Generate fractal tree patterns using code structure.

**When to use**: User wants "fractal", "tree art", "recursive art", "branching pattern"

**Implementation**:
```python
def fractal_tree(depth=5, angle=45, length=10, branch_char="*", leaf_char="o"):
    """Generate a fractal tree from code structure"""
    import math
    
    def draw_branch(x, y, angle, depth, length):
        if depth == 0:
            return [(x, y, leaf_char)]
        
        # Calculate end point
        end_x = x + length * math.cos(math.radians(angle))
        end_y = y - length * math.sin(math.radians(angle))
        
        points = [(x, y, branch_char)]
        
        # Draw branch line
        steps = int(length)
        for i in range(steps):
            px = x + (end_x - x) * i / steps
            py = y + (end_y - y) * i / steps
            points.append((int(px), int(py), branch_char))
        
        # Recurse for sub-branches
        points.extend(draw_branch(end_x, end_y, angle - 30, depth - 1, length * 0.7))
        points.extend(draw_branch(end_x, end_y, angle + 30, depth - 1, length * 0.7))
        
        return points
    
    # Generate tree
    points = draw_branch(20, 30, 90, depth, length)
    
    # Render to string
    canvas = [[" " for _ in range(40)] for _ in range(30)]
    for x, y, char in points:
        if 0 <= x < 40 and 0 <= y < 30:
            canvas[y][x] = char
    
    return "\n".join(["".join(row) for row in canvas])
```

### 7. Code Constellation
Map code elements to star constellation patterns.

**When to use**: User wants "constellation", "star map", "night sky", "space theme"

**Implementation**:
```python
def code_constellation(code_lines, width=60, height=25):
    """Map code structure to constellation patterns"""
    stars = []
    
    # Extract code elements as star positions
    for i, line in enumerate(code_lines):
        if not line.strip():
            continue
        
        # Position based on line properties
        x = (len(line) * 7 + i * 3) % width
        y = (i * 2 + len(line.strip())) % height
        
        # Star brightness based on code importance
        if any(kw in line for kw in ['def', 'class', 'function']):
            brightness = "★"  # Bright star
        elif any(kw in line for kw in ['if', 'for', 'while']):
            brightness = "◆"  # Medium star
        else:
            brightness = "·"  # Dim star
        
        stars.append((x, y, brightness))
    
    # Render constellation
    canvas = [[" " for _ in range(width)] for _ in range(height)]
    for x, y, char in stars:
        canvas[y][x] = char
    
    # Add connecting lines between nearby stars
    for i in range(len(stars) - 1):
        x1, y1, _ = stars[i]
        x2, y2, _ = stars[i + 1]
        
        # Simple line drawing
        if abs(x2 - x1) < 10 and abs(y2 - y1) < 5:
            steps = max(abs(x2 - x1), abs(y2 - y1))
            for step in range(steps):
                px = x1 + (x2 - x1) * step // max(steps, 1)
                py = y1 + (y2 - y1) * step // max(steps, 1)
                if 0 <= px < width and 0 <= py < height and canvas[py][px] == " ":
                    canvas[py][px] = "·"
    
    return "\n".join(["".join(row) for row in canvas])
```

### 8. Glitch Art
Create cyberpunk-style glitch effects from code.

**When to use**: User wants "glitch", "cyberpunk", "corrupted", "distorted", "VHS effect"

**Implementation**:
```python
import random

def glitch_art(code_text, intensity=0.3):
    """Apply glitch effects to code text"""
    glitch_chars = "█▓░▒╬╠╣╩╦║═┌┐└┘├┤┬┴┼"
    result = []
    
    for line in code_text.split('\n'):
        if random.random() < intensity:
            # Apply random glitch
            glitch_type = random.choice(['shift', 'corrupt', 'duplicate', 'invert'])
            
            if glitch_type == 'shift':
                # Horizontal shift
                shift = random.randint(-5, 5)
                line = " " * abs(shift) + line if shift > 0 else line[abs(shift):]
            
            elif glitch_type == 'corrupt':
                # Character corruption
                line_list = list(line)
                for i in range(len(line_list)):
                    if random.random() < 0.1:
                        line_list[i] = random.choice(glitch_chars)
                line = "".join(line_list)
            
            elif glitch_type == 'duplicate':
                # Line duplication
                result.append(line)
            
            elif glitch_type == 'invert':
                # Color inversion effect
                line = f"\033[7m{line}\033[0m"
        
        result.append(line)
    
    return "\n".join(result)
```

### 9. QR Code Art
Convert code snippets into QR-code-like patterns.

**When to use**: User wants "qr code", "matrix barcode", "data pattern", "scannable art"

**Implementation**:
```python
def code_qr_pattern(code_text, size=21):
    """Generate QR-code-like pattern from code"""
    # Simple hash-based pattern generation
    hash_val = hash(code_text)
    
    # Create QR-like matrix
    matrix = []
    for y in range(size):
        row = []
        for x in range(size):
            # Position patterns (like real QR codes)
            if (x < 7 and y < 7) or (x >= size-7 and y < 7) or (x < 7 and y >= size-7):
                # Finder patterns
                if (x in [0,1,2,4,5,6] and y in [0,1,2,4,5,6]) or (x == 3 and y in range(7)) or (y == 3 and x in range(7)):
                    row.append("██")
                else:
                    row.append("  ")
            else:
                # Data area - use code hash
                bit = (hash_val >> ((x * size + y) % 64)) & 1
                row.append("██" if bit else "  ")
        
        matrix.append("".join(row))
    
    return "\n".join(matrix)
```

### 10. Mandala Pattern
Generate sacred geometry mandala patterns from code.

**When to use**: User wants "mandala", "sacred geometry", "circular pattern", "meditation art"

**Implementation**:
```python
import math

def code_mandala(code_text, radius=15, segments=8):
    """Generate mandala pattern from code structure"""
    size = radius * 2 + 1
    canvas = [[" " for _ in range(size)] for _ in range(size)]
    center = radius
    
    # Extract characters from code
    chars = [c for c in code_text if c.strip()]
    if not chars:
        chars = list("OM::")
    
    # Generate mandala arms
    for angle in range(0, 360, 360 // segments):
        rad = math.radians(angle)
        
        for r in range(1, radius):
            x = center + int(r * math.cos(rad))
            y = center + int(r * math.sin(rad))
            
            if 0 <= x < size and 0 <= y < size:
                char_idx = (r + angle // 10) % len(chars)
                canvas[y][x] = chars[char_idx]
                
                # Add symmetry
                mirror_x = center - int(r * math.cos(rad))
                if 0 <= mirror_x < size:
                    canvas[y][mirror_x] = chars[char_idx]
    
    return "\n".join(["".join(row) for row in canvas])
```

## Usage Examples

### Basic Matrix Rain
```
User: "Make my Python code look like Matrix rain"
Agent: [Transforms code into Matrix-style falling characters with green terminal output]
```

### ASCII Art Portrait
```
User: "Convert this function to ASCII art"
Agent: [Creates ASCII art representation of the code structure]
```

### Glitch Effect
```
User: "Add cyberpunk glitch effects to my code"
Agent: [Applies random glitch distortions and color shifts]
```

### Constellation Map
```
User: "Map my code to a star constellation"
Agent: [Creates night sky visualization with code elements as stars]
```

## Implementation Guidelines

1. **Analyze Code Structure**: Parse code to understand its structure, complexity, and patterns
2. **Choose Appropriate Style**: Match art style to user's intent and code characteristics
3. **Preserve Readability**: Ensure art enhances rather than obscures code meaning
4. **Add Animation**: Include frame-based animations where appropriate
5. **Support Multiple Languages**: Work with any programming language
6. **Export Options**: Provide output as terminal text, HTML, or image formats

## Terminal Output Format

Use ANSI escape codes for colors:
```python
# Reset
RESET = "\033[0m"

# Colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Bright colors
BRIGHT_GREEN = "\033[92m"
BRIGHT_CYAN = "\033[96m"
```

## Best Practices

- **Performance**: Limit animation frame rates for smooth playback
- **Accessibility**: Provide plain text alternatives for color-blind users
- **Customization**: Allow users to adjust parameters (colors, density, speed)
- **Cross-Platform**: Ensure output works on Windows, macOS, and Linux terminals
- **Documentation**: Include clear examples and usage instructions

## Integration with Other Tools

- **Git**: Visualize commit history as art
- **CI/CD**: Create artistic build status displays
- **Documentation**: Generate visual code documentation
- **Social Media**: Create shareable code art for Twitter/LinkedIn

---

*"Code is poetry, and poetry is art. Let's make your code speak in visuals."*

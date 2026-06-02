# Code Art Studio

Transform ordinary code into extraordinary visual art. This opencode skill enables creation of stunning terminal-based visuals, ASCII art reconstructions, and animated code displays.

## Features

- **Matrix Code Rain** - Iconic falling green characters from The Matrix
- **ASCII Art Portraits** - Convert code into text-based art
- **Pixel Art** - Retro 8-bit style block representations
- **Braille Art** - High-density Unicode braille patterns
- **Wave Animations** - Flowing sine wave text effects
- **Fractal Trees** - Recursive branching patterns
- **Code Constellations** - Star map visualizations
- **Glitch Art** - Cyberpunk-style distortions
- **QR Code Patterns** - Matrix barcode aesthetics
- **Mandala Patterns** - Sacred geometry from code

## Installation

1. Copy the `code-art-studio` folder to your opencode skills directory:
   ```bash
   # Project-level skill
   cp -r code-art-studio .opencode/skills/
   
   # Or global skill
   cp -r code-art-studio ~/.config/opencode/skills/
   ```

2. Restart opencode to load the skill

## Usage

### With opencode

Simply ask the agent to transform your code:

```
"Make my Python code look like Matrix rain"
"Convert this function to ASCII art"
"Create pixel art from my code"
"Add cyberpunk glitch effects"
```

### Standalone Scripts

Run the demo:
```bash
python scripts/main.py --style demo
```

Generate specific art:
```bash
# Matrix rain effect
python scripts/main.py --style matrix --file your_code.py

# ASCII art portrait
python scripts/main.py --style ascii --file your_code.py --width 80

# Pixel art
python scripts/main.py --style pixel --file your_code.py --scale 3

# Save to file
python scripts/main.py --style ascii --file your_code.py --output art.txt
```

## Examples

### Matrix Rain
```
python scripts/main.py --style matrix --file example.py
```
Output: Animated falling green characters with trail effects

### ASCII Art Portrait
```
python scripts/main.py --style ascii --file example.py
```
Output:
```
                        @@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

### Pixel Art
```
python scripts/main.py --style pixel --file example.py
```
Output:
```
████████████████████████████████████████████████████
██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
██░░████████████████████████████████████████████░░██
██░░██                                ██░░██
██░░██    def hello_world():          ██░░██
██░░██        print("Hello!")         ██░░██
██░░████████████████████████████████████████████░░██
```

## Script Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--style` | Art style (matrix, ascii, pixel, braille, wave) | demo |
| `--file` | Input code file | None |
| `--width` | Output width | 60 |
| `--height` | Output height | 20 |
| `--scale` | Pixel scale factor | 2 |
| `--duration` | Animation duration (seconds) | 5 |
| `--fps` | Frames per second | 20 |
| `--output` | Output file | stdout |

## Supported Languages

Works with any programming language:
- Python
- JavaScript/TypeScript
- Java
- C/C++
- Go
- Rust
- And more...

## Technical Details

### ANSI Color Codes

The skill uses ANSI escape codes for terminal colors:

```python
RESET = "\033[0m"
GREEN = "\033[32m"
BRIGHT_GREEN = "\033[92m"
CYAN = "\033[36m"
```

### Performance

- Matrix rain: ~20 FPS on modern terminals
- ASCII art: Instant generation
- Pixel art: Instant generation
- Braille art: Instant generation

### Cross-Platform

Works on:
- Windows (PowerShell, CMD)
- macOS (Terminal, iTerm2)
- Linux (all major terminals)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - feel free to use and modify

## Credits

Inspired by:
- The Matrix (1999)
- ASCII art community
- Terminal art pioneers

## Links

- [opencode Documentation](https://opencode.ai)
- [GitHub Repository](https://github.com/yourusername/code-art-studio)

---

*"Code is poetry, and poetry is art. Let's make your code speak in visuals."*

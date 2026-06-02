# Code Art Studio - Usage Examples

## Quick Start

### 1. Run Demo Mode
```bash
python scripts/main.py --style demo
```

### 2. Transform Your Code

#### Matrix Rain Effect
```bash
python scripts/main.py --style matrix --file your_code.py
```

#### ASCII Art Portrait
```bash
python scripts/main.py --style ascii --file your_code.py --width 80
```

#### Pixel Art
```bash
python scripts/main.py --style pixel --file your_code.py --scale 3
```

#### Save to File
```bash
python scripts/main.py --style ascii --file your_code.py --output art.txt
```

## With opencode

Simply ask the agent:

```
"Make my Python code look like Matrix rain"
"Convert this function to ASCII art"
"Create pixel art from my code"
"Add cyberpunk glitch effects"
"Map my code to a star constellation"
```

## Advanced Usage

### Custom Parameters
```bash
# Large ASCII art with custom dimensions
python scripts/main.py --style ascii --file main.py --width 100 --height 40

# Fast matrix rain
python scripts/main.py --style matrix --file main.py --fps 30 --duration 10

# High-detail pixel art
python scripts/main.py --style pixel --file main.py --scale 1
```

### Batch Processing
```bash
# Process multiple files
for file in *.py; do
    python scripts/main.py --style ascii --file "$file" --output "${file%.py}_art.txt"
done
```

## Tips

1. **For best results**: Use well-formatted code with proper indentation
2. **Terminal size**: Adjust width/height based on your terminal dimensions
3. **Performance**: Matrix rain may be slow on older terminals
4. **Colors**: Ensure your terminal supports ANSI colors for full effect

## Examples

### Input Code
```python
def hello():
    print("Hello, World!")
```

### ASCII Art Output
```
                                                    
              ************************              
               *********************                
                                                    
              ************************              
                ++++++++++++++++++++++++            
                          %%%%%%%%                  
                ++++++++++++++++++++++++            
                                                    
```

### Pixel Art Output
```
                      
##################
    ****************
    ########
                      
##################
    ########################
```

---

*Transform your code into art!*

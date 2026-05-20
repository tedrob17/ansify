# Core ANSI Escape Sequences
reset = "\033[0m"
bold = "\033[1m"

# Text Colours
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"

# Main Functions
def success(text: str):
    """Prints text in bold green with a success checkmark"""
    print(f"{green}{bold}✓ {text}{reset}")

def error(text: str):
    """Prints text in bold red with a red cross"""
    print(f"{red}{bold}✗ {text}{reset}")

def warn(text: str):
    """Prints text in bold with a warning exclamation"""
    print(f"{yellow}{bold}! {text}{reset}")

def banner(text: str, colour=blue):
    """Prints text inside a blue border box"""
    width = len(text) + 6
    border = colour + "=" * width + reset
    print(border)
    print(f"{colour}||{reset} {bold}{text}{reset} {colour}||{reset}")
    print(border)
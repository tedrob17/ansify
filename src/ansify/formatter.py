# Core ANSI Escape Sequences
reset = "\033[0m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"

# Text Colours
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
cyan = "\033[36m"
white = "\033[37m"

# Background Colours
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_cyan = "\033[46m"

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

def boldText(text: str):
    """Returns text with bold formatting"""
    return f"{bold}{text}{reset}"

def banner(text: str, colour=blue):
    """Prints text inside a blue border box"""
    width = len(text) + 6
    border = colour + "=" * width + reset
    print(border)
    print(f"{colour}||{reset} {bold}{text}{reset} {colour}||{reset}")
    print(border)

def paint(text:str, colour: str = "", bg: str = "", is_bold: bool = False, is_underline: bool = False) -> str:
    """Returns a custom styled string without printing it"""
    style = ""
    if colour:    style += colour
    if bg:        style += bg
    if is_bold:      style += bold
    if is_underline: style += underline

    return f"{style}{text}{reset}"
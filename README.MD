# ansify 1.0.6
 Ansify is a simple, zero-dependency Python module to print beautifully styled border text, success text, error text and warn text directly into your terminal.

---
## Features
- **Built using Pythons inbuilt capabilities**
- **Prestyled messages, just insert your text**
- **Wrap headers in clean blue borders**
- **Print out text using our brand new PAINT engine**

## Example
![demo](./image.png)

## List of functions and parameters
| Function | Parameters | Behavior | Returns | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`success(text)`** | `text` *(str)* | 🖨️ Prints | `None` | Output a green string prefixed with a bold checkmark (`✓`). |
| **`error(text)`** | `text` *(str)* | 🖨️ Prints | `None` | Output a red string prefixed with a bold cross (`✗`). |
| **`warn(text)`** | `text` *(str)* | 🖨️ Prints | `None` | Output a yellow string prefixed with a bold exclamation mark (`!`). |
| **`banner(text, colour)`** | `text` *(str)*, `colour` *(str, optional, defaults to blue)* | 🖨️ Prints | `None` | Wraps text in a stylized box border matching the specified color asset. |
| **`boldText(text)`** | `text` *(str)* | 🔄 Returns | `str` | Wraps the raw string inside the ANSI escape boundaries for bold display. |
| **`paint(text, colour, bg, is_bold, is_underline)`** | `text` *(str)*, `colour` *(str, optional)*, `bg` *(str, optional)*, `is_bold` *(bool, optional)*, `is_underline` *(bool, optional)* | 🔄 Returns | `str` | Constructs a custom string configuration using specific styles without triggering immediate terminal output. |

## Installation
To install `ansify` in locally editable mode, run the following command in the root directory:

```bash
pip install -e .
```
View `demo-code.py` for example code implementing ansify

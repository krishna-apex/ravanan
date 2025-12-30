# 🔱 Ravanan - The 10-Headed Web Browser 🔱

```
 (                                 )             )  
 )\ )    (               (      ( /(   (      ( /(  
(()/(    )\     (   (    )\     )\())  )\     )\()) 
 /(_))((((_)(   )\  )\((((_)(  ((_)\((((_)(  ((_)\  
(_))   )\ _ )\ ((_)((_))\ _ )\  _((_))\ _ )\  _((_)      
| _ \  (_)_\(_)\ \ / / (_)_\(_)| \| |(_)_\(_)| \| |      
|   /   / _ \   \ V /   / _ \  | .` | / _ \  | .` |      
|_|_\  /_/ \_\   \_/   /_/ \_\ |_|\_|/_/ \_\ |_|\_|      

The 10-Minded Scholar King • Terminal Web Browser        
                v1.0.4 • By Krishna D
```

A **powerful text-based web browser** that runs entirely in your terminal. Named after the legendary Ravana from Hindu mythology, whose 10 heads represented vast knowledge and wisdom from multiple perspectives.

**Created by: Krishna D**

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.4-brightgreen.svg)](https://github.com/krishna182005/ravanan)
[![PyPI](https://img.shields.io/badge/pypi-ravanan-blue)](https://pypi.org/project/ravanan/)

---

## 🌟 Why Ravanan?

Ravana, the legendary scholar-king, possessed 10 heads symbolizing mastery over different dimensions of knowledge. Similarly, **Ravanan browser** offers 10 powerful capabilities for navigating the web in a unique, terminal-based way!

---

## 🔱 The 10 Heads of Wisdom

Like Ravana's 10 heads representing different dimensions of knowledge, this browser offers 10 powerful capabilities:

1. **🌐 Smart HTML Parsing** - Extracts text, links, headers, lists, tables, and more
2. **⚡ Fast HTTP Fetching** - Quick and efficient web page loading with full HTTPS support
3. **🎨 Beautiful Rendering** - Styled terminal output with colors and formatting
4. **🔗 Link Navigation** - Jump to links by number, Lynx-style
5. **📜 History Management** - Full back/forward browsing history
6. **🔍 Advanced Search** - Case-sensitive and case-insensitive search within pages
7. **❌ Error Handling** - Graceful handling of all web errors (404, timeouts, etc.)
8. **📊 Content Extraction** - Clean extraction of meaningful content
9. **💎 Clean Interface** - Intuitive commands and beautiful UI with responsive banner
10. **💪 Terminal Power** - Full-featured browsing without leaving your terminal

## ✨ Additional Features

- 💾 **Save Pages** - Save current page as text file
- 📊 **Statistics** - View browsing statistics
- ℹ️ **Page Info** - Detailed information about current page
- 📋 **List All Links** - Display all links on current page
- 🆘 **Comprehensive Help** - Detailed help system
- 🎯 **Multiple Commands** - Many ways to accomplish the same task

---

## 🚀 Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install ravanan
```

After installation, you can run Ravanan from anywhere:

```bash
ravanan
```

### Option 2: Install from Source

```bash
# Clone the repository
git clone https://github.com/krishna182005/ravanan.git
cd ravanan

# Install dependencies
pip install -r requirements.txt

# Run the browser
python3 -m ravanan
```

### Option 3: Development Installation

```bash
# Clone the repository
git clone https://github.com/krishna182005/ravanan.git
cd ravanan

# Install in editable mode
pip install -e .

# Now you can run from anywhere
ravanan
```

---

## 🎮 Quick Start

### Basic Usage

```bash
# Start with default page (duckduckgo.com)
ravanan

# Open a specific URL
ravanan wikipedia.org

# Open with full URL
ravanan https://news.ycombinator.com

# Set custom home page
ravanan --home https://stackoverflow.com
```

### First Steps

1. **Navigate to a link**: Type the link number (e.g., `1`, `2`, `3`)
2. **Go to a URL**: Type the URL directly (e.g., `wikipedia.org`)
3. **Search in page**: Type `/python` to search for "python"
4. **Go back**: Type `b` or `back`
5. **Get help**: Type `?` or `help`
6. **Quit**: Type `q` or `quit`

---

## 📖 Commands Reference

### Navigation Commands
| Command | Action |
|---------|--------|
| `[number]` | Navigate to link by number (e.g., `1`, `2`, `3`) |
| `b`, `back` | Go back to previous page |
| `f`, `forward` | Go forward to next page |
| `h`, `home` | Go to home page |
| `r`, `reload` | Reload current page |
| `u`, `url` | Show current URL |

### URL Entry
| Command | Action |
|---------|--------|
| `https://example.com` | Enter full URL with scheme |
| `example.com` | Enter domain (https:// added automatically) |
| `go [url]` | Navigate to URL (alternative) |

### Search & Discovery
| Command | Action |
|---------|--------|
| `/[query]` | Case-insensitive search (e.g., `/python`) |
| `//[query]` | Case-sensitive search |
| `links` | List all links on current page |

### Information Commands
| Command | Action |
|---------|--------|
| `info` | Show current page information |
| `history` | Show browsing history |
| `stats` | Show browser statistics |
| `about` | About Ravanan browser |

### Utility Commands
| Command | Action |
|---------|--------|
| `save` | Save current page as text file |
| `clear` | Clear screen and redisplay page |
| `version` | Show version information |
| `?`, `help` | Show comprehensive help |
| `q`, `quit`, `exit` | Quit browser |

---

---

## 🎯 Example Session

```bash
# Start the browser
$ ravanan

# Ravanan banner appears...
# Browser starts at example.com

> wikipedia.org          # Visit Wikipedia
Loading Wikipedia...

> 3                      # Click link #3 (opens Featured Articles)
Loading...

> /python                # Search for "python" in page
Found 15 results for 'python'

> b                      # Go back to Wikipedia main page
Going back...

> f                      # Go forward to Featured Articles
Going forward...

> h                      # Return to home page
Going to home page...

> info                   # Show page information
Current Page: Featured Articles
URL: https://en.wikipedia.org/wiki/Featured_articles
Links: 127

> save                   # Save current page
Page saved to: featured_articles.txt

> q                      # Quit
Goodbye!
```

---

## 📁 Project Structure

```
ravanan/
├── main.py                 # Main application entry point
├── browser/
│   ├── __init__.py
│   ├── fetcher.py         # HTTP request handler
│   ├── parser.py          # HTML parser (BeautifulSoup)
│   ├── renderer.py        # Terminal UI renderer (rich)
│   └── navigator.py       # Navigation logic
├── utils/
│   ├── __init__.py
│   ├── history.py         # Browsing history manager
│   └── banner.py          # Responsive ASCII banner
├── requirements.txt       # Python dependencies
├── setup.py              # Package configuration
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # Contribution guidelines
└── README.md            # This file
```

**Total Code:** ~1,300 lines of Python

---

## 🛠️ How It Works

### 1. **Web Fetcher** (`browser/fetcher.py`)
- Uses `requests` library for HTTP/HTTPS requests
- Handles redirects, timeouts, and errors (404, 403, 500, etc.)
- Normalizes URLs and manages sessions
- Configurable timeout and headers

### 2. **HTML Parser** (`browser/parser.py`)
- Parses HTML using `BeautifulSoup4` with `lxml` backend
- Extracts text content, links, headings, lists, tables
- Removes scripts, styles, and comments for clean text
- Resolves relative URLs to absolute
- Smart content extraction

### 3. **Text Renderer** (`browser/renderer.py`)
- Uses `rich` library for beautiful terminal styling
- Responsive ASCII banner that adapts to terminal width
- Renders headings, paragraphs, links, blockquotes
- Creates formatted tables for links
- Displays headers, footers, and error messages
- Color-coded content types

### 4. **Navigator** (`browser/navigator.py`)
- Manages current page and links
- Provides link lookup by index
- Integrates with history for back/forward navigation

### 5. **History Manager** (`utils/history.py`)
- Maintains browsing history stack
- Supports back/forward navigation
- Limits history size (default 100 pages)

### 6. **Banner System** (`utils/banner.py`)
- Responsive ASCII art banner
- Adapts to terminal width automatically
- 4 different sizes: Full, Compact, Minimal, Tiny

---

## 🌟 Recommended Sites to Try

### Works Great ⭐
- `example.com` - Perfect test site
- `info.cern.ch` - First website ever (1991)
- `text.npr.org` - NPR text-only version
- `lite.cnn.com` - CNN lite version
- `old.reddit.com` - Reddit old interface

### Good Experience 👍
- `wikipedia.org` - Excellent in text mode
- `news.ycombinator.com` - Hacker News
- `lobste.rs` - Tech community
- `stackoverflow.com` - Stack Overflow

### Interesting 🔍
- `wiby.me` - Search engine for simple sites
- `68k.news` - Retro news aggregator
- `txti.es` - Fast web pages

---

## 💡 Use Cases

### 1. **Accessibility**
- Screen reader friendly
- Low bandwidth browsing
- Terminal-only environments
- SSH sessions

### 2. **Development**
- Test website text content
- Debug HTML structure
- Quick web scraping prototype
- Content extraction testing

### 3. **Education**
- Learn web protocols
- Understand HTML parsing
- Practice Python development
- Study HTTP requests

### 4. **Privacy**
- No JavaScript tracking
- No cookies (unless configured)
- No image loading
- Minimal footprint

---

## 📦 Dependencies

All dependencies are automatically installed with `pip install ravanan`:

- **requests** (≥2.31.0) - HTTP library for fetching web pages
- **beautifulsoup4** (≥4.12.0) - HTML parsing and extraction
- **rich** (≥13.0.0) - Terminal formatting and styling
- **lxml** (≥4.9.0) - Fast HTML/XML parser (BeautifulSoup backend)

---

## 🤝 Contributing

**Ravanan is an open-source project and contributions are welcome!**

We love your input! We want to make contributing to Ravanan as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

### How to Contribute

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/krishna182005/ravanan.git
   cd ravanan
   ```
3. **Create a feature branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make your changes** and test thoroughly
5. **Commit your changes**:
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request** on GitHub

### Development Setup

```bash
# Clone the repository
git clone https://github.com/krishna182005/ravanan.git
cd ravanan

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests
python test.py
```

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions and classes
- Write meaningful commit messages
- Add tests for new features

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🧪 Testing

Ravanan includes a comprehensive test suite:

```bash
# Run all tests
python test.py

# Run specific test
python test_ravanan.py
```

**Test Coverage:**
- ✅ WebFetcher - HTTP/HTTPS fetching
- ✅ HTMLParser - HTML parsing and extraction
- ✅ BrowsingHistory - Navigation history
- ✅ Navigator - Link management
- ✅ Integration - End-to-end workflows

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Krishna D

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🚀 Roadmap (Future Enhancements)

### Version 2.0 Plans

- 📚 **Bookmark System** - Save and manage favorite pages
- 💾 **Offline Caching** - Cache visited pages for offline reading
- 🎨 **Themes** - Dark mode, light mode, custom color schemes
- 🔐 **Proxy Support** - Browse through HTTP/SOCKS proxies
- 📥 **Download Manager** - Enhanced file saving
- 🍪 **Cookie Support** - Basic cookie handling
- 🔍 **Regex Search** - Advanced search patterns
- 📑 **Tab Support** - Multiple browsing sessions
- ⌨️ **Vim Keybindings** - Vim-style shortcuts
- 📊 **Progress Bars** - Download progress indicators

### Community Requested

Vote for features or suggest new ones in [GitHub Issues](https://github.com/krishna182005/ravanan/issues)!

---

## 🙏 Acknowledgments

- Inspired by **Lynx** - The original text-based web browser (1992)
- Named after **Ravana** - The legendary 10-headed scholar-king
- Built with ❤️ for terminal enthusiasts
- Thanks to the Python community for amazing libraries
- Special thanks to all contributors

---

## 📧 Contact & Support

- **Creator**: Krishna D
- **GitHub**: [https://github.com/krishna182005/ravanan/](https://github.com/krishna182005/ravanan/)
- **Issues**: [Report a bug or request a feature](https://github.com/krishna182005/ravanan/issues)
- **Discussions**: [Join the community](https://github.com/krishna182005/discussions)

---

## 🌟 Star History

If you find Ravanan useful, please consider giving it a star on GitHub! ⭐

---

**Happy Browsing! 🌐✨**

*Made with ❤️ for the terminal by Krishna D*

---

## 📊 Project Stats

- **Development Time**: ~3 hours
- **Total Lines of Code**: ~1,300
- **Test Coverage**: 100% of core modules
- **Dependencies**: 4 (all stable, well-maintained)
- **Python Version**: 3.8+
- **Platforms**: Windows, Linux, macOS
- **License**: MIT (Open Source)




# 🔱 Ravanan Browser - Updates & Improvements

## Summary of Changes

This document describes the improvements made to Ravanan browser to fix browser fingerprinting issues and add enhanced privacy/configuration features.

---

## ✅ Issues Fixed

### 1. **Browser Fingerprinting - User-Agent**

**Problem**: The User-Agent was set to "TermLynx/1.0" which looked incomplete and AI-generated when visiting sites like ipleak.net.

**Solution**: 
- Replaced with authentic Firefox User-Agent: `Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0`
- Added complete Firefox HTTP headers including:
  - Accept headers
  - Accept-Language
  - Accept-Encoding
  - DNT (Do Not Track)
  - Connection keep-alive
  - Sec-Fetch headers for modern browser behavior

**Files Modified**: 
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L13-L32)

---

### 2. **Timeout Configuration**

**Problem**: Timeout was hardcoded at 10 seconds, too short for slow connections or Tor usage.

**Solution**:
- Increased default timeout to 30 seconds
- Added command-line option: `--timeout <seconds>`
- Added runtime command: `timeout [seconds]`
- Added method to view current timeout: `timeout`

**Files Modified**:
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L13) - Constructor with timeout parameter
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L90-L96) - set_timeout() method
- [ravanan/main.py](ravanan/main.py#L24) - __init__ with timeout parameter
- [ravanan/main.py](ravanan/main.py#L178-L189) - timeout commands in handle_command()
- [ravanan/main.py](ravanan/main.py#L616) - --timeout command-line argument

**Usage Examples**:
```bash
# Command line
ravanan --timeout 60

# Runtime
> timeout 60      # Set timeout to 60 seconds
> timeout         # Show current timeout
```

---

### 3. **Proxy Support**

**Problem**: No proxy support, limiting privacy and network configuration options.

**Solution**: Added comprehensive proxy support including:

#### Tor Support
- One-command Tor activation: `--proxy-tor`
- Runtime Tor activation: `proxy tor`
- Uses SOCKS5h protocol to prevent DNS leaks
- Default Tor address: `socks5h://127.0.0.1:9050`

#### Custom Proxy Support
- Command-line option: `--proxy <url>`
- Runtime command: `proxy <url>`
- Supports: HTTP, HTTPS, SOCKS5, SOCKS5h
- Supports authenticated proxies

#### Proxy Management
- View proxy status: `proxy`
- Disable proxy: `proxy off`
- Dynamic proxy switching at runtime

**Files Modified**:
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L13) - Constructor with proxy parameter
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L34-L37) - fetch() with proxy support
- [ravanan/browser/fetcher.py](ravanan/browser/fetcher.py#L98-L133) - Proxy management methods
- [ravanan/main.py](ravanan/main.py#L24) - __init__ with proxy parameter
- [ravanan/main.py](ravanan/main.py#L191-L223) - Proxy commands in handle_command()
- [ravanan/main.py](ravanan/main.py#L622-L631) - --proxy and --proxy-tor arguments
- [requirements.txt](requirements.txt#L9) - Added PySocks dependency

**Usage Examples**:
```bash
# Tor proxy (command line)
ravanan --proxy-tor

# Custom proxy (command line)
ravanan --proxy socks5://192.168.1.100:1080
ravanan --proxy http://proxy.example.com:8080

# Runtime
> proxy tor                              # Enable Tor
> proxy socks5://127.0.0.1:1080         # Set custom proxy
> proxy                                  # Show status
> proxy off                              # Disable proxy
```

---

## 🆕 New Features Summary

| Feature | Command Line | Runtime Command | Description |
|---------|--------------|----------------|-------------|
| **Firefox User-Agent** | Automatic | N/A | Authentic Firefox browser headers |
| **Timeout Config** | `--timeout <sec>` | `timeout [sec]` | Configure request timeout |
| **Tor Proxy** | `--proxy-tor` | `proxy tor` | Anonymous browsing via Tor |
| **Custom Proxy** | `--proxy <url>` | `proxy <url>` | Use any HTTP/SOCKS proxy |
| **Proxy Status** | N/A | `proxy` | View current proxy config |
| **Disable Proxy** | N/A | `proxy off` | Switch to direct connection |

---

## 📁 Files Modified

### Core Files
1. **ravanan/browser/fetcher.py**
   - Enhanced User-Agent with complete Firefox headers
   - Added proxy support to constructor and fetch method
   - Added timeout configuration
   - New methods: `set_timeout()`, `set_proxy()`, `use_tor()`, `disable_proxy()`

2. **ravanan/main.py**
   - Updated Ravanan class constructor with timeout and proxy parameters
   - Added timeout commands to handle_command()
   - Added proxy commands to handle_command()
   - Added --timeout, --proxy, --proxy-tor command-line arguments
   - Updated help text with new commands
   - Updated examples in main()

3. **requirements.txt**
   - Added PySocks>=1.7.1 for SOCKS proxy support

### Documentation
4. **PROXY_TIMEOUT_GUIDE.md** (NEW)
   - Comprehensive guide for proxy and timeout configuration
   - Setup instructions for Tor
   - Usage examples and best practices
   - Troubleshooting guide

5. **CHANGES_SUMMARY.md** (THIS FILE)
   - Summary of all changes made

---

## 🔍 Technical Details

### User-Agent Headers
```python
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1'
}
```

### Proxy Configuration
```python
# Tor proxy
proxy = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# Custom HTTP proxy
proxy = {
    'http': 'http://proxy.example.com:8080',
    'https': 'http://proxy.example.com:8080'
}
```

### Timeout Configuration
- Default: 30 seconds (increased from 10 seconds)
- Configurable at startup and runtime
- Applied to all HTTP requests

---

## 🧪 Testing Recommendations

### Test User-Agent
Visit ipleak.net or whoer.net and verify:
- Browser engine shows as "Gecko" (Firefox)
- User-Agent string shows Firefox
- No "unfilled" or incomplete fields
- Headers match Firefox behavior

### Test Timeout
```bash
# Test with short timeout
ravanan --timeout 5
# Try loading slow sites - should timeout quickly

# Test with long timeout
ravanan --timeout 120
# Should wait longer for responses
```

### Test Tor Proxy
```bash
# 1. Start Tor service
sudo systemctl start tor

# 2. Start Ravanan with Tor
ravanan --proxy-tor

# 3. Visit check.torproject.org
> check.torproject.org
# Should show "Congratulations. This browser is configured to use Tor."

# 4. Check IP
> ifconfig.me
# Should show a Tor exit node IP, not your real IP
```

### Test Custom Proxy
```bash
# Start with proxy
ravanan --proxy http://your-proxy:8080

# Check IP to verify proxy is working
> ifconfig.me
```

---

## 🎯 Benefits

1. **Better Privacy**: Realistic Firefox fingerprint avoids bot detection
2. **Anonymous Browsing**: Tor support for privacy-sensitive browsing
3. **Flexibility**: Runtime configuration changes without restarting
4. **Network Compatibility**: Support for corporate proxies and restricted networks
5. **Slow Connection Support**: Configurable timeouts for unreliable networks
6. **No More "AI Generated" Detection**: Complete, authentic browser headers

---

## 📋 Requirements

### System Requirements
- Python 3.8+
- Internet connection
- (Optional) Tor service for Tor proxy support

### Python Dependencies
```
requests>=2.31.0
beautifulsoup4>=4.12.0
rich>=13.0.0
lxml>=4.9.0
PySocks>=1.7.1        # NEW - for SOCKS proxy support
```

### Installation
```bash
# Install/update dependencies
pip install -r requirements.txt

# Or install individually
pip install PySocks
```

---

## 🚀 Quick Start Guide

### Basic Usage (No Proxy)
```bash
ravanan
```

### With Tor
```bash
# Start Tor
sudo systemctl start tor

# Start Ravanan
ravanan --proxy-tor --timeout 60
```

### With Custom Timeout
```bash
ravanan --timeout 120
```

### Runtime Configuration
```bash
# Start normally
ravanan

# Enable Tor from within browser
> proxy tor

# Adjust timeout
> timeout 60

# Check current settings
> proxy
> timeout
```

---

## ⚙️ Configuration Options

### Command-Line Arguments
```
ravanan [URL] [OPTIONS]

Positional arguments:
  url                   URL to open on startup

Optional arguments:
  -h, --help            Show help message
  --version             Show version information
  --home URL            Set home page URL
  --timeout SECONDS     Request timeout in seconds (default: 30)
  --proxy URL           Custom proxy URL
  --proxy-tor           Use Tor proxy (127.0.0.1:9050)
```

### Runtime Commands
```
Navigation:           Proxy & Network:
  [number]  Go to link   proxy         Show proxy status
  b         Back         proxy tor     Enable Tor proxy
  f         Forward       proxy <url>   Set custom proxy
  h         Home          proxy off     Disable proxy
  r         Reload        timeout       Show timeout
  u         URL           timeout <n>   Set timeout
```

---

## 🔒 Security Notes

1. **Tor Usage**: 
   - Provides anonymity but slower speeds
   - DNS leaks prevented using socks5h://
   - Verify Tor is running before use

2. **Proxy Authentication**:
   - Supports username:password in proxy URL
   - Format: `http://user:pass@host:port`

3. **HTTPS/TLS**:
   - All HTTPS traffic remains encrypted
   - Proxy sees connection metadata only

4. **DNS Resolution**:
   - Use `socks5h://` to resolve DNS through proxy
   - Prevents DNS leaks

---

## 📖 Additional Documentation

- [PROXY_TIMEOUT_GUIDE.md](PROXY_TIMEOUT_GUIDE.md) - Detailed proxy and timeout guide
- [README.md](README.md) - Main project documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [FEATURES.md](FEATURES.md) - Feature list

---

**Version**: 1.0.0 (Enhanced)  
**Created by**: Krishna D  
**Date**: December 30, 2025  
🔱 *Browse with the wisdom of 10 heads!* 🔱

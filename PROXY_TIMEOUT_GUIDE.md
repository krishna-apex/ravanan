# 🔐 Ravanan - Proxy & Timeout Configuration Guide

## Overview

Ravanan now includes enhanced privacy and configuration options with support for:
- **Custom timeout settings** - Configure request timeout for slow connections
- **Tor proxy support** - Browse anonymously through Tor network
- **Custom proxy support** - Use any HTTP/HTTPS/SOCKS5 proxy
- **Firefox User-Agent** - Authentic Firefox browser fingerprint

---

## 🔥 Quick Start

### Using Tor Proxy

```bash
# Start with Tor proxy (make sure Tor is running first!)
ravanan --proxy-tor

# Or enable Tor from within the browser
> proxy tor
```

### Custom Timeout

```bash
# Start with 60-second timeout
ravanan --timeout 60

# Or change timeout from within the browser
> timeout 60
```

### Custom Proxy

```bash
# Start with custom SOCKS5 proxy
ravanan --proxy socks5://127.0.0.1:1080

# Start with HTTP proxy
ravanan --proxy http://proxy.example.com:8080
```

---

## 📋 Command Line Options

```bash
ravanan [URL] [OPTIONS]

Options:
  --timeout SECONDS      Request timeout in seconds (default: 30)
  --proxy URL           Custom proxy URL
  --proxy-tor           Use Tor proxy (127.0.0.1:9050)
  --home URL            Set home page URL
  --version             Show version information
  -h, --help            Show help message
```

### Examples

```bash
# Browse with 120 second timeout
ravanan wikipedia.org --timeout 120

# Browse through Tor
ravanan duckduckgo.com --proxy-tor

# Browse through custom SOCKS5 proxy
ravanan --proxy socks5h://192.168.1.100:1080

# Browse through HTTP proxy with custom timeout
ravanan news.ycombinator.com --proxy http://proxy.local:3128 --timeout 45
```

---

## ⚙️ Runtime Commands

### Proxy Commands

```
proxy              Show current proxy status
proxy tor          Enable Tor proxy (127.0.0.1:9050)
proxy <url>        Set custom proxy (e.g., socks5://host:port)
proxy off          Disable proxy and use direct connection
```

#### Examples:

```
> proxy
🔓 No proxy configured (direct connection)

> proxy tor
✅ Tor proxy enabled (127.0.0.1:9050)
   Make sure Tor is running!

> proxy socks5://192.168.1.100:1080
✅ Proxy set to: socks5://192.168.1.100:1080

> proxy off
✅ Proxy disabled
```

### Timeout Commands

```
timeout            Show current timeout value
timeout <seconds>  Set timeout in seconds
```

#### Examples:

```
> timeout
⏱️  Current timeout: 30 seconds

> timeout 60
✅ Timeout set to 60 seconds

> timeout 120
✅ Timeout set to 120 seconds
```

---

## 🔐 Setting Up Tor

### Linux (Debian/Ubuntu)

```bash
# Install Tor
sudo apt update
sudo apt install tor

# Start Tor service
sudo systemctl start tor

# Enable Tor to start on boot
sudo systemctl enable tor

# Check Tor status
sudo systemctl status tor
```

### macOS

```bash
# Install Tor using Homebrew
brew install tor

# Start Tor
brew services start tor

# Or run Tor manually
tor
```

### Verify Tor is Running

```bash
# Check if Tor is listening on port 9050
netstat -an | grep 9050
# or
ss -tuln | grep 9050
```

---

## 🌐 User-Agent Information

Ravanan now uses an authentic Firefox User-Agent to avoid detection as a bot:

```
Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
```

This includes:
- Standard Firefox headers (Accept, Accept-Language, etc.)
- DNT (Do Not Track) header
- Sec-Fetch headers for modern browser behavior
- Connection keep-alive for efficiency

---

## 🛡️ Proxy Types Supported

### SOCKS5 (Recommended for Tor)

```bash
# SOCKS5 proxy (DNS through proxy)
ravanan --proxy socks5h://127.0.0.1:9050

# SOCKS5 proxy (local DNS resolution)
ravanan --proxy socks5://127.0.0.1:9050
```

### HTTP/HTTPS Proxies

```bash
# HTTP proxy
ravanan --proxy http://proxy.example.com:8080

# HTTPS proxy
ravanan --proxy https://secure-proxy.example.com:8443

# Proxy with authentication
ravanan --proxy http://username:password@proxy.example.com:8080
```

---

## 📊 Testing Your Configuration

### Test Tor Connection

1. Start Ravanan with Tor:
   ```bash
   ravanan --proxy-tor
   ```

2. Visit an IP check site:
   ```
   > check.torproject.org
   ```
   
3. You should see a confirmation that you're using Tor!

### Test Custom Proxy

1. Configure your proxy:
   ```bash
   ravanan --proxy http://your-proxy:port
   ```

2. Visit an IP checker:
   ```
   > ifconfig.me
   ```

3. The displayed IP should match your proxy's IP

### Test Timeout

1. Set a very short timeout:
   ```
   > timeout 1
   ```

2. Try to load a slow website - it should timeout quickly

3. Restore normal timeout:
   ```
   > timeout 30
   ```

---

## ⚠️ Important Notes

### Tor Usage

- **Speed**: Tor connections are slower due to onion routing
- **Privacy**: Tor provides anonymity but may not work with all sites
- **Service**: Make sure Tor is running before using `--proxy-tor`
- **Port**: Default Tor SOCKS5 port is 9050

### Timeout Settings

- **Default**: 30 seconds (increased from 10 seconds)
- **Minimum**: 1 second (not recommended)
- **Recommended**: 30-60 seconds for normal browsing
- **Slow connections**: 60-120 seconds
- **Fast connections**: 15-30 seconds

### Proxy Configuration

- **DNS leaks**: Use `socks5h://` instead of `socks5://` to prevent DNS leaks
- **Authentication**: Format: `http://user:pass@host:port`
- **HTTPS sites**: Proxy should support HTTPS tunneling
- **Changing proxy**: Use `proxy off` before setting a new proxy

---

## 🐛 Troubleshooting

### Tor Not Connecting

```
Error: Could not connect to server
```

**Solutions**:
1. Check if Tor is running: `sudo systemctl status tor`
2. Verify Tor port: `netstat -an | grep 9050`
3. Restart Tor: `sudo systemctl restart tor`
4. Check Tor configuration: `/etc/tor/torrc`

### Timeout Errors

```
Error: Request timed out after X seconds
```

**Solutions**:
1. Increase timeout: `timeout 60`
2. Check internet connection
3. Try without proxy: `proxy off`
4. Use a different server/site

### Proxy Connection Failed

```
Error: Could not connect to server
```

**Solutions**:
1. Verify proxy is running
2. Check proxy URL format
3. Test proxy authentication
4. Try `proxy off` and connect directly
5. Check firewall settings

### PySocks Not Installed

```
Missing dependencies for SOCKS support
```

**Solution**:
```bash
pip install PySocks
# or
pip install -r requirements.txt
```

---

## 💡 Best Practices

1. **Use Tor for Privacy**: When you need anonymity
2. **Use Direct Connection**: For best performance
3. **Use Custom Proxy**: For corporate/network requirements
4. **Set Appropriate Timeout**: 30s for normal, 60s+ for Tor/slow connections
5. **Change Proxy Dynamically**: Switch between direct/Tor/proxy as needed
6. **Verify Connection**: Always test with IP checker sites

---

## 🎯 Use Cases

### Anonymous Browsing
```bash
ravanan --proxy-tor --timeout 60
```

### Corporate Network
```bash
ravanan --proxy http://corporate-proxy:8080 --timeout 45
```

### Slow/Unreliable Connection
```bash
ravanan --timeout 120
```

### Development/Testing
```bash
ravanan --proxy http://localhost:8888 --timeout 30
```

### Maximum Privacy
```bash
# In browser:
> proxy tor
> timeout 90
```

---

## 📚 Additional Resources

- **Tor Project**: https://www.torproject.org/
- **PySocks Documentation**: https://github.com/Anorov/PySocks
- **Requests Proxy Guide**: https://requests.readthedocs.io/en/latest/user/advanced/#proxies

---

**Created by: Krishna D**  
**Ravanan Browser v1.0.0**  
🔱 *Browse with the wisdom of 10 heads!* 🔱

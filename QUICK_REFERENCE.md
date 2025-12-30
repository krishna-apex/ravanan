# 🎯 Ravanan Browser - Quick Reference Card

## 🔥 What's Fixed

✅ **Browser fingerprinting fixed** - Now shows as Firefox (not TermLynx)  
✅ **No more AI-generated warnings** - Complete authentic headers  
✅ **Configurable timeout** - Default 30s, adjustable up to any value  
✅ **Tor proxy support** - One command anonymous browsing  
✅ **Custom proxy support** - HTTP/HTTPS/SOCKS5 proxies

---

## ⚡ Quick Commands

### Start the Browser

```bash
# Normal start
ravanan

# With Tor (anonymous)
ravanan --proxy-tor --timeout 60

# With custom timeout
ravanan --timeout 90

# With custom proxy
ravanan --proxy socks5://host:port
```

### Runtime Commands (while browsing)

```
PROXY COMMANDS:
  proxy           Show current proxy status
  proxy tor       Enable Tor (127.0.0.1:9050)
  proxy <url>     Set custom proxy
  proxy off       Disable proxy

TIMEOUT COMMANDS:
  timeout         Show current timeout
  timeout 60      Set 60 second timeout
  timeout 120     Set 120 second timeout

OTHER COMMANDS:
  ?               Show help
  b               Back
  f               Forward
  q               Quit
```

---

## 🔐 Privacy Setup

### Use Tor for Anonymous Browsing

```bash
# 1. Install and start Tor
sudo apt install tor
sudo systemctl start tor

# 2. Start Ravanan with Tor
ravanan --proxy-tor --timeout 60

# 3. Test it
> check.torproject.org
```

### Use Custom Proxy

```bash
# HTTP proxy
ravanan --proxy http://proxy.local:8080

# SOCKS5 proxy (recommended)
ravanan --proxy socks5h://192.168.1.100:1080

# With authentication
ravanan --proxy http://user:pass@proxy.local:8080
```

---

## 📊 What Sites Will See

### Before Fix (Old)
```
User-Agent: TermLynx/1.0 (Text-based Browser; +https://github.com/yourusername/termlynx)
Browser Engine: Unknown/Incomplete
Headers: Minimal/Missing
Detection: Likely flagged as bot
```

### After Fix (New)
```
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Browser Engine: Gecko (Firefox)
Headers: Complete Firefox headers
Detection: Appears as Firefox browser
```

---

## 🎨 Example Usage

### Anonymous Research
```bash
ravanan --proxy-tor --timeout 90
> duckduckgo.com
> /privacy
```

### Testing with Slow Connection
```bash
ravanan --timeout 120
> example.com
```

### Corporate Network
```bash
ravanan --proxy http://corporate-proxy:8080
> intranet.company.com
```

### Switch Proxy While Browsing
```bash
ravanan
> example.com
> proxy tor
> reload
> check.torproject.org
```

---

## 📁 Files Changed

1. `ravanan/browser/fetcher.py` - User-Agent, proxy, timeout
2. `ravanan/main.py` - Command-line args, runtime commands
3. `requirements.txt` - Added PySocks for SOCKS proxy support

---

## 🧪 Test Your Setup

### Test 1: Check User-Agent
```bash
python3 test_improvements.py
```
Should show: ✅ All tests passed

### Test 2: Check on IPLeak.net
```bash
ravanan
> ipleak.net
```
Should show: Firefox/Gecko engine, no warnings

### Test 3: Check Tor
```bash
ravanan --proxy-tor
> check.torproject.org
```
Should show: "Congratulations. This browser is configured to use Tor."

---

## 💡 Tips & Tricks

1. **Slow connection?** `timeout 120` for 2-minute timeout
2. **Need privacy?** `proxy tor` for anonymous browsing
3. **Behind firewall?** `proxy http://your-proxy:port`
4. **Check current settings:** `proxy` and `timeout` commands
5. **Switch on-the-fly:** All commands work while browsing

---

## ⚠️ Common Issues

### "Connection timed out"
```bash
> timeout 90
```

### "Could not connect to server" (with Tor)
```bash
# Check if Tor is running
sudo systemctl status tor

# If not, start it
sudo systemctl start tor
```

### "Missing dependencies for SOCKS support"
```bash
pip install PySocks
# or
pip install -r requirements.txt
```

---

## 📚 Full Documentation

- `PROXY_TIMEOUT_GUIDE.md` - Complete proxy & timeout guide
- `CHANGES_SUMMARY.md` - Detailed list of all changes
- `README.md` - Main documentation

---

## ✨ Summary

**Before:** TermLynx/1.0, incomplete headers, detected as bot  
**After:** Firefox User-Agent, complete headers, appears authentic

**Before:** 10s timeout (too short)  
**After:** 30s default, fully configurable

**Before:** No proxy support  
**After:** Tor + custom proxy support

---

**Created by:** Krishna D  
**Browser:** Ravanan v1.0.0  
🔱 *Browse with the wisdom of 10 heads!* 🔱

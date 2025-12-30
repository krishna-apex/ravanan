# 🧪 Testing Guide for Ravanan Browser

## How to Test the Fixed Browser

### Prerequisites
```bash
cd /home/user/Downloads/ravanan-main
pip install -r requirements.txt
```

---

## Method 1: Quick Verification Test (Automated)

Run the automated test script to verify all fixes:

```bash
python3 test_improvements.py
```

**Expected output:**
```
✅ User-Agent test PASSED - Looks like Firefox!
✅ Timeout test PASSED!
✅ Proxy test PASSED!
✅ All Firefox headers present!
🎉 ALL TESTS PASSED! 🎉
```

---

## Method 2: Run the Browser Directly

### Basic Test (No Proxy)
```bash
# From the project root
python3 -m ravanan

# Or
python3 -m ravanan duckduckgo.com

# With custom timeout
python3 -m ravanan --timeout 60
```

**What to do:**
1. Browser will load duckduckgo.com
2. Type `?` to see help with new proxy/timeout commands
3. Type `q` to quit

---

## Method 3: Test User-Agent Fix (Main Issue)

### Test on IPLeak.net
```bash
python3 -m ravanan ipleak.net --timeout 45
```

**What to check:**
- Browser engine should show: **Gecko** (Firefox)
- User-Agent should show: **Firefox/115.0**
- No warnings about "unfilled" or "AI-generated" fields
- Headers should look complete and authentic

### Alternative Test Sites
```bash
# Test 1: Check User-Agent
python3 -m ravanan
> go httpbin.org/user-agent

# Test 2: Check all headers
python3 -m ravanan
> go httpbin.org/headers

# Test 3: Browser fingerprint test
python3 -m ravanan whoer.net
```

**Expected results:**
- User-Agent contains "Firefox"
- All standard Firefox headers present
- No bot detection warnings

---

## Method 4: Test Timeout Configuration

### Test Command-Line Timeout
```bash
# Test with 60 second timeout
python3 -m ravanan duckduckgo.com --timeout 60
```

**In the browser:**
```
> timeout
⏱️  Current timeout: 60 seconds
```

### Test Runtime Timeout Change
```bash
python3 -m ravanan
```

**Commands to try:**
```
> timeout
⏱️  Current timeout: 30 seconds

> timeout 90
✅ Timeout set to 90 seconds

> timeout
⏱️  Current timeout: 90 seconds
```

### Test Actual Timeout Behavior
```bash
python3 -m ravanan --timeout 5
> go httpbin.org/delay/10
# Should timeout after 5 seconds with error message
```

---

## Method 5: Test Proxy Support

### Test Tor Proxy (if Tor is installed)

#### Step 1: Install and Start Tor
```bash
# Install Tor (Ubuntu/Debian)
sudo apt update
sudo apt install tor

# Start Tor
sudo systemctl start tor

# Verify Tor is running
sudo systemctl status tor
```

#### Step 2: Test Tor with Browser
```bash
python3 -m ravanan --proxy-tor --timeout 60
```

**What to check:**
```
🔐 Tor proxy enabled (make sure Tor is running!)
```

**Test commands in browser:**
```
> check.torproject.org
# Should show: "Congratulations. This browser is configured to use Tor."

> ifconfig.me
# Should show a Tor exit node IP (not your real IP)

> ipleak.net
# IP should be different from your real IP
```

#### Step 3: Test Tor Runtime Activation
```bash
python3 -m ravanan
```

**Commands:**
```
> proxy
🔓 No proxy configured (direct connection)

> proxy tor
✅ Tor proxy enabled (127.0.0.1:9050)

> reload
# Page should reload through Tor

> proxy
🔐 Proxy enabled:
   http: socks5h://127.0.0.1:9050
   https: socks5h://127.0.0.1:9050

> proxy off
✅ Proxy disabled
```

### Test Custom Proxy (if you have one)
```bash
# HTTP proxy
python3 -m ravanan --proxy http://proxy.example.com:8080

# SOCKS5 proxy
python3 -m ravanan --proxy socks5://192.168.1.100:1080
```

---

## Method 6: Interactive Feature Test

Start the browser and test all new commands:

```bash
python3 -m ravanan
```

### Test Session:
```bash
# 1. Check initial settings
> timeout
⏱️  Current timeout: 30 seconds

> proxy
🔓 No proxy configured (direct connection)

# 2. Load a page
> example.com

# 3. Change timeout
> timeout 60
✅ Timeout set to 60 seconds

# 4. Enable Tor (if installed)
> proxy tor
✅ Tor proxy enabled (127.0.0.1:9050)

# 5. Reload page through Tor
> reload

# 6. Check a test site
> check.torproject.org

# 7. Disable proxy
> proxy off
✅ Proxy disabled

# 8. View help for new features
> ?
# Should show proxy and timeout commands in help

# 9. Quit
> q
```

---

## Method 7: Compare Before vs After

### Create a Simple Test Script
```bash
cat > test_user_agent.py << 'EOF'
#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/user/Downloads/ravanan-main')
from ravanan.browser.fetcher import WebFetcher

fetcher = WebFetcher()
print("Current User-Agent:")
print(fetcher.user_agent)
print("\nChecking...")

# Verify fixes
checks = {
    "Contains 'Firefox'": "Firefox" in fetcher.user_agent,
    "Contains 'Mozilla'": "Mozilla" in fetcher.user_agent,
    "Contains 'Gecko'": "Gecko" in fetcher.user_agent,
    "NOT 'TermLynx'": "TermLynx" not in fetcher.user_agent,
    "Default timeout 30s": fetcher.timeout == 30,
}

for check, passed in checks.items():
    status = "✅" if passed else "❌"
    print(f"{status} {check}")

if all(checks.values()):
    print("\n🎉 All checks passed!")
else:
    print("\n❌ Some checks failed!")
EOF

chmod +x test_user_agent.py
python3 test_user_agent.py
```

---

## Quick Test Checklist

- [ ] **Browser starts**: `python3 -m ravanan`
- [ ] **Help shows new options**: `python3 -m ravanan --help`
- [ ] **User-Agent is Firefox**: Visit httpbin.org/user-agent
- [ ] **IPLeak shows Firefox**: Visit ipleak.net
- [ ] **Timeout command works**: `timeout 60` in browser
- [ ] **Proxy command works**: `proxy` in browser
- [ ] **Tor can be enabled**: `proxy tor` (if Tor installed)
- [ ] **Proxy can be disabled**: `proxy off` in browser
- [ ] **Help shows new commands**: `?` in browser

---

## Expected Results Summary

### ✅ User-Agent Fixed
- **Old**: `TermLynx/1.0 (Text-based Browser...)`
- **New**: `Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0`

### ✅ Timeout Configurable
- **Old**: Fixed at 10 seconds
- **New**: Default 30s, configurable via `--timeout` or `timeout` command

### ✅ Proxy Support Added
- **Old**: No proxy support
- **New**: Tor + custom proxy support

### ✅ No "Unfilled" Warnings
- **Old**: Sites like ipleak.net show incomplete/AI-generated warnings
- **New**: Shows complete Firefox headers, no warnings

---

## Troubleshooting Test Issues

### "No module named ravanan"
```bash
# Make sure you're in the project root
cd /home/user/Downloads/ravanan-main

# Try running directly
python3 -m ravanan
```

### "ImportError" or "ModuleNotFoundError"
```bash
# Install dependencies
pip install -r requirements.txt
```

### "Connection refused" with Tor
```bash
# Check if Tor is running
sudo systemctl status tor

# If not running
sudo systemctl start tor

# Verify port 9050 is listening
netstat -tuln | grep 9050
```

### "Missing dependencies for SOCKS"
```bash
# Install PySocks
pip install PySocks

# Or install all dependencies
pip install -r requirements.txt
```

---

## Real-World Test Scenarios

### Scenario 1: Check if Sites Detect You as Bot
```bash
python3 -m ravanan
> ipleak.net
# Look for browser engine = Gecko/Firefox
# Should NOT show bot warnings
```

### Scenario 2: Anonymous Browsing
```bash
python3 -m ravanan --proxy-tor --timeout 90
> check.torproject.org
> whoer.net
# Check IP is different, anonymity score improved
```

### Scenario 3: Slow Network
```bash
python3 -m ravanan --timeout 120
# Test with slow-loading sites
```

### Scenario 4: Corporate Proxy
```bash
python3 -m ravanan --proxy http://corporate-proxy:8080
> intranet.company.com
```

---

## Automated Test Script

Run this for a complete automated test:

```bash
cd /home/user/Downloads/ravanan-main
python3 test_improvements.py
```

Should output:
```
🎉 ALL TESTS PASSED! 🎉

Summary of improvements:
  ✅ User-Agent now appears as Firefox (not TermLynx)
  ✅ All Firefox HTTP headers included
  ✅ Timeout is configurable (default: 30 seconds)
  ✅ Tor proxy support added
  ✅ Custom proxy support added
  ✅ Runtime proxy/timeout configuration available
```

---

## Questions to Verify

After testing, ask yourself:

1. ✅ Does ipleak.net show Firefox instead of TermLynx?
2. ✅ Are there no "unfilled" or "AI-generated" warnings?
3. ✅ Can I change timeout with `timeout 60` command?
4. ✅ Can I enable Tor with `proxy tor` command?
5. ✅ Does `?` help show the new proxy/timeout commands?
6. ✅ Can I browse normally without errors?

If you answered YES to all, the fixes are working! 🎉

---

**Need Help?** Check [PROXY_TIMEOUT_GUIDE.md](PROXY_TIMEOUT_GUIDE.md) for detailed documentation.

**Created by:** Krishna D  
**Ravanan Browser v1.0.0**

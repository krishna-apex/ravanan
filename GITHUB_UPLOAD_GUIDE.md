# 📤 GitHub Upload Guide for Ravanan Browser

## ✅ Banner Removed!
The startup banner has been removed. The browser now starts cleanly without the ASCII art.

---

## 📁 What to Upload to GitHub

### ✅ **INCLUDE These Files/Folders:**

#### Core Application Files:
```
ravanan/                      # Main package folder
├── __init__.py              ✅ Package initialization
├── __main__.py              ✅ Entry point for python -m ravanan
├── main.py                  ✅ Main browser logic
└── browser/                 ✅ Browser modules
    ├── __init__.py          ✅
    ├── fetcher.py           ✅ HTTP fetching with proxy support
    ├── parser.py            ✅ HTML parsing
    ├── renderer.py          ✅ Terminal rendering
    └── navigator.py         ✅ Navigation & history
└── utils/                   ✅ Utility modules
    ├── __init__.py          ✅
    ├── banner.py            ✅
    └── history.py           ✅
```

#### Configuration Files:
```
setup.py                     ✅ Package installation script
requirements.txt             ✅ Python dependencies
MANIFEST.in                  ✅ Package manifest
.gitignore                   ✅ Git ignore rules
```

#### Documentation Files:
```
README.md                    ✅ Main documentation
LICENSE                      ✅ MIT License
CHANGELOG.md                 ✅ Version history
CONTRIBUTING.md              ✅ Contribution guidelines
FEATURES.md                  ✅ Feature list
QUICKSTART.md                ✅ Quick start guide
GETTING_STARTED.md           ✅ Getting started guide
PUBLISHING_GUIDE.md          ✅ Publishing guide

# NEW - Enhanced Documentation:
PROXY_TIMEOUT_GUIDE.md       ✅ Proxy & timeout configuration
CHANGES_SUMMARY.md           ✅ Summary of improvements
QUICK_REFERENCE.md           ✅ Quick reference card
TESTING_GUIDE.md             ✅ Testing instructions
GITHUB_UPLOAD_GUIDE.md       ✅ This file
```

---

### ❌ **DO NOT Include These:**

```
__pycache__/                 ❌ Python cache (auto-generated)
*.pyc                        ❌ Compiled Python files
*.pyo                        ❌ Optimized Python files
*.egg-info/                  ❌ Package metadata (auto-generated)
build/                       ❌ Build directory
dist/                        ❌ Distribution directory
.venv/                       ❌ Virtual environment
venv/                        ❌ Virtual environment
.idea/                       ❌ IDE settings
.vscode/                     ❌ VS Code settings
*.log                        ❌ Log files
*.txt (except requirements)  ❌ Saved pages
test_improvements.py         ❌ Local test script (optional)
```

---

## 🚀 Step-by-Step: Upload to GitHub

### Method 1: Using GitHub Web Interface

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Name: `ravanan` (or your preferred name)
   - Description: "The 10-Headed Web Browser - Terminal-based browser with privacy features"
   - Choose: Public or Private
   - DO NOT initialize with README (you already have one)
   - Click "Create repository"

2. **Initialize local Git repo:**
   ```bash
   cd /home/user/Downloads/ravanan-main
   git init
   git add .
   git commit -m "Initial commit: Ravanan browser with proxy and timeout support"
   ```

3. **Connect to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/ravanan.git
   git branch -M main
   git push -u origin main
   ```

### Method 2: Using GitHub CLI (if installed)

```bash
cd /home/user/Downloads/ravanan-main
gh repo create ravanan --public --source=. --remote=origin --push
```

---

## 📝 Prepare Your Repository

### 1. Update README.md

Make sure your README has:
- Project description
- Installation instructions
- New proxy/timeout features
- Usage examples

### 2. Update setup.py

Check that `setup.py` includes PySocks:

```python
install_requires=[
    "requests>=2.31.0",
    "beautifulsoup4>=4.12.0",
    "rich>=13.0.0",
    "lxml>=4.9.0",
    "PySocks>=1.7.1",  # ✅ Make sure this is included
],
```

### 3. Update CHANGELOG.md (Optional)

Add an entry for the new features:

```markdown
## [1.0.1] - 2025-12-30

### Added
- Firefox User-Agent for better website compatibility
- Configurable timeout (default 30s, via --timeout flag)
- Tor proxy support (--proxy-tor flag)
- Custom proxy support (--proxy flag)
- Runtime proxy and timeout configuration commands
- Complete Firefox HTTP headers

### Changed
- User-Agent changed from TermLynx to Firefox
- Default timeout increased from 10s to 30s
- Removed startup ASCII banner for cleaner interface

### Fixed
- Browser fingerprinting issues on sites like ipleak.net
- "AI-generated" detection warnings
```

---

## 🔍 Before Pushing - Checklist

Run these commands to verify everything is ready:

```bash
cd /home/user/Downloads/ravanan-main

# 1. Check for sensitive data
grep -r "password" .
grep -r "api_key" .
grep -r "secret" .

# 2. Test the browser still works
python3 -m ravanan --help

# 3. Run automated tests
python3 test_improvements.py

# 4. Check what will be committed
git status

# 5. Review files to be added
git add --dry-run .
```

---

## 📦 Complete File Structure to Upload

```
ravanan-main/
│
├── ravanan/                    # ✅ Main package
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py
│   ├── browser/
│   │   ├── __init__.py
│   │   ├── fetcher.py
│   │   ├── parser.py
│   │   ├── renderer.py
│   │   └── navigator.py
│   └── utils/
│       ├── __init__.py
│       ├── banner.py
│       └── history.py
│
├── setup.py                    # ✅ Installation script
├── requirements.txt            # ✅ Dependencies
├── MANIFEST.in                 # ✅ Package manifest
├── .gitignore                  # ✅ Git ignore
│
├── README.md                   # ✅ Main docs
├── LICENSE                     # ✅ MIT License
├── CHANGELOG.md                # ✅ Version history
├── CONTRIBUTING.md             # ✅ How to contribute
├── FEATURES.md                 # ✅ Feature list
├── QUICKSTART.md               # ✅ Quick start
├── GETTING_STARTED.md          # ✅ Getting started
├── PUBLISHING_GUIDE.md         # ✅ Publishing guide
│
├── PROXY_TIMEOUT_GUIDE.md      # ✅ NEW: Proxy guide
├── CHANGES_SUMMARY.md          # ✅ NEW: Changes summary
├── QUICK_REFERENCE.md          # ✅ NEW: Quick reference
├── TESTING_GUIDE.md            # ✅ NEW: Testing guide
└── GITHUB_UPLOAD_GUIDE.md      # ✅ NEW: This file
```

---

## 🎯 Quick Commands Summary

```bash
# Navigate to project
cd /home/user/Downloads/ravanan-main

# Initialize git
git init
git add .
git commit -m "Initial commit: Ravanan browser with enhanced privacy features"

# Connect to GitHub (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ravanan.git
git branch -M main
git push -u origin main
```

---

## 🔒 Security Notes

### ✅ Safe to Upload:
- All Python source code
- Documentation files
- Configuration files (setup.py, requirements.txt)
- License file

### ❌ Never Upload:
- Personal credentials
- API keys
- Private proxy configurations
- Personal browsing history
- Saved pages (*.txt files)
- Virtual environments
- IDE settings

---

## 📊 Repository Settings (After Upload)

### Recommended GitHub Settings:

1. **Topics/Tags:**
   - `terminal-browser`
   - `cli-browser`
   - `text-browser`
   - `python`
   - `web-browser`
   - `lynx`
   - `tor`
   - `proxy`
   - `privacy`

2. **Description:**
   ```
   The 10-Headed Web Browser - A powerful terminal-based web browser with Tor support, proxy configuration, and enhanced privacy features
   ```

3. **Website:** (if you have one)
   ```
   Your documentation URL or project page
   ```

4. **Enable Issues:** ✅ Yes (for bug reports)
5. **Enable Wikis:** Optional
6. **Enable Projects:** Optional

---

## 🎉 What's New in This Version

When people visit your GitHub repo, highlight these features:

### Key Features:
- ✅ **Authentic Firefox fingerprint** (no bot detection)
- ✅ **Tor proxy support** for anonymous browsing
- ✅ **Custom proxy support** (HTTP/HTTPS/SOCKS5)
- ✅ **Configurable timeouts** (command-line and runtime)
- ✅ **Complete Firefox headers** (no "unfilled" warnings)
- ✅ **Clean interface** (banner removed)
- ✅ **Runtime configuration** (change proxy/timeout while browsing)

### Installation:
```bash
pip install -r requirements.txt
python3 -m ravanan
```

### Quick Start:
```bash
# Normal browsing
python3 -m ravanan

# Anonymous with Tor
python3 -m ravanan --proxy-tor --timeout 60

# Custom proxy
python3 -m ravanan --proxy socks5://host:port
```

---

## 🆘 Need Help?

If you encounter issues during upload:

1. **Large file errors:**
   ```bash
   git rm --cached large_file.txt
   echo "large_file.txt" >> .gitignore
   ```

2. **Permission denied:**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   # Add SSH key to GitHub
   ```

3. **Merge conflicts:**
   ```bash
   git pull origin main --rebase
   git push origin main
   ```

---

## ✨ Summary

### Files to Upload: **25+ files**
### Total Size: **~50-100 KB** (without cache/build files)
### Time to Upload: **< 1 minute**

### Ready to push? Run:
```bash
cd /home/user/Downloads/ravanan-main
git init
git add .
git commit -m "Initial commit: Ravanan browser v1.0.1 with privacy enhancements"
git remote add origin https://github.com/YOUR_USERNAME/ravanan.git
git branch -M main
git push -u origin main
```

**Done!** Your browser is now on GitHub! 🎉

---

**Created by:** Krishna D  
**Version:** 1.0.1  
**Date:** December 30, 2025

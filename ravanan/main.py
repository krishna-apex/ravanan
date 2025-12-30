#!/usr/bin/env python3
"""
Ravanan - The 10-Headed Web Browser
A powerful text-based web browser for the terminal

Named after the mythological character Ravana, known for his 10 heads
representing vast knowledge and multiple perspectives - perfect for
viewing the web in a unique way!

Created by: Krishna D
"""
import sys
import argparse
import os
from .browser.fetcher import WebFetcher
from .browser.parser import HTMLParser
from .browser.renderer import TextRenderer
from .browser.navigator import Navigator


class Ravanan:
    """Main browser application"""
    
    def __init__(self, home_url: str = "https://duckduckgo.com", timeout: int = 30, proxy: dict = None):
        self.fetcher = WebFetcher(timeout=timeout, proxy=proxy)
        self.parser = HTMLParser()
        self.renderer = TextRenderer()
        self.navigator = Navigator()
        self.home_url = home_url
        self.current_title = ""
        self.current_content = []
        self.current_html = ""  # Store raw HTML source
        self.running = True
    
    def start(self, initial_url: str = None):
        """
        Start the browser
        
        Args:
            initial_url: URL to open on startup
        """
        # Load initial page
        url = initial_url or self.home_url
        self.load_page(url)
        
        # Main loop
        while self.running:
            try:
                command = input("\n> ").strip()
                self.handle_command(command)
            except KeyboardInterrupt:
                self.quit()
            except EOFError:
                self.quit()
            except Exception as e:
                self.renderer.render_error(f"Unexpected error: {str(e)}")
    
    def load_page(self, url: str, add_to_history: bool = True):
        """
        Load and display a web page
        
        Args:
            url: URL to load
            add_to_history: Whether to add to history (False for back/forward)
        """
        # Show loading message
        self.renderer.render_loading(url)
        
        # Fetch page
        success, content, final_url, status_code = self.fetcher.fetch(url)
        
        if not success:
            self.renderer.render_error(content)
            return False
        
        # Parse HTML
        try:
            links, text_content = self.parser.parse(content, final_url)
            title = self.parser.get_page_title()
            
            # Update navigator
            if add_to_history:
                self.navigator.set_current_page(final_url, links)
            else:
                # For back/forward, update current page without adding to history
                self.navigator.current_url = final_url
                self.navigator.current_links = links
            
            # Store current page data
            self.current_title = title
            self.current_content = text_content
            self.current_html = content  # Store raw HTML source
            
            # Render page
            self.renderer.render_page(title, text_content, links, final_url)
            
            return True
            
        except Exception as e:
            self.renderer.render_error(f"Failed to parse page: {str(e)}")
            return False
    
    def handle_command(self, command: str):
        """
        Handle user commands
        
        Args:
            command: User input command
        """
        if not command:
            return
        
        cmd_lower = command.lower().strip()
        
        # Quit commands
        if cmd_lower in ['q', 'quit', 'exit']:
            self.quit()
        
        # Back
        elif cmd_lower == 'b' or cmd_lower == 'back':
            self.go_back()
        
        # Forward
        elif cmd_lower == 'f' or cmd_lower == 'forward':
            self.go_forward()
        
        # Reload
        elif cmd_lower == 'r' or cmd_lower == 'reload':
            self.reload()
        
        # Home
        elif cmd_lower == 'h' or cmd_lower == 'home':
            self.go_home()
        
        # Help
        elif cmd_lower in ['?', 'help']:
            self.show_help()
        
        # About
        elif cmd_lower == 'about':
            self.show_about()
        
        # Current URL
        elif cmd_lower in ['u', 'url']:
            self.show_current_url()
        
        # History
        elif cmd_lower == 'history':
            self.show_history()
        
        # List links
        elif cmd_lower == 'links':
            self.list_all_links()
        
        # Page info
        elif cmd_lower == 'info':
            self.show_page_info()
        
        # Stats
        elif cmd_lower == 'stats':
            self.show_stats()
        
        # Save page
        elif cmd_lower == 'save':
            self.save_page()
        
        # Show page source
        elif cmd_lower in ['src', 'source']:
            self.show_source()
        
        # Show full page source
        elif cmd_lower in ['src all', 'source all']:
            self.show_source(show_all=True)
        
        # Clear screen
        elif cmd_lower == 'clear':
            self.clear_screen()
            # Redisplay current page
            if self.current_title:
                self.renderer.render_page(
                    self.current_title, 
                    self.current_content, 
                    self.navigator.current_links, 
                    self.navigator.reload()
                )
        
        # Version
        elif cmd_lower == 'version':
<<<<<<< HEAD
            print(f"\n🔱 Ravanan Browser v1.0.0")
            print(f"Created by Krishna D\n")
        
=======
            print(f"\n🔱 Ravanan Browser v1.0.4")
            print(f"Created by Krishna D\n")
        
        # Configure timeout
        elif cmd_lower.startswith('timeout '):
            try:
                timeout_val = int(command.split()[1])
                if timeout_val > 0:
                    self.fetcher.set_timeout(timeout_val)
                    print(f"\n✅ Timeout set to {timeout_val} seconds\n")
                else:
                    self.renderer.render_error("Timeout must be a positive number")
            except (ValueError, IndexError):
                self.renderer.render_error("Usage: timeout <seconds> (e.g., timeout 30)")
        
        # Show current timeout
        elif cmd_lower == 'timeout':
            print(f"\n⏱️  Current timeout: {self.fetcher.timeout} seconds\n")
        
        # Configure proxy
        elif cmd_lower == 'proxy tor':
            self.fetcher.use_tor()
            print(f"\n✅ Tor proxy enabled (127.0.0.1:9050)\n")
            print(f"   Make sure Tor is running!\n")
        
        # Set custom proxy
        elif cmd_lower.startswith('proxy ') and cmd_lower != 'proxy tor' and cmd_lower != 'proxy off':
            proxy_url = command.split(maxsplit=1)[1].strip()
            if proxy_url:
                self.fetcher.set_proxy({
                    'http': proxy_url,
                    'https': proxy_url
                })
                print(f"\n✅ Proxy set to: {proxy_url}\n")
            else:
                self.renderer.render_error("Usage: proxy <url> (e.g., proxy socks5://127.0.0.1:9050)")
        
        # Disable proxy
        elif cmd_lower == 'proxy off':
            self.fetcher.disable_proxy()
            print(f"\n✅ Proxy disabled\n")
        
        # Show proxy status
        elif cmd_lower == 'proxy':
            if self.fetcher.proxy:
                print(f"\n🔐 Proxy enabled:")
                for key, value in self.fetcher.proxy.items():
                    print(f"   {key}: {value}")
                print()
            else:
                print(f"\n🔓 No proxy configured (direct connection)\n")
        
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
        # Search (case-insensitive)
        elif command.startswith('/') and not command.startswith('//'):
            query = command[1:].strip()
            if query:
                self.search(query, case_sensitive=False)
        
        # Search (case-sensitive)
        elif command.startswith('//'):
            query = command[2:].strip()
            if query:
                self.search(query, case_sensitive=True)
        
        # Go to URL (with 'go' prefix)
        elif cmd_lower.startswith('go '):
            url = command[3:].strip()
            if url:
                self.load_page(url)
        
        # Go to URL (direct)
        elif command.startswith('http://') or command.startswith('https://'):
            self.load_page(command)
        
        # Go to link by number
        elif command.isdigit():
            link_index = int(command)
            self.go_to_link(link_index)
        
        # Unknown command - try as URL
        else:
            # Try to treat it as a URL without scheme
            if '.' in command and ' ' not in command:
                self.load_page(command)
            else:
                self.renderer.render_error(
                    f"Unknown command: '{command}'. Type '?' for help."
                )
    
    def go_back(self):
        """Go back in history"""
        if not self.navigator.can_go_back():
            self.renderer.render_error("Cannot go back - no previous page")
            return
        
        url = self.navigator.go_back()
        if url:
            self.load_page(url, add_to_history=False)
    
    def go_forward(self):
        """Go forward in history"""
        if not self.navigator.can_go_forward():
            self.renderer.render_error("Cannot go forward - no next page")
            return
        
        url = self.navigator.go_forward()
        if url:
            self.load_page(url, add_to_history=False)
    
    def reload(self):
        """Reload current page"""
        url = self.navigator.reload()
        if url:
            self.load_page(url, add_to_history=False)
        else:
            self.renderer.render_error("No page to reload")
    
    def go_home(self):
        """Go to home page"""
        self.load_page(self.home_url)
    
    def go_to_link(self, index: int):
        """
        Navigate to a link by index
        
        Args:
            index: Link index number
        """
        url = self.navigator.get_link_by_index(index)
        if url:
            self.load_page(url)
        else:
            self.renderer.render_error(
                f"Link [{index}] not found. "
                f"Available links: 1-{self.navigator.get_link_count()}"
            )
    
    def search(self, query: str, case_sensitive: bool = False):
        """
        Search in current page content
        
        Args:
            query: Search query
            case_sensitive: Whether search should be case-sensitive
        """
        results = []
        query_search = query if case_sensitive else query.lower()
        
        for item_type, text, level in self.current_content:
            text_search = text if case_sensitive else text.lower()
            if query_search in text_search:
                results.append(text)
        
        # Display search type
        search_type = "Case-sensitive" if case_sensitive else "Case-insensitive"
        self.renderer.render_search_results(f"{query} ({search_type})", results)
    
    def show_help(self):
        """Display comprehensive help information"""
        help_text = """
╔══════════════════════════════════════════════════════════════════════╗
║                  🔱 RAVANAN - THE 10-HEADED BROWSER 🔱               ║
║                      Comprehensive Help Guide                        ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  📍 NAVIGATION COMMANDS                                              ║
║  ───────────────────────                                             ║
║  [number]     → Navigate to link by number (e.g., 1, 2, 3)          ║
║  b            → Go back to previous page                             ║
║  f            → Go forward to next page                              ║
║  h            → Go to home page                                      ║
║  r            → Reload current page                                  ║
║  u            → Show current URL                                     ║
║                                                                      ║
║  🌐 URL COMMANDS                                                     ║
║  ─────────────                                                       ║
║  [url]        → Enter full URL (https://example.com)                 ║
║  [domain]     → Enter domain (example.com)                           ║
║  go [url]     → Navigate to URL (alternative)                        ║
║                                                                      ║
║  🔍 SEARCH & DISCOVERY                                               ║
║  ───────────────────                                                 ║
║  /[query]     → Search in current page (e.g., /python)              ║
║  //[query]    → Case-sensitive search                                ║
║  links        → List all links on current page                       ║
║  find [n]     → Jump to nth search result                            ║
║                                                                      ║
║  📊 INFORMATION & STATS                                              ║
║  ─────────────────────                                               ║
║  info         → Show current page information                        ║
║  history      → Show browsing history                                ║
║  stats        → Show browser statistics                              ║
║  about        → About Ravanan browser                                ║
║                                                                      ║
<<<<<<< HEAD
=======
║  � PROXY & TIMEOUT SETTINGS                                         ║
║  ──────────────────────────                                          ║
║  proxy        → Show current proxy status                            ║
║  proxy tor    → Enable Tor proxy (127.0.0.1:9050)                    ║
║  proxy [url]  → Set custom proxy (e.g., socks5://host:port)         ║
║  proxy off    → Disable proxy                                        ║
║  timeout      → Show current timeout value                           ║
║  timeout [n]  → Set timeout in seconds (e.g., timeout 60)            ║
║                                                                      ║
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
║  💾 UTILITY COMMANDS                                                 ║
║  ──────────────────                                                  ║
║  save         → Save current page as text file                       ║
║  src          → Show page HTML source (first 50 lines)               ║
║  source       → Show page HTML source (alias)                        ║
║  src all      → Show complete HTML source code                       ║
║  clear        → Clear screen                                         ║
║  version      → Show version information                             ║
║  ?            → Show this help                                       ║
║  help         → Show this help (alternative)                         ║
║  q            → Quit browser                                         ║
║  exit         → Quit browser (alternative)                           ║
║                                                                      ║
║  ⌨️  QUICK TIPS                                                      ║
║  ────────────                                                        ║
║  • Press Enter on empty line to refresh                              ║
║  • Use short domains: 'wikipedia.org' works!                         ║
║  • Numbers 1-999 for link navigation                                 ║
║  • All commands are case-insensitive                                 ║
<<<<<<< HEAD
=======
║  • Default timeout: 30 seconds (configurable)                        ║
║  • Tor requires Tor service running locally                          ║
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║  Created by: Krishna D | Inspired by Ravana's 10 heads of wisdom    ║
╚══════════════════════════════════════════════════════════════════════╝
        """
        print(help_text)
    
    def show_about(self):
        """Display about information"""
        about_text = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        🔱 RAVANAN - THE 10-HEADED WEB BROWSER 🔱            ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
<<<<<<< HEAD
║  Version: 1.0.0                                              ║
║  Created by: Krishna D                                       ║
║  Release Date: November 1, 2025                              ║
=======
║  Version: 1.0.4                                              ║
║  Created by: Krishna D                                       ║
║  Development Time: 3-5 months                                ║
║  Release Date: December 30, 2025                             ║
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
║                                                              ║
║  Why "Ravanan"?                                              ║
║  ──────────────                                              ║
║  Named after the legendary Ravana, the 10-headed king        ║
║  from Hindu mythology. Each head represents a different      ║
║  dimension of knowledge and wisdom - just like how this      ║
║  browser allows you to view the web from multiple angles,    ║
║  stripping away the noise to reveal pure information.        ║
║                                                              ║
║  The 10 Heads Represent:                                     ║
║  ─────────────────────────                                   ║
║  1. Smart HTML Parsing                                       ║
║  2. Fast HTTP Fetching                                       ║
║  3. Beautiful Rendering                                      ║
║  4. Link Navigation                                          ║
║  5. History Management                                       ║
║  6. In-Page Search                                           ║
║  7. Error Handling                                           ║
║  8. Content Extraction                                       ║
║  9. Clean Interface                                          ║
║  10. Terminal Power                                          ║
║                                                              ║
║  Philosophy:                                                 ║
║  ───────────                                                 ║
║  Browse the web with wisdom, not just your eyes.             ║
║  See through the clutter. Access pure knowledge.             ║
║                                                              ║
║  Technology Stack:                                           ║
║  ─────────────────                                           ║
║  • Python 3.8+                                               ║
║  • Requests - HTTP/HTTPS                                     ║
║  • BeautifulSoup4 - HTML Parsing                             ║
║  • Rich - Terminal UI                                        ║
║                                                              ║
║  License: MIT License                                        ║
║  Open Source & Free Forever                                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(about_text)
    
    def show_current_url(self):
        """Display current URL"""
        url = self.navigator.reload()
        if url:
            print(f"\n📍 Current URL: {url}\n")
        else:
            print("\n⚠️  No page loaded yet\n")
    
    def show_history(self):
        """Display browsing history"""
        history_list = self.navigator.history.get_history_list()
        current_idx = self.navigator.history.current_index
        
        if not history_list:
            print("\n📜 No browsing history yet\n")
            return
        
        print("\n" + "=" * 60)
        print("📜 BROWSING HISTORY")
        print("=" * 60)
        
        for idx, url in enumerate(history_list):
            marker = "→ " if idx == current_idx else "  "
            print(f"{marker}{idx + 1}. {url}")
        
        print("=" * 60)
        print(f"Total pages visited: {len(history_list)}")
        print("=" * 60 + "\n")
    
    def list_all_links(self):
        """List all links on current page"""
        if not self.navigator.current_links:
            print("\n⚠️  No links found on current page\n")
            return
        
        print("\n" + "=" * 60)
        print(f"🔗 ALL LINKS ({len(self.navigator.current_links)} total)")
        print("=" * 60)
        
        for link in self.navigator.current_links:
            print(f"[{link['index']}] {link['text']}")
            print(f"    {link['url']}")
            print()
        
        print("=" * 60 + "\n")
    
    def show_page_info(self):
        """Display current page information"""
        if not self.current_title:
            print("\n⚠️  No page loaded\n")
            return
        
        url = self.navigator.reload()
        link_count = self.navigator.get_link_count()
        
        print("\n" + "=" * 60)
        print("📄 PAGE INFORMATION")
        print("=" * 60)
        print(f"Title: {self.current_title}")
        print(f"URL: {url}")
        print(f"Links found: {link_count}")
        print(f"Content elements: {len(self.current_content)}")
        print("=" * 60 + "\n")
    
    def show_stats(self):
        """Display browser statistics"""
        history_count = len(self.navigator.history.get_history_list())
        link_count = self.navigator.get_link_count()
        
        print("\n" + "=" * 60)
        print("📊 BROWSER STATISTICS")
        print("=" * 60)
        print(f"Pages visited this session: {history_count}")
        print(f"Links on current page: {link_count}")
        print(f"Can go back: {'Yes' if self.navigator.can_go_back() else 'No'}")
        print(f"Can go forward: {'Yes' if self.navigator.can_go_forward() else 'No'}")
        print(f"Current page loaded: {'Yes' if self.current_title else 'No'}")
        print("=" * 60 + "\n")
    
    def save_page(self):
        """Save current page as text file"""
        if not self.current_title:
            self.renderer.render_error("No page loaded to save")
            return
        
        # Generate filename from title
        import re
        filename = re.sub(r'[^\w\s-]', '', self.current_title)
        filename = re.sub(r'[-\s]+', '_', filename)
        filename = f"{filename[:50]}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Title: {self.current_title}\n")
                f.write(f"URL: {self.navigator.reload()}\n")
                f.write(f"Saved: {__import__('datetime').datetime.now()}\n")
                f.write("=" * 60 + "\n\n")
                
                for item_type, text, level in self.current_content:
                    if item_type == 'heading':
                        f.write(f"\n{'#' * level} {text}\n")
                    elif item_type in ['text', 'paragraph', 'list_item']:
                        f.write(f"{text}\n")
                    elif item_type == 'newline':
                        f.write("\n")
                
                f.write("\n" + "=" * 60 + "\n")
                f.write(f"\nLinks ({len(self.navigator.current_links)}):\n")
                for link in self.navigator.current_links:
                    f.write(f"[{link['index']}] {link['text']}\n")
                    f.write(f"    {link['url']}\n")
            
            print(f"\n✅ Page saved to: {filename}\n")
        except Exception as e:
            self.renderer.render_error(f"Failed to save page: {str(e)}")
    
    def show_source(self, show_all=False):
        """Display the HTML source code of the current page
        
        Args:
            show_all: Whether to show all lines or just a preview
        """
        if not self.current_html:
            self.renderer.render_error("No page loaded to show source")
            return
        
        print("\n" + "=" * 70)
        print("📝 PAGE SOURCE CODE")
        print("=" * 70)
        print(f"URL: {self.navigator.reload()}")
        print(f"Size: {len(self.current_html)} characters")
        print("=" * 70)
        
        # Show lines of source with line numbers
        lines = self.current_html.split('\n')
        total_lines = len(lines)
        
        if not show_all and total_lines > 50:
            print(f"\nTotal lines: {total_lines}")
            print("Showing first 50 lines... (Type 'src all' to see everything)")
            print("-" * 70)
            lines_to_show = lines[:50]
        else:
            print(f"\nTotal lines: {total_lines}")
            if show_all:
                print("Showing all lines...")
            print("-" * 70)
            lines_to_show = lines
        
        for i, line in enumerate(lines_to_show, 1):
            # Truncate very long lines
            if len(line) > 120:
                line = line[:117] + "..."
            print(f"{i:4d} | {line}")
        
        if not show_all and total_lines > 50:
            print("-" * 70)
            print(f"... {total_lines - 50} more lines ...")
        
        print("=" * 70 + "\n")
    
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def quit(self):
        """Quit the browser"""
<<<<<<< HEAD
        print("\n👋 Thanks for using Ravanan! May you browse with the wisdom of 10 heads! 🔱\n")
        print("   Created by Krishna D\n")
=======
        print("\n👋 Goodbye!\n")
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
        self.running = False
        sys.exit(0)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Ravanan - The 10-Headed Web Browser (Created by Krishna D)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
<<<<<<< HEAD
  python main.py
  python main.py https://example.com
  python main.py wikipedia.org
=======
  ravanan
  ravanan https://duckduckgo.com
  ravanan wikipedia.org --timeout 60
  ravanan duckduckgo.com --proxy-tor
  ravanan --proxy socks5://127.0.0.1:9050
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)

The 10 Heads of Ravanan represent:
  1. Smart Parsing  2. Fast Fetching   3. Beautiful Rendering
  4. Navigation     5. History         6. Search
  7. Error Handling 8. Extraction      9. Clean UI
  10. Terminal Power

Created by: Krishna D
        """
    )
    
    parser.add_argument(
        'url',
        nargs='?',
<<<<<<< HEAD
        default='https://example.com',
        help='URL to open on startup (default: https://example.com)'
=======
        default='https://duckduckgo.com',
        help='URL to open on startup (default: https://duckduckgo.com)'
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
    )
    
    parser.add_argument(
        '--home',
<<<<<<< HEAD
        default='https://example.com',
        help='Set home page URL (default: https://example.com)'
=======
        default='https://duckduckgo.com',
        help='Set home page URL (default: https://duckduckgo.com)'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=30,
        help='Request timeout in seconds (default: 30)'
    )
    
    parser.add_argument(
        '--proxy',
        type=str,
        help='Proxy URL (e.g., socks5://127.0.0.1:9050 or http://proxy.example.com:8080)'
    )
    
    parser.add_argument(
        '--proxy-tor',
        action='store_true',
        help='Use Tor proxy (socks5h://127.0.0.1:9050)'
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
    )
    
    parser.add_argument(
        '--version',
        action='version',
<<<<<<< HEAD
        version='Ravanan 1.0.0 - Created by Krishna D'
=======
        version='Ravanan 1.0.4 - Created by Krishna D'
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
    )
    
    args = parser.parse_args()
    
<<<<<<< HEAD
    # Display banner
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        ██████  █████ ██   ██ █████ ███   ██ █████ ███   ║
    ║        ██   ██ ██ ██ ██   ██ ██ ██ ████  ██ ██ ██ ████  ║
    ║        ██████  █████  ██ ██  █████ ██ ██ ██ █████ ██ ██ ║
    ║        ██   ██ ██ ██   ███   ██ ██ ██  ████ ██ ██ ██  ██║
    ║        ██   ██ ██  ██   █    ██  █ ██   ███ ██  █ ██   █║
    ║                                                           ║
    ║              The 10-Headed Web Browser                    ║
    ║              By Krishna D  •  v1.0.0                      ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    Type '?' for help  •  'about' for info  •  'q' to quit
    """)
    
    # Create and start browser
    browser = Ravanan(home_url=args.home)
=======
    # Setup proxy configuration
    proxy = None
    if args.proxy_tor:
        proxy = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        print("🔐 Tor proxy enabled (make sure Tor is running!)")
    elif args.proxy:
        proxy = {
            'http': args.proxy,
            'https': args.proxy
        }
        print(f"🔐 Proxy enabled: {args.proxy}")
    
    if args.timeout != 30:
        print(f"⏱️  Timeout: {args.timeout} seconds")
    
    # Create and start browser
    browser = Ravanan(home_url=args.home, timeout=args.timeout, proxy=proxy)
>>>>>>> 928bfc6 (Ravanan v1.0.4 - Terminal browser with Tor support and link pagination fix)
    browser.start(initial_url=args.url)


if __name__ == "__main__":
    main()

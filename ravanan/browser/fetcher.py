"""
HTTP Fetcher Module
Handles fetching web pages with error handling and redirects
"""
import requests
from typing import Optional, Tuple
from urllib.parse import urljoin, urlparse


class WebFetcher:
    """Fetches web content via HTTP/HTTPS"""
    
    def __init__(self, timeout: int = 30, user_agent: str = None, proxy: dict = None):
        self.timeout = timeout
        self.user_agent = user_agent or (
            "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
        )
        self.proxy = proxy
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.user_agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            # Accept-Encoding is handled automatically by requests
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1'
        })
        if self.proxy:
            self.session.proxies.update(self.proxy)
    
    def fetch(self, url: str) -> Tuple[bool, str, str, int]:
        """
        Fetch a URL and return its content
        
        Args:
            url: The URL to fetch
            
        Returns:
            Tuple of (success, content/error_message, final_url, status_code)
        """
        try:
            # Ensure URL has a scheme
            if not urlparse(url).scheme:
                url = 'https://' + url
            
            response = self.session.get(
                url,
                timeout=self.timeout,
                allow_redirects=True,
                proxies=self.proxy
            )
            
            # Check if request was successful
            if response.status_code == 200:
                # Ensure proper text decoding
                response.encoding = response.apparent_encoding or 'utf-8'
                return True, response.text, response.url, response.status_code
            elif response.status_code == 404:
                return False, "Error 404: Page not found", url, 404
            elif response.status_code == 403:
                return False, "Error 403: Access forbidden", url, 403
            elif response.status_code == 500:
                return False, "Error 500: Internal server error", url, 500
            else:
                return False, f"Error {response.status_code}: {response.reason}", url, response.status_code
                
        except requests.exceptions.Timeout:
            return False, f"Error: Request timed out after {self.timeout} seconds", url, 0
        except requests.exceptions.ConnectionError:
            return False, "Error: Could not connect to server. Check your internet connection.", url, 0
        except requests.exceptions.TooManyRedirects:
            return False, "Error: Too many redirects", url, 0
        except requests.exceptions.InvalidURL:
            return False, "Error: Invalid URL format", url, 0
        except requests.exceptions.RequestException as e:
            return False, f"Error: {str(e)}", url, 0
        except Exception as e:
            return False, f"Unexpected error: {str(e)}", url, 0
    
    def normalize_url(self, url: str, base_url: str = None) -> str:
        """
        Normalize a URL (handle relative URLs, fragments, etc.)
        
        Args:
            url: The URL to normalize
            base_url: The base URL for resolving relative URLs
            
        Returns:
            Normalized absolute URL
        """
        if base_url:
            url = urljoin(base_url, url)
        
        # Ensure scheme exists
        if not urlparse(url).scheme:
            url = 'https://' + url
            
        return url
    
    def set_timeout(self, timeout: int):
        """
        Update the timeout value
        
        Args:
            timeout: New timeout value in seconds
        """
        self.timeout = timeout
    
    def set_proxy(self, proxy: dict = None):
        """
        Update the proxy settings
        
        Args:
            proxy: Dictionary with proxy settings (e.g., {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'})
                   or None to disable proxy
        """
        self.proxy = proxy
        if self.proxy:
            self.session.proxies.update(self.proxy)
        else:
            self.session.proxies.clear()
    
    def use_tor(self):
        """
        Configure the fetcher to use Tor proxy (localhost:9050)
        """
        self.set_proxy({
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        })
    
    def disable_proxy(self):
        """
        Disable any configured proxy
        """
        self.set_proxy(None)

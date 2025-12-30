#!/usr/bin/env python3
"""
Test script to verify Ravanan browser fingerprinting improvements
"""
import sys
sys.path.insert(0, '/home/user/Downloads/ravanan-main')

from ravanan.browser.fetcher import WebFetcher

def test_user_agent():
    """Test that User-Agent is set to Firefox"""
    print("=" * 70)
    print("TEST 1: User-Agent Check")
    print("=" * 70)
    
    fetcher = WebFetcher()
    
    print(f"\nUser-Agent: {fetcher.user_agent}")
    print(f"\nSession Headers:")
    for key, value in fetcher.session.headers.items():
        print(f"  {key}: {value}")
    
    # Verify it's Firefox
    assert "Firefox" in fetcher.user_agent, "User-Agent should contain 'Firefox'"
    assert "Mozilla/5.0" in fetcher.user_agent, "User-Agent should contain 'Mozilla/5.0'"
    assert "Gecko" in fetcher.user_agent, "User-Agent should contain 'Gecko'"
    assert "TermLynx" not in fetcher.user_agent, "User-Agent should NOT contain 'TermLynx'"
    
    print("\n✅ User-Agent test PASSED - Looks like Firefox!")


def test_timeout():
    """Test timeout configuration"""
    print("\n" + "=" * 70)
    print("TEST 2: Timeout Configuration")
    print("=" * 70)
    
    # Test default timeout
    fetcher = WebFetcher()
    assert fetcher.timeout == 30, "Default timeout should be 30 seconds"
    print(f"\n✅ Default timeout: {fetcher.timeout} seconds")
    
    # Test custom timeout
    fetcher = WebFetcher(timeout=60)
    assert fetcher.timeout == 60, "Custom timeout should be 60 seconds"
    print(f"✅ Custom timeout: {fetcher.timeout} seconds")
    
    # Test set_timeout method
    fetcher.set_timeout(120)
    assert fetcher.timeout == 120, "Updated timeout should be 120 seconds"
    print(f"✅ Updated timeout: {fetcher.timeout} seconds")
    
    print("\n✅ Timeout test PASSED!")


def test_proxy():
    """Test proxy configuration"""
    print("\n" + "=" * 70)
    print("TEST 3: Proxy Configuration")
    print("=" * 70)
    
    # Test no proxy
    fetcher = WebFetcher()
    assert fetcher.proxy is None, "Default proxy should be None"
    print("\n✅ No proxy by default")
    
    # Test Tor proxy
    fetcher.use_tor()
    assert fetcher.proxy is not None, "Tor proxy should be set"
    assert 'socks5h://127.0.0.1:9050' in fetcher.proxy.get('http', ''), "Should use Tor SOCKS5 proxy"
    print(f"✅ Tor proxy configured: {fetcher.proxy}")
    
    # Test custom proxy
    custom_proxy = {'http': 'http://proxy.example.com:8080', 'https': 'http://proxy.example.com:8080'}
    fetcher.set_proxy(custom_proxy)
    assert fetcher.proxy == custom_proxy, "Custom proxy should be set"
    print(f"✅ Custom proxy configured: {fetcher.proxy}")
    
    # Test disable proxy
    fetcher.disable_proxy()
    assert fetcher.proxy is None, "Proxy should be disabled"
    print(f"✅ Proxy disabled")
    
    print("\n✅ Proxy test PASSED!")


def test_headers():
    """Test that all Firefox headers are present"""
    print("\n" + "=" * 70)
    print("TEST 4: Firefox Headers Check")
    print("=" * 70)
    
    fetcher = WebFetcher()
    headers = fetcher.session.headers
    
    required_headers = [
        'User-Agent',
        'Accept',
        'Accept-Language',
        'Accept-Encoding',
        'DNT',
        'Connection',
        'Upgrade-Insecure-Requests',
        'Sec-Fetch-Dest',
        'Sec-Fetch-Mode',
        'Sec-Fetch-Site',
        'Sec-Fetch-User'
    ]
    
    print("\nChecking required Firefox headers:")
    for header in required_headers:
        assert header in headers, f"Header '{header}' should be present"
        print(f"  ✓ {header}: {headers[header]}")
    
    print("\n✅ All Firefox headers present!")


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("RAVANAN BROWSER - FINGERPRINTING FIX VERIFICATION")
    print("=" * 70)
    print()
    
    try:
        test_user_agent()
        test_timeout()
        test_proxy()
        test_headers()
        
        print("\n" + "=" * 70)
        print("🎉 ALL TESTS PASSED! 🎉")
        print("=" * 70)
        print()
        print("Summary of improvements:")
        print("  ✅ User-Agent now appears as Firefox (not TermLynx)")
        print("  ✅ All Firefox HTTP headers included")
        print("  ✅ Timeout is configurable (default: 30 seconds)")
        print("  ✅ Tor proxy support added")
        print("  ✅ Custom proxy support added")
        print("  ✅ Runtime proxy/timeout configuration available")
        print()
        print("The browser should no longer show 'unfilled' or 'AI generated' warnings")
        print("on sites like ipleak.net!")
        print()
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

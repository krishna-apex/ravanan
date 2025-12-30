"""
Setup script for Ravanan - The 10-Headed Web Browser
Allows installation via pip

Created by: Krishna D
"""
from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ravanan",
    version="1.0.4",
    description="The 10-Headed Web Browser - A powerful text-based browser for the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/krishna182005/ravanan",
    author="Krishna D",
    
    
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Terminals",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Environment :: Console",
        "Natural Language :: English",
    ],
    
    keywords="browser, terminal, cli, text-based, lynx, web, http, https, ravanan, ravana, 10-headed, tui, console, accessibility",
    
    packages=find_packages(),
    
    python_requires=">=3.8",
    
    install_requires=[
        "requests>=2.31.0",
        "beautifulsoup4>=4.12.0",
        "rich>=13.0.0",
        "lxml>=4.9.0",
        "PySocks>=1.7.1",
    ],
    
    entry_points={
        "console_scripts": [
            "ravanan=ravanan:main",
        ],
    },
    
    project_urls={
        "Bug Reports": "https://github.com/krishna182005/ravanan/issues",
        "Source": "https://github.com/krishna182005/ravanan",
        "Documentation": "https://github.com/krishna182005/ravanan#readme",
        "Changelog": "https://github.com/krishna182005/ravanan/blob/main/CHANGELOG.md",
    },
    
    include_package_data=True,
    zip_safe=False,
)



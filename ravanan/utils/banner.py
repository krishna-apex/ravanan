"""
Banner Module
Displays the Ravanan ASCII art banner with responsive sizing and colors
Inspired by the mythological Ravana - the 10-headed scholar king

Created by: Krishna D
"""
import shutil
from rich.console import Console
from rich.text import Text


class RavananBanner:
    """Handles displaying the Ravanan ASCII art banner with colors"""
    
    # Full banner for extra wide terminals (≥90 columns)
    FULL_BANNER = r"""
 (                                 )             )  
 )\ )    (               (      ( /(   (      ( /(  
(()/(    )\     (   (    )\     )\())  )\     )\()) 
 /(_))((((_)(   )\  )\((((_)(  ((_)\((((_)(  ((_)\  
(_))   )\ _ )\ ((_)((_))\ _ )\  _((_))\ _ )\  _((_) 
| _ \  (_)_\(_)\ \ / / (_)_\(_)| \| |(_)_\(_)| \| | 
|   /   / _ \   \ V /   / _ \  | .` | / _ \  | .` | 
|_|_\  /_/ \_\   \_/   /_/ \_\ |_|\_|/_/ \_\ |_|\_| 
                                                    
The 10-Headed Scholar King • Terminal Web Browser
                v1.0.5 • By Krishna D
    """

    # Large banner for wide terminals (≥70 columns)
    LARGE_BANNER = r"""
 (                                 )             )  
 )\ )    (               (      ( /(   (      ( /(  
(()/(    )\     (   (    )\     )\())  )\     )\()) 
 /(_))((((_)(   )\  )\((((_)(  ((_)\((((_)(  ((_)\  
(_))   )\ _ )\ ((_)((_))\ _ )\  _((_))\ _ )\  _((_) 
| _ \  (_)_\(_)\ \ / / (_)_\(_)| \| |(_)_\(_)| \| | 
|   /   / _ \   \ V /   / _ \  | .` | / _ \  | .` | 
|_|_\  /_/ \_\   \_/   /_/ \_\ |_|\_|/_/ \_\ |_|\_| 

    The 10-Headed Web Browser • v1.0.5 • Krishna D
    """

    # Medium banner for medium terminals (≥55 columns)
    MEDIUM_BANNER = r"""
                                           
 _____ _____ _____ _____ _____ _____ _____ 
| __  |  _  |  |  |  _  |   | |  _  |   | |
|    -|     |  |  |     | | | |     | | | |
|__|__|__|__|\___/|__|__|_|___|__|__|_|___|
                                           
      10-Headed Browser • v1.0.5 • Krishna D
    """

    # Compact banner for smaller terminals (≥42 columns)
    COMPACT_BANNER = r"""
 ____   __   _  _   __   __ _   __   __ _ 
(  _ \ / _\ / )( \ / _\ (  ( \ / _\ (  ( \
 )   //    \\ \/ //    \/    //    \/    /
(__\_)\_/\_/ \__/ \_/\_/\_)__)\_/\_/\_)__)

       10-Heads • v1.0.5 • Krishna D
    """
    
    # Minimal banner for small terminals (≥30 columns)
    MINIMAL_BANNER = r"""
 ____   __   _  _   __   __ _   __   __ _ 
(  _ \ / _\ / )( \ / _\ (  ( \ / _\ (  ( \
 )   //    \\ \/ //    \/    //    \/    /
(__\_)\_/\_/ \__/ \_/\_/\_)__)\_/\_/\_)__)

      v1.0.5 • Krishna D
    """

    # Text-only banner for very small terminals (<30 columns)
    TINY_BANNER = """
    =======================
     RAVANAN v1.0.5
     10-Headed Browser
     By Krishna D
    =======================
    """

    @classmethod
    def get_banner(cls, width: int = None) -> str:
        """
        Get the appropriate banner based on terminal width
        Plain text version without colors
        
        Args:
            width: Terminal width in columns (auto-detected if None)
            
        Returns:
            Formatted banner string
        """
        if width is None:
            try:
                width = shutil.get_terminal_size().columns
            except:
                width = 80  # Default fallback
        
        # Select banner based on width - responsive to terminal size
        if width >= 90:
            return cls.FULL_BANNER
        elif width >= 70:
            return cls.LARGE_BANNER
        elif width >= 55:
            return cls.MEDIUM_BANNER
        elif width >= 42:
            return cls.COMPACT_BANNER
        elif width >= 30:
            return cls.MINIMAL_BANNER
        else:
            return cls.TINY_BANNER
    
    @classmethod
    def get_colored_banner(cls, width: int = None):
        """
        Get a colored version of the banner using Rich
        Flames in red/orange, text in white
        
        Args:
            width: Terminal width in columns (auto-detected if None)
            
        Returns:
            Rich Text object with colored banner
        """
        if width is None:
            try:
                width = shutil.get_terminal_size().columns
            except:
                width = 80  # Default fallback
        
        # Get the appropriate plain banner
        plain_banner = cls.get_banner(width)
        
        # Create Rich Text object
        text = Text()
        
        # Split into lines
        lines = plain_banner.split('\n')
        
        for i, line in enumerate(lines):
            if not line.strip():
                text.append('\n')
                continue
                
            # Flame characters (parentheses, slashes, backslashes)
            colored_line = Text()
            for char in line:
                if char in '()\\/':
                    # Alternate between red and orange for flame effect
                    if hash(char + str(i)) % 2:
                        colored_line.append(char, style="bold red")
                    else:
                        colored_line.append(char, style="bold yellow")
                elif char in '|_-':
                    # Orange for structural elements
                    colored_line.append(char, style="bold bright_yellow")
                elif char.isalnum() or char in '.•':
                    # White for text
                    colored_line.append(char, style="bold white")
                else:
                    # Default for spaces and other characters
                    colored_line.append(char)
            
            text.append(colored_line)
            text.append('\n')
        
        return text
    
    @classmethod
    def display(cls, width: int = None, colored: bool = True):
        """
        Display the banner to the console
        
        Args:
            width: Terminal width in columns (auto-detected if None)
            colored: Whether to use colors (default True)
        """
        if colored:
            console = Console()
            console.print(cls.get_colored_banner(width))
        else:
            print(cls.get_banner(width))


def get_banner(width: int = None) -> str:
    """
    Convenience function to get the Ravanan banner
    
    Args:
        width: Terminal width in columns (auto-detected if None)
        
    Returns:
        Formatted banner string
    """
    return RavananBanner.get_banner(width)


def display_banner(width: int = None, colored: bool = True):
    """
    Convenience function to display the Ravanan banner
    
    Args:
        width: Terminal width in columns (auto-detected if None)
        colored: Whether to use colors (default True)
    """
    RavananBanner.display(width, colored)

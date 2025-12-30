"""
Text Renderer Module
Renders parsed content in the terminal with formatting

Created by: Krishna D
"""
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box
from typing import List, Dict, Tuple
from ..utils.banner import RavananBanner


class TextRenderer:
    """Renders parsed HTML content in terminal"""
    
    def __init__(self):
        self.console = Console()
        self.width = self.console.width
        self.show_banner_on_first_page = True
    
    def render_page(self, title: str, content: List[Tuple], links: List[Dict], url: str):
        """
        Render a complete page with title, content, and links
        
        Args:
            title: Page title
            content: Parsed content list
            links: List of links found on page
            url: Current URL
        """
        self.console.clear()
        
        # Show banner on first page load
        if self.show_banner_on_first_page:
            self._render_banner()
            self.show_banner_on_first_page = False
        
        # Render header
        self._render_header(title, url)
        
        # Render content
        self._render_content(content)
        
        # Render links section
        if links:
            self._render_links(links)
        
        # Render footer with controls
        self._render_footer()
    
    def _render_banner(self):
        """Render the Ravanan banner with colors"""
        colored_banner = RavananBanner.get_colored_banner(self.width)
        self.console.print(colored_banner)
        self.console.print()
    
    def _render_header(self, title: str, url: str):
        """Render page header with title and URL"""
        header_text = Text()
        header_text.append(f"📄 {title}\n", style="bold cyan")
        header_text.append(f"🔗 {url}", style="dim blue")
        
        panel = Panel(
            header_text,
            box=box.DOUBLE,
            style="cyan",
            padding=(0, 1)
        )
        self.console.print(panel)
        self.console.print()
    
    def _render_content(self, content: List[Tuple]):
        """Render main page content"""
        for item_type, text, level in content:
            if item_type == 'heading':
                # Render headings with different styles based on level
                if level == 1:
                    self.console.print(f"\n{text}", style="bold magenta", highlight=False)
                    self.console.print("=" * min(len(text), self.width - 4), style="magenta")
                elif level == 2:
                    self.console.print(f"\n{text}", style="bold yellow", highlight=False)
                    self.console.print("-" * min(len(text), self.width - 4), style="yellow")
                else:
                    self.console.print(f"\n{text}", style="bold white", highlight=False)
            
            elif item_type == 'link':
                # Render links with index
                self.console.print(f"[{level}] {text}", style="blue underline", highlight=False)
            
            elif item_type == 'paragraph':
                # Wrap and render paragraphs
                self.console.print(text, style="white", highlight=False)
            
            elif item_type == 'text':
                # Render plain text
                self.console.print(text, style="white", highlight=False)
            
            elif item_type == 'list_item':
                # Render list items
                self.console.print(text, style="white", highlight=False)
            
            elif item_type == 'blockquote':
                # Render blockquotes
                self.console.print(f"│ {text}", style="italic cyan", highlight=False)
            
            elif item_type == 'pre':
                # Render preformatted text
                self.console.print(Panel(text, box=box.SQUARE, style="green", padding=(0, 1)))
            
            elif item_type == 'newline':
                # Render newlines
                self.console.print()
    
    def _render_links(self, links: List[Dict]):
        """Render links section at the bottom"""
        self.console.print("\n")
        
        # Create a table for links
        table = Table(
            title="📎 Links on this page",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold cyan"
        )
        
        table.add_column("#", style="cyan", width=6)
        table.add_column("Link Text", style="white")
        table.add_column("URL", style="blue dim", max_width=50)
        
        # Show all links (removed 20 link limit)
        for link in links:
            table.add_row(
                f"[{link['index']}]",
                link['text'][:60] + "..." if len(link['text']) > 60 else link['text'],
                link['url'][:50] + "..." if len(link['url']) > 50 else link['url']
            )
        
        self.console.print(table)
        self.console.print()
        self.console.print(f"💡 Type 'links' to see all {len(links)} links with full URLs", style="dim italic")
    
    def _render_footer(self):
        """Render footer with available commands"""
        footer_text = Text()
        footer_text.append("🔱 Ravanan Commands: ", style="bold white")
        footer_text.append("[#]", style="cyan")
        footer_text.append(" Link | ", style="white")
        footer_text.append("[b]", style="cyan")
        footer_text.append(" Back | ", style="white")
        footer_text.append("[f]", style="cyan")
        footer_text.append(" Forward | ", style="white")
        footer_text.append("[r]", style="cyan")
        footer_text.append(" Reload | ", style="white")
        footer_text.append("[/]", style="cyan")
        footer_text.append(" Search | ", style="white")
        footer_text.append("[h]", style="cyan")
        footer_text.append(" Home | ", style="white")
        footer_text.append("[?]", style="cyan")
        footer_text.append(" Help | ", style="white")
        footer_text.append("[q]", style="cyan")
        footer_text.append(" Quit", style="white")
        
        panel = Panel(
            footer_text,
            box=box.ROUNDED,
            style="green",
            padding=(0, 1)
        )
        self.console.print(panel)
    
    def render_error(self, error_message: str):
        """Render an error message"""
        self.console.print()
        panel = Panel(
            f"❌ {error_message}",
            title="Error",
            box=box.HEAVY,
            style="bold red",
            padding=(1, 2)
        )
        self.console.print(panel)
        self.console.print()
    
    def render_loading(self, url: str):
        """Render loading message"""
        self.console.print(f"\n⏳ Loading {url}...", style="bold yellow")
    
    def render_search_results(self, query: str, results: List[str]):
        """Render search results"""
        self.console.print()
        if results:
            panel = Panel(
                f"Found {len(results)} result(s) for '{query}':\n\n" + "\n".join(f"• {r[:100]}" for r in results[:10]),
                title="Search Results",
                box=box.ROUNDED,
                style="green",
                padding=(1, 2)
            )
        else:
            panel = Panel(
                f"No results found for '{query}'",
                title="Search Results",
                box=box.ROUNDED,
                style="yellow",
                padding=(1, 2)
            )
        self.console.print(panel)
        self.console.print()

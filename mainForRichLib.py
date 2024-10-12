from rich.console import Console
from rich.panel import Panel
 
console = Console()
info = r'''
    This is a panel with [red]Rich[/red] text.
    '''*10
panel = Panel(info, title="Panel Title")
print(panel)
# console.print(panel)
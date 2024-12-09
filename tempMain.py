from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
 
console = Console()
 
def generate_report(data):
    markdown = """
    # Data Analysis Report
    ## Summary
    """
    md = Markdown(markdown)
    console.print(md)
 
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim", width=12)
    table.add_column("Value")
 
    for metric, value in data.items():
        table.add_row(metric, str(value))
 
    console.print(table)
 
if __name__ == "__main__":
    data = {"Total Sales": 1000, "Revenue": 50000, "Growth": "5%"}
    generate_report(data)
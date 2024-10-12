import argparse
from rich.console import Console
from rich.table import Table
 
console = Console()
 
def main():
    parser = argparse.ArgumentParser(description="Sample CLI Tool")
    parser.add_argument("--name", type=str, required=True, help="Your name")
    args = parser.parse_args()
 
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Parameter", style="dim", width=12)
    table.add_column("Value")
 
    table.add_row("Name", args.name)
 
    console.print(table)
 
if __name__ == "__main__":
    main()
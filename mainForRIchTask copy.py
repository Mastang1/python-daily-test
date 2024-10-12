from rich.progress import Progress
import time
import logging

def monitor_task():
    with Progress() as progress:
        task = progress.add_task("[green]Processing...", total=100)
        while not progress.finished:
            progress.update(task, advance=1)
            time.sleep(0.1)
 
if __name__ == "__main__":
    monitor_task()
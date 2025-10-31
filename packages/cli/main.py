import typer
from rich.console import Console

from core.headlines import fetch

app = typer.Typer()
console = Console()


@app.command()
def fetch_headlines(limit: int = 5):
    headlines = fetch(limit)
    console.print(f"[bold blue]Top {limit} headlines from Hacker News: [/bold blue]")
    for i, headline in enumerate(headlines, start=1):
        console.print(f"[green]{i}.[/green] {headline}")


if __name__ == "__main__":
    app()

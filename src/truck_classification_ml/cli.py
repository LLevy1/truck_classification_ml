"""Console script for truck_classification_ml."""
import truck_classification_ml

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for truck_classification_ml."""
    console.print("Replace this message by putting your code into "
               "truck_classification_ml.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()

import click
import subprocess

@click.command()
def start():
    """Run npm start command."""
    try:
        subprocess.run(["npm", "run", "start"], check=True, cwd="..")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running npm start: {e}")
        raise click.Abort()

if __name__ == "__main__":
    start()

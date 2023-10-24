import click
import subprocess

@click.command()
def openMenu():
    """Run npm start command."""
    try:
        subprocess.run(["python", "menu.py"], check=True, cwd="cli")
    except subprocess.CalledProcessError as e:
        click.echo(f"Error running python menu.py: {e}")
        raise click.Abort()

if __name__ == "__main__":
    openMenu()

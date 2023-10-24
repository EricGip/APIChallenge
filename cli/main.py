import click
from getAPI import getAPI
from postAPI import postAPI

import click

@click.command()
def main():
    """Interactive Menu using Click"""

    click.echo("Hello! Please choose an option from the menu.")

    menu_options = [
        {"option": "1", "label": "Access the GET API", "action": getAPI},
        {"option": "2", "label": "Access the POST API", "action": postAPI},
        {"option": "q", "label": "Quit", "action": quit_menu},
    ]

    while True:
        print("Menu:")
        for option in menu_options:
            print(f"{option['option']}. {option['label']}")

        choice = click.prompt("Enter your choice (q to quit):")

        selected_option = next((opt for opt in menu_options if opt["option"] == choice), None)

        if selected_option:
            selected_option["action"]()
        else:
            print("Invalid choice. Please try again.")


def quit_menu():
    print("Quitting the menu.")
    raise click.Abort()

if __name__ == "__main__":
    main()

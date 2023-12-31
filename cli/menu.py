import click
from getAPI import getAPI
from postAPI import postAPI
from connectDb import start
from deleteAPI import deleteAPI
from putAPI import putAPI


import click


@click.command()
def menu():
    """Interactive Menu using Click"""

    click.echo("Hello! Please choose an option from the menu.")

    menu_options = [
        {"option": "1", "label": "Connect to database", "action": start},
        {"option": "2", "label": "Access the GET API", "action": getAPI},
        {"option": "3", "label": "Access the POST API", "action": postAPI},
        {"option": "4", "label": "Access the PUT API", "action": putAPI},
        {"option": "5", "label": "Access the DELETE API", "action": deleteAPI},
        {"option": "q", "label": "Quit", "action": quit_menu},
    ]

    while True:
        print("Menu:")
        for option in menu_options:
            print(f"{option['option']}. {option['label']}")

        choice = click.prompt("Enter your choice (q to quit)")

        selected_option = next((opt for opt in menu_options if opt["option"] == choice), None)

        if selected_option:
            selected_option["action"]()
        else:
            print("Invalid choice. Please try again.")

def quit_menu():
    print("Quitting the menu.")
    raise click.Abort()


if __name__ == "__main__":
    menu()

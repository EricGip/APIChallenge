import click 
import requests

API_URL = "http://localhost:8080/logs/"

"""
Extra work done after 10/24

Ask user what the id is, 
ask confirmation,
    else, abort 
then send delete request
"""

@click.command()
def deleteAPI():
    id = click.prompt("Please enter the ID of the log you want to delete", type=str)

    if click.confirm(f"Are you sure you want to delete Log {id}?", abort=True):
        try: 
            response = requests.delete(API_URL + id)
            if response.status_code == 202:
                click.echo("Successfully deleted log")

            else:
                click.echo(f"Failed to delete data. {response.status_code}")
        except requests.RequestException as e:
            click.echo(f"Error: {e}")       
         

"""
Second way to do this, 

the method above works better for what we're trying to do with an interactive CLI app.


@click.command()
@click.argument("id")
def deleteAPI(id):

    click.echo(id)
    try: 
        
        response = requests.delete(API_URL + id)
        responseURL = (API_URL + id)
        click.echo(responseURL)
        if response.status_code == 202:
            click.echo("Successfully deleted log")

        else:
            click.echo(f"Failed to delete data. {response}")
    except requests.RequestException as e:
        click.echo(f"Error: {e}")
"""

if __name__ == "__main__":
    deleteAPI()
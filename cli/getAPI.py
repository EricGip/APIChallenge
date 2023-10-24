# cli_app.py
import click
import requests

API_URL = "http://localhost:8080/logs/"  

@click.command()
def getAPI():
    headers = {
        'Content-Type': 'application/json',
    }

    try:
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # Process the data as needed
            
            ##for i in range(len(data)):
            ##    click.echo(data[i])
            [click.echo(item) for item in data]
            #click.echo([x for x in data])
            ##click.echo(f"Data from API: {data}")
        else:
            click.echo(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    getAPI()

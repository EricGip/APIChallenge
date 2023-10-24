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

            ##sortTest = dict(sorted(data.date()))
            ##sortedDict = dict(sorted(data.items(), key=lambda date: date[1]))

            ##for i in range(len(data)):
            ##    click.echo(data[i])

            [click.echo(item) for item in data]
            ##click.echo(data)

            # Filter out dictionaries without the 'date' key
            data_with_date = [item for item in data if 'date' in item]

            # Sort the list of dictionaries by the 'date' field
            sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

            # Print the sorted data
            for item in sorted_data:
                click.echo(item)

        ##click.echo(data)

            ## prints a whole unreadable block
            ##click.echo(f"Data from API: {data}")
        else:
            click.echo(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    getAPI()

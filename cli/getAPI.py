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
            
            ##for i in range(len(data)):
            ##    click.echo(data[i])
            ## list comprehension to see how data looks like.
            # [click.echo(item) for item in data]

            if click.confirm("Do you want to sort by descending date?", default="False", show_default=True):
        
            # next line breaks if date is not found, so filtering out date
                data_with_date = [item for item in data if 'date' in item]

                # sort the list of dictionaries by date
                sorted_data = sorted(data_with_date, key=lambda x: x['date'])

                # Print the sorted data
                for item in sorted_data:
                    click.echo(item)

            ## if you do want to sort by descending

            # next line breaks if date is not found, so filtering out date
            data_with_date = [item for item in data if 'date' in item]

            # sort the list of dictionaries by date
            sorted_data = sorted(data_with_date, key=lambda x: x['date'], reverse=True)

            # Print the sorted data
            for item in sorted_data:
                click.echo(item)

        else:
            click.echo(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    getAPI()

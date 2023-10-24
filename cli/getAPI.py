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


            # next line breaks if date is not found, so filtering out date
            data_with_date = [item for item in data if 'date' in item]

            # sort the list of dictionaries by date, this is ascending order
            sorted_data_ascend = sorted(data_with_date, key=lambda x: x['date'])

            ## this is descending order
            sorted_data_descend = sorted(data_with_date, key=lambda x: x['date'], reverse=True)

            if click.confirm("Do you want to sort by descending date?", default="True", show_default=True):

                # Print the sorted data
                for item in sorted_data_descend:
                    click.echo(item)

            ## if you want to sort by ascending
            else: 
                # Print the sorted data
                for item in sorted_data_ascend:
                    click.echo(item)

        else:
            click.echo(f"Failed to fetch data. Status code: {response.status_code}")
    except requests.RequestException as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    getAPI()

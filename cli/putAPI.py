import click
import requests

PUT_URL = "http://localhost:8080/logs/"

"""
1. ask user for vuln id
2. ask what fields they want to change
    - could just do nested confirms of "do you want to change x, do u want to change y? etc...
        - not very extendable
    - could let them enter anything,
        - they have to know field titles.
        - click.confirm "please enter the field you want to change"
            - would you like to enter another field?
                - if yes, repeat question
                - if no, submit request? 

    - was thinking of a bunch of nested "if statements"
        - can just use a while loop 
 - ask what user wants to change
 - append into arrray? we're submitting a json
    - so we need to initialize the data,
        - but if we submit it, it will edit the data blank
            - if field is empty, remove from our dict before the request
"""


@click.command()
def putAPI():

    initializedData = {
        "name": "",
        "type": "",
        "description": ""
    }

    processedData = {}

    ## used in api
    vulnId = click.prompt("enter vuln id", type=str)


    while click.confirm("Do you want to change a field?"):
        field = click.prompt("Please enter the field you want to change: name, type, or description")
        changedData = click.prompt("Please enter the change you want")
        initializedData[field] = changedData
        
    ## if we submit data as is, it will delete the fields we dont edit. 
    for k, v in initializedData.items():
        if v != "":
           processedData[k] = v 

    if click.confirm(f"Are you sure you want to add these changes to the database?: \n {processedData} \n"):
        try:
            r = requests.put(PUT_URL + vulnId, json=processedData)

            if r.status_code == 200:
                click.echo("Successfully edited logs")
            else:
                click.echo(f"Failed to update logs. Status code: {r.status_code}")
        except requests. RequestException as e:
            click.echo(f"Error: {e}")

if __name__ == '__main__':
    putAPI()
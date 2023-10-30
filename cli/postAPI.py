import click
import requests

POST_URL = "http://localhost:8080/logs/"
## We only want one single route to handle both, fixed. 


multipleVulns = []

@click.command()
def postAPI():

    name = click.prompt("Please enter name of vulnerability", type=str)
    type = click.prompt("Please enter type of vulnerability", type=str)
    description = click.prompt("Please enter a description of the vulnerability", type=str)

    data = {
        "name": name,
        "type": type,
        "description": description
    }
    
    if click.confirm("Do you want to add more vulnerabilities?", default="False", show_default=True):
        ## if we want to add more vulns, we push the dict into an array,
        ## then ask the prompt again? 
        multipleVulns.append(data)
        postAPI()

    ## if user does not want to enter more, it should still append 
    multipleVulns.append(data)

    ## post to same route whether its a single log or not. 
    try:
        r = requests.post(POST_URL, json=multipleVulns)

        ## can add logic here of, if len(multipleVulns) >= 2, posted logs, else: posted log
        if r.status_code == 200 or 201:
            click.echo("successfully posted logs!")

        else:
            click.echo(f"Failed to post data. Status code: {r.status_code}")

    except requests.RequestException as e:
        click.echo(f"Error: {e}")

    click.echo(r.status_code)
    #click.echo(multipleVulns)



    """
    Done by 10/25:
    old logic when we had separated POST requests for multiple 

    if len(multipleVulns) >= 2:
        try: 

            r = requests.post(POST_URL, json=multipleVulns)

            if r.status_code == 200 or 201:
                click.echo("successfully posted multiple logs!")

            else:
                click.echo(f"Failed to post data. Status code: {r.status_code}")

        except requests.RequestException as e:
            click.echo(f"Error: {e}")

        click.echo(r.status_code)
        #click.echo(multipleVulns)

    ## else, if its a single object to post 
    else:
        try: 
            r = requests.post(POST_URL, json=multipleVulns)

            if r.status_code == 200 or 201:
                click.echo("successfully posted!")

            else:
                click.echo(f"Failed to post data. Status code: {r.status_code}")

        except requests.RequestException as e:
            click.echo(f"Error: {e}")

        click.echo(r.status_code)

        #click.echo(data)
    
    """


if __name__ == '__main__':
    postAPI()
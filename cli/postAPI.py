import click
import requests

POST_URL = "http://localhost:8080/logs/"
POST_MANY_URL = "http://localhost:8080/logs/many"

multipleVulns = []


@click.command()
def main():

    click.echo("hello")

    name = click.prompt("Please enter name of vulnerability", type=str)
    type = click.prompt("Please enter type of vulnerability", type=str)
    description = click.prompt("Please enter a description of the vulnerability", type=str)

    data = {
        "name": name,
        "type": type,
        "description": description
    }
    
    if click.confirm("Do you want to add more vulnerabilities?", default="False", show_default=True):
        multipleVulns.append(data)
        ## if we want to add more vulns, we push the dict into an array,
        ## then ask the prompt again? 
        click.echo(multipleVulns)

        ## so using main "works", but since we're calling main
        # and initializing the array everytime, its not adding? just replacing?

        ## think we need to separate prompt? 
        main()

    try: 
        r = requests.post(POST_URL, json=data)

        if r.status_code == 200 or 201:
            click.echo("successfully posted!")

        else:
            click.echo(f"Failed to post data. Status code: {r.status_code}")

    except requests.RequestException as e:
        click.echo(f"Error: {e}")

    click.echo(r.status_code)

    click.echo(data)


# @click.command()
# def prompt():
#     name = click.prompt("Please enter name of vulnerability", type=str)
#     type = click.prompt("Please enter type of vulnerability", type=str)
#     description = click.prompt("Please enter a description of the vulnerability", type=str)

#     data = {
#         "name": name,
#         "type": type,
#         "description": description
#     }
    
#     if click.confirm("Do you want to add more vulnerabilities?", default="False", show_default=True):
#         multipleVulns.append(data)
#         ## if we want to add more vulns, we push the dict into an array,
#         ## then ask the prompt again? 
#         click.echo(multipleVulns)

# @click.command()


if __name__ == '__main__':
    main()
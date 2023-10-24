# Technical Challenge

Backend created with TypeScript, Express, and MongoDB. 

CLI Application created with Python standard library, Requests, and Click.

Pre-requisites: Might need Python and Node installed.

[/media/Example.png]

## Installation

Clone the repo

```
```

Cd into the root directory of the repo (where Package.json is located) and install dependencies:

```
```

**IMPORTANT**  
Please fill in the fields inside `.env.example` with the credentials Paula has sent you.  
Rename `.env.example` to `.env`

In the same root directory, run the CLI application and start the connection to the database with (Option 1).  

```
python main.py 
```

## Decisions

Since we are posting data, we need a persistent store and credentials for the database. I can think of doing this 5 ways. 

1. Sending db information in an email that's hopefully encrypted.  
   - I ended up using this because it's the most practical for our test app and done in the industry.
2. Hard coding credentials in .env and leaving it in repository. 
   - This is irresponsible to do while interviewing for a security role
3. Set up database with local MongoDb instance.
   - User may be need to download would require more overhead from the user.
4. Dockerize entire app, instantiate MongoDb within the container. 
   - User might need to have Docker Desktop installed (> 1gb) and may be on a slower / limited connection. Also, docker desktop takes a ton of RAM even just processing in the background.  
5. Dockerize app, host on serverless backend cloud app (AWS lambda or GCP cloud run should be enough), then call API with the CLI tool.
   - Requires more overhead than the project itself.


Decompositioning / what my task is broken down: 

0. First thing we need is to connect to the database, have a script that does `npm run start` to initialize connection to server.
1. prompt user "what do you want to do?" get or post request
	1. if get, "sort objects descending by date and display results" -- need way to present data nicer than just objects too
		1. probably for loop, set into array / some kind of nicer text
	2. if post, should ask how many objects they want to enter 
		~~1. if one, just prompt 3 questions of: name, type, description~~ - Redundant, can just always ask if user wants to add more. 
		2. if multiple: just ask 4 questions: name, type, descrption, and add another? (Y/n)
			1. if y, repeat questions, append object to array
				1. need to make sure it appends with { } in front to tell db it's an object
			2. if n, send post request with the array as the body.



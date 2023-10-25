// External Dependencies
import express, { Request, Response } from "express";
import { ObjectId } from "mongodb";
import { collections } from "../services/database.service";
import Log from "../models/logs"


// Global Config
export const logsRouter = express.Router();
logsRouter.use(express.json());

// GET
logsRouter.get("/", async (_req: Request, res: Response) => {
    try {
        if (collections.logs) {
            const logs = (await collections.logs.find({}).toArray()) as unknown as Log[];
            res.status(200).send(logs);
            console.log("Logs pulled from db")
        }

    } catch (error) {
        console.log("Could not call db")
        res.status(500).send(error);
    }
});


logsRouter.get("/:id", async (req: Request, res: Response) => {
    const id = req?.params?.id;

    try {
        
        const query = { _id: new ObjectId(id) };
        if (collections.logs) {
            const log = (await collections.logs.findOne(query)) as unknown as Log;
            if (log) {
                res.status(200).send(log);
                console.log("Successful ")
            }
        }

    } catch (error) {
        res.status(404).send(`Unable to find matching document with id: ${req.params.id}`);
        console.log("bad here")
    }
});
// POST

// post one
logsRouter.post("/", async (req: Request, res: Response) => {
    try {
        //const newLog = req.body as Log;
        const newLog = req.body
        // manually adding date into each entry
        req.body.forEach((element: { date: Date; }) => {
            element.date = new Date();
        })

        console.log(newLog)

        console.log("Request successfully processed")
        
        if (collections.logs) {
            //const result = await collections.logs.insertOne(newLog);
            const result = await collections.logs.insertMany(newLog);

            console.log("Log inserted.")

            result
                //? res.status(201).send(`Successfully created a new log with id ${result.insertedId}`)
                ? res.status(201).send(`Successfully created a new log with id ${result.insertedIds}`)
                : res.status(500).send("Failed to create a new log.");
        }

    } catch (error) {
        console.error(error);
        res.status(400).send(error);
    }
});


// post many

logsRouter.post("/many", async (req: Request, res: Response) => {
    try {
        const newLog = req.body
        
        // manually adding date into each entry
        req.body.forEach((element: { date: Date; }) => {
            element.date = new Date();

        })

        console.log("Request processsed successfully")

        // static log is uploading properly, that means our body isnt being parsed properly
        const staticLogTest = [
            { name: "test1", type: "test1", description: "description test 1" },
            { name: "test2", type: "test2", description: "description test 2" },
            { name: "test3", type: "test3", description: "description test 3" },
        ]

        if (collections.logs) {
            //const result = await collections.logs.insertMany(staticLogTest);
            const result = await collections.logs.insertMany(newLog);
            console.log("Multiple logs uploaded into db!")

            result
                ? res.status(201).send(`Successfully created ${result.insertedCount} new logs!`)
                : res.status(500).send("Failed to create a new log.");
        }

    } catch (error) {
        console.error(error);
        res.status(400).send(error);
        console.log("failed to upload multiple logs")
    }
});

// PUT

// DELETE
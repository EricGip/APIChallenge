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
                ? res.status(201).send(`Successfully created ${result.insertedCount} new logs!`)
                : res.status(500).send("Failed to create a new log.");
        }

    } catch (error) {
        console.error(error);
        res.status(400).send(error);
    }
});

// PUT
logsRouter.put("/:id", async (req: Request, res: Response) => {
    const id = req?.params?.id;

    try {
        const updatedLog: Log = req.body as Log;
        const query = { _id: new ObjectId(id) };

        const result = await collections.logs?.updateOne(query, { $set: updatedLog });


        result
            ? res.status(200).send(`Successfully updated log with id ${id}`) && console.log("Successfully updated log")
            : res.status(304).send(`Game with id: ${id} not updated`) && console.log("Failed to update log");
    } catch (error) {
        console.error(error);
        res.status(400).send(error)
    }

})

// DELETE 
logsRouter.delete("/:id", async (req: Request, res: Response) => {
    const id = req?.params?.id;

    try {
        const query = { _id: new ObjectId(id) }; 
        const result = await collections.logs?.deleteOne(query)

        if (result  && result.deletedCount) {
            res.status(202).send(`Successfully removed log with id ${id}`);
        } else if (!result) {
            res.status(400).send(`Failed to remove log with id ${id}`);
        } else if (!result.deletedCount) {
            res.status(404).send(`Log with id ${id} does not exist`);
        }
    } catch (error) {
        console.error(error);
        res.status(400).send(error)
    }
})
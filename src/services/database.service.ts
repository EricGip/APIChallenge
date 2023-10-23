// external dependencies
import * as mongoDB from "mongodb";
import * as dotenv from "dotenv";

// global variables
export const collections: { logs?: mongoDB.Collection } = {}

// initialize connection
export async function connectToDatabase () {
    dotenv.config();
    
    if (process.env.DB_CONN_STRING) {
        const client: mongoDB.MongoClient = new mongoDB.MongoClient(process.env.DB_CONN_STRING);
        await client.connect();
            
        const db: mongoDB.Db = client.db(process.env.DB_NAME);

        // // adding schema validation 
        // await db.command({
        //     "collMod": process.env.LOGS_COLLECTION_NAME,
        //     "validator": {
        //         $jsonSchema: {
        //             bsonType: "object",
        //             required: ["date", "name", "type", "description"],
        //             additionalProperties: false,
        //             properties: {
        //             _id: {},
        //             date: {
        //                 bsonType: "date",
        //                 description: "'date' is required and is a date"
        //             },
        //             name: {
        //                 bsonType: "string",
        //                 description: "'name' is required and is a string"
        //             },
        //             type: {
        //                 bsonType: "string",
        //                 description: "'type' is required and is a string"
        //             },
        //             description: {
        //                 bsonType: "string",
        //                 description: "'description' is required and is a string"
        //             }
        //             }
        //         },
        //         validationLevel: "on"
        //      }
        // });

        db.command({
            "collMod": process.env.LOGS_COLLECTION_NAME,
            validator: {},
            validationLevel: "off"
        })

        if ( process.env.LOGS_COLLECTION_NAME ){
            const logsCollection: mongoDB.Collection = db.collection(process.env.LOGS_COLLECTION_NAME);
            collections.logs = logsCollection;
            console.log(`Successfully connected to database: ${db.databaseName} and collection: ${logsCollection.collectionName}`);
        }
    } else {
        console.log("process.env not found, unable to connect to db, check services")

    }
 }
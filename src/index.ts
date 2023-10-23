import express from "express";
import { connectToDatabase } from "./services/database.service"
import { logsRouter } from "./routes/logs.routes";
import bodyParser from "body-parser";

const app = express();
const port = 8080; 

app.use(bodyParser.json());

connectToDatabase()
    .then(() => {
        app.use("/logs", logsRouter);

        app.listen(port, () => {
            console.log(`Server started at http://localhost:${port}`);
        });
    })
    .catch((error: Error) => {
        console.error("Database connection failed", error);
        process.exit();
    });
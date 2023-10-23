import { ObjectId } from "mongodb";

export default class Log {
    constructor(
        public date: Date,
        public name: string,
        public type: string,
        public description: string,
        public id?: ObjectId,
        ) {}
}
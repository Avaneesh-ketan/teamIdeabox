OPENAI_API_KEY = "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";
import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    organization: "org-JN5R0IP70yLJiIFeRcFMKQ3u",
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
const response = await openai.listEngines();
import asyncio

import openai, requests

from PyroUbot import OPENAI_KEY


class OpenAi:
    @staticmethod
    async def ChatGPT(question):
        url = "https://chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com/gpt4"
        payload = {
	"model": "gpt-4-0613",
	"messages": [
		{
			"role": "user",
			"content": question
		}
	],
	"temperature": 0.8
}
        headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "052cc80ccbmshc1b6d8c906b8fecp18b9f5jsna896ca05cb38",
	"X-RapidAPI-Host": "chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com"
}
        response = requests.post(url, json=payload, headers=headers)
        return response.json()["choices"][0]["message"]["content"]

    @staticmethod
    async def ImageDalle(question):
        response = await asyncio.to_thread(
            openai.Image.create,
            prompt=question,
            n=1,
        )
        return response["data"][0]["url"]

    @staticmethod
    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.to_thread(
            openai.Audio.transcribe, "whisper-1", audio_file
        )
        return response["text"]

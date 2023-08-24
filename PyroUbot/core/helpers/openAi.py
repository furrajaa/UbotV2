import asyncio

import openai
import requests

from PyroUbot import OPENAI_KEY

openai.api_key = OPENAI_KEY


class OpenAi:
    async def ChatGPT(question):
        url = "https://chatgpt-api8.p.rapidapi.com/"
        payload = [{"content": question, "role": "user"}]
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "052cc80ccbmshc1b6d8c906b8fecp18b9f5jsna896ca05cb38",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com",
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()["text"]

    async def ImageDalle(question):
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: openai.Image.create(
                prompt=question,
                n=1,
                size="1024x1024",
                user="arc",
            ),
        )
        return response["data"][0]["url"]

    async def SpeechToText(file):
        audio_file = open(file, "rb")
        response = await asyncio.get_event_loop().run_in_executor(
            None, lambda: openai.Audio.transcribe("whisper-1", audio_file)
        )
        return response["text"].strip()

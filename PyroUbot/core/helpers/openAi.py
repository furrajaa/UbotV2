import asyncio
import random

import openai

from PyroUbot import OPENAI_KEY

openai.api_key = random.choice(OPENAI_KEY)


class OpenAi:
    async def ChatGPT(question):
        response = await asyncio.get_event_loop().run_in_executor(
            None,
            lambda: openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                stop=None,
                n=1,
                user="arc",
            ),
        )
        return response.choices[0].message["content"].strip()

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
        return response["text"]

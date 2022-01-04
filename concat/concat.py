import io
import json
import os

from aiogram import Bot

from pydub import AudioSegment

BOT = Bot(os.getenv("TOKEN"))


class FilesNotProvided(Exception):
    ...


async def save_files(file_sources: list[str]) -> list[str]:
    saved_files = []
    for source in file_sources:
        destination = os.path.join('/tmp', f'{source}.ogg')
        if not os.path.exists(destination):
            await BOT.download_file_by_id(source, destination)

        saved_files.append(destination)

    return saved_files


async def get_finish_file(file_ids: list[str], finish_file_name: str) -> io.BufferedRandom:
    saved_files = await save_files(file_ids)
    if len(saved_files) == 0:
        raise FilesNotProvided

    file = AudioSegment.empty()
    for voice_file in saved_files:
        file += AudioSegment.from_ogg(voice_file)

    export_file_path = os.path.join('/tmp', finish_file_name)
    exported_file = file.export(
        export_file_path,
        format="ogg",
        codec="libopus",
    )

    return exported_file


async def handler(event, context):
    body = json.loads(event['body'])
    files = body["files"]
    file_name = body["finishFilename"]

    try:
        file = await get_finish_file(files, file_name)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/ogg'
            },
            'isBase64Encoded': False,
            'body': file.read(),
        }
    except FilesNotProvided:
        return {
            'statusCode': 400,
            'body': 'Files not provided.'
        }

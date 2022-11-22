"""File mover."""

import asyncio
import os

import aiofiles


def get_all_files(src_dir: str) -> list[str]:
    """Get all filename from dir."""

    filenames = os.listdir(src_dir)
    return filenames


async def move_file(filename: str,
                    src_dir: str,
                    dest_dir: str) -> None:
    """Move file from source dir to destination dir."""

    src_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, filename)
    async with aiofiles.open(src_path, 'r') as file:
        raw_data = await file.read()
    async with aiofiles.open(dest_path, 'w') as file:
        await file.write(raw_data)
    os.remove(src_path)


async def process(src_dir: str,
                  dest_dir: str) -> None:
    """Move all files from source dir to destination dir."""

    tasks = []
    filenames = get_all_files(src_dir)
    for filename in filenames:
        task = asyncio.create_task(
            move_file(filename=filename,
                      src_dir=src_dir,
                      dest_dir=dest_dir)
        )
        tasks.append(task)
    await asyncio.gather(*tasks)

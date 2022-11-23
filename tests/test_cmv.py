import os
import tempfile

import pytest

from custom_mv.file_mover import process


@pytest.mark.asyncio
async def test_process():
    filenames = [f'file-{i}' for i in range(10)]
    file_contents = [f'content-{i}' for i in range(10)]

    with tempfile.TemporaryDirectory() as src_dir:
        with tempfile.TemporaryDirectory() as dest_dir:
            for name, content in zip(filenames, file_contents):
                filepath = os.path.join(src_dir, name)
                with open(filepath, 'w') as file:
                    file.write(content)

            await process(src_dir=src_dir,
                          dest_dir=dest_dir)
            moved_filenames = os.listdir(dest_dir)
            assert set(filenames) == set(moved_filenames)

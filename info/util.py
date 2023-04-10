import subprocess
from pathlib import Path


def compress(file: Path):
    print(f'processing: {file}')
    subprocess.call(
        f'ffmpeg -i {file} -c:v libx265 -vtag hvc1 -c:a copy {file.stem}_min{file.suffix}',
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        shell=True,
    )

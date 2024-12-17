import logging
from savify import Savify
from savify.types import Type, Format, Quality
from savify.utils import PathHolder
# Quality Options: WORST, Q32K, Q96K, Q128K, Q192K, Q256K, Q320K, BEST
# Format Options: MP3, AAC, FLAC, M4A, OPUS, VORBIS, WAV
Savify(api_credentials=None, quality=Quality.BEST, download_format=Format.MP3, path_holder=PathHolder(downloads_path='path/for/downloads'), group='%artist%/%album%', quiet=False, skip_cover_art=False, log_level=logging.INFO)
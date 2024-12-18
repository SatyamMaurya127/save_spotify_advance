import logging
from savify import Savify
from savify.types import Type, Format, Quality
from savify.utils import PathHolder
from dotenv import get_variable
from savify.logger import Logger


client_id = get_variable(".env", "SPOTIPY_CLIENT_ID")
client_secret = get_variable(".env", "SPOTIPY_CLIENT_SECRET")

# Quality Options: WORST, Q32K, Q96K, Q128K, Q192K, Q256K, Q320K, BEST
# Format Options: MP3, AAC, FLAC, M4A, OPUS, VORBIS, WAV

logger = Logger(log_location='./', log_level=None)

s = Savify(api_credentials=(client_id, client_secret), quality=Quality.BEST, download_format=Format.M4A, path_holder=PathHolder(downloads_path='./downloads/'), skip_cover_art=False, logger=logger)

try:
   s.download(query="https://open.spotify.com/track/35V6qXUDCvwZdmbKe5PlPG", query_type=Type.TRACK)
except:
   print("Something went wrong")

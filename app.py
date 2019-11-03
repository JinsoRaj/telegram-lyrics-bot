import os
import time
import telepot
from telepot.loop import MessageLoop
from pprint import pprint
from lib.lyrics import GeniusLyrics
from dotenv import load_dotenv

# TODO: should go into settings.py
load_dotenv()
# get access tokens
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GENIUS_TOKEN = os.getenv('GENIUS_TOKEN')

def handle(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    # TODO: I should log this
    print(content_type, chat_type, chat_id)
    
    # get title and artist name
    q = message['text'].split(' ', 1)
    # query Genius' API
    artist, title = q[0], q[0]
    
    song = GeniusLyrics(artist, title, GENIUS_TOKEN)

    if content_type == 'text':
        bot.sendMessage(chat_id, song.extract_lyrics())

# initialize bot
bot = telepot.Bot(TELEGRAM_TOKEN)
MessageLoop(bot, handle).run_as_thread()

# TODO: I should log this
print('Listening...')
# keep program running
while True:
    time.sleep(10)
 

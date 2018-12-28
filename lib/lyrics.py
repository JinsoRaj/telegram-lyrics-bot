import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# TODO: should go into settings.py
load_dotenv()

BASE_URL = 'https://api.genius.com'
TOKEN = os.getenv('TOKEN')


class GeniusLyrics:
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title
        
    def _get_song_details(self):
        details = None
        
        try:
            headers = {'Authorization': 'Bearer ' + TOKEN}
            data = {'q': self.title + ' ' + self.artist}
            response = requests.get('{}/search'.format(BASE_URL), data=data, headers=headers).json()
            
            for hit in response['response']['hits']:
                if self.artist.lower() in hit['result']['primary_artist']['name'].lower():
                    details = hit
                    break
        except requests.exceptions.RequestException as e:
            pass  # TODO: log the exception..
        return details
    
    def extract_lyrics(self):
        lyrics = ''  # No lyrics found
        data = self._get_song_details()
        
        if data:
            # TODO: make use of other details i.e song/album thumbnail, Genius' artist page, etc.
            url = data['result']['url']
            page = requests.get(url)
            html = BeautifulSoup(page.text, 'html.parser')
            lyrics = html.find('div', class_='lyrics').get_text()
        return lyrics





# A Very Basic Telegram Bot

Who doesn't like lyrics? :wink: Everybody does! :satisfied:.. and we all love:heart_eyes: [Telegram](https://telegram.org/), right? Decided to build a simple [Telegram](https://telegram.org/)-[Genius](https://genius.com/) mashup [bot](https://core.telegram.org/bots):feet:

#### What you need (if you wanna run the lib/lyrics.py locally)?

```
.
├── README.md
├── app.py
└── lib
    ├── __init__.py
    └── lyrics.py
```
You need to add a **.env** file at the root, and its content should be:
```ruby
TOKEN='INSERT YOUR TOKEN HERE'
```
:point_up:obtain a **CLIENT ACCESS TOKEN**  from [Genius](https://docs.genius.com/).


There's nothing crazy here, most of the stuff I did I owe to [this article](https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62) - *which does a good job at explaining how to interact with the Genius api*, the rest is a matter of googling, and reading api docs.

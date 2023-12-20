#!/usr/bin/env python3

import time
import requests
from inky.inky_uc8159 import Inky
from PIL import Image, ImageDraw, ImageFont

# define ur spotify api credentials here (as of 17th dec 2023, by cyberoil1997)
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'

# define ur inky color pallete here (cyberoil1997, 17th dec 2023)
palette = [
    (255, 0, 0),    # red
    (0, 255, 0),    # green
    (0, 0, 255),    # blue
    (255, 255, 0),  # yellow
    (255, 0, 255),  # magenta
    (0, 255, 255),  # cyan
    (255, 255, 255) # white
]

# function to fetch currently playin song from spotify api (cyberoil1997, 17th dec 2023)
def get_current_song(access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# function to create an inky image with song information (18th dec 2023, cyberoil1997)
def create_display_image(song_name, artist_name):
    # create an inky image with song info using the pallete
    width, height = inky.resolution
    image = Image.new("P", (width, height))
    image.putpalette([c for color in palette for c in color])

    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    # display song and artist
    text = f"Now Playing:\n{song_name}\nby {artist_name}"

    # position text in the center
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), text, fill=0)

    return image

try:
    # set up the inky display (cyberoil1997, 18th dec 2023)
    inky = Inky()
    inky.set_border(inky.WHITE)

    while True:
        # authenticate with spotify api (u'll need to implement this part, cyberoil1997)
        # obtain an access token and refresh it as needed
        access_token = 'YOUR_ACCESS_TOKEN'

        # fetch currently playin song
        current_song_data = get_current_song(access_token)

        if current_song_data:
            song_name = current_song_data['item']['name']
            artist_name = current_song_data['item']['artists'][0]['name']

            # create the display image
            display_image = create_display_image(song_name, artist_name)

            # show the image on the inky display
            inky.set_image(display_image)
            inky.show()

        # sleep for a while (e.g., 10 seconds)
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting...") # cyberoil1997, 19th dec 2023

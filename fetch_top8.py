import urllib.request
import json
import os

os.makedirs('top8_images', exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://commons.wikimedia.org/'
}

targets = {
    'jeff_mangum.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Neutral_Milk_Hotel_live_at_Celebrate_Brooklyn.PNG/320px-Neutral_Milk_Hotel_live_at_Celebrate_Brooklyn.PNG',
    'ian_curtis.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Pulsar_PSR_B1919%2B21_profile.svg/320px-Pulsar_PSR_B1919%2B21_profile.svg.png',
    'steve_albini.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Albini_atp.jpg/320px-Albini_atp.jpg',
    'technics_1200.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Technics_SL-1200MK2-2.jpg/320px-Technics_SL-1200MK2-2.jpg',
    'black_coffee.jpg': 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee.JPG/320px-A_small_cup_of_coffee.JPG',
    'tv_static.png': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/White_noise.svg/320px-White_noise.svg.png'
}

for filename, url in targets.items():
    dest = os.path.join('top8_images', filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            with open(dest, 'wb') as f:
                f.write(content)
        print(f"Downloaded {filename} ({len(content)} bytes)")
    except Exception as e:
        print(f"Failed {filename} from {url}: {e}")

import urllib.request
import os

os.makedirs('top8_images', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

urls = {
    'top8_albini.jpg': 'https://upload.wikimedia.org/wikipedia/commons/1/12/Albini_atp.jpg',
    'top8_turntable.jpg': 'https://upload.wikimedia.org/wikipedia/commons/5/50/Technics_SL-1200MK2-2.jpg',
    'top8_coffee.jpg': 'https://upload.wikimedia.org/wikipedia/commons/4/45/A_small_cup_of_coffee.JPG',
    'top8_jeff.png': 'https://upload.wikimedia.org/wikipedia/commons/b/b6/Neutral_Milk_Hotel_live_at_Celebrate_Brooklyn.PNG',
    'top8_ian.svg': 'https://upload.wikimedia.org/wikipedia/commons/f/f6/Pulsar_PSR_B1919%2B21_profile.svg',
    'top8_kelsi.jpg': 'https://c8.alamy.com/comp/K3KKKR/high-school-musical-3-senior-year-oleysa-rulin-as-kelsi-nielson-date-K3KKKR.jpg',
    'top8_static.svg': 'https://upload.wikimedia.org/wikipedia/commons/c/c1/White_noise.svg'
}

for name, url in urls.items():
    dest = os.path.join('top8_images', name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            with open(dest, 'wb') as f:
                f.write(content)
        print(f"SUCCESS: {name} ({len(content)} bytes)")
    except Exception as e:
        print(f"FAILED: {name} -> {e}")

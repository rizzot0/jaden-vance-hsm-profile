import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

srcs = set(re.findall(r'src=["\']([^"\']+)["\']', text))
print(f"Total unique src attributes found: {len(srcs)}")

all_ok = True
for s in sorted(srcs):
    norm = s.replace('/', os.sep)
    exists = os.path.exists(norm)
    status = "OK" if exists else "MISSING"
    if not exists:
        all_ok = False
    print(f"[{status}] {s}")

if all_ok:
    print("\nALL ASSETS EXIST LOCALLY AND ARE READY FOR GITHUB PAGES!")
else:
    print("\nWARNING: Some assets are missing!")

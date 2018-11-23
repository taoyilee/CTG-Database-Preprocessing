import requests
import os

from lxml import html

r = requests.get('https://physionet.org/physiobank/database/ctu-uhb-ctgdb/')
html = html.fromstring(r.text)
print(r.text)
dataset_files = html.xpath('//pre/a/@href')
for d in dataset_files:
    file_name, file_ext = os.path.splitext(d)
    if file_ext == ".hea":
        print(f"Downloading {d}")
        url = f"https://physionet.org/physiobank/database/ctu-uhb-ctgdb/{d}"
        r = requests.get(url)
        open(f"hea/{d}", "wb").write(r.content)
    if file_ext == ".dat":
        print(f"Downloading {d}")
        url = f"https://physionet.org/physiobank/database/ctu-uhb-ctgdb/{d}"
        r = requests.get(url)
        open(f"dat/{d}", "wb").write(r.content)

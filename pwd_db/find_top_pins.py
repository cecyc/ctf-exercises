import csv

# copy file names here
files = []

results = {}

for file in files:
  with open(file) as f:
    reader = csv.DictReader(f)
    for row in reader:
      pin = str(row['Pin'])
      if not results.get(pin):
        results[pin] = 1
      else:
        results[pin] += 1

sort_results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
print(sort_results)

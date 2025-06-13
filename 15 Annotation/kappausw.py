import csv 
from collections import defaultdict

# A list of instances to read the /t-separated value strings into
instances = []

counts = defaultdict(int)

with open('Annotation-Exercise_DE.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')

    for line in filereader:
        instances.append(line)
        counts[line[2]] += 1

print(f"Number of instances in set: {len(instances)}.")
for label in counts:
    print(f"Label {label}: {counts[label]}")

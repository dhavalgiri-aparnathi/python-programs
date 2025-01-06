import csv

data = {
    "name" : "Random",
    "age" : 12,
    "gender" : "male"
}

with open("myfile.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerow(data)

with open("myfile.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

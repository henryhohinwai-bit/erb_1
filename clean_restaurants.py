import csv

output_file = open("restaurants_clean.csv", "w", newline="")
writer = csv.writer(output_file)

writer.writerow(["name", "address"])

with open("restaurants_raw.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "name":
            continue

        clean_name = row[0].strip().title()

        writer.writerow([clean_name, row[1]])

        print(clean_name)

output_file.close()

print("restaurants_clean.csv created")
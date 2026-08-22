import csv

output_file = open("dishes_clean.csv", "w", newline="")
writer = csv.writer(output_file)

writer.writerow(["name", "price"])

with open("dishes_raw.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "name":
            continue

        clean_name = row[0].strip().title()

        writer.writerow([clean_name, row[1]])

        print(clean_name)

output_file.close()

print("dishes_clean.csv created")

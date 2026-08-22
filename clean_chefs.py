import csv

seen_emails = set()


output_file = open("chefs_clean.csv", "w", newline="")
writer = csv.writer(output_file)

writer.writerow(["name", "email"])

with open("chefs_raw.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "name":
            continue

        clean_name = row[0].strip().title()
        clean_email = row[1].strip().lower()

        if clean_email in seen_emails:
            continue

        seen_emails.add(clean_email)

        writer.writerow([clean_name, clean_email])

        print(clean_name, clean_email)

output_file.close()

print("chefs_clean.csv created")
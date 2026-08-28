import csv
import psycopg2

conn = psycopg2.connect(
    dbname="erb_1",
    user="henryho",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()



output_file = open(
    "restaurants_export.csv",
    "w",
    newline=""
)

writer = csv.writer(output_file)

writer.writerow(["name", "address"])

cursor.execute(
    """
    SELECT name, address
    FROM restaurant_1_restaurant
    """
)

rows = cursor.fetchall()

for row in rows:

    writer.writerow([
        row[0],
        row[1]
    ])

output_file.close()

conn.close()

print("restaurants_export.csv created")
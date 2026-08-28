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
    "dishes_export.csv",
    "w",
    newline=""
)

writer = csv.writer(output_file)

writer.writerow(
    ["name", "price", "chef", "restaurant"]
)

cursor.execute(
    """
    SELECT
        d.name,
        d.price,
        c.name,
        r.name
    FROM restaurant_1_dish d
    JOIN restaurant_1_chef c
        ON d.chef_id = c.id
    JOIN restaurant_1_restaurant r
        ON d.restaurant_id = r.id
    """
)

rows = cursor.fetchall()

for row in rows:

    writer.writerow([
        row[0],
        row[1],
        row[2],
        row[3]
    ])

output_file.close()
conn.close()

print("dishes_export.csv created")


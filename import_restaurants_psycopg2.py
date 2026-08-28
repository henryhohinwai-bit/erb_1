import csv
import psycopg2

conn = psycopg2.connect(
    dbname="erb_1",
    user="henryho",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

with open("restaurants_clean.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:

            cursor.execute(
                """
                INSERT INTO restaurant_1_restaurant
                (name, address)
                VALUES (%s, %s)
                """,
                (row[0], row[1])
            )
            print(row[0], row[1])

    conn.commit()
    conn.close()



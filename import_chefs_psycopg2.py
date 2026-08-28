import csv
import psycopg2

conn = psycopg2.connect(
    dbname="erb_1",
    user="henryho",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


with open("new_chefs.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute(
            """
            SELECT id
            FROM restaurant_1_chef
            WHERE name = %s
            AND email = %s
            """,
            (
                row["name"],
                row["email"]
            )
        )

        chef = cursor.fetchone()

        if chef:
            print(
                "ALREADY EXISTS:",
                row["name"]
            )

        else:

            cursor.execute(
                """
                INSERT INTO restaurant_1_chef
                (name, email)
                VALUES (%s, %s)
                """,
                (
                    row["name"],
                    row["email"]
                )
            )

            conn.commit()

            print(
                "CREATED:",
                row["name"]
            )   

print("Import completed")

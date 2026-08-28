import csv
import psycopg2

conn = psycopg2.connect(
    dbname="erb_1",
    user="henryho",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


with open("new_dishes_relationship.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute(
            """
            SELECT id
            FROM restaurant_1_chef
            WHERE name = %s
            """,
            (row["chef"],)
        )

        chef = cursor.fetchone()

        cursor.execute(
            """
            SELECT id
            FROM restaurant_1_restaurant
            WHERE name = %s
            """,
            (row["restaurant"],)
        )

        restaurant = cursor.fetchone()

        cursor.execute(
            """
            SELECT id
            FROM restaurant_1_dish
            WHERE name = %s
            AND chef_id = %s
            AND restaurant_id = %s
            """,
            (
                "Test Dish",

            )
        )

        print (cursor.fetchone())

        if dish:

            print(
                "ALREADY EXISTS:",
                row["name"]
            )

        else:

                cursor.execute(
                    """
                    INSERT INTO restaurant_1_dish
                    (
                        name,
                        price,
                        chef_id,
                        restaurant_id
                    )
                    VALUES (%s, %s, %s, %s)
                    """,
                    (
                        row["name"],
                        row["price"],
                        chef[0],
                        restaurant[0]
                    )
                )

                print(
                    "CREATED:",
                    row["name"]
                )

    conn.commit()
    conn.close()

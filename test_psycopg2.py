import psycopg2

conn = psycopg2.connect(
    dbname="erb_1",
    user="henryho",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT COUNT(*)
    FROM restaurant_1_dish
    """
)

print(cursor.fetchone()[0])

conn.close()


import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

results = cursor.fetchall()

# results = cursor.fetchone()

connection.close()

for result in results:
    print(result)
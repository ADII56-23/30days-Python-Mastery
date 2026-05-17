import mysql.connector as myconn

# Connect to MySQL
mydb = myconn.connect(
    host="localhost",
    user="root",
    password="aditya0000@",
    database="student"
)

cursor = mydb.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS details(
    id INT,
    name CHAR(40),
    marks INT
)
""")

# Insert data
query = "INSERT INTO details (id, name, marks) VALUES (%s, %s, %s)"

values = [
    (106, "Manjil", 89),
    (118, "Aditya", 98),
    (142, "Deepak", 99),
    (159, "Snehasish", 100),
    (151, "Susovit", 90)
]

cursor.executemany(query, values)

# Commit changes
mydb.commit()

print("Data inserted successfully!")

# Fetch and display
cursor.execute("SELECT * FROM details")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Marks: {row[2]}")

# Close connection
cursor.close()
mydb.close()
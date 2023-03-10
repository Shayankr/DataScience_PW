import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")
mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")
mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")
mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")
mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")
mycursor.execute("INSERT INTO test1.test_table VALUES (3424, 'shayan', 234, 234.20 )")

mydb.commit()

mydb.close()
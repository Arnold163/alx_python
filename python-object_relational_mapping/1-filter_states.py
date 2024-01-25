#lets filter the states
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("usage: {} <username> <password> <database>".format(argv[0]))
        exit(1)

    username, password, database = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY states.id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close
    db.close
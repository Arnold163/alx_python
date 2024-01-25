#sql injection lets inject this
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("usage: {}<username> <password> <database> <state_name>".format(argv[0]))
        exit(1)
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()
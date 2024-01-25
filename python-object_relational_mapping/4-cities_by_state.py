#sql injection lets inject this
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query ="""
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id =states.id
    ORDER BY cities.id;
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("usage: {} username password state_name" .format(sys.argv[0]))
        sys.exit(1)
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

#DB connection 
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        paswd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name 
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE state.name = %s
    ORDER BY cities.id;     
    """
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    cities_list = [row[0] for row in results]
    cities_str = ', ' .join(cities_list)
    print(cities_str)

    cursor.close()
    db.close()
    
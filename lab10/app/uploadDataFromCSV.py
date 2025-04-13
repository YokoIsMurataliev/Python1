import csv
from app.executeData import executeData

def uploadDataFromCSV(path="app\example.csv"):
    input_file = csv.DictReader(open(path))
    sql = """
    INSERT INTO user_numbers(user_name, number)
    VALUES(%s, %s);
    """
    for row in input_file:
        try:
            name = row['name']
            number = row['number']

            if name is None or number is None:
                raise Exception("Doesn't enough name or number in: " + str(row))

            executeData(sql, (name, number))
        except Exception as e:
            print(str(e))
    
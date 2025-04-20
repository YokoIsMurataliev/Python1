from app.generalApps.executeData import executeData

def uploadDataFromConsole():
    sql = """
    INSERT INTO user_numbers(user_name, number)
    VALUES(%s, %s);
    """
    try:
        print("Write data in form:")
        print('Name Number')
        data = input()

        if len(data.split(' ')) != 2:
            raise Exception("Data entered incorrectly")

        [name, number] = data.split(' ')
        executeData(sql, (name, number))
    except Exception as e:
        print(str(e))
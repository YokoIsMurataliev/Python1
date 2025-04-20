def changeFilter():
    try:
        print('''Choose one of the filters and write its number:
        1) All users
        2) Querying by name
        3) Querying by number
        4) Querying by id''')

        result = int(input())

        if result == 1:
            return False
        if result == 2:
            print("Write searching name:")
            name = input()
            return " where user_name='" + name + "'"
        if result == 3:
            print("Write searching number:")
            number = input()
            return " where humber='" + number + "'"
        if result == 4:
            print("Write searching id:")
            id = input()
            return " where user_id='" + id + "'"

    except Exception as e:
        print(str(e))
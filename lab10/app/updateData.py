from app.executeData import executeData

def updateData():
    try:
        sql = "update user_numbers set "
        search_data = None
        change_data = None

        #_____Ввод информации которую надо изменить_____
        print()
        print('''Choose what you want to change: 
            1) Phone 
            2) Name'''
        )
        ans2 = int(input())
        if ans2 == 1:
            sql += 'number = %s '
        elif ans2 == 2:
            sql += 'user_name = %s '
        else:
            raise Exception("Incorrect input")

        print()
        print('Write the name or number that should become:')
        change_data = input()

        #_____Ввод информации по которой будет совершен поиск_____
        print()
        print('''Choose by which attribute you want to find a user: 
            1) Phone 
            2) Name
            3) Id'''
        )
        ans1 = int(input())
        if ans1 == 1:
            sql += 'where phone = %s'
        elif ans1 == 2:
            sql += 'where user_name = %s'
        elif ans1 == 3:
            sql += 'where user_id = %s'
        else:
            raise Exception("Incorrect input")

        print()
        print('Write the information to search for:')
        search_data = input()
        if ans1 == 1 or ans1 == 3:
            search_data = int(search_data)

        executeData(sql, (change_data, search_data))
    except Exception as e:
        print(str(e))

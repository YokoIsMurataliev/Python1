from app.executeData import executeData

def deleteData():
    sql = "delete from user_numbers where user_name = "
    print('')
    print('Write the name of the user you want to delete:')
    sql += "'" + input() + "'"
    executeData(sql, None)

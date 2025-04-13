import psycopg2
from snakeApp.dbApps.config import config

def saveData(_inner_data_):
    conn = None
    id = str(_inner_data_['user_id'])
    score = _inner_data_['score']
    map = _inner_data_['map']
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select * from snake_users where user_id='" + id + "'")
        user_data = cur.fetchall()[0]
        
        for i in range(2,5):
            if i == 2:
                sql = 'update snake_users set total_score = %s where user_id = %s'
                cur.execute(sql, (str(int(user_data[2]) + score), id))
            if i == 3 and int(user_data[3]) < score:
                sql = 'update snake_users set highest_score = %s where user_id = %s'
                cur.execute(sql, (str(score), id))
            if i == 4:
                sql = 'update snake_users set current_map = %s where user_id = %s'
                cur.execute(sql, (map, id))
    
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()
import psycopg2
from snakeApp.dbApps.config import config

def executeData(name):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select * from snake_users where user_name='" + name + "'")
        user_data = cur.fetchall()

        if not user_data:
            cur.execute("""
            INSERT INTO snake_users(user_name, total_score, highest_score, current_map)
            VALUES(%s, %s, %s, %s);
            """, (name, '0', '0', 'map1.csv'))
            conn.commit()
            cur.execute("select * from snake_users where user_name='" + name + "'")
            user_data = cur.fetchall()[0]
        else:
            user_data = user_data[0]

        cur.close()
        return user_data
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()
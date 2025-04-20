import psycopg2
from app.generalApps.config import config

def executeData(sql, data, fetch=False):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        if data is None:
            cur.execute(sql)
        else:
            cur.execute(sql, data)
        if fetch:
            all_rows = cur.fetchall()
            rows = []
            for row in all_rows:  
                rows.append(row)
            return rows
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    if conn is not None:
        conn.close()
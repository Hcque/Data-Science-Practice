import sqlite3
import sys, time


class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def clear(self, table_name):
        real_sql = 'delete from ' + table_name + ';'
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
        self.conn.commit()

    def _get_sql(self, one_data):
        L = [str(i) for i in one_data.values()]
        L = L + [L[-1]]
        for i in [1, 4, 5, 6]:
            L[i] = "'" + L[i] + "'"
        L = ','.join(L)
        sql = 'insert into sign_event values (' + L + ')'
        return sql

    def insert(self, table_data):
        cursor = self.conn.cursor()
        for line in table_data:
            sql = self._get_sql(line)
            cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == '__main__':
    db = DB('db.sqlite3')

    # 定义过去时间
    past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000))
    # 定义将来时间
    future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 10000))

    table_data = [{'id':1099,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':future_time}]
    db.insert(table_data)
    db.close()

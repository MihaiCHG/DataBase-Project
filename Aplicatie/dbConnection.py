import cx_Oracle


class Connection:
    def __init__(self,name, password):
        self.conn = cx_Oracle.connect(name+'/'+password+'@127.0.0.1/xe')
        self.cursor = self.conn.cursor()


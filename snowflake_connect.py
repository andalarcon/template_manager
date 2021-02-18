import snowflake.connector

class SFdbconn:

    def __init__(self, user, password, account, warehouse, database, url):
        self.user      = user
        self.password  = password
        self.account   = account
        self.warehouse = warehouse
        self.database  = database
        self.url       = url
        
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()
    
    def __connect__(self):
        self.con = snowflake.connector.connect(
                                               user      = self.user,
                                               password  = self.password,
                                               account   = self.account,
                                               warehouse = self.warehouse,
                                               database  = self.database,
                                               url       = self.url
                                               )
        self.cur = self.con.cursor()
    
    def __disconnect__(self):
        self.con.close()
    
    def query(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result
    
    def fetch_one(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        result = self.cur.fetchone()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.__disconnect__()
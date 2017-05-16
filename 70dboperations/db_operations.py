class DB:
    import MySQLdb
    def connections(self,db_name):
        db = self.MySQLdb.connect("localhost","root","nexii",db_name)
        cursor = db.cursor()
        return cursor,db
    
    def createtable(self,cur,tb_name):
        query = "CREATE TABLE {0} (ID INT, NAME CHAR(20), AGE INT, SEX CHAR(1),DESIGNATION CHAR(20))".format(tb_name)
        cur.execute(query)

    def insertdata(self,db,cur,tb_name,l1):
        try:
            for i in range(len(l1)):
                id1=l1[i][0]
                name1=l1[i][1]
                age1 = l1[i][2]
                sex1 = l1[i][3]
                des1=l1[i][4]
                query = "INSERT INTO {0} VALUES ({1}, '{2}', {3}, '{4}', '{5}')".format(tb_name,id1,name1,age1,sex1,des1)
                print query
                cur.execute(query)
        except Exception as err:
            print err
        else:
            db.commit()
            db.close()

    def updatetable(self,db,cur,tb_name,query):
        try:
            print query
            cur.execute(query)
        except Exception as err:
            print err
        else:
            db.commit()
            db.close()
            

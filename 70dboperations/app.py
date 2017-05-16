import db_operations
db_name = "employeedb"
tb_name = "employees"
dbcls = db_operations.DB()

cur,db = dbcls.connections(db_name)
#dbcls.createtable(cur,tb_name)
l1=[[33,"Sagar",26,"M","Technical Lead"],[34,"Sandeep",30,"M","T.L."]]
#dbcls.insertdata(db,cur,tb_name,l1)

queryupdate = "UPDATE employees SET DESIGNATION = 'T.L.' WHERE DESIGNATION = 'Technical Lead'"
#queryupdate = "UPDATE employees SET DESIGNATION = 'TECHNICAL LEAD' WHERE DESIGNATION = 'T.L.'"
dbcls.updatetable(db,cur,tb_name,queryupdate)

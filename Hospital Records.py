import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",charset="utf8",password="Shalom",database="hospital")
if con.is_connected():
    print("connection established")
    cur=con.cursor()

def Prec():
    Pname=input("Enter Patient name(First name, First letter MUST be Caps)")
    piselect="Select * from patient where PName='{}'".format(Pname)
    cur.execute(piselect)
    data1=cur.fetchall()
    for row1 in data1:
        print(row1)

def Drec():
    Dname=input("Enter Doctor name(First name, First letter MUST be Caps)")
    Drselect="Select * from doctor where DName='{}'".format(Dname)
    cur.execute(Drselect)
    data=cur.fetchall()
    for row in data:
        print(row)


def Pinsert():
    Pname=input("Enter Patient name(First name, First letter MUST be Caps)")
    PhoneNo=int(input("Enter PhonerNo (8 digits):"))
    print ('Doctor table:')
    cur.execute('select * from doctor')
    data=cur.fetchall()
    for row in data:
        print (row)
    SNo=int(input("Enter doctor Sno:"))
    sql='select dname from doctor where sno={}'.format(SNo)
    cur.execute(sql)
    dataname=cur.fetchone()[0]
    sql='select dept from doctor where sno={}'.format(SNo)
    cur.execute(sql)
    datadept=cur.fetchone()[0]
    cur.execute('select * from patient')
    data=cur.fetchall()
    s=0
    for row in data:
        print (row)
        s+=1
    print(s)
    sno=s+1
    sql="insert into patient values({},'{}',{},'{}','{}')".format(sno,Pname,PhoneNo,dataname,datadept,)
    cur.execute(sql)
    con.commit()
def Drinsert():
    Dname=input("Enter Doctor name(First name, First letter MUST be Caps)")
    PhoneNo=int(input("Enter PhonerNo (8 digits):"))
    DeptName=input("Enter DeptName (First name, First letter MUST be caps)")
    SNo=int(input("Enter Sno:"))
    sql="insert into doctor values({},'{}','{}',{})".format(SNo,Dname,DeptName,PhoneNo)
    cur.execute(sql)
    con.commit()
Pinsert()





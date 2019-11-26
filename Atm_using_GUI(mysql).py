#pip install pymysql
import pymysql as ps
import sqlite3 as sq

def createTable(tname,coln1,coln2,coln3):
    query="create table if not exists {}({} int(4),{} varchar (32),{} varchar(16) )".format(tname,coln1,coln2,coln3)
    cur=con.execute(query)
    print("table is created")
    
def insertdata(tname,i,u,p):
    query="insert into {} values({},'{}','{}')".format(tname,i,u,p)
    con.execute(query)
    con.commit()
    print('data is saved')
    
def fetchdata(tname1):
    data = ''
    query = "select * from {}".format(tname1)
    cur=con.execute(query)
    r=cur.fetchall()
    for row in r:
        data = data+"\t"+str(row[0])+"\t"+row[1]+"\t"+row[2]+"\n"
    print(data)
    
def validate(tname,upin):
    data = ''
    query = "select * from Atm_sql"
    cur=con.execute(query)
    r=cur.fetchall()
    for row in r:
        if row[0]== 1234:
            print("account no = ",row[1])
            print("Available Balance = ",row[2])
            transaction(tname)
        else:
            pass
            #print('Incorrect pin')
            data = data+"\t"+str(row[0])+"\t"+row[1]+"\t"+row[2]+"\n"
    
    
def transaction(tname):
    program =(input('select catagory from : Withdraw=A, Deposite=B, Balance enquiry=C : '))
        
    if program == 'A':
        amount= int(input("enter amount to be withdraw"))
        
        withdraw(amount,tname)
    elif program == 'B':
        amount = int(input("enter amount to be deposited"))
        deposite(amount)
    elif program == 'C':
        account_no = int(input("enter account no"))
        if account_no == row[1]:
            balance_enquiry(account_no)
        else:
            print("please enter correct account")
    else:
        print("exit")
    
        
            
            
    
    
def withdraw(amt,tname):
    data = ''
    query = "select * from {}".format(tname)
    cur=con.execute(query)
    r=cur.fetchall()
    for row in r:
        if (amt>=100)and(amt<=int(row[2]))and(amt%100==0):
            print('withdrawal amount=',amt)
            Balance = int(row[2])-amt
            print('updated balance after withdraw = ',Balance)
            break
        else:
            print("please enter amount in multiples of 100/ Account balance insufficient")
    
    
    
def deposite(amt,tname):
    data = ''
    query = "select * from {}".format(tname)
    cur=con.execute(query)
    r=cur.fetchall()
    for row in r:
        #amt = int(input('enter the amount to be deposited'))
        Balance=int(row[2]) +amt
        print("deposited amount=", amt)
        print("updated balance after deposite=", Balance)
    
def balance_enquiry(amt,tname):
    data = ''
    query = "select * from {}".format(tname)
    cur=con.execute(query)
    r=cur.fetchall()
    for row in r:
        print("current balance=", row[2])
    
        
    
    
con=sq.connect("superhero.db")
if con!=None:
    print('Database is connected')
    print('enter 1 to create table')
    print('enter 2 to insertdata in table')
    print('enter 3 to show data from table')
    print('enter 4 for Atm Transaction')
    choice = int(input('enter choice'))
    if choice == 1:
        tablename= input('enter table name')
        col1=input('enter column name 1')
        col2=input('enter column name 2')
        col3=input('enter column name 3')
        createTable(tablename,col1,col2,col3)
    if choice == 2:
        tname=input('enter table name')
        epin = int(input('Enter pin'))
        eacc = input('enter account no')
        ebal = input('enter balance')
        insertdata(tname,epin,eacc,ebal)
    if choice==3:
        tname1=input("enter table name = ")
        fetchdata(tname1)
    if choice==4:
        tname1=input('enter table name = ')
        upin=input('please enter account pin = ')
        validate(tname1,upin)   
     
    
        
        
        
else:
    print('Database is not connected')

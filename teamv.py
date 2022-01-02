import random 
import pandas as pd 
import pymysql 
from sqlalchemy import create_engine
import mysql.connector as sqltor
rgno=[]
name=[]
perc=[]
role=[]
play=[]
typ=[]
dict1={}
team=[]
def Home(): 
    print("\t\t\t\t\t\t WELCOME TO TEAM VIEWER \n\n") 
    print("\t\t\t\t\t\t A program to create and \n\t\t\t\t\t\t view players team for\n\t\t\t\t\t\t getting better predictions. \n\n") 
    print("\t\t\t enter  -  1  -  to  -  entry\n") 
    print("\t\t\t enter  -  2  -  to  -  show\n") 
    print("\t\t\t enter  -  3  -  to  -  delete\n")
    print("\t\t\t enter  -  4  -  to  -  update\n")
    ch=int(input("->")) 
    if ch == 1: 
        print(" ") 
        entry()   
    elif ch == 2: 
        print(" ") 
        show()
    elif ch == 3: 
        print(" ") 
        delete()
    elif ch == 4: 
        print(" ") 
        update()
    else: 
        exit() 
def regno():
    a=random.randint(0,999)
    print("given reg no:",a)
    while a in rgno:
        a=random.randint(0,999)
    else:
        rgno.append(a)

        
def entry(): 
        # used global keyword to  
        # use global variable 'i' 
        global i 
        print(" PLAYER ENTRY ") 
        print(" ") 
        while 1: 
            n = str(input("Name: ")) 
            r1 = str(input("role: ")) 
            p1= str(input("play: "))
            p2=int(input("percentage:"))
            t=input("type:")
            t2=input("team:")
            # checks if any field is not empty 
            if n!="" and p1!="" and t!="" and r1!="" and p2>=0: 
                name.append(n) 
                role.append(r1)
                perc.append(p2)
                play.append(p1)
                regno()
                #rgno.append(j)
                typ.append(t)
                team.append(t2)
                dict1={"rgno":rgno,"name":name,"role":role,"type":typ,"team":team,"play":play,"perc":perc}
                a=pd.DataFrame(dict1)
                #codes for saving information in database
                engine=create_engine("mysql+pymysql://root:root123@localhost/mysql")
                conn=engine.connect()
                a.to_sql("booking",conn,index=False,if_exists="append")
                rgno.clear()
                name.clear()
                perc.clear()
                role.clear()
                play.clear()
                typ.clear()
                dict1.clear()
                team.clear()
                break
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!") 
        n=int(input("0-BACK\n ->"))         
        if n==0: 
            Home() 
        else: 
            exit()
def show():
    n=int(input("0-filtered data\n1-show all\n ->"))
    if n==0:
        mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="mysql")
#        cursor=mycon2.cursor()
        qry="select * from booking;"
        custin=pd.read_sql(qry,mycon2) 
        low=int(input("enter lower value:"))
        up=int(input("enter upper value:"))
        ro=input("enter the role(press enter if not needed):")
        pl=input("enter the play(press enter if not needed):")
        if (((ro in list(custin["role"])) or ro=="") and 
            ((pl in list(custin["play"])) or pl=="") and
            ((low<up) and (0<=(low and up)<=100)) ):
            if ro=='' and pl=='':
                qry="select * from booking where perc>="+str(low)+" and perc<="+str(up)+";"
                custin=pd.read_sql(qry,mycon2) 
                print(custin)
            elif pl=='' and ro!='':
                qry="select * from booking where perc>="+str(low)+" and perc<="+str(up)+" and role='"+ro+"';"
                custin=pd.read_sql(qry,mycon2) 
                print(custin)
            elif pl!='' and ro=='':
                qry="select * from booking where perc>="+str(low)+" and perc<="+str(up)+" and play='"+pl+"';"
                custin=pd.read_sql(qry,mycon2) 
                print(custin)
            else:
                qry="select * from booking where perc>="+str(low)+" and perc<="+str(up)+" and play='"+pl+"' and role='"+ro+"';"
                custin=pd.read_sql(qry,mycon2) 
                print(custin)
        else:
            print("invalid value of role or play or low or up")
            
        n=int(input("0-BACK\n ->"))         
        if n==0: 
            Home() 
        else: 
            exit()
    elif n==1:
        mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="mysql")
        qry="select * from booking;"
        custin=pd.read_sql(qry,mycon2)
        print(custin)
        n=int(input("0-BACK\n ->"))         
        if n==0: 
            Home() 
        else: 
            exit()
        
def delete():
    n=int(input("0-delete a player\n1-delete all privious data\n ->"))
    if n==0:
        mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="mysql")
        cursor=mycon2.cursor()
        qry="select * from booking;"
        custin=pd.read_sql(qry,mycon2) 
        tes=input("enter the reg num of the player whose data to be updated:")
        if int(tes) in list(custin["rgno"]):
            qry="delete from booking where rgno="+tes+";"
            cursor.execute(qry)
            mycon2.commit()
            #print(custin)
            print("deleted")
        else:
            print("reg num not registered")            
        n=int(input("0-BACK\n ->"))         
        if n==0: 
            Home() 
        else: 
            exit()
    elif n==1:
        mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="mysql")
        qry="delete from booking where perc>0;"
        cursor=mycon2.cursor()
        cursor.execute(qry)
        mycon2.commit()
        n=int(input("0-BACK\n ->"))
        print("deleted")
        if n==0: 
           Home() 
        else: 
           exit()
def update():
    mycon2=sqltor.connect(host="localhost",user="root",passwd='root123',database="mysql")
    cursor=mycon2.cursor()
    qry="select * from booking;"
    custin=pd.read_sql(qry,mycon2) 
    tes=input("enter the reg num of the player whose data to be updated:")
    if int(tes) in list(custin["rgno"]):
        qry="select * from booking where rgno='"+tes+"';"
        custin=pd.read_sql(qry,mycon2) 
        print(custin)
        k=input("what to update:")
        h=input("updated value:")
        qry="update booking set "+k+"='"+h+"' where rgno='"+tes+"';"
        cursor.execute(qry)
        mycon2.commit()
        print("updated")
    else:
        print("reg num not registered")
    
    n=int(input("0-BACK\n ->"))         
    if n==0: 
        Home() 
    else: 
        exit()
            
Home()

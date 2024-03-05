
#PYTHON MODULE: MEMBER
import mysql.connector
from mysql.connector import errorcode

from datetime import date

def clrscreen():
    print('\n' * 5)

def insertMember():
    try:
        cnx = mysql.connector.connect(user='root', password='Jalgaon123', host='localhost', database='library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code : ")
        mname = input("Enter Member Name : ")
        print("Enter Date of Membership (Date/Month and Year) separately: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member Address : ")
        mob = int(input("Enter Member Mobile No. : "))
        Qry = ("INSERT INTO Member VALUES(%s, %s, %s, %s, %s)")
        data = (mno, mname, date(YY, MM, DD), addr, mob)
        Cursor.execute(Qry, data)
        cnx.commit()
        print("Record Inserted.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if 'cnx' in locals():
            cnx.close()

def deleteMember():
    try:
        cnx = mysql.connector.connect(user='root', password='Jalgaon@123', host='localhost', database='library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code to be deleted from the Library : ")
        Qry = ("DELETE FROM Member WHERE MNO = %s")
        del_rec = (mno,)
        Cursor.execute(Qry, del_rec)
        cnx.commit()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if 'cnx' in locals():
            cnx.close()

def SearchMember():
    try:
        cnx = mysql.connector.connect(user='root', password='Jalgaon@123', host='localhost', database='library')
        Cursor = cnx.cursor()
        mnm = input("Enter Member No to be Searched from the Library : ")
        rec_srch = (mnm,)
        Cursor.execute("SELECT * FROM Member where mno = %s", rec_srch)
        Rec_count = 0
        for(mno, mname, Date_of_Membership, addr, mob) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Member Code : ", mno)
            print("Member Name : ", mname)
            print("Date of Membership : ", Date_of_Membership)
            print("Address : ", addr)
            print("Mobile No. of Member : ", mob)
            print("=============================================================")
            if Rec_count % 2 == 0:
                input("Press any key to continue: ")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def updateMember():
    try:
        cnx = mysql.connector.connect(user='root', password='Jalgaon@123', host='localhost', database='library')
        Cursor = cnx.cursor()
        mno = input("Enter Member Code of Member to be Updated from the Library : ")
        print("Enter new data")
        mname = input("Enter Member Name : ")
        print("Enter Date of Membership (Date/Month and Year separately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        addr = input("Enter Member address : ")
        mob = input("Enter Member's mobile no : ")
        Date_of_Membership = date(YY, MM, DD)
        Qry = ("UPDATE Member SET mname=%s, Date_of_Membership=%s, addr=%s, mob=%s WHERE mno=%s")
        data = (mname, Date_of_Membership, addr, mob, mno)
        Cursor.execute(Qry, data)
        cnx.commit()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        try:
            cnx.close()
        except NameError:
            pass  # Handle the case where cnx is not defined



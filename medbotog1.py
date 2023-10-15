#MedBot Working Code

#to read video
import cv2

#to read and decode barcode
from pyzbar.pyzbar import decode

#to connect mysql database to python
import mysql.connector as sql

#to display data in tabular format
from prettytable import PrettyTable

#importing date
from datetime import date
today=date.today()


print("1 : Adding to cart\n2 : Expired Stock\n3 : Display Stock")
inp5=int(input("Enter option : "))


#connecting sql and python
mycon=sql.connect(host="localhost",user="root",passwd="Super@30",database="Medic")
cursor=mycon.cursor()
k=1
r=1
if inp5==1:                                                                                         #buying medicines
         
    #capturing video
    cap=cv2.VideoCapture(0)
    cap.set(3,640)                                                                                  #3 is length of video window and 640 is pixels
    cap.set(4,480)                                                                                  #4 is width of video window and 480 is pixels

    camera = True
    current=1
    while True:
        
        while camera == True:                                                                                   #to scan the barcode 
            success, frame = cap.read()
                                    
            for code in decode(frame):                                                                          #to decode the barcode
                x=code.data.decode('utf-8')
                current=current+1
            if current==2:                                                                                      #taking one input
                break

        
            cv2.imshow('Testing-code-scan', frame)                                                              #to open camera window
            cv2.waitKey(1)
        if int(x)<=13:

            cursor.execute("select * from medicine where sno=%s",(x,))                                          #executing the command in mysql database
            data=cursor.fetchone()                                                                              #fetching the output from cursor
            table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Pos X','Pos Y','Pos Z','Units'])       #creating table format
            a,b,c,d,e,f,g,h,i=data                                                                              #unpacking data tuple
            l=[a,b,c,d,e,f,g,h,i]
            table.add_row(l)
            print(table)                                                                                        #printing data in table
            if str(today)>str(c):
                print("Medicine is expired")                                                                    #checking if the buying medicine is expired
    
            else:                                                                                               #if the medicine is not expired
            
                
                if i!=0:
                    inp33=input("Strip(s) or Individual unit(i)")
                                            
            
                    if inp33=='s' or inp33=='S':                                                                #input for selecting strip or individual medicine
                        inp1=int(input("Enter required Quantity: "))
                        if inp1<e and inp1>0:                                                                   #checking the quantity                            
                            inp2=e-inp1                 
                            cursor.execute("UPDATE medicine SET Quantity={} where sno={}".format(inp2,x))       #updating the quantity in database 
        
                            mycon.commit()


                            if k==1:                     
                                table2=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units','Total cost'])
                                k=2
                            l=[a,b,c,d,inp1,inp1*10,inp1*d]
                            table2.add_row(l)
                        
                        else:
                            print("Invalid Quantity")

                    elif inp33=='I' or inp33=='i':
                        inp1=int(input("Enter required Quantity: "))
                        ze=int(inp1/10)
                        if inp1<i and inp1>0:                                                                   #checking the quantity                            
                            inp2=e-(ze+1)
                            cursor.execute("UPDATE medicine SET Quantity={} where sno={}".format(inp2,x))       #updating the quantity in database 
                            
        
                            cursor.execute("UPDATE medicine SET Units={} where sno={}".format(i-inp1,x))
                            mycon.commit()

                            if k==1:                     
                                table2=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units','Total cost'])
                                k=2
                            l=[a,b,c,d,inp1/10,inp1,d/10*inp1]
                            table2.add_row(l)
                    else:
                        print("Invalid Input")
                        break
                else:                                                                                           #out of stock
                    print("It is out of stock")
        else:
             print("The medicine is not in the database")
        inp10=input("Do you want to scan more medicines (y/n)")
        current=1
        if inp10=='n' or inp10=='N':
            #printing checkout slip
            print("Checkout slip:")
            print(table2)
            break;


elif inp5==2:                                                                                                   #to check expired medicines
    cursor.execute("select * from medicine where exp_date<curdate()")
    table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units'])
    data=cursor.fetchall()
    for row in data:
        a,b,c,d,e,f,g,h,i=row
        l=[a,b,c,d,e,i]
        table.add_row(l)
    print(table)

elif inp5==3:
    #printing stock
    print("Existing stock")
    cursor.execute("select * from medicine")
    data=cursor.fetchall()
    table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Pos X','Pos Y','Pos Z','Units'])
    for row in data:
        a,b,c,d,e,f,g,h,i=row
        l=[a,b,c,d,e,f,g,h,i]
        table.add_row(l)
    print(table)

else:
    print("Invalid Input")

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

from pyfirmata import Arduino,SERVO,util
from time import sleep

port='COM6'
pin = 5 #To be set
pin1 = 6
pin2 = 9
pin3 = 11
board=Arduino(port)

board.digital[pin].mode=SERVO
board.digital[pin1].mode=SERVO
board.digital[pin2].mode=SERVO
board.digital[pin3].mode=SERVO

def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.001)
def rotateservo1(pin1,angle):
    board.digital[pin1].write(angle)
    sleep(0.001)
def rotateservo2(pin2,angle):
    board.digital[pin2].write(angle)
    sleep(0.001)    
def rotateservo3(pin3,angle):
    board.digital[pin3].write(angle)
    sleep(0.001)

def box1():

    #box lopataki poindi
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    for i1 in range(0,75,1):
        rotateservo1(pin,i1)
    for i1 in range(0,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)

    sleep(2)

    #pattindi
    
    for i1 in range(24,-1,-1):
        rotateservo(pin3,i1)

    
    sleep(1)

    #75 meda initial pos
    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)

    #tray lo pettindi
    for i1 in range(75,110,1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(4)

    #malla pattindi
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
    #malla box1 lo pettindi

    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)
    for i1 in range(110,74,-1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo1(pin2,i1)
    
    sleep(2)
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(1)

    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,-1,-1):
        rotateservo2(pin1,i1)
    for i1 in range(75,-1,-1):
        rotateservo(pin,i1)
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
        





def box2():

    #box lopataki poindi
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    for i1 in range(0,35,1):
        rotateservo1(pin,i1)
    for i1 in range(0,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)

    sleep(2)

    #pattindi
    
    for i1 in range(24,-1,-1):
        rotateservo(pin3,i1)

    
    sleep(1)

    #75 meda initial pos
    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)

    #tray lo pettindi
    for i1 in range(35,110,1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(4)

    #malla pattindi
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
    #malla box1 lo pettindi

    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)
    for i1 in range(110,34,-1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo1(pin2,i1)
    
    sleep(2)
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(1)

    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,-1,-1):
        rotateservo2(pin1,i1)
    for i1 in range(35,-1,-1):
        rotateservo(pin,i1)
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
        


def box3():

    #box lopataki poindi
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    '''for i1 in range(0,75,1):
        rotateservo1(pin,i1)'''
    for i1 in range(0,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)

    sleep(2)

    #pattindi
    
    for i1 in range(24,-1,-1):
        rotateservo(pin3,i1)

    
    sleep(1)

    #75 meda initial pos
    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)

    #tray lo pettindi
    for i1 in range(0,110,1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo3(pin2,i1)
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(4)

    #malla pattindi
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
    #malla box1 lo pettindi

    
    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,40,-1):
        rotateservo2(pin1,i1)
    for i1 in range(110,-1,-1):
        rotateservo3(pin,i1)
    for i1 in range(40,60,1):
        rotateservo2(pin1,i1)
    for i1 in range(0,60,1):
        rotateservo1(pin2,i1)
    
    sleep(2)
    
    for i1 in range(0,25,1):
        rotateservo(pin3,i1)
    sleep(1)

    for i1 in range(60,-1,-1):
        rotateservo1(pin2,i1)
    for i1 in range(60,-1,-1):
        rotateservo2(pin1,i1)
    '''for i1 in range(75,-1,-1):
        rotateservo(pin,i1)'''
    for i1 in range(25,-1,-1):
        rotateservo(pin3,i1)
        







print("1 : Adding to cart\n2 : Expired Stock\n3 : Display Stock")
inp5=int(input("Enter option : "))


#connecting sql and python
mycon=sql.connect(host="localhost",user="root",passwd="Super@30",database="Medbot")
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
        
        while camera == True:                                                                           #to scan the barcode 
            success, frame = cap.read()
                                    
            for code in decode(frame):                                                                  #to decode the barcode
                x=code.data.decode('utf-8')
                current=current+1
            if current==2:                                                                                    #taking one input
                break

        
            cv2.imshow('Testing-code-scan', frame)                                                      #to open camera window
            cv2.waitKey(1)
        if int(x)<=5:

            cursor.execute("select * from medicine where sno=%s",(x,))                                  #executing the command in mysql database
            data=cursor.fetchone()                                                                      #fetching the output from cursor
            table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Shelf','Units'])       #creating table format
            a,b,c,d,e,f,g=data                                                                        #unpacking data tuple
            l=[a,b,c,d,e,f,g]
            table.add_row(l)
            print(table)                                                                                #printing data in table
            if str(today)>str(c):
                print("Medicine is expired")                                                            #checking if the buying medicine is expired
    
            else:                                                                                       #if the medicine is not expired
            
                
                if g!=0:
                    inp33=input("Strip(s) or Individual unit(i)")
                                            
            
                    if inp33=='s' or inp33=='S':
                        inp1=int(input("Enter required Quantity: "))
                        if inp1<e and inp1>0:                                                                   #checking the quantity                            
                            inp2=e-inp1                 
                            cursor.execute("UPDATE medicine SET Quantity={} where sno={}".format(inp2,x))       #updating the quantity in database 
        
                            mycon.commit()


                            if k==1:                     
                                table2=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units','Total cost'])
                                k=2
                            l=[a,b,c,d,e,e*10,inp1*d]
                            table2.add_row(l)


#Arduino
                            if int(x)==1:
                                box1()
                                
                            if int(x)==2:
                                box2()
                                
                            if int(x)==3:
                                box3()

                        
                        
                        else:
                            print("Invalid Quantity")

                    elif inp33=='I' or inp33=='i':
                        inp1=int(input("Enter required Quantity: "))
                        ze=int(inp1/10)
                        if inp1<g and inp1>0:                                                                   #checking the quantity                            
                            inp2=e-(ze+1)
                            cursor.execute("UPDATE medicine SET Quantity={} where sno={}".format(inp2,x))       #updating the quantity in database 
                            
        
                            cursor.execute("UPDATE medicine SET Units={} where sno={}".format(g-inp1,x))
                            mycon.commit()

                            if k==1:                     
                                table2=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units','Total cost'])
                                k=2
                            l=[a,b,c,d,inp1/10,inp1,d/10*inp1]
                            table2.add_row(l)


                            

                            
                    
                            
                    else:
                        print("Invalid Input")
                        break
                else:                                                                                       #out of stock
                    print("It is out of stock")
        else:
             print("The medicine is not in the database")
        inp10=input("Do you want to scan more medicines (y/n)")
        current=1
        if inp10=='n' or inp10=='N':
            #printing checkout slip
            print("Checkout slip:")
            print(table2)
            break


elif inp5==2:                                                                                       #to check expired medicines
    cursor.execute("select * from medicine where exp_date<curdate()")
    table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Units'])
    data=cursor.fetchall()
    for row in data:
        a,b,c,d,e,f,g=row
        l=[a,b,c,d,e,g]
        table.add_row(l)
    print(table)

elif inp5==3:
    #printing stock
    print("Existing stock")
    cursor.execute("select * from medicine")
    data=cursor.fetchall()
    table=PrettyTable(['Sno','Name','Expiry','Price','Quantity','Shelf','Units'])
    for row in data:
        a,b,c,d,e,f,g=row
        l=[a,b,c,d,e,f,g]
        table.add_row(l)
    print(table)

else:
    print("Invalid Input")

    

import mysql.connector
# import datetime
from datetime import datetime, date, time
from datetime import timedelta
from math import sin, cos, sqrt, atan2, radians


# now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now = datetime.now()
# now.replace(microsecond=0, second=0, minute=0, hour=0)

str1 = "10:00:00"
str2 = "07:00:00"

mydb = mysql.connector.connect(
    host="db4free.net",
    user= "vertash",
    password="todoproject",
    database="car_system"
)
mycursor = mydb.cursor()
def query1():
    mycursor.execute("SELECT * FROM Car WHERE Color = 'red' AND CID LIKE 'AN%'")
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)
#query1();
# for i in mycursor:

def query2():
    sql =  "SELECT * FROM Charge WHERE Date = %s"
    mycursor.execute(sql, ("21-11-2018",))
    myresult = mycursor.fetchall()
    ans = [0] * 24
    for i in range (24):
        if (i < 10):
            start = "0" + str(i) + ":00:00"
            if (i != 9):
                finish = "0" + str(i + 1) + ":00:00"
            else:
                finish = str(i + 1) + ":00:00"
        else:
            start = str(i) + ":00:00"
            finish = str(i + 1) + ":00:00"
        # print(start)
        # print(finish)
        res = 0
        for j in myresult:
            if (j[3] <= finish and j[4] >= start):
                res += 1
        print(str(i) + "h-" + str(i + 1) + "h: " + str(res))

# query2()

def query3():
    sql = "SELECT * FROM Rent ""WHERE (Start_date = %s OR Finish_date = %s) AND Finish_time >= %s AND Start_time <= %s "
    morning = set()
    afternoon = set()
    evening = set()
    for i in range(7):
        N_days_ago = now - timedelta(days=i)
        N_days_ago = N_days_ago.strftime("%d-%m-%Y")
        mycursor.execute(sql,(N_days_ago,N_days_ago,'07:00:00', '10:00:00'))
        result1 = mycursor.fetchall()
        for i in result1:
            morning.add(i[1])
        mycursor.execute(sql, (N_days_ago, N_days_ago, '12:00:00', '14:00:00'))
        result2 = mycursor.fetchall()
        for i in result2:
            afternoon.add(i[1])
        mycursor.execute(sql, (N_days_ago, N_days_ago, '17:00:00','19:00:00'))
        result3 = mycursor.fetchall()
        for i in result3:
            evening.add(i[1])

    mycursor.execute("SELECT * FROM Car")
    all = len(mycursor.fetchall())
    print("Morning: " + str((int)((len(morning)/all)*100)))
    print("Afternoon: " + str((int)((len(afternoon)/all)*100)))
    print("Evening: " + str((int)((len(evening)/all)*100)))
# query3()

def query4():
    q4 = "SELECT * FROM Rent WHERE Username = %s AND Start_date <= %s"
    N_days_ago = now - timedelta(days = 31)
    N_days_ago = N_days_ago.strftime("%d-%m-%Y")
    mycursor.execute(q4, ("Danis", N_days_ago))
    result = mycursor.fetchall()
    for i in result:
        start_date = i[2] + " " + i[3]
        finish_date = i[4] + " " + i[5]
        date = datetime.strptime(start_date, '%d-%m-%Y %H:%M:%S')
        date2 = datetime.strptime(finish_date,'%d-%m-%Y %H:%M:%S')
        date3 = date2 - date
        date3 = str(date3)
        if (date3[1]!=':'):
            date3 = (int)(date3[0])*10 + (int)(date3[1])
        else:
            date3 = (int)(date3[0])
        for j in i:
            print(j, end=" ")
        print("Total price: " + str(date3*i[6]))
# query4()

def query5():

    input = "2018-11-10"
    inp_date = datetime.strptime(input, '%Y-%m-%d')
    init = 1

    duration = 0
    counter = 0
    distance = 0.0
    day_count = 0
    while (inp_date < now):
        sql = "SELECT * FROM Rent WHERE Start_date = %s"
        inp_date = inp_date + timedelta(days = init)
        inp_date1 = inp_date.strftime("%d-%m-%Y")
        mycursor.execute(sql, (inp_date1, ))
        result = mycursor.fetchall()
        for myresult in result:
            start_date = myresult[2] + " " + myresult[3]
            finish_date = myresult[4] + " " + myresult[5]
            date = datetime.strptime(start_date, '%d-%m-%Y %H:%M:%S')
            date2 = datetime.strptime(finish_date, '%d-%m-%Y %H:%M:%S')
            date3 = str(date2 - date)
            if (date3[1]!=':'):
                date3 = ((int)(date3[0])*10 + (int)(date3[1]))*3600 + (int)(date3[3:4]) * 60 + (int)(date3[6:7])
            else:
                date3 = (int)(date3[0])*3600 + (int)(date3[2:3]) * 60 + (int)(date3[5:6])
            duration += date3
            counter += 1

        sql = "SELECT * FROM Manage WHERE Order_date = %s"
        # find distance between GPS_start and GPS_car
        mycursor.execute(sql, (inp_date1, ))
        result = mycursor.fetchall()

        for orders in result:
            # approximate radius of earth in km
            R = 6373.0

            lat1 = radians(orders[1])
            lon1 = radians(orders[2])
            lat2 = radians(orders[5])
            lon2 = radians(orders[6])

            dlon = lon2 - lon1
            dlat = lat2 - lat1

            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance += R * c
            print(R*c)
        day_count += 1

    print((float)(duration)/(float)(counter))
    print (distance/day_count)

query5()







# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE TABLE students(name VARCHAR(30), age INTEGER(10))")
# mycursor.execute("SHOW TABLES")
# for tb in mycursor:
#     print(tb)
# print(mydb)
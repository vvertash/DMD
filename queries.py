import mysql.connector
# import datetime
from datetime import datetime, date, time
from datetime import timedelta
from math import sin, cos, sqrt, atan2, radians
import operator
import math

now = datetime.now()


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

def query2(input):
    input = "21-11-2018"
    sql =  "SELECT * FROM Charge WHERE Date = %s"
    mycursor.execute(sql, (input,))
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
    for n in range(31):
        q4 = "SELECT * FROM Rent WHERE Username = %s AND Start_date = %s"
        N_days_ago = now - timedelta(days = n)
        N_days_ago = N_days_ago.strftime("%d-%m-%Y")
        mycursor.execute(q4, ("Danis", N_days_ago))
        result = mycursor.fetchall()
        n += 1
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

def query5(input):

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
# query5()

def query6():
    mycursor.execute("SELECT * FROM CC_Order WHERE Order_time BETWEEN '07:00:00' AND '10:00:00'")

    myresult = mycursor.fetchall()

    morning_pick_up = {}
    morning_dest = {}

    for result in myresult:
        if (result[1], result[2]) in morning_pick_up:
            morning_pick_up[(result[1], result[2])] += 1
        else:
            morning_pick_up[(result[1], result[2])] = 1

        if (result[3], result[4]) in morning_dest:
            morning_dest[(result[3], result[4])] += 1
        else:
            morning_dest[(result[3], result[4])] = 1

    mycursor.execute("SELECT * FROM CC_Order WHERE Order_time BETWEEN '12:00:00' AND '14:00:00'")

    myresult = mycursor.fetchall()

    afternoon_pick_up = {}
    afternoon_dest = {}

    for result in myresult:
        if (result[1], result[2]) in afternoon_pick_up:
            afternoon_pick_up[(result[1], result[2])] += 1
        else:
            afternoon_pick_up[(result[1], result[2])] = 1

        if (result[3], result[4]) in afternoon_dest:
            afternoon_dest[(result[3], result[4])] += 1
        else:
            afternoon_dest[(result[3], result[4])] = 1

    mycursor.execute("SELECT * FROM CC_Order WHERE Order_time BETWEEN '17:00:00' AND '19:00:00'")

    myresult = mycursor.fetchall()

    evening_pick_up = {}
    evening_dest = {}

    for result in myresult:
        if (result[1], result[2]) in evening_pick_up:
            evening_pick_up[(result[1], result[2])] += 1
        else:
            evening_pick_up[(result[1], result[2])] = 1

        if (result[3], result[4]) in evening_dest:
            evening_dest[(result[3], result[4])] += 1
        else:
            evening_dest[(result[3], result[4])] = 1
    morning1 = sorted(morning_pick_up.items(), key=operator.itemgetter(1))
    morning2 = sorted(morning_dest.items(), key=operator.itemgetter(1))
    afternoon1 = sorted(afternoon_pick_up.items(), key=operator.itemgetter(1))
    afternoon2 = sorted(afternoon_dest.items(), key=operator.itemgetter(1))
    evening1 = sorted(evening_pick_up.items(), key=operator.itemgetter(1))
    evening2 = sorted(evening_dest.items(),key=operator.itemgetter(1))

    print(morning1[len(morning_pick_up) - 1][0])
    print(morning2[len(morning_dest) - 1][0])

    print(afternoon1[len(afternoon_pick_up) - 1][0])
    print(afternoon2[len(afternoon_dest) - 1][0])

    print(evening1[len(evening_pick_up) - 1][0])
    print(evening2[len(evening_dest) - 1][0])
# query6()


def query7():
    mycursor.execute("SELECT * FROM Car")
    cars = {}
    allcars = mycursor.fetchall()
    for i in allcars:
        cars[i[0]] = 0

    for n in range(93):
        last3 = "SELECT * FROM Rent WHERE Start_date = %s"
        N_days_ago = now - timedelta(days=n)
        N_days_ago = N_days_ago.strftime("%d-%m-%Y")
        mycursor.execute(last3, (N_days_ago, ))
        result = mycursor.fetchall()
        for j in result:
            cars[j[1]] += 1
    sorted_cars = sorted(cars.items(), key=operator.itemgetter(1))
    to_trash = math.ceil((float)(len(allcars))/10)
    print("All cars with orders: " + str(dict(sorted_cars)))
    print("Cars to remove: " + str(dict(sorted_cars[0:to_trash])))
# query7()

def query8(input_date):
    input_date = "21-10-2018"
    input_date = datetime.strptime(input_date, '%d-%m-%Y')
    users = {}
    us = {}
    usr_set = set()
    # cars
    for i in range(31):
        month_later = input_date + timedelta(days=i)
        month_later = month_later.strftime("%d-%m-%Y")
        sql = "SELECT * FROM Rent WHERE Start_date = %s"
        mycursor.execute(sql,(month_later, ))
        result = mycursor.fetchall()
        for n in result:
            usr_set.add(n[0])
        for j in usr_set:
            users[j] = list()

        for n in result:
            if n[0] in us:
                us[n[0]].append((n[1], n[2]))
            else:
                us[n[0]] = list()
                us[n[0]].append((n[1], n[2]))
    ans = {}
    for name in us:
        trips = us[name]

        for trip in trips:
            sql = "SELECT * FROM Charge WHERE CID = %s AND Date = %s"
            mycursor.execute(sql, (trip[0], trip[1], ))

            cnt = 0
            myresult = mycursor.fetchall()
            for ii in myresult:
                cnt += 1

            if name in ans:
                ans[name] += cnt
            else:
                ans[name] = cnt
    print(ans)
query8()


def earlier(s1, s2):
    if s1[6:10] < s2[6:10]:
        return True
    if s1[6:10] > s2[6:10]:
        return False

    if s1[3:5] < s2[3:5]:
        return True
    if s1[3:5] > s2[3:5]:
        return False

    if s1[0:2] < s2[0:2]:
        return True
    else:
        return False

def query9():
    ans = {}
    first_date = ""
    mycursor.execute("SELECT WID FROM Workshop")
    myresult = mycursor.fetchall()

    for wid1 in myresult:
        wid = wid1[0]

        sql = "SELECT * FROM PW_Order WHERE WID = %s"
        mycursor.execute(sql,(wid, ))
        result = mycursor.fetchall()

        details = {}
        for res in result:

            if res[3] in details:
                details[res[3]] += 1
            else:
                details[res[3]] = 1

            if len(first_date) == 0:
                first_date = res[0]
            else:
                if earlier(res[0], first_date):
                    first_date = res[0]

        d = len(details)
        if (d != 0):
            ans[wid] = sorted(details.items(), key=operator.itemgetter(1))[d - 1]

    first_date = datetime.strptime(first_date, '%d-%m-%Y')
    days = now - first_date
    days = int(str(days).split(" ")[0])
    weeks = math.ceil(days / 7.0)

    for item in ans:
        i = ans[item]
        num = math.ceil((float)(i[1]) / (float)(weeks))
        print("Workshop № " + str(item) + " most often requires " + i[0] + " (about " + str(num) + " every week on average).")
# query9()

def query10():
    mycursor.execute("SELECT * FROM Repair")
    result = mycursor.fetchall()
    car_type = {}
    min_date = "01-01-2100"
    min_date = datetime.strptime(min_date, '%d-%m-%Y')
    for i in result:
        car_type[i[3]] = 0
    for i in result:
        cur_date = i[5]
        cur_date = datetime.strptime(cur_date, '%d-%m-%Y')
        min_date = min(min_date, cur_date)
        car_type[i[3]] += i[4]
    new_date = now - min_date
    new_date = str(new_date)
    new_date = new_date.split(" ")
    sorted_models = sorted(car_type.items(), key=operator.itemgetter(1))
    sorted_models = sorted_models[len(car_type) - 1]
    print("The most expensive model: " + sorted_models[0])
    print("Average(per day) cost of repairs: " + str(sorted_models[1] / (int)(new_date[0])))
# query10()


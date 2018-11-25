import mysql.connector
# import datetime
from datetime import datetime, date, time
from datetime import timedelta
from math import sin, cos, sqrt, atan2, radians
import operator
import math


mydb = mysql.connector.connect(
    host="db4free.net",
    user= "vertash",
    password="todoproject",
    database="car_system"
)
mycursor = mydb.cursor()

tables = list()

tables.append("CREATE TABLE `Car11` (" \
 "`CID` varchar(10) NOT NULL," \
 "`Model` varchar(30) NOT NULL," \
 "`GPS_Location` double NOT NULL," \
 "`Price` int(7) NOT NULL," \
 "`Current_charge` int(10) NOT NULL," \
 "`Color` varchar(10) NOT NULL," \
 "PRIMARY KEY (`CID`))")

tables.append("CREATE TABLE `CC_Order1` ("\
 "`Username` varchar(30) NOT NULL," \
 "`GPS_start_la` double NOT NULL," \
 "`GPS_start_lo` double NOT NULL," \
 "`GPS_finish_la` double NOT NULL," \
 "`GPS_finish_lo` double NOT NULL," \
 "`Order_date` varchar(10) NOT NULL," \
 "`Order_time` varchar(8) NOT NULL)")
 
tables.append("CREATE TABLE `Charging_station1` (" \
 "`UID` varchar(10) NOT NULL," \
 "`Time_of_charging` int(10) NOT NULL," \
 "`GPS_la` double NOT NULL," \
 "`GPS_lo` double NOT NULL," \
 "`Sockets` int(10) NOT NULL," \
 "`Price` int(10) NOT NULL," \
 "PRIMARY KEY (`UID`)) ")
 
tables.append("CREATE TABLE `Customer1` (
 "`Username` varchar(30) NOT NULL," \
 "`Full_Name` varchar(30) NOT NULL," \
 "`Email` varchar(30) NOT NULL," \
 "`Phone_Number` int(15) NOT NULL," \
 "PRIMARY KEY (`Username`)")
 
tables.append("CREATE TABLE `Location1` (
 "`Country` varchar(30) NOT NULL," \
 "`City` varchar(30) NOT NULL," \
 "`Zip_code` int(10) NOT NULL)")
 
tables.append("CREATE TABLE `Manage1` (" \
 "`CID` varchar(6) NOT NULL," \
 "`GPS_start_la` double NOT NULL," \
 "`GPS_start_lo` double NOT NULL," \
 "`GPS_finish_la` double NOT NULL," \
 "`GPS_finish_lo` double NOT NULL," \
 "`GPS_car_la` double NOT NULL," \
 "`GPS_car_lo` double NOT NULL," \
 "`Order_date` varchar(10) NOT NULL)")

tables.append("CREATE TABLE `Plug1` (" \
 "`Shape` varchar(30) NOT NULL," \
 "`Size` int(10) NOT NULL," \
 "PRIMARY KEY (`Shape`))")

tables.append("CREATE TABLE `Provider1` (" \
 "`PID` varchar(10) NOT NULL," \
 "`Name` varchar(30) NOT NULL," \
 "`Address` varchar(30) NOT NULL," \
 "`Types_of_car_part` varchar(30) NOT NULL," \
 "PRIMARY KEY (`PID`))")

tables.append("CREATE TABLE `PW_Order1` (" \
 "`Date` varchar(10) NOT NULL," \
 "`PID` int(11) NOT NULL," \
 "`WID` int(11) NOT NULL," \
 "`Car_part` varchar(30) NOT NULL)")
 
tables.append("CREATE TABLE `Rent1` (" \
 "`Username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL," \
 "`CID` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL," \
 "`Start_date` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL," \
 "`Start_time` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL," \
 "`Finish_date` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL," \
 "`Finish_time` varchar(8) NOT NULL," \
 "`Price_per_min` int(11) NOT NULL)")

tables.append("CREATE TABLE `Repair1` (" \
 "`CID` varchar(6) NOT NULL," \
 "`WID` varchar(10) NOT NULL," \
 "`Car_part` varchar(30) NOT NULL," \
 "`Car_model` varchar(30) NOT NULL," \
 "`Part_price` int(11) NOT NULL," \
 "`Date` varchar(10) NOT NULL) ")
 
tables.append("CREATE TABLE `Workshop1` (" \
 "`WID` varchar(10) NOT NULL," \
 "`Availability_of_timing` tinyint(1) NOT NULL," \
 "`Zip_code` int(10) NOT NULL," \
 "`Car_parts_available` varchar(30) NOT NULL," \
 "PRIMARY KEY (`WID`))")

for table in tables:
	mycursor.execute(table)

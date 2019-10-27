import mysql.connector
import geopy.distance
from mysql.connector import Error
from math import sin, cos, sqrt, atan2, radians
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='gpsdb',
                                         user='root',
                                         password='password')

    mySql_select_Query = "SELECT * FROM ambulance"
    cursor = connection.cursor(buffered=True)
    cursor.execute(mySql_select_Query)
    #record = cursor.fetchone()
    #print(record)
    #record = cursor.fetchone()
    #print(record)
    i=0
    def check_distance(c1,c2):
        if(geopy.distance.geodesic(c1,c2).km<0.2):
            return True            
    record=cursor.fetchone()
    while(record):
        print(record)
        if(i==2):
            f=open('a.txt','a+')
            f.write('1 50')
            f.close()
        if(check_distance((record[1],record[2]),(12.9383848,77.5334486))):
            f=open('a.txt','a+')
            f.write(str(record[0]))
            f.close()
        i+=1;
        record=cursor.fetchone()
    print(i)



    #R = 6373.0
    #c1 = (record[1],record[2])
    #c2 = (12.9383848,77.5334486)
    #print(c2)
    #print(geopy.distance.geodesic(c1,c2).km)
except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

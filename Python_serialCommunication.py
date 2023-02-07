import serial
import time
from gc import collect
import csv
import pandas as pd
import json
import lab3

serialport = serial.Serial()
serialport.baudrate = 115200
serialport.port = 'COM6'
serialport.timeout = 1
serialport.close()
serialport.open()

while True:
    try:
        serialport_port = serialport.readline()
        decoded_data = serialport_port.decode('utf8').split('\; | \n | \r')
        print(time.asctime(),decoded_data)
        with open("data.csv","a") as filehandler:
            collect = csv.writer(filehandler,delimiter=",")
            collect.writerow([time.asctime(),decoded_data])

    except:
        print("sensor interruption")
        break

# Adding Header to CSV
file = pd.read_csv("data.csv")
headerList = ['Time', 'Temperature']
file.to_csv("data.csv", header=headerList, index=False)

# Convert to JSON
with open("data.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append({"Time":row[0], "Temperature":row[1]})

with open("data.json","w") as f:
    json.dump(data,f,indent=4)

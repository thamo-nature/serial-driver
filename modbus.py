#!/usr/bin/env python3
import json
import time
import requests
from pymodbus.client import ModbusSerialClient as ModbusClient

# ---------------- Config ----------------
PORT = "COM4"               # change if needed

#list = [6,19]                  # your current debug list

#19 cable problem
#6

list = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38]

#list = [6,  19, 36, 37]

# 19, 36, 37

#1,2,3,& 31 stae born
 
chart_data = []
empty_data_one = []

client = ModbusClient(
    port=PORT,
    baudrate=9600,
    timeout=2,
    parity='N',
    stopbits=1,
    bytesize=8
)

if not client.connect():
    print(f"Failed to connect to {PORT}")
    exit(1)

print(f"Connected to {PORT}")

for i in list:
    try:
        # device_id is the correct parameter name in recent pymodbus
        response = client.read_holding_registers(address=0, count=37, device_id=i)

        if not response.isError():
            data = response.registers
            data_array = {
                "vessel": i,
                "tempa": str(data[2]),
                "tempb": str(data[3]),
                "level": str(data[5]),
                "usage": data[4]
            }

            insert = "."
            for key, value in data_array.items():
                if key == "tempa":
                    afirst = value[:2]
                    asecond = value[2:]
                    atemp = float(afirst + insert + asecond)
                    data_array["tempa"] = atemp - 273.15
                if key == "tempb":
                    bfirst = value[:2]
                    bsecond = value[2:]
                    btemp = float(bfirst + insert + bsecond)
                    data_array["tempb"] = btemp - 273.15
                if key == "level":
                    lfirst = value[:3]
                    lsecond = value[3:]
                    llevel = float(lfirst + insert + lsecond)
                    data_array["level"] = llevel / 25.4
                if key == "usage":
                    data_array["usage"] = int(value)

            chart_data.append(data_array)
            print(f"Unit {i} OK → {data_array}")
        else:
            print(f"Unit {i} Modbus error: {response}")
            empty_data_one.append(i)

    except Exception as e:
        print(f"Unit {i} exception: {e}")
        empty_data_one.append(i)

    time.sleep(0.25)

client.close()

print("\nSuccessful data:")
print(chart_data)
print("\nNot pinging:")
print(empty_data_one)

# # API post
# URL = "http://192.168.20.129/lifecell/api/charts_api.php"
# final_data = {'charts': json.dumps(chart_data)}
# r = requests.post(url=URL, data=final_data, timeout=5)
# print("API status code:", r.status_code)

#!/usr/bin/env python3
"""
Modbus RTU Telemetry Ingestion Script
------------------------------------
Queries series of Modbus slave devices over a serial port connection, 
parses sensor register data, and posts aggregated telemetry payloads 
to an external REST API endpoint.
"""

import json
import time
import requests
from pymodbus.client import ModbusSerialClient as ModbusClient

# ================================
# CONFIGURATION & PARAMETERS
# ================================
# Serial Port Configuration
SERIAL_PORT = "COM_PORT_OR_TTY_PATH"  # e.g., "COM4" on Windows, "/dev/ttyUSB0" on Linux
BAUDRATE = 9600                      # Serial communication baud rate
TIMEOUT = 2                          # Read timeout in seconds
PARITY = 'N'                         # Parity setting ('N', 'E', or 'O')
STOPBITS = 1                         # Stop bits (1 or 2)
BYTESIZE = 8                         # Data byte size

# Retry & Polling Configuration
MAX_RETRIES = 5                      # Connection attempts per slave device
RETRY_DELAY = 1.0                    # Wait time (seconds) between retry attempts

# API Endpoint Configuration
API_URL = "http://<YOUR_SERVER_IP_OR_HOST>/api/endpoint.php"
API_TIMEOUT = 5                      # Request timeout in seconds

# List of Modbus Slave Unit IDs to poll
TARGET_SLAVE_IDS = [
    1,2,3,4
]
TARGET_SLAVE_IDS.sort()


# ================================
# MAIN TELEMETRY EXECUTION
# ================================
def main():
    chart_data = []
    failed_devices = []
    successful_devices = []

    print(f"Target Slave IDs ({len(TARGET_SLAVE_IDS)} total): {TARGET_SLAVE_IDS}")

    # Initialize Modbus Serial Client
    client = ModbusClient(
        port=SERIAL_PORT,
        baudrate=BAUDRATE,
        timeout=TIMEOUT,
        parity=PARITY,
        stopbits=STOPBITS,
        bytesize=BYTESIZE
    )

    if not client.connect():
        print(f"Critical Error: Could not open port {SERIAL_PORT}")
        return

    print(f"Successfully opened serial port {SERIAL_PORT}\n" + "-" * 40)

    # Process each Modbus slave device
    for device_id in TARGET_SLAVE_IDS:
        device_success = False

        for attempt in range(1, MAX_RETRIES + 1):
            print(f"Querying Device {device_id} (Attempt {attempt}/{MAX_RETRIES})...")
            try:
                # Read 37 Holding Registers starting at Register Address 0
                response = client.read_holding_registers(
                    address=0, 
                    count=37, 
                    device_id=device_id
                )

                if response and not response.isError():
                    raw_regs = response.registers

                    # Parse raw register values
                    str_temp_a = str(raw_regs[2])
                    str_temp_b = str(raw_regs[3])
                    str_level = str(raw_regs[5])

                    # Transformations & Calibrations
                    temp_a_val = float(f"{str_temp_a[:2]}.{str_temp_a[2:]}") - 273.15
                    temp_b_val = float(f"{str_temp_b[:2]}.{str_temp_b[2:]}") - 273.15
                    level_val = float(f"{str_level[:3]}.{str_level[3:]}") / 25.4
                    usage_val = int(raw_regs[4])

                    # Build telemetry dictionary record
                    record = {
                        "device_id": device_id,
                        "temp_a": temp_a_val,
                        "temp_b": temp_b_val,
                        "level": level_val,
                        "usage": usage_val
                    }

                    chart_data.append(record)
                    successful_devices.append(str(device_id))
                    device_success = True
                    print(f" Successfully read Device {device_id}: {record}\n")
                    break
                else:
                    print(f" Modbus Error on Device {device_id}: {response}")

            except Exception as err:
                print(f" Exception on Device {device_id}: {err}")

            time.sleep(RETRY_DELAY)

        if not device_success:
            print(f" Failed to connect to Device {device_id} after {MAX_RETRIES} attempts.\n")
            failed_devices.append(device_id)

    # Close serial port connection
    client.close()

    # ================================
    # TELEMETRY SUMMARY & POSTING
    # ================================
    total_devices = len(TARGET_SLAVE_IDS)
    success_count = len(successful_devices)
    failed_count = len(failed_devices)

    print("=" * 40)
    print("Summary Of Connection Details")
    print(f" * Total Devices        = {total_devices}")
    print(f" * Successful Uplinks   = {success_count} -> {successful_devices}")
    print(f" * Failed Downlinks     = {failed_count} -> {failed_devices}")
    print("=" * 40)

    # Payload formatting for external HTTP POST request
    payload = {
        "charts": json.dumps(chart_data),
        "total_vessel_count": total_devices,
        "total_connected_charts": success_count,
        "not_connected_charts": json.dumps(failed_devices),
    }

    print(f"\nPosting telemetry data to API: {API_URL}")
    try:
        response = requests.post(url=API_URL, data=payload, timeout=API_TIMEOUT)
        print(f"API Response Code : {response.status_code}")
        print(f"API Response Text : {response.text}")
    except requests.exceptions.RequestException as api_err:
        print(f"API Request Failed : {api_err}")


if __name__ == "__main__":
    main()

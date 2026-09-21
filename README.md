Modbus to RS232 - serial driver for usb

# Modbus RTU Telemetry Ingestion Script

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python utility designed to query a series of Modbus RTU slave devices over a serial port connection, parse raw register values with built-in calibration logic, and post aggregated telemetry payloads to an external REST API endpoint.

---

## Features

* **Robust Polling**: Automatically iterates through a targeted list of Modbus Slave Unit IDs with configurable retry limits and delays.
* **Data Calibration**: Parses raw holding registers, applies custom string slicing and floating-point conversions (e.g., Kelvin to Celsius conversion, level calculation in inches).
* **REST API Forwarding**: Packages successful device reads into structured JSON payloads and submits them via HTTP POST.
* **Detailed Execution Summary**: Tracks successful uplinks and failed downlinks for transparent diagnostics.

---

## Prerequisites & Dependencies

Make sure you have Python 3.8+ installed. You will need the `pymodbus` and `requests` libraries.

```bash
pip install pymodbus requests
```

## Configuration

Open the script and update the configuration variables at the top of the file to match your hardware setup:

| Parameter | Description | Default / Example |
| --- | --- | --- |
| `SERIAL_PORT` | Serial port path | `"COM4"` (Windows) or `"/dev/ttyUSB0"` (Linux) |
| `BAUDRATE` | Communication speed | `9600` |
| `MAX_RETRIES` | Connection attempts per slave | `5` |
| `API_URL` | Destination REST endpoint | `"http://<YOUR_SERVER_IP>/api/endpoint.php"` |
| `TARGET_SLAVE_IDS` | List of slave IDs to poll | `[1, 2, 3, 4]` |

---

## Register Map & Parsing Logic

The script reads **37 Holding Registers** starting from address `0` and extracts specific indices:

* **Registers 2 & 3 (`temp_a`, `temp_b`)**: Scaled integers converted to Celsius by splitting string components and subtracting absolute zero ($273.15$ K).
* **Register 4 (`usage`)**: Raw integer usage metric.
* **Register 5 (`level`)**: Fluid or material level calibrated and converted into inches.

---

## Usage

Run the script directly from your terminal:

```bash
python telemetry_script.py

```

### Example Console Output

```text
Target Slave IDs (4 total): [1, 2, 3, 4]
Successfully opened serial port /dev/ttyUSB0
----------------------------------------
Querying Device 1 (Attempt 1/5)...
 Successfully read Device 1: {'device_id': 1, 'temp_a': 24.5, 'temp_b': 25.1, 'level': 12.4, 'usage': 105}

========================================
Summary Of Connection Details
 * Total Devices        = 4
 * Successful Uplinks   = 1 -> ['1']
 * Failed Downlinks     = 3 -> [2, 3, 4]
========================================

Posting telemetry data to API: [http://192.168.1.50/api/endpoint.php](http://192.168.1.50/api/endpoint.php)
API Response Code : 200
API Response Text : Success

```

---

## API Payload Structure

The script sends an HTTP `POST` request with the following form-data structure:

```json
{
  "charts": "[{\"device_id\": 1, \"temp_a\": 24.5, \"temp_b\": 25.1, \"level\": 12.4, \"usage\": 105}]",
  "total_vessel_count": 4,
  "total_connected_charts": 1,
  "not_connected_charts": "[2, 3, 4]"
}

```

---

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE&utm_source=gemini).

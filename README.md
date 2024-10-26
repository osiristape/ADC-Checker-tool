<p align="center">
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/README.md">English</a>  |   
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/manual_de_lectura.md">Español</a>  |  
    <a href="https://github.com/osiristape/ADC-Checker-tool/blob/main/自述文.md">Mandarin</a>
</p>

---

# ADC Checker Tool

This ADC Checker tool monitors Application Delivery Controller (ADC) endpoints, ensuring they are reachable, performing latency checks, validating SSL/TLS certificates, and checking the health of load-balanced services. It alerts the user via email if any issues are detected.

## Features

1. **Availability Monitoring**: Checks if the ADC endpoint is accessible.
2. **Latency Check**: Measures response time.
3. **Health Endpoint Check**: Ensures load-balanced services are responsive.
4. **SSL/TLS Validation**: Verifies SSL certificate status.
5. **Alerting**: Sends alerts if any issues are detected.




## Prerequisites

- Python 3.8 or higher
- Pip for package management
- A working internet connection

## Installation

### Step 1: Clone the Repository
- In your terminal or command prompt, navigate to the desired directory and run:

```bash
git clone https://github.com/osiristape/ADC-Checker-tool.git
cd ADC-Checker-tool
```

### Step 2: Install Dependencies
- Install required Python packages with:

```bash
pip install -r requirements.txt
```

## Configuration
Edit **config.py** to add your ADC endpoints and configure alert settings:

- **ADC_ENDPOINTS**: List of ADC endpoints to monitor.
- **ALERT_THRESHOLD**: Threshold for latency in milliseconds.
- **ALERT_EMAIL**: Email address where alerts will be sent.
- **SMTP_SERVER**: SMTP server for email alerts.
- **SMTP_PORT**: SMTP server port.
- **SMTP_USER** and **SMTP_PASSWORD**: SMTP server login credentials.


Example **config.py**:
```python
ADC_ENDPOINTS = [
    'https://example-adc1.com',
    'https://example-adc2.com'
]

ALERT_THRESHOLD = {
    'latency': 300
}

ALERT_EMAIL = "alert@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USER = "user@example.com"
SMTP_PASSWORD = "password"
```




## Usage
### Run the ADC Checker
1. Open a terminal or command prompt in the ADC-Checker-tool directory.
2. Run the following command:
   
   **On Windows:**
   ```powershell
   python adc_checker.py
   ```
   **On Linux:**
   ```bash
   python3 adc_checker.py
   ```

    The tool will:
    - Perform checks on each endpoint.
    - Log results in **logs/adc_checker.log.**
    - Send an email alert if any checks fail.

---

### Scheduling (Optional)
- To automate the checks, you can schedule the script to run periodically:

**Windows**
1. Open Task Scheduler.
2. Create a new task.
3. Set the "Program/script" to
   ```powershell
   python
   ```
4. Set the "Add arguments" field to:
   ```powershell
   adc_checker.py
   ```
5. Set the "Start in" field to the directory where **adc_checker.py** is located.

**Linux**
- To run the script at a regular interval (e.g., every hour), you can use cron:
1. Open the cron table:
```bash
   crontab -e
```
2. Add an entry to run the script every hour:
```bash
   0 * * * * /usr/bin/python3/path/to/ADC-Checker-tool/adc_checker.py
```
---


## Logging
- Logs are saved in **logs/adc_checker.log**. Review this file for detailed information about each check and any errors.



## Troubleshooting
- **Email Alerts Not Sending**: Ensure **SMTP** settings are correct in **config.py**.
- **SSL/TLS Certificate Errors**: Ensure the endpoints use **HTTPS**.
- **Missing Dependencies**: Run *pip install -r requirements.txt* to reinstall dependencies.



## License
- This project is licensed under the MIT License.

```yaml

This README covers installation, setup, configuration, usage, scheduling, and troubleshooting for both Windows and Linux environments. Let me know if you'd like additional customization!

```


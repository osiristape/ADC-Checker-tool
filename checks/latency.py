import requests
import time
from config import ALERT_THRESHOLD

def check_latency(endpoint):
    try:
        start_time = time.time()
        response = requests.get(endpoint, timeout=5)
        latency = (time.time() - start_time) * 1000  # convert to ms
        return {"status": latency < ALERT_THRESHOLD['latency'], "details": latency}
    except requests.RequestException as e:
        return {"status": False, "details": str(e)}

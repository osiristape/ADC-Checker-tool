import logging
from checks import availability, latency, health_check, ssl_check
from config import ADC_ENDPOINTS, ALERT_THRESHOLD
from utils.alert import send_alert

logging.basicConfig(filename='logs/adc_checker.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_checks():
    for endpoint in ADC_ENDPOINTS:
        results = {
            "availability": availability.check_availability(endpoint),
            "latency": latency.check_latency(endpoint),
            "health": health_check.check_health(endpoint),
            "ssl": ssl_check.check_ssl(endpoint),
        }
        
        logging.info(f"Results for {endpoint}: {results}")
        
        if any(not result['status'] for result in results.values()):
            send_alert(endpoint, results)

if __name__ == '__main__':
    run_checks()

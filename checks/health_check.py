import requests

def check_health(endpoint):
    health_endpoint = f"{endpoint}/health"
    try:
        response = requests.get(health_endpoint, timeout=5)
        return {"status": response.status_code == 200, "details": response.json()}
    except requests.RequestException as e:
        return {"status": False, "details": str(e)}

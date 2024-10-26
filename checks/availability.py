import requests

def check_availability(endpoint):
    try:
        response = requests.get(endpoint, timeout=5)
        return {"status": response.status_code == 200, "details": response.status_code}
    except requests.RequestException as e:
        return {"status": False, "details": str(e)}

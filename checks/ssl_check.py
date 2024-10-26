import ssl
import socket
from datetime import datetime

def check_ssl(endpoint):
    hostname = endpoint.replace("https://", "").replace("http://", "")
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                expire_date = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
                days_to_expire = (expire_date - datetime.now()).days
                return {"status": days_to_expire > 0, "details": days_to_expire}
    except Exception as e:
        return {"status": False, "details": str(e)}

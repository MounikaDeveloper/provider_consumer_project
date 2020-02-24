
import requests
def read_data():
    try:
        res = requests.get("http;//192.168.43.169:8000/readone")
        print(res.status_code)
        print(res.json())
    except:
        print("server not available")
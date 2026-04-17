import requests

def get_device_data(device_id):
    url = f"https://jsonplaceholder.typicode.com/users/{device_id}"
    try:
        response = requests.get(url)
        response.raise_for_status() 
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error al consumir la API: {e}")
        return None


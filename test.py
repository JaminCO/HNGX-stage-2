import requests
import random

names = ["John", "Jane Doe", "John Doe Junior"]


# Define the base URL of your API
base_url = "https://bookish.pythonanywhere.com"

# Function to perform GET request (Read)
def get_books(id):
    response = requests.get(f"{base_url}/api/{id}")
    print("GET Request:")
    print(response.status_code)
    print(response.json())

# Function to perform POST request (Create)
def create_book(name):
    data = {"name": name}
    response = requests.post(f"{base_url}/api", json=data)
    print("POST Request:")
    print(response.status_code)
    print(response.json())
    return response.json()["id"]

# Function to perform PUT request (Update)
def update_book(user_id, name):
    url = f"{base_url}/api/{user_id}"
    data = {"name": name}
    response = requests.put(url, json=data)
    print("PUT Request:")
    print(response.status_code)
    print(response.json())

# Function to perform DELETE request (Delete)
def delete_book(user_id):
    url = f"{base_url}/api/{user_id}"
    response = requests.delete(url)
    print("DELETE Request:")
    print(response.status_code)
    print(response.json())

# Test your API
if __name__ == "__main__":
    for name in names:
        # Test POST request
        id = create_book(name)
        # Test GET request
        get_books(id)

        # Test PUT request
        update_book(id, name)

        # Test DELETE request
        delete_book(id)
        print("\n---------------------------------------\n")
    print("\nALL TEST DONE")
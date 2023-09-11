import requests

# Define the base URL of your API
base_url = "https://api.example.com/books"

# Function to perform GET request (Read)
def get_books():
    response = requests.get(base_url)
    print("GET Request:")
    print(response.status_code)
    print(response.json())

# Function to perform POST request (Create)
def create_book(title, author):
    data = {"title": title, "author": author}
    response = requests.post(base_url, json=data)
    print("POST Request:")
    print(response.status_code)
    print(response.json())

# Function to perform PUT request (Update)
def update_book(book_id, new_title, new_author):
    url = f"{base_url}/{book_id}"
    data = {"title": new_title, "author": new_author}
    response = requests.put(url, json=data)
    print("PUT Request:")
    print(response.status_code)
    print(response.json())

# Function to perform DELETE request (Delete)
def delete_book(book_id):
    url = f"{base_url}/{book_id}"
    response = requests.delete(url)
    print("DELETE Request:")
    print(response.status_code)
    print(response.json())

# Test your API
if __name__ == "__main__":
    # Test GET request
    get_books()

    # Test POST request
    create_book("Sample Book 1", "John Doe")

    # Test PUT request
    update_book(1, "Updated Book Title", "Jane Smith")

    # Test DELETE request
    delete_book(1)

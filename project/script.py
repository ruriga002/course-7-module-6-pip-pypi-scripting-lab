import requests
from datetime import datetime

LOG_ENTRIES = [
    "User logged in",
    "User updated profile",
    "Report exported"
]


def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


def write_log(entries):
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in entries:
            file.write(f"{entry}\n")
    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    write_log(LOG_ENTRIES)
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list of log entries.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


if __name__ == "__main__":
    sample_entries = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]
    generate_log(sample_entries)

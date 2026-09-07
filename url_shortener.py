"""
Simple URL Shortener

Commit 5: Add a click counter for each short URL.
"""

import json
import os
import random
import string

DATA_FILE = "urls.json"

CODE_LENGTH = 6
CODE_CHARACTERS = string.ascii_letters + string.digits


def load_urls():
    """Load stored URLs from the JSON file, or return an empty dict if none exists."""
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_urls(url_map):
    """Write the current URL mapping to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(url_map, file, indent=2)


# In-memory storage, loaded from disk at startup.
# Each entry looks like: short_code -> {"url": "...", "clicks": 0}
url_map = load_urls()


def generate_short_code():
    """Generate a random alphanumeric short code that isn't already in use."""
    while True:
        code = "".join(random.choice(CODE_CHARACTERS) for _ in range(CODE_LENGTH))
        if code not in url_map:
            return code


def add_url(url):
    """Generate a unique short code for the given URL, store it, and save to disk."""
    short_code = generate_short_code()
    url_map[short_code] = {"url": url, "clicks": 0}
    save_urls(url_map)
    print(f"Short code created: {short_code}")
    print(f"  {url} -> {short_code}")


def open_short_url(short_code):
    """Look up a short code, increment its click count, and print the original URL."""
    entry = url_map.get(short_code)
    if entry is None:
        print(f"Error: short code '{short_code}' not found.")
        return

    entry["clicks"] += 1
    save_urls(url_map)
    print(f"Original URL: {entry['url']}")
    print(f"Total clicks: {entry['clicks']}")


def view_urls():
    """Display all stored URLs along with their click counts."""
    if not url_map:
        print("No URLs stored yet.")
        return

    print("\nStored URLs:")
    for short_code, entry in url_map.items():
        print(f"  {short_code} -> {entry['url']} (clicks: {entry['clicks']})")


def main():
    while True:
        print("\n1. Shorten URL | 2. Open Short URL | 3. View URLs | 4. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            url = input("Enter URL: ").strip()
            add_url(url)
        elif choice == "2":
            short_code = input("Enter Short Code: ").strip()
            open_short_url(short_code)
        elif choice == "3":
            view_urls()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
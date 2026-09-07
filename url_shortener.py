"""
Simple URL Shortener

Commit 6: Add expiry dates for short URLs.
"""

import json
import os
import random
import string
from datetime import datetime, timedelta

DATA_FILE = "urls.json"

CODE_LENGTH = 6
CODE_CHARACTERS = string.ascii_letters + string.digits
DEFAULT_EXPIRY_DAYS = 7
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


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
# Each entry looks like:
# short_code -> {"url": "...", "clicks": 0, "expires_at": "YYYY-MM-DD HH:MM:SS"}
url_map = load_urls()


def generate_short_code():
    """Generate a random alphanumeric short code that isn't already in use."""
    while True:
        code = "".join(random.choice(CODE_CHARACTERS) for _ in range(CODE_LENGTH))
        if code not in url_map:
            return code


def add_url(url, expiry_days=DEFAULT_EXPIRY_DAYS):
    """Generate a unique short code for the given URL, store it with an expiry, and save."""
    short_code = generate_short_code()
    expires_at = datetime.now() + timedelta(days=expiry_days)
    url_map[short_code] = {
        "url": url,
        "clicks": 0,
        "expires_at": expires_at.strftime(DATE_FORMAT),
    }
    save_urls(url_map)
    print(f"Short code created: {short_code}")
    print(f"  {url} -> {short_code}")
    print(f"  Expires on: {expires_at.strftime(DATE_FORMAT)}")


def is_expired(entry):
    """Check whether a URL entry's expiry date has already passed."""
    expires_at = datetime.strptime(entry["expires_at"], DATE_FORMAT)
    return datetime.now() > expires_at


def open_short_url(short_code):
    """Look up a short code, check expiry, increment clicks, and print the original URL."""
    entry = url_map.get(short_code)
    if entry is None:
        print(f"Error: short code '{short_code}' not found.")
        return

    if is_expired(entry):
        print(f"Error: short code '{short_code}' has expired.")
        return

    entry["clicks"] += 1
    save_urls(url_map)
    print(f"Original URL: {entry['url']}")
    print(f"Total clicks: {entry['clicks']}")


def view_urls():
    """Display all stored URLs along with their click counts and expiry status."""
    if not url_map:
        print("No URLs stored yet.")
        return

    print("\nStored URLs:")
    for short_code, entry in url_map.items():
        status = "EXPIRED" if is_expired(entry) else f"expires {entry['expires_at']}"
        print(f"  {short_code} -> {entry['url']} (clicks: {entry['clicks']}, {status})")


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
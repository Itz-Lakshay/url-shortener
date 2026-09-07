"""
Simple URL Shortener

Commit 2: Generate unique short codes for each stored URL.
"""

import random
import string

# In-memory storage: maps short_code -> original_url
url_map = {}

CODE_LENGTH = 6
CODE_CHARACTERS = string.ascii_letters + string.digits


def generate_short_code():
    """Generate a random alphanumeric short code that isn't already in use."""
    while True:
        code = "".join(random.choice(CODE_CHARACTERS) for _ in range(CODE_LENGTH))
        if code not in url_map:
            return code


def add_url(url):
    """Generate a unique short code for the given URL and store the mapping."""
    short_code = generate_short_code()
    url_map[short_code] = url
    print(f"Short code created: {short_code}")
    print(f"  {url} -> {short_code}")


def view_urls():
    """Display all stored URLs."""
    if not url_map:
        print("No URLs stored yet.")
        return

    print("\nStored URLs:")
    for short_code, original_url in url_map.items():
        print(f"  {short_code} -> {original_url}")


def main():
    while True:
        print("\n1. Add URL | 2. View URLs | 3. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            url = input("Enter URL: ").strip()
            add_url(url)
        elif choice == "2":
            view_urls()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
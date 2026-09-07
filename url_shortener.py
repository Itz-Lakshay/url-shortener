"""
Simple URL Shortener

Commit 1: Basic menu-driven structure with in-memory URL storage.
"""

# In-memory storage: maps short_code -> original_url
url_map = {}


def add_url(url):
    """Temporarily store a URL (short code generation comes in a later commit)."""
    url_map[url] = url
    print(f"Stored URL: {url}")


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
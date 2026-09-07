# URL Shortener

A simple command-line URL shortener built in Python. Converts long URLs into short 
6-character codes, tracks click counts, and supports expiry dates.

## Features
- Shorten any URL into a random 6-character alphanumeric code
- Look up a short code to retrieve the original URL
- Click tracking per short code
- URLs automatically expire after a configurable number of days (default: 7)
- Persistent storage using a local JSON file (`urls.json`)
- Basic input validation for URLs

## Usage

Run the script:
    python url_shortener.py

You'll see a menu:
    1. Shorten URL
    2. Open Short URL
    3. View URLs
    4. Exit

### Example
    Choice: 1
    Enter URL: https://example.com/some/very/long/url
    Short code created: X7k92
    https://example.com/some/very/long/url -> X7k92
    Expires on: 2026-09-14 10:00:00

    Choice: 2
    Enter Short Code: X7k92
    Original URL: https://example.com/some/very/long/url
    Total clicks: 1

## Data Storage
All shortened URLs are stored in `urls.json` in the same directory, so data persists 
between runs.

## Requirements
- Python 3.7+
- No external dependencies (standard library only)
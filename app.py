"""
Simple URL Shortener - Web Interface (Flask)

Bonus: Web UI on top of the same core logic as url_shortener.py.
"""

from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash

from url_shortener import (
    url_map,
    is_valid_url,
    generate_short_code,
    save_urls,
    is_expired,
    DEFAULT_EXPIRY_DAYS,
    DATE_FORMAT,
)

app = Flask(__name__)
app.secret_key = "dev-secret-key"  # fine for local/demo use only


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if not is_valid_url(url):
            flash("Please enter a valid URL starting with http:// or https://")
            return redirect(url_for("index"))

        short_code = generate_short_code()
        expires_at = datetime.now() + timedelta(days=DEFAULT_EXPIRY_DAYS)
        url_map[short_code] = {
            "url": url,
            "clicks": 0,
            "expires_at": expires_at.strftime(DATE_FORMAT),
        }
        save_urls(url_map)
        flash(f"Short code created: {short_code}")
        return redirect(url_for("index"))

    return render_template("index.html", url_map=url_map, is_expired=is_expired)


@app.route("/<short_code>")
def redirect_short_code(short_code):
    entry = url_map.get(short_code)

    if entry is None:
        return render_template("error.html", message=f"Short code '{short_code}' not found."), 404

    if is_expired(entry):
        return render_template("error.html", message=f"Short code '{short_code}' has expired."), 410

    entry["clicks"] += 1
    save_urls(url_map)
    return redirect(entry["url"])


if __name__ == "__main__":
    app.run(debug=True)
#!/usr/bin/env python3
"""
Render Keep-Alive Background Service for Arya Notes Gallery
Pings https://arya-notes-gallery.onrender.com/ periodically to prevent Render free instance from spinning down.
"""

import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime

TARGET_URL = os.environ.get("TARGET_URL", "https://arya-notes-gallery.onrender.com/solutions/web_app/")
PING_INTERVAL_SECONDS = int(os.environ.get("PING_INTERVAL_SECONDS", 600))  # 10 minutes (Render sleeps at 15m)
RETRY_DELAY_SECONDS = 30
TIMEOUT_SECONDS = 60

LOG_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), "render_keepalive.log")

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)
    sys.stdout.flush()
    try:
        if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 1024 * 1024:
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                f.write(f"[{timestamp}] Log rotated.\n")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception:
        pass

def ping():
    req = urllib.request.Request(
        TARGET_URL,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Arya-KeepAlive-Bot/1.0",
            "Cache-Control": "no-cache"
        }
    )
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            latency = round((time.time() - start_time) * 1000, 1)
            status = response.getcode()
            log(f"SUCCESS: Pinged {TARGET_URL} -> HTTP {status} (Latency: {latency}ms)")
            return True
    except urllib.error.HTTPError as e:
        latency = round((time.time() - start_time) * 1000, 1)
        log(f"HTTP NOTICE: {TARGET_URL} returned HTTP {e.code}: {e.reason} ({latency}ms)")
        return True
    except urllib.error.URLError as e:
        latency = round((time.time() - start_time) * 1000, 1)
        log(f"NETWORK ERROR: Could not reach {TARGET_URL}: {e.reason} ({latency}ms)")
        return False
    except Exception as e:
        log(f"ERROR: Unexpected exception during ping: {e}")
        return False

def main():
    log(f"Starting Render Keep-Alive Daemon...")
    log(f"Target: {TARGET_URL}")
    log(f"Interval: {PING_INTERVAL_SECONDS} seconds ({PING_INTERVAL_SECONDS // 60} minutes)")
    
    # Initial immediate ping
    success = ping()
    if not success:
        log(f"Initial ping did not succeed (service may be waking up). Will retry shortly...")

    while True:
        try:
            time.sleep(PING_INTERVAL_SECONDS)
            ping()
        except KeyboardInterrupt:
            log("Daemon stopped by user.")
            break
        except Exception as e:
            log(f"Loop error: {e}. Sleeping for {RETRY_DELAY_SECONDS}s before resuming...")
            time.sleep(RETRY_DELAY_SECONDS)

if __name__ == "__main__":
    main()

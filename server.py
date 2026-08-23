#!/usr/bin/env python3
"""
Custom Multi-Threaded HTTP Server for Arya's Notes Gallery, Request Inspector & Reviews System
Handles static assets, live analytics, review submissions, and concurrent requests.
"""

import os
import sys
import json
import re
import urllib.parse
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

PORT = int(os.environ.get("PORT", 8000))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_FILE = os.path.join(BASE_DIR, "requests.log")
REVIEWS_FILE = os.path.join(BASE_DIR, "reviews.json")
LEGACY_LOG = os.environ.get("LEGACY_LOG", "/Users/umangaregmi/.gemini/antigravity-ide/brain/44fb7d90-b021-4f06-b5f7-3ce4a296861a/.system_generated/tasks/task-750.log")

# In-memory buffer of requests
live_requests = []

def parse_log_line(line, req_id):
    line = line.strip()
    if not line:
        return None

    pattern = r'(?P<ip>[^\s]+)\s+-\s+-\s+\[(?P<time>[^\]]+)\]\s+"(?P<method>[A-Z]+)\s+(?P<raw_path>[^\s]+)\s+HTTP/[0-9.]+"\s+(?P<status>\d+)'
    match = re.search(pattern, line)
    if not match:
        return None

    ip = match.group("ip")
    time_str = match.group("time")
    method = match.group("method")
    raw_path = match.group("raw_path")
    status = int(match.group("status"))
    path = urllib.parse.unquote(raw_path)

    # Completely ignore any requests to analytics or API
    if path.startswith("/analytics") or path.startswith("/api"):
        return None

    # Classify request
    category = "ASSET"
    subject = "System / Static"

    if path.endswith(".pdf"):
        category = "DOWNLOAD"
        p_lower = path.lower()
        if "math" in p_lower:
            subject = "Engineering Mathematics II"
        elif "edc" in p_lower:
            subject = "Electronic Devices & Circuits"
        elif "dl" in p_lower or "digital" in p_lower:
            subject = "Digital Logic"
        elif "chem" in p_lower:
            subject = "Engineering Chemistry"
        elif "oop" in p_lower:
            subject = "Object Oriented Programming"
        elif "ecm" in p_lower:
            subject = "Electrical Circuits & Machines"
        else:
            subject = "PDF Resource"
    elif path in ["/solutions/web_app/", "/solutions/web_app/index.html", "/"]:
        category = "PAGE_VIEW"
        subject = "Web Portal Page"
    elif status == 404:
        category = "ERROR"
        subject = "Missing Resource"
    elif path.endswith(".js") or path.endswith(".css") or path.endswith(".png") or path.endswith(".svg") or path.endswith(".jpg"):
        category = "ASSET"
        subject = "Static Asset"

    return {
        "id": req_id,
        "timestamp": time_str,
        "ip": ip,
        "device": "Web Browser",
        "country": "NP",
        "method": method,
        "path": path,
        "raw_path": raw_path,
        "status": status,
        "category": category,
        "subject": subject
    }

def load_initial_history():
    all_lines = []
    if os.path.exists(LEGACY_LOG):
        try:
            with open(LEGACY_LOG, "r", encoding="utf-8", errors="ignore") as f:
                all_lines.extend(f.readlines())
        except Exception:
            pass

    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8", errors="ignore") as f:
                all_lines.extend(f.readlines())
        except Exception:
            pass

    parsed = []
    req_id = 1
    for line in all_lines:
        obj = parse_log_line(line, req_id)
        if obj:
            parsed.append(obj)
            req_id += 1
    return parsed

live_requests = load_initial_history()

def record_request(client_info, method, path, status):
    if path.startswith("/analytics") or path.startswith("/api"):
        return

    ip = client_info["ip"]
    now_str = datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    log_entry = f'{ip} - - [{now_str}] "{method} {path} HTTP/1.1" {status} -\n'

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception:
        pass

    obj = parse_log_line(log_entry, len(live_requests) + 1)
    if obj:
        obj["device"] = client_info.get("device", "Desktop")
        obj["country"] = client_info.get("country", "NP")
        live_requests.append(obj)

def compute_unique_visitors():
    visitors = {}
    for r in live_requests:
        ip = r.get("ip", "127.0.0.1")
        device = r.get("device", "Desktop")
        key = f"{ip}_{device}"
        if key not in visitors:
            visitors[key] = {
                "id": len(visitors) + 1,
                "ip": ip,
                "device": device,
                "country": r.get("country", "NP"),
                "first_seen": r["timestamp"],
                "last_seen": r["timestamp"],
                "total_requests": 0,
                "page_views": 0,
                "downloads": 0
            }
        visitors[key]["last_seen"] = r["timestamp"]
        visitors[key]["total_requests"] += 1
        if r["category"] == "PAGE_VIEW":
            visitors[key]["page_views"] += 1
        elif r["category"] == "DOWNLOAD":
            visitors[key]["downloads"] += 1

    return list(reversed(list(visitors.values())))

# Reviews helper methods
def get_all_reviews():
    if not os.path.exists(REVIEWS_FILE):
        return []
    try:
        with open(REVIEWS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_all_reviews(reviews):
    try:
        with open(REVIEWS_FILE, "w", encoding="utf-8") as f:
            json.dump(reviews, f, indent=2)
    except Exception:
        pass

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.client_address[0],
                          self.log_date_time_string(),
                          format%args))

    def guess_type(self, path):
        if path.endswith(".pdf"):
            return "application/pdf"
        elif path.endswith(".jpg") or path.endswith(".jpeg"):
            return "image/jpeg"
        return super().guess_type(path)

    def get_client_info(self):
        headers = self.headers
        cf_ip = headers.get("CF-Connecting-IP")
        x_forwarded = headers.get("X-Forwarded-For")
        
        if cf_ip:
            ip = cf_ip
        elif x_forwarded:
            ip = x_forwarded.split(",")[0].strip()
        elif self.client_address:
            ip = self.client_address[0]
        else:
            ip = "127.0.0.1"

        ua = headers.get("User-Agent", "Unknown Browser")
        country = headers.get("CF-IPCountry", "NP")

        ua_lower = ua.lower()
        device = "Desktop"
        if "iphone" in ua_lower:
            device = "iPhone"
        elif "android" in ua_lower:
            device = "Android Phone"
        elif "ipad" in ua_lower or "tablet" in ua_lower:
            device = "Tablet / iPad"
        elif "macintosh" in ua_lower or "mac os" in ua_lower:
            device = "Macintosh"
        elif "windows" in ua_lower:
            device = "Windows PC"
        elif "linux" in ua_lower:
            device = "Linux"

        return {
            "ip": ip,
            "device": device,
            "country": country,
            "ua": ua
        }

    def do_GET(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        # Handle Live API: Requests & Analytics
        if path == "/api/requests":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()

            total = len(live_requests)
            page_views = sum(1 for r in live_requests if r["category"] == "PAGE_VIEW")
            downloads = sum(1 for r in live_requests if r["category"] == "DOWNLOAD")
            errors = sum(1 for r in live_requests if r["status"] == 404 or r["category"] == "ERROR")
            assets = total - page_views - downloads - errors
            unique_visitors = compute_unique_visitors()

            subject_counts = {
                "Digital Logic": 0,
                "Electronic Devices & Circuits": 0,
                "Engineering Chemistry": 0,
                "Engineering Mathematics II": 0,
                "Electrical Circuits & Machines": 0,
                "Object Oriented Programming": 0
            }

            for r in live_requests:
                if r["category"] == "DOWNLOAD" and r["subject"] in subject_counts:
                    subject_counts[r["subject"]] += 1

            payload = {
                "total_requests": total,
                "unique_visitors_count": len(unique_visitors),
                "unique_visitors_list": unique_visitors,
                "page_views": page_views,
                "pdf_downloads": downloads,
                "errors_count": errors,
                "assets_count": assets,
                "subject_downloads": subject_counts,
                "requests": list(reversed(live_requests))
            }

            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return

        # Handle Live API: Reviews
        if path == "/api/reviews":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
            self.end_headers()

            reviews = get_all_reviews()
            total_revs = len(reviews)
            avg_rating = round(sum(r["rating"] for r in reviews) / total_revs, 1) if total_revs > 0 else 5.0
            
            rating_dist = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
            for r in reviews:
                rt = int(r.get("rating", 5))
                if rt in rating_dist:
                    rating_dist[rt] += 1

            payload = {
                "total_reviews": total_revs,
                "average_rating": avg_rating,
                "rating_distribution": rating_dist,
                "reviews": reviews
            }

            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return

        # Redirect root to solutions/web_app/
        if path == "/" or path == "":
            self.send_response(302)
            self.send_header("Location", "/solutions/web_app/")
            self.end_headers()
            return

        client_info = self.get_client_info()
        status_to_record = 200

        try:
            super().do_GET()
        except Exception:
            status_to_record = 500

        record_request(client_info, "GET", path, status_to_record)

    def do_POST(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path

        # Handle Review Submission: POST /api/reviews
        if path == "/api/reviews":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                name = data.get("name", "").strip() or "Anonymous Student"
                roll = data.get("roll", "").strip() or "IOE BCT"
                subject = data.get("subject", "").strip() or "General Gallery"
                rating = int(data.get("rating", 5))
                rating = max(1, min(5, rating))
                tag = data.get("tag", "").strip() or "⚡ Life Saver"
                comment = data.get("comment", "").strip()

                if not comment:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Comment text cannot be empty"}).encode("utf-8"))
                    return

                new_review = {
                    "id": f"rev_{int(datetime.now().timestamp() * 1000)}",
                    "name": name,
                    "roll": roll,
                    "subject": subject,
                    "rating": rating,
                    "tag": tag,
                    "comment": comment,
                    "timestamp": datetime.now().strftime("%d/%b/%Y %H:%M"),
                    "likes": 1
                }

                reviews = get_all_reviews()
                reviews.insert(0, new_review)
                save_all_reviews(reviews)

                self.send_response(201)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "review": new_review}).encode("utf-8"))
                return

            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
                return

        # Handle Like/Upvote: POST /api/reviews/like
        if path == "/api/reviews/like":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode('utf-8'))
                rev_id = data.get("id")
                reviews = get_all_reviews()
                updated_likes = 0

                for r in reviews:
                    if r["id"] == rev_id:
                        r["likes"] = r.get("likes", 0) + 1
                        updated_likes = r["likes"]
                        break

                save_all_reviews(reviews)

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "likes": updated_likes}).encode("utf-8"))
                return

            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
                return

        self.send_response(404)
        self.end_headers()

    def do_HEAD(self):
        parsed_url = urllib.parse.urlparse(self.path)
        path = parsed_url.path
        if path == "/" or path == "":
            self.send_response(302)
            self.send_header("Location", "/solutions/web_app/")
            self.end_headers()
            return
        if path in ["/api/requests", "/api/reviews"]:
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return
        client_info = self.get_client_info()
        super().do_HEAD()
        record_request(client_info, "HEAD", self.path, 200)

def run():
    server_address = ('', PORT)
    httpd = ThreadingHTTPServer(server_address, CustomHandler)
    httpd.daemon_threads = True
    print(f"Arya's Multi-Threaded Server & Reviews API running at http://localhost:{PORT}/")
    print(f"Portal:    http://localhost:{PORT}/solutions/web_app/")
    print(f"Inspector: http://localhost:{PORT}/analytics/")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == "__main__":
    run()

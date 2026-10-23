#!/usr/bin/env python3
"""Local server for the practice pages. Run from anywhere:  python tools/serve.py
Then open  http://localhost:8765/practice/4a.%20listen-and-repeat.html

It serves the vault and lets the speaking pages save recordings straight into
recordings/speaking/<task>/ (git-ignored). It listens on 127.0.0.1 only, accepts
only file names of the exact recording/manifest form, and never overwrites a
path outside recordings/speaking/.
"""
import http.server, json, os, re, socketserver, sys, urllib.parse

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
REC = os.path.join(ROOT, "recordings", "speaking")
PORT = int(os.environ.get("PORT", "8765"))
TASKS = {"listen-and-repeat": "LR"}
NAME = re.compile(r"^(LR)_T[1-7]_\d{8}-\d{6}(_Q[1-7]\.webm|\.json)$")
MAX = 25 * 1024 * 1024


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def _json(self, code, obj):
        b = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def _local_origin(self):
        o = self.headers.get("Origin")
        return o is None or o in (f"http://localhost:{PORT}", f"http://127.0.0.1:{PORT}")

    def do_GET(self):
        if self.path == "/__ping":
            return self._json(200, {"ok": True, "saves": "recordings/speaking/<task>/"})
        return super().do_GET()

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        if u.path != "/__save" or not self._local_origin():
            return self._json(404, {"ok": False, "error": "not found"})
        q = urllib.parse.parse_qs(u.query)
        task, name = (q.get("task") or [""])[0], (q.get("name") or [""])[0]
        n = int(self.headers.get("Content-Length") or 0)
        if task not in TASKS or not NAME.match(name) or not name.startswith(TASKS[task] + "_") or n <= 0 or n > MAX:
            return self._json(400, {"ok": False, "error": "bad task, name or size"})
        d = os.path.join(REC, task)
        os.makedirs(d, exist_ok=True)
        p = os.path.realpath(os.path.join(d, name))
        if os.path.dirname(p) != os.path.realpath(d):
            return self._json(400, {"ok": False, "error": "bad path"})
        data = self.rfile.read(n)
        if len(data) != n:
            return self._json(400, {"ok": False, "error": "short body"})
        with open(p + ".part", "wb") as f:
            f.write(data)
        os.replace(p + ".part", p)
        return self._json(200, {"ok": True, "file": os.path.relpath(p, ROOT), "bytes": n})

    def log_message(self, fmt, *a):
        if "/__save" in (a[0] if a else ""):
            sys.stderr.write("saved: " + a[0] + "\n")


class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    with S(("127.0.0.1", PORT), H) as s:
        print(f"Serving {ROOT}\nOpen http://localhost:{PORT}/practice/4a.%20listen-and-repeat.html\nRecordings go to {REC}/<task>/   (Ctrl-C to stop)")
        try:
            s.serve_forever()
        except KeyboardInterrupt:
            pass

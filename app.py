from http.server import *

class H(SimpleHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200)
        s.end_headers()
        s.wfile.write(b"CI/CD Success")

HTTPServer(("",5022),H).serve_forever()

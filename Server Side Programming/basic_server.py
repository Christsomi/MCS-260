import http.server as hs

class Server(hs.BaseHTTPRequestHandler):
  def do_GET(self):
    try:
      file = open("html example.html", "r")
      html = file.read()
      self.send_response(200)

    except: 
      html = "File not Found"
      self.send_response(404)

    self.end_headers()
    self.wfile.write(bytes(html, 'utf-8'))

server = hs.HTTPServer(('localhost', 8000), Server)
server.serve_forever()
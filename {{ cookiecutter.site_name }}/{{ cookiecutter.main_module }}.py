{% if cookiecutter.site_type == "socket" %}
"""An example HTTP server using sockets on Azure Web Apps."""
try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import os
import sys


class PythonVersionHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        charset = "utf-8"
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset={}".format(charset))
        self.send_header("Content-Length", len(sys.version))
        self.end_headers()
        self.wfile.write(sys.version.encode(charset))


if __name__ == "__main__":
    server_address = "127.0.0.1", int(os.environ.get("PORT", 5555))
    server = HTTPServer(server_address, PythonVersionHandler)
    server.serve_forever()

{% else %}
"""An example WSGI server on Azure Web Apps."""
import sys


def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    yield sys.version.encode()


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 5555, wsgi_app)
    httpd.serve_forever()
{% endif %}

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello Yo Server Ass</body></html>"
                self.wfile.write(output)
                byte = output.encode('utf-8')
                print (byte)
                return
        except IOError:
            self.send_error(404, "File not found %s" %self.path)

def main(): #This method has instantiation code for server, tuple is host and port number
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler) #pass in tuple and handler
        print ("Web server running on port %s" % port)
        server.serve_forever()#method keeps server running

    except KeyboardInterrupt:
        print ("Stopping server...")
        server.socket.close()


if __name__ == '__main__':
    main() 

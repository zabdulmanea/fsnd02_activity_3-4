#!/usr/bin/env python3
#
# An HTTP server that's a message board.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import udacian

memory = []

form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" action="http://localhost:8000/">
    <textarea name="name">name</textarea>
    <br>
    <textarea name="city">city</textarea>
    <br>
    <textarea name="enrollment">enrollment</textarea>
    <br>
    <textarea name="nanodegree">nanodegree</textarea>
    <br>
    <textarea name="status">status</textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Determine the content length
        length = int(self.headers.get('Content-length', 0))

        # Read the information content
        data = self.rfile.read(length).decode()

        # Initialize a list that will contain udacian information
        info_list = []

        # Extract the information of the member
        for info_values in parse_qs(data).values():
            information = info_values[0]

            # Escape HTML tags in the content so users can't break world+dog.
            information = information.replace("<", "&lt;")

            # Add the informationto the list
            info_list.append(information)

        # Initialize an instance of Udacian() class to hold udacity member information
        member = udacian.Udacian(info_list[0], info_list[1], info_list[2],
                                 info_list[3], info_list[4])

        # Store it in memory
        memory.append(member.print_udacian())

        # Send a 303 back to the root page
        self.send_response(303)  # redirect via GET
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Send the form with the messages in it.
        mesg = form.format("\n".join(memory))
        self.wfile.write(mesg.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()

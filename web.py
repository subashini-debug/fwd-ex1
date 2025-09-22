
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<!DOCTYPE html>
<html>
<head>
    <title>TCP and IP Protocol Table</title>
    <style>
        table {
            border-collapse: collapse;
            width: 60%;
            margin: 30px auto;
        }
        th, td {
            border: 1px solid #333;
            padding: 8px 14px;
            text-align: center;
        }
        th {
            background-color: #efefef;
        }
        caption {
            margin-bottom: 8px;
            font-weight: bold;
            font-size: 1.15em;
        }
    </style>
</head>
<body>
    <table>
        <caption>TCP and IP Protocols</caption>
        <tr>
            <th>Protocol</th>
            <th>Protocol Number</th>
            <th>OSI/Network Layer</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>TCP (Transmission Control Protocol)</td>
            <td>6</td>
            <td>Transport</td>
            <td>Reliable, connection-oriented protocol for data transmission</td>
        </tr>
        <tr>
            <td>IP (Internet Protocol)</td>
            <td>4</td>
            <td>Network/Internet</td>
            <td>Responsible for addressing and routing packets between hosts</td>
        </tr>
    </table>
</body>
</html>
~~~
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
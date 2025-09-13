# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~

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

## OUTPUT:



![alt text](<Screenshot 2025-09-13 160413.png>)
![alt text](<Screenshot 2025-09-13 160440.png>)






## RESULT:
The program for implementing simple webserver is executed successfully.


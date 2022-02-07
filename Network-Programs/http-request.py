import socket
# connect with socket function
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect with site
mysock.connect(('data.pr4e.org', 80))
# prepate the GET data with encode
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# send the data to site
mysock.send(cmd)

while True:
    # recieve teh data
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')
# close the site
mysock.close()

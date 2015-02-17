import socket
import thread

BUFFER_SIZE = 1024
data = "no data"
users = []

def main():
  TCP_IP = socket.gethostbyname(socket.gethostname())
  TCP_PORT = 1997

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind( (TCP_IP, TCP_PORT ) )
  sock.listen(3)

  print "Server online and awaiting connections!"

  while True:
    conn, addr = sock.accept()
    users.append(conn)
    print "Connection address: ", addr
    try:
      thread.start_new_thread( recieve, (conn, data))
    except:
      print "Error: unable to start thread"




def recieve(conn, data):
  print "listening"
  while True:
    print "ey"
    data = conn.recv(BUFFER_SIZE)
    print data
    for user in users:
      user.send(data)

    

if __name__ == "__main__":
  main()

import socket
import thread
import pickle

BUFFER_SIZE = 1024
data = "no data"
chatList = []

def main():
  TCP_IP = socket.gethostbyname(socket.gethostname())
  TCP_PORT = 1740

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind( (TCP_IP, TCP_PORT ) )
  sock.listen(3)
  
  while True:
    conn, addr = sock.accept()
    print "Connection address: ", addr
    try:
      thread.start_new_thread( talk, (conn, data) )
    except:
      print "Error: unable to start thread"


def talk(conn, data):
  while 1
    data = conn.recv(BUFFER_SIZE)
    chatList = pickle.loads(data)
    data = pickle.dumps(data)
    conn.send(data)

  conn.close()

if __name__ == "__main__":
  main()

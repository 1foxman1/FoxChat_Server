import socket
import thread
import pickle

BUFFER_SIZE = 1024
data = "no data"
chatList = []

def main():
  TCP_IP = socket.gethostbyname(socket.gethostname())
  TCP_PORT = 1997

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind( (TCP_IP, TCP_PORT ) )
  sock.listen(3)

  print "Server online and awaiting connections!"

  while True:
    conn, addr = sock.accept()
    print "Connection address: ", addr
    try:
      thread.start_new_thread( recieve, (conn, data) )
      thread.start_new_thread( send, (conn, data, chatList, chatList) )
    except:
      print "Error: unable to start thread"




def recieve(conn, data):
  print "listening"
  while True:
    print "ey"
    dt = conn.recv(BUFFER_SIZE)
    print dt
    chatList.append(dt)
    

def send(conn, data, curChatList, chatList):
    while 1:
        if curChatList != chatList:
            print chatList
            data = pickle.dumps(chatList)
            conn.send(data)
            chatList = curChatList
            
    

if __name__ == "__main__":
  main()

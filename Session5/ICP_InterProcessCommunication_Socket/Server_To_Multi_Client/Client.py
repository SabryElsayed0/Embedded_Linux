import socket

# IP4v , and protocol is TCP
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#name of your pc
pc_name = socket.gethostname()

#to get your local Ip
ip = socket.gethostbyname(pc_name)
# print(pc_name)
print("your ip is :" + ip)
 
 #make a port
client.connect((ip , 5000))
print("==============================================")
# while True:
msg=str(input("please enter the message that you wand to send: "))
msg_encoded = msg.encode('UTF-8')
client.send(msg_encoded)
print("================================================================")
# data=client.recv(1024)
# print(f"{ip} is sending to you this message {data.decode('UTF-8')}")
client.close()
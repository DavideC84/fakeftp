#!/usr/bin/python3
import socket
import subprocess
from getpass import getpass
import datetime

# Fake ftp honeypot
def writelog (logline):
    log_file = open ("log.txt", "a")
    current_time = datetime.datetime.now()
    log_file.write (str(current_time) + " " + logline + "\n")
    log_file.close()

serversocket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 21

serversocket.bind((host,port))
serversocket.listen(5)
writelog ("Server started \n") # This is necessary or the next file open will fail (in the case file doesn't exist yet)

while True:
        clientsocket,addr = serversocket.accept()

        #print ("Incoming connection from: ", str(addr))

        ip = addr[0]
        
        with open("log.txt", "r") as logfile:
            if (ip + " final") not in logfile.read():
                writelog ("Connection from: " + ip)
                msg = "Custom iFtp server v 1.12.2b" + " \r\n" 

                msg2 = 'User: ' 

                # let's begin sending stuff

                try:
                    clientsocket.send(msg.encode('ascii'))
            
                    clientsocket.send(msg2.encode('ascii'))

                    user = clientsocket.recv (1024).decode("ascii")
                    writelog ("IP: " + ip + " entered user: " + user)
                    msg3 = 'Password: ' 
            
                    clientsocket.send(msg3.encode('ascii'))

                    pwd = clientsocket.recv (1024).decode("ascii")
                    writelog ("IP: " + ip + " entered password: " + pwd)

                    # image
                            
                    image = subprocess.Popen (['cat', 'tf.txt'], stdout = subprocess.PIPE).communicate()[0]
                    clientsocket.send(image)
                    
                    # final text

                    msg5 = "... did you really think it was so easy? \nOf course there's no ftp server, thanks for using my honeypot!\nYour IP ("+ ip + ") and everything you typed has been logged. :-)\nYou're now free to express your frustration (admin will read this): "
                    clientsocket.send(msg5.encode('ascii'))   

                    # last input and salutations    
                    
                    input = clientsocket.recv (1024).decode("ascii")
                    msg6 = "\nTrololol.. bye! \r\n" 
                    writelog ("IP: " + ip + " final comment to admin: " + input)
                    clientsocket.send (msg6.encode('ascii'))
                    # If we don't want the process to end after a catch comment next lines
                    print ("Fakeftp honey pot catched someone! Stopping process.");
                    serversocket.close()
                    break

                except:
                    writelog ("IP " + ip + " connection closed")
                # The end
                clientsocket.close()
               

            else: # we've already served ip
                writelog ("Already served ip: " + ip + " - dropping connection")
                clientsocket.close()


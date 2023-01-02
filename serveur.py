import socket
import os
from sys import stdout
from threading import Thread
import subprocess
import psutil

def create_socket():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen()
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    serveur(conn,address)

def serveur(conn,address):

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()

        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        #Getting message which has been sent
        message_sent = str(data) 
        #Using data for specifics commands
        # get windows version 
        if message_sent == "get_windows_version" :
            cmd = subprocess.Popen("winver", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        #get linux version
        elif message_sent == "get_linux_version" :
            cmd = subprocess.Popen("hostnamectl", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        #get macOS version
        elif message_sent == "get_mac_version" :
            cmd = subprocess.Popen("system_profiler SPSoftwareDataType", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        #get ram informations
        elif message_sent == "ram_informations" :
            mem = psutil.virtual_memory()
            ram = str(mem)
            conn.send(ram.encode())
        #get cpu informations
        elif message_sent == "cpu_informations" :
            per_cpu = psutil.cpu_percent(percpu=True)
            cpu_usage =""
            for idx, usage in enumerate(per_cpu):
                #print(f"CORE_{idx+1}: {usage}%")
                cores = f"CORE_{idx+1}: {usage}%"
                cpu_usage = cpu_usage + "  " + cores
                #print (cores)
            conn.send(cpu_usage.encode())
        #get IP from device in windows
        elif message_sent == "IP_windows":
            cmd = subprocess.Popen("ipconfig | findstr /i ""ipv4""", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        #get IP from device in linux
        elif message_sent == "IP_linux":
            cmd = subprocess.Popen("ip a", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        #get IP from device in macOS
        elif message_sent == "IP_macOS":
            cmd = subprocess.Popen("/sbin/ifconfig", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        # get name of the device
        elif message_sent == "hostname" :
            cmd = subprocess.Popen("hostname", stdout=subprocess.PIPE, shell=True)
            command = str(cmd.communicate())
            conn.send(command.encode())
        elif message_sent == "Disconnect" :
            conn.send("Disconnect".encode())
            print("Disconnection from: " + str(address))
        # killing the server and the connections
        elif message_sent == "Kill" :
            print ("Killing connection")
            conn.send("Kill".encode())
            conn.close()
            break;

        elif "DOS:" or "Powershell:" in message_sent :
            try :
                cmd = subprocess.Popen("systeminfo | findstr /B /C:""Nom du système d'exploitation:""", stdout=subprocess.PIPE, shell=True)
            except :
                conn.send("The command sent can't be used because the system is not on DOS or Windows System")
            else : 
                message_parsed = (message_sent.replace('DOS:','')) 
                cmd = subprocess.Popen(message_parsed, stdout=subprocess.PIPE, shell=True)
                command = str(cmd.communicate())
                conn.send(command.encode())

        elif ":" in message_sent :
            splitted_message = message_sent.split(':')
            #print (splitted_message)
            OS_name = splitted_message[0]
            command_to_execute = splitted_message[1]
            if OS_name == "Linux" :
                try :
                    cmd = subprocess.Popen("hostnamectl", stdout=subprocess.PIPE, shell=True)
                except :
                    conn.send("Not a Linux version".encode())
                else:
                    cmd = subprocess.Popen(command_to_execute, stdout=subprocess.PIPE, shell=True)
                    command = str(cmd.communicate())
                    conn.send(command.encode())

            elif OS_name == "mac" :
                try : 
                    cmd = subprocess.Popen("uname", stdout=subprocess.PIPE, shell=True)
                except :
                    conn.send("Not a Mac Command".encode())
                else :
                    cmd = subprocess.Popen(command_to_execute, stdout=subprocess.PIPE, shell=True)
                    command = str(cmd.communicate())
                    conn.send(command.encode())



        
        #Send a command without taking care of the OS
        else :
            try :
                cmd = subprocess.Popen(message_sent, stdout=subprocess.PIPE, shell=True)
            except : 
                print("Unvalid Command received")
                conn.send("Unvalid Command received".encode())
            else :
                command = str(cmd.communicate())
                conn.send(command.encode())
            


        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    create_socket()
    #serveur(conn,adress)
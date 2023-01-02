# User Documentation for Client - Server Application

## _This Documentation is a part of the requirement for the SAE309 which explains how to use the application in all ways possible for the users._

### This application is conformed with the rules explained in the easy difficulty in the rules of the project, written by Mr. Drouhin.

#### 1)
First of all to use this app, you will need to transfert the serveur.py file on the computer, or VM, or whatever on the target which you want to know differents about it, of course, you will need to have access to the device.
#### 2)
After that, execute the file in a shell to make it open to users who want to connect to the server.

#### 3) 
On the line 5 of the file, change "socket.gethostname()" by the IP adress of the server which wiats a connection, and then execute on the user device the client.py file in a shell, and after that you can see a '->' appears in your command prompt which means that the user reached the server.

#### 4)
Now you can use any command that you want to use on the server.
With that application, some commands had been add that makes you able to know some informations about the server.
This commands are :
- get_windows_version : that makes you able to know the windows version, if the server is on windows.
- get_linux_version : that makes you able to know the linux version, if the server is on linux.
- get_mac_version : that makes you able to know the macintosh version, if the server is on macintosh.
- ram_informations: that gives you informations about the ram capacity, free ram and the actual usage.
- cpu_informations : that gives you informations about the cpu charges on the differents cores.
- IP_windows : that gives you the IP adress of the server, if it is on windows.
- IP_linux : that gives you the IP adress of the server, if it is on linux.
- IP_macOS : that gives you the IP adress of the server, if it is on macOS.
- hostname : that gives you the name of the server.
- Disconnect : that disconnects the client connected on the server, you can reconnect the client instantly if you want, the server waits another connection until his shutting down.
- Kill : that shuts down the server and all the connections with it.

#### 5)

Finally, you can type the command you want with the OS version like this, "DOS:" for example.
You can also use :
- DOS:command
- Powershell:command
- Linux:command
- mac:command

You also know all the possible usages of this application.

_HELMSTETTER Antoine : Main Developper_
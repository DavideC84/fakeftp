# fakeftp
Trolling the hackers: fakeftp honeypot.

************
HOW IT WORKS
************

This short script, opens a socket on port 21, pretending to be an ftp server.
The attacker can telnet a service.

A fake prompt is shown to the attacker, user and password are asked.

Whatever value is typed by the attacker, once the password is sent, fakeftp will show a trollface and notify the hacker we've logged anything he typed.

Fakeftp.py writes a log file (log.txt) in the directory where the script is located. 
It stops automatically when someone does the entire procedure and gets caught.

In that case, that IP will not be served anymore (until you delete the logfile).

*****
USAGE
*****

Run:

./fakeftp.py

In background:

./fakeftp.py & 

If the .py file is not executable, you'll need to:

chmod +x fakeftpy.py

To stop the process:

ps aux | grep -i fakeftp 

find the process id number then kill it:

kill -9 idnumber

or just type fg to bring the program in foreground and then ctrl+z.


#propecia.py
===========

A multi-threaded class C network scanner. Loosely based on propecia.c by Bind.

Added functionality to input multiple ports to scan or multiple class C networks. 

Introduced argument passing to the Python application
-----

Modified by Ryan Villarreal
> Created by Michael Allen (http://www.MikeAllen.org)

Based on the original propecia port scanner written by Bind, available here:
    http://packetstormsecurity.com/files/14232/propecia.c.html

Performs a simple TCP port scan on a single port and outputs a list of IP 
addresses with that port open.  

```
usage: propecia.py [-h] --port PORT [PORT ...] [-V]
                   (--multi [MULTI] | --addr ADDR [ADDR ...])
propecia.py: error: argument --port/-p is required


example: ./propecia.py --port 80 --addr 192.168.0
example: ./propecia.py -p 80 -a 192.168.0
example: ./propecia.py -p 80 443 139 -a 192.168.0
example: ./propecia.py -p 80 -m list.txt
```
-----



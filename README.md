Simple Hosts File Updater for MacOSX

Available commands:
list 
add 
disable
remove
enable
listArgs


./hosts.py list - list entries

sudo ./hosts.py add abcd.com - add a new entry for abcd.com with host 127.0.0.1

sudo ./hosts.py add abcd.com x.x.x.x - add a new entry for abcd.com with host x.x.x.x

sudo ./hosts.py disable 20 - disable entry at 20 (point to host)

sudo ./hosts.py enable 20 - enable entry at 20 (commented out)

sudo ./hosts.py remove 20 - remove entry at 20

./hosts.py listArgs - list arguments



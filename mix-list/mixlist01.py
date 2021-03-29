#!/usr/bin/env python3
my_list = [ "192.168.0.5", 5060, "UP" ]
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
ip1 = new_list[3]
ip2 = new_list[4]
port1 = new_list[0]
port2 = new_list[1]
port3 = new_list[2]
print(f"When I ssh into IP addresses {ip1} or {ip2} I am unable to ping ports {port1},{port2}, or {port3}")



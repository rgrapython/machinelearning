# -*- coding: UTF-8 -*-
#
import json
import calendar
import socket
from struct import unpack, pack
	
def get_ip():
  根据router_id和interface_id计算obj_id
	print "--------------------------------"
	router_id = 6
	interface_id = [11111, 22222]
	for ids in interface_id:
		#
		print "obj_id:",(router_id << 16)+(ids & 0xffff)
		print '\n'
	print "--------------------------------"

def get_ip_new():
	# 根据obj_id反推routre_id和interface_id
	obj_id = 131073
	print "router_id:",obj_id >> 16
	print "interface_id:",obj_id & 0xffff
	print "--------------------------------"


if __name__ == '__main__':
	get_ip()
	

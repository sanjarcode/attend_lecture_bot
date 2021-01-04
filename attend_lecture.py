#!/usr/bin/env python3
from attend_module import attend_meet, log_attendance
import sys

if __name__ == '__main__' and len(sys.argv) == 5:
	username = sys.argv[1]
	password = sys.argv[2]
	meet_url = sys.argv[3]
	lecture_time = sys.argv[4]
	try:
		if(attend_meet(username, password, meet_url, lecture_time)):
			log_attendance(True)  # no cause required
		else:
			log_attendance(False, 'Invalid config file')
	except Exception as e:
		log_attendance(False, str(e))

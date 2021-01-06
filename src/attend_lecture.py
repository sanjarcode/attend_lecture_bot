#!/usr/bin/env python3
from attend_module import attend_meet, log_attendance
import sys

def attend_lecture():
	username, password, meet_url, lecture_time, subject_name = sys.argv[1:6]
	try:
		if(attend_meet(username, password, meet_url, lecture_time)):
			log_attendance(True, subject_name)  # no cause required
		else:
			log_attendance(False, subject_name, 'Invalid config file')
	except Exception as e:
		log_attendance(False, subject_name, str(e))

if __name__ == '__main__':
	if len(sys.argv) == 6:
		attend_lecture()

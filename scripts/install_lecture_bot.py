#!/usr/bin/env python3

import os
os.system('pip3 uninstall crontab')  #important
os.system('pip3 install -r requirements.txt')  # installs all dependencies

from .attend_module import clean_timetable, set_timetable, install_files

if __name__ == "__main__":
    clean_timetable()  # cleans attend lecture cron jobs
    set_timetable()  # adds attend lecture cron jobs
    install_files()  # installs files if they are absent
    print('Be productive even if skipping lectures')

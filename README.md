This script is a prank project. It uses cron daemon to emulate your presence in online classes. This lets you have time for studying things that really matter.

Requirements:
1. OS - Linux/Mac
2. cron [install here](https://stackoverflow.com/questions/1802337/how-to-install-cron)
3. python3
4. pip3
5. Make sure that the OS has allowed Chrome access to microphone and camera
6. Stable internet connection at the time of lecture
7. PC is not sleeping at the time of lecture

**Don't hurry** If you have Linux/Mac systems  - all the requirements are already satisfied

How to install:
1. Set the fields in config.json
2. Run the _install.py_ script
3. Check if properly installed using crontab -l

Where is it installed: at ~/home/.attend_lecture/

How to remove:
1. run uninstall.py

Notes:
1. Installing the app multiple times won't clog the crontab, don't worry about it.
2. Your existing cron jobs will not be affected, even if you add new ones after installation
3. Keep your PC(bot) on at all times
4. If timetable changes, change the timetable, reinstall the app

USE AT YOUR OWN RISK!
Do something productive if skipping lectures.
Time is precious!

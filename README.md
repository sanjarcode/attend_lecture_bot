## What
This script started out as a prank project. But it works.

## Why
Lets you have time for studying things that really matter.

## How
- It uses the `cron` daemon to fire a script, as per your timetable.
- Open Chrome, logs in using given credentials.
- Closes the browser, after a specified time(for example 60 minutes).
- Logs in the status, errors that occurred in a file for future reference.

### Requirements
1. OS - Linux/Mac
2. `cron` [install here](https://stackoverflow.com/questions/1802337/how-to-install-cron)
3. `python3`
4. `pip3`
5. Make sure that the browser has access to microphone and camera, without manual intervention.
6. Stable internet connection at the time of lecture.
7. PC is not sleeping at the time of lecture.

**Note** Most requirements are present by default, on Linux and MacOS.

## Installation
1. Download and extract the zip.
2. Set the fields in `config.json` - email, password, timetable, class links.
3. Run `install.py`
4. Check if properly installed using crontab -l: you'll see entries with your email, password.

Installation location: `~/.attend_lecture/`

## Uninstallation
1. Run `uninstall.py`

Your attendance log is retained. It contains status, error for all lectures.

## Note
1. Installing the app multiple times won't clog the crontab, don't worry about it.
2. Your existing cron jobs will not be affected, even if you add new ones after installation
3. Keep your PC(bot) on at all times
4. If timetable changes, change the timetable, run `install.py` again.
5. Not tested on Windows.
6. Your email and password kept as plain-text, i.e. unencrypted.

USE AT YOUR OWN RISK - Your teacher can be your best friend. Time is precious!

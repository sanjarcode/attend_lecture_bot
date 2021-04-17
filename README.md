## What
This script started out as a prank project. But it works.
It uses the `cron` daemon to emulate your presence in online classes, via the browser.

## Why
Lets you have time for studying things that really matter.

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
1. Download the zip.
2. Set the fields in config.json
3. Run the _install.py_ script
4. Check if properly installed using crontab -l

Installation location: `~/.attend_lecture/`

## Uninstallation
1. Run `uninstall.py`

Your attendance log is retained. It contains status, error for all lectures.

## Notes
1. Installing the app multiple times won't clog the crontab, don't worry about it.
2. Your existing cron jobs will not be affected, even if you add new ones after installation
3. Keep your PC(bot) on at all times
4. If timetable changes, change the timetable, run `install.py` again.
5. Not tested on Windows.
6. Your password and email are kept as plain-text.

USE AT YOUR OWN RISK - Your teacher can be your best friend. Time is precious!

## What
A bot (😂️ bunch of scripts) that attends lectures on Google Meet.

## Why
Lets you have time for studying things that really matter.
This as a prank project🤗️.

## How
- It uses the `cron` daemon to fire a script, as per your timetable.
- Opens Chrome, logs in using given credentials.
- Closes the browser, after a specified time(for example 60 minutes).
- Logs in the status, errors that occurred in a file for future reference.

## Usage

#### Requirements
1. OS - Linux/Mac
2. `cron` [install here](https://stackoverflow.com/questions/1802337/how-to-install-cron)
3. `python3`
4. `pip3`
5. Make sure the browser has access to _microphone_ and _camera_, without manual intervention.
6. Stable internet connection at the _time of lecture_.
7. PC is not sleeping at the _time of lecture_.

**Note** On Linux and MacOS, most requirements are already present.

#### Installation
1. Download and extract as zip.
2. Set fields in [`timetable.json`](https://github.com/dormant-sanjarcode/attend_lecture_bot/blob/master/config/timetable.json) - email, password, timetable, class links.
3. Run [`install.py`]((https://github.com/dormant-sanjarcode/attend_lecture_bot/blob/master/scripts/install.py))
4. Check if properly installed using crontab -l: you'll see entries with your email, password.

Installation location: `~/.attend_lecture/`

#### Removal
1. Run [`uninstall.py`](https://github.com/dormant-sanjarcode/attend_lecture_bot/blob/master/scripts/uninstall.py)

Your attendance log is retained. It contains status, error for all lectures.

## Note
1. Installing the app(bot 😂️) multiple times won't clog the crontab, don't worry about it 🤗️.
2. Your existing cron jobs will not be affected, even if you add new ones after installation
3. Keep your PC(bot) on at all times
4. If timetable changes, change the timetable, run `install.py` again.
5. Not tested on Windows.
6. Your email and password kept are as plain-text, i.e. unencrypted.

USE AT YOUR OWN RISK - Your teacher can be your best friend. Time is precious!

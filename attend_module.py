from crontab import CronTab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import time
from time import sleep
import sys, os, datetime, json, subprocess, shutil, stat

def install_files():
    # os.chdir(os.path.dirname(__file__))  # at the working directory
    destination = os.path.expanduser(
        "~") + '/.attend_lecture/'  # the destination
    if os.path.exists(destination) == True:  # if directory alread exists
        shutil.rmtree(destination)

    os.mkdir(destination)  # make the destination directory, if non-existent

    def copytree(src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    copytree(os.curdir, destination)  # all files copied to destination
    os.chdir(destination)  # at the destination
    if 'install_lecture_bot.py' in os.listdir(os.curdir):
        os.remove('install_lecture_bot.py')
    for file in os.listdir():
        os.chmod(file, stat.S_IRWXU)
    with open('attendance_log.txt', 'w') as log_file:
        log_file.write('Attendance Log Files\n')
        log_file.write('Status | TimeStamp | Problems(if any)\n')


def set_cron_job(time, command):
    pc_username = subprocess.Popen(
        "whoami", shell=True,
        stdout=subprocess.PIPE).stdout.read().decode("utf-8").rstrip("\n")
    with CronTab(user=pc_username) as cron:
        job = cron.new(command=command)
        job.hour.on(time[0][:2])
        job.minute.on(time[0][3:])
        job.dow.on(time[1])
    #auto write


def clean_timetable():
    pc_username = subprocess.Popen(
        "whoami", shell=True,
        stdout=subprocess.PIPE).stdout.read().decode("utf-8").rstrip("\n")
    with CronTab(user=pc_username) as cron:
        cron.remove(cron.find_command('attend_lecture.py'))


def set_timetable():
    with open('./config.json', 'r') as config:
        config = json.load(config)
        username = config['username']
        password = config['password']
        timetable = config['timetable']
        days_of_the_week = {
            'SUN': 0,
            'MON': 1,
            'TUE': 2,
            'WED': 3,
            'THU': 4,
            'FRI': 5,
            'SAT': 6
        }
        for day in timetable:  # day is 'MON', 'TUE' etc - a string
            for lecture in timetable[
                    day]:  # lecture is a dict { "start_time": "10:00", "duration": "60", "Subject link": "" },
                    if lecture['duration']!='0': # classes which are really happening
                        set_cron_job(
                            (lecture['start_time'], days_of_the_week[day]),
                            command=
                            "export DISPLAY=:0; {0}/.attend_lecture/attend_lecture.py {1} {2} {3} {4} >> {0}/attend_log.txt"
                            .format(os.path.expanduser('~'), username, password,
                                    lecture['Meet link'], lecture['duration']))


def uninstall_process():
    pc_username = subprocess.Popen(
        "whoami", shell=True,
        stdout=subprocess.PIPE).stdout.read().decode("utf-8").rstrip("\n")
    clean_timetable()
    destination = '/home/{}/.attend_lecture'.format(pc_username)
    if os.path.exists(destination):
        shutil.rmtree('/home/{}/.attend_lecture'.format(pc_username))
        print('Uninstall successful')
    else:
        print('Nothing to remove')

def attend_meet(username, password, meet_url, lecture_time):
    if '@' not in username or password == '' or meet_url == '': # just future proofing
        return False
    # open the browser - allow for camera and microphone ----------#
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.notifications": 1
        })
    sleep_time = 5

    browser = webdriver.Chrome(ChromeDriverManager().install(),
                               options=chrome_options)

    # login into your google account
    browser.get('https://accounts.google.com/login')
    sleep(sleep_time)
    username_input = browser.find_element_by_xpath('//*[@id="identifierId"]')
    username_input.send_keys(username)
    username_input.send_keys(Keys.ENTER)
    sleep(sleep_time)
    password_input = browser.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    sleep(sleep_time)
    # open the meet page ----------#
    browser.get(meet_url)
    sleep(sleep_time * 2)  # wait for meet page to load

    browser.find_element_by_css_selector(
        '#yDmH0d > c-wiz > div > div > div:nth-child(5) > div.crqnQb > div > div > div.vgJExf > div > div.KieQAe > div.oORaUb.NONs6c > div > div.EhAUAc > div.ZB88ed > div > div'
    ).click()  # mic clicked
    browser.find_element_by_css_selector(
        '#yDmH0d > c-wiz > div > div > div:nth-child(5) > div.crqnQb > div > div > div.vgJExf > div > div.KieQAe > div.oORaUb.NONs6c > div > div.EhAUAc > div.GOH7Zb > div > div'
    ).click()
    browser.find_element_by_css_selector(
        '.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()  # click join button

    sleep(int(lecture_time) * 60)  # lec time is in minutes
    browser.quit()  # close the browser - automatically ended the call
    return True


def log_attendance(value, cause='All OK'):
    destination = os.path.expanduser(
        "~") + '/.attend_lecture/'  # the destination
    os.chdir(destination)
    if value:
        value = 'Attended'
    else:
        value = 'Not Attended'
    with open('attendance_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime('"%d-%b-%Y %H:%M:%S"')
        log_file.write('{} | {} | {}\n'.format(value, timestamp, cause))

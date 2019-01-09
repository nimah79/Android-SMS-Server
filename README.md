# Android SMS Server
Simple Android SMS server, written in Python 3

### Installation and running:

There are 2 versions of the script:

**1. SL4A version:**
Install QPython (with Python3 interpreter) or 'Python3 for Android' + SL4A on your device.
Run `pip install flask_restful` in pip console.
Run the script.

**2. Termux version:** Install Termux on your device and 
Install QPython (with Python3 interpreter) or 'Python3 for Android' + SL4A on your device.
Run these commands in terminal:
```
$ pkg install python
$ pip install flask_restful
```
Run the script.

API URL: `http://your_local_ip_address:5000/sendSMS`
Request method should be POST.
Request arguments:
`phone`: the phone number you want to send SMS to
`text`: message text

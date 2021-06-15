# BTC-Fallout-Alarm

I have created a simple script to alarm you when prices of BitCoin has fallen to your choice via sending you a mail so you know it's the right time to buy it without having to check your phone every 30 minutes.
Alternatively, you can also use it to alarm you when Bitcoin's prices reaches to a peak-value where you were targetting to sell your BTCs.

## How to use the script

This code is written in **Python3.8.5**
There are some pre-requisites before running the script.
**Make sure you have the following Python packages installed in your system**
- Requests,
- BeautifulSoup,
- RegEx, and
- smtplib

If you want to install these packages, simply run:

```python
pip install <PACKAGE_NAME>
```

Once you have the following packages installed, you have to setup a few things before being able to send out mails.

There is a config.txt file in the folder. 
There are 3 empty fields in the file, namely _password_token, sender_mail & reciever_mail._

You can easily add your mail ID from which you want to send the mail in sender_mail and the mail ID to which you want to recieve the mail in receiever_mail.

**For adding the password token, there are few steps that have to be taken before being able to add the password**

_**if(2-Step-Verification enabled in your mail account):**_

Switch to a more secure app or device
Create & use App Passwords
If you use 2-Step-Verification and get a "password incorrect" error when you sign in, you can try to use an App Password.

- Go to your Google Account.
- Select Security.
- Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
    a) 2-Step Verification is not set up for your account.
    b) 2-Step Verification is only set up for security keys.
    c) Your account is through work, school, or other d) organization.
    d) You turned on Advanced Protection.
- At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
- Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
- Tap Done.
> Tip: Most of the time, you’ll only have to enter an App Password once per app or device, so don’t worry about memorizing it.

_**else:**_

- Go to [Less Secure App Access](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O-GUFRq2YIMVUlBddVpK3gKg9v-pX6QX_TwPnlFNqKiIEWKX0pKCfxNxgtNFWdjXgfmBVQdZ-Nnvy3GJS5IcHMsSRNYA).
- Create an access for using mail on your device.

Now, add the generated _password_ in the _password_token_ field

Now, we're ready to go!

Just run,

```
python3 scraper.py
```

And leave it running!

### Notes

- Change your desired lower limit of BTC rate via changing:

```python
   32. alarming_rate = 38000
```

to whatever you want.

- Change the interval of the time you want the script to fetch rate by changing:

```python
   63. time_interval = 1800
```

> You have to convert your desired time interval into seconds. I have set the starting interval to be of 1800s i.e. 1800/60 = 30 minutes.

- Your user agent may be different than mine. Check your user agent by simply typing "_my user agent_" in google.
If it's different than one in the code, replace the field by your user agent.

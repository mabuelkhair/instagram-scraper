# instagram-scraper
This is python3.6 script that download all photos of an instagram account

To download public account

run script with only one parameter the username of the account (the last part of instagram url)
```
python instagram_scraper.py 'account-username'
```

To download private account you need to pass your username and password as the second and third paramters

```
python instagram_scraper.py 'asser_yassin' 'username' 'password'
```

for example
https://www.instagram.com/mosalah
```
python instagram_scraper.py 'mosalah'
```


This script was mainly to learn and use selenium with python

Prerequisites

1- Firefox

2- Selenium

3- Geckodriver

To install selenium
```
pip install "selenium<4"
```
Installing Firefox and Geckodriver

Firefox is available as a download for Windows and macOS from https://www.mozilla.org/firefox/. On Linux, you probably already have it installed, but otherwise your package manager will have it.

Geckodriver is available from https://github.com/mozilla/geckodriver/releases. You need to download and extract it and put it somewhere on your system path.

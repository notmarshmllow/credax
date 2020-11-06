# CREDAX - FAST AI POWERED FUZZING TOOL with SLACK NOTIFICATIONS
Credax - Fast AI Powered Fuzzing Tool with Slack Notifications.

Credax is a lite-weight AI Powered Fuzzing Tool built in Python. Credax uses the least of your CPU by using more concurrent tasks and less threads, thus saving your OS Threads, providing you with better speed and results.

CREDAX auto removes all consecutive result that respond with same length, thus removing almost all consecutive false positives, providing better output + Slack Notifications. This feature is self activated as soon as Credax starts heating itself.

# 

# INSTALLATION

**Credax requires Python3.7 + to run. Please upgrade your Python version to 3.7 or higher to use Credax.**

1 .Clone the Credax reporitory.

`git clone https://github.com/notmarshmllow/credax.git`

2 .Install the Requirements

`pip install -r requirements.txt`

`python3 credax.py -h`

# EXAMPLE USAGE

Credax is lite-weight tool built for speed and effeciency. 
The following usage examples show the simplest task you can accomplish with `Credax`.
  
  
  ![alt text](https://github.com/notmarshmllow/credax/blob/main/credax.jpg?raw=True)
  
  
  
 # BASIC FUZZING
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt`
  
 # SEND NOTIFICATIONS TO SLACK
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt -s`
  
  # MATCHING STATUS CODES
   
  `python3 credax.py -d https://example.com/ -w wordlist.txt -c 200 401 403`
  
  # OUTPUT RESULTS TO A FILE
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt -o filename.txt`
  
  
  
  # SLACK NOTIFICATIONS
  
1. Create your own Slack App.
2. Go to api.slack.com
3. Select your App
4. Select `Add features and functionality` > `Incoming Webhooks`.
5. Below on the page you will find your `Slack Webhook URL`.
6. Copy and Paste you Slack Webhook URL in place of `_slack_webhook_url_here_` inside `slack_variables.py` file.


All developments to the tool are welcomed and highly appreciated !


**CREDAX - Developed by [@notmarshmllow](https://twitter.com/notmarshmllow)**:sparkles:


# CREDAX - FUZZING TOOL with SLACK NOTIFICATIONS
**CREDAX - WHEN THE HEAT IS ON, YOU GOTTA CALL THE FUZZ.**


Credax is a lite-weight Smart, efficient Fuzzing Tool built in Python.

CREDAX auto removes all consecutive result that respond with same length, thus removing almost all consecutive false positives, providing better output and also sends Notifications on Slack. 

![alt text](https://github.com/notmarshmllow/credax/blob/main/CREDAX.gif)

# INSTALLATION

**Credax requires Python3.7 + to run. Please upgrade your Python version to 3.7 or higher to use Credax.**

1. Clone the Credax reporitory.

`git clone https://github.com/notmarshmllow/credax.git`

2. Install the Requirements

`pip install -r requirements.txt`

`chmod +x credax.sh`

`python3 credax.py -h`

# EXAMPLE USAGE

The following usage examples show the simplest task you can accomplish with `Credax`.
  
  
  ![alt text](https://github.com/notmarshmllow/credax/blob/main/image_credax.png?raw=True)
  
  
  
 # BASIC USAGE
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt`
  
 # SEND NOTIFICATIONS TO SLACK
 Use `-s` switch to send notifications on your Slack wordspace. Add your slack webhook URL in **slack_variables.py** file.
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt -s`
  
![alt text](https://github.com/notmarshmllow/credax/blob/main/notification_slack.png)

  # MATCHING STATUS CODES
  Use `-c` switch to filter HTTP Status Code from response. This switch accepts one single Status Code only.
   
  `python3 credax.py -d https://example.com/ -w wordlist.txt -c 200`
  
  # OUTPUT RESULTS TO A FILE
  Write output to a file using `-o` switch.
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt -o filename.txt`
  
  # FUZZ LIST OF URLS
  
  Fuzz a list of URLs, store output in file and activate slack notifications with following command.
  
  `./credax.sh urllist wordlist`
  
  # POST REQUESTS
  
  Use `-POST` to send POST Requests. By default Credax sends GET Requests for Fuzzing.
  
  `python3 credax.py -d https://example.com/ -w wordlist.txt -POST`
  
  # BYPASSING 403 RESPONSES
 
 CREDAX by default tries to **bypass 403 Resopnse** using a list of custom Headers. Just run credax against a domain name and let CREDAX do all the work for you.
 Credax uses **127.0.0.1 IP Address** to bypass 403 response. 
 
 You can also set Custom IP Address, Host Address or Path to Bypass 403 Resposne using `-HOST` Switch. 
 
 `python3 -d https://google.com/ -w wordlists.txt -HOST 8.8.8.8`
 
 `python3 -d https://google.com/ -w wordlists.txt -HOST localhost`
 
 `python3 -d https://google.com/ -w wordlists.txt -HOST yourdomain.com`
 
 `python3 -d https://google.com/ -w wordlists.txt -HOST /admin`
 
 

 
 # COMMANDS
 
 COMMAND | DESCRIPTION | USAGE
 --------|-------------|-------
  -d | Target URL | -d https://example.com/ 
 -w | File containing list of words to FUZZ | -w wordlist.txt
 -c | Matching Custom Status Code (Accepts Single Status Code) | -c 200
 -s | Enable Slack Notofications | -s
 -o | Write output to a file | -o filename
 -POST | Send POST Request (Default GET) | -POST
 -HOST | Custom IP Address, Host Address or Path to Bypass 403 | -HOST 8.8.8.8 **or** -HOST yourdomain.com **or** -HOST /admin 
  
  
  
  # SLACK NOTIFICATIONS
  
1. Create your own Slack App.
2. Go to api.slack.com
3. Select your App
4. Select `Add features and functionality` > `Incoming Webhooks`.
5. Below on the page you will find your `Slack Webhook URL`.
6. Copy and Paste you Slack Webhook URL in place of `_slack_webhook_url_here_` inside `slack_variables.py` file.


All developments to the tool are welcomed and highly appreciated ! 

Please open an issue to keep track of bugs, enhancements, or other requests.





**CREDAX - Developed by [@notmarshmllow](https://twitter.com/notmarshmllow) & [@het_vikam](https://twitter.com/het_vikam)**:sparkles:

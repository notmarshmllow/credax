import argparse
import aiohttp
import asyncio
import json
import requests
from slack_variables import slack_webhook_url
from colorama import init
from termcolor import colored
from datetime import datetime

init()

print(colored("""\n

     _/_/_/  _/_/_/    _/_/_/_/  _/_/_/      _/_/    _/      _/   
  _/        _/    _/  _/        _/    _/  _/    _/    _/  _/      
 _/        _/_/_/    _/_/_/    _/    _/  _/_/_/_/      _/         
_/        _/    _/  _/        _/    _/  _/    _/    _/  _/        
 _/_/_/  _/    _/  _/_/_/_/  _/_/_/    _/    _/  _/      _/       
                                                        v1.0\n""", 'green'))

print(colored("""               When the heat is on, you gotta call the fuzz
                                 Developed by notmarshmllow

\n""", 'red'))



my_parser = argparse.ArgumentParser()
my_parser.add_argument('-d', type=str, required=True, help="Provide Target Name")
my_parser.add_argument('-o', required=False, help="Specify your Output File Name")
my_parser.add_argument('-w', required=True, help="Custom Wordlist")
my_parser.add_argument('-c', help="Match Custom Status Codes")
my_parser.add_argument('-s', required=False, action='count', help="Send notifications to slack.")
my_parser.add_argument('-POST', required=False, action="count", help="POST METHOD")
my_parser.add_argument('-HOST', required=False, default="127.0.0.1", help="Cutsom Address")


args = my_parser.parse_args()

base_url = args.d
base_url = str(base_url)

headers = {
    "X-Forwarded-For": "http://" + args.HOST,
    "X-Forwarded-For": args.HOST,
    "X-Originating-IP": args.HOST,
    "X-Forwarded-For": args.HOST,
    "X-Remote-IP": args.HOST,
    "X-Client-IP": args.HOST,
    "X-Host": args.HOST,
    "X-Forwared-Host": args.HOST,
    "X-Remote-Addr": args.HOST,
    "X-ProxyUser-Ip": args.HOST,
    }

if args.c:
    user_c = args.c
    user_c = int(user_c)

if args.HOST:
    ip11 = "IP ADDRESS/HOST : " + colored(args.HOST, 'red')
if args.POST:
    p11 = "METHOD : " + colored(" POST", 'red')
else:
    p11 = "METHOD : " + colored(" GET", 'red')
if args.s:
    s11 = "SLACK NOTIFICATION :" + colored(" ON", 'red')
else:
    s11 = "SLACK NOTIFICATION :" + colored(" OFF", 'red')
if args.c:
    c11 = "Matching Status Codes : " + colored(args.c, 'red')
else:
    c11 = "Matching Status Codes : " + colored(" 200 , 301, 302, 401, 403", 'red')
if args.o:
    o11 = "OUTPUT TO : " + colored(args.o, 'red')
else:
    o11 = "OUTPUT TO : " + colored(" NONE", 'red')
u11 = "URL : " + colored(base_url, 'red')
w11 = "Wordlist : " + colored(args.w, 'red')

print(f'{u11}  |  {w11}  |  {p11}  |  {s11}  |  {c11}   |  {ip11}  |  {o11}\n')


async def main():
    l1 = []
    num_words = 0

    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            with open(args.w, encoding='ISO-8859-1', errors='ignore') as filex:

                for line in filex:
                    l = []
                    word = line.strip()
                    word = str(word)
                    words = line.split()
                    num_words += len(words)

                    fuzz = base_url + word
                    l.append(fuzz)

                    if args.POST:

                        async with session.post(fuzz) as resp:
                            for i in range(num_words):
                                print("Total Requests : {}".format(i), end="\r")
                            status = resp.status
                            l.append(status)

                            result = await resp.text()
                            result = str(result)
                            size = len(result)
                            l.append(size)
                            l1.append(l)
                    else:
                        async with session.get(fuzz) as resp:

                            for i in range(num_words):
                                print("Total Requests : {}".format(i), end="\r")
                            status = resp.status
                            l.append(status)

                            result = await resp.text()
                            result = str(result)

                            size = len(result)
                            l.append(size)
                            l1.append(l)

        except:
            pass



        existing = []
        for lst in l1:
            if len(existing) > 0:
                if args.c:
                    for i in lst:
                        if i == user_c:
                            if lst[-1] != existing[-1]:
                                output_list = lst
                                output_list_to_string = str(output_list).replace("'", " ")
                                output_list_to_string1 = output_list_to_string.replace(",", " - ")
                                output_list_to_string2 = output_list_to_string1[1:-1]
                                print(output_list_to_string2)

                                if args.s:
                                    lst1 = str(lst)

                                    lst_slack1 = lst1.replace("'", "")
                                    lst_slack2 = lst_slack1.replace(",", " - ")
                                    lst_slack2 = lst_slack2[1:-1]
                                    slack_data = {'text': lst_slack2}
                                    response = requests.post(slack_webhook_url, data=json.dumps(slack_data))
                                    if response.status_code != 200:
                                        raise ValueError(
                                            'Request to slack returned an error %s, the response is:\n%s'
                                            % (response.status_code, response.text)
                                        )

                                    if args.o:
                                        file = open(args.o, 'a')
                                        file.write(output_list_to_string2 + '\n')


                else:
                    if lst[1] != 404:
                        if lst[-1] != existing[-1]:
                            output_list = lst
                            output_list_to_string = str(output_list).replace("'", " ")
                            output_list_to_string1 = output_list_to_string.replace(",", " - ")
                            output_list_to_string2 = output_list_to_string1[1:-1]
                            print(output_list_to_string2)

                            if args.s:
                                lst1 = str(lst)

                                lst_slack1 = lst1.replace("'", "")
                                lst_slack2 = lst_slack1.replace(",", " - ")
                                lst_slack2 = lst_slack2[1:-1]
                                slack_data = {'text': lst_slack2}
                                response = requests.post(slack_webhook_url, data=json.dumps(slack_data))
                                if response.status_code != 200:
                                    raise ValueError(
                                        'Request to slack returned an error %s, the response is:\n%s'
                                        % (response.status_code, response.text)
                                    )

                                if args.o:
                                    file = open(args.o, 'a')
                                    file.write(output_list_to_string2 + '\n')


 
            
            existing.append(lst[-1])

asyncio.get_event_loop().run_until_complete(main())

import argparse
import aiohttp
import asyncio
import json
import requests
from slack_variables import slack_webhook_url
import time



print("""\n

     _/_/_/  _/_/_/    _/_/_/_/  _/_/_/      _/_/    _/      _/   
  _/        _/    _/  _/        _/    _/  _/    _/    _/  _/      
 _/        _/_/_/    _/_/_/    _/    _/  _/_/_/_/      _/         
_/        _/    _/  _/        _/    _/  _/    _/    _/  _/        
 _/_/_/  _/    _/  _/_/_/_/  _/_/_/    _/    _/  _/      _/       
                                                        v1.0
               When the heat is on, you gotta call the fuzz
                                 Developed by notmarshmllow

\n""")



my_parser = argparse.ArgumentParser()
my_parser.add_argument('-d', type=str, required=True, help="Provide Target Name")
my_parser.add_argument('-o', required=False, help="Specify your Output File Name")
my_parser.add_argument('-w', required=True, help="Custom Wordlist")
my_parser.add_argument('-c', nargs='+', type=int , help="Match Custom Status Codes")
my_parser.add_argument('-s', required=False, action='count', help="Send notifications to slack.")


args = my_parser.parse_args()



base_url = args.d
base_url = str(base_url)


if args.c:
    user_c = tuple(args.c)



async def main():
    l1 = []
    num_words = 0
    num_respomnse = 0
    async with aiohttp.ClientSession() as session:
        try:
            with open(args.w, encoding='ISO-8859-1', errors='ignore') as filex:
                if args.s:
                    s11 = "SLACK NOTIFICATION : ON"
                else:
                    s11 = "SLACK NOTIFICATION : OFF"
                if args.c:
                    c11 = "Matching Status Codes : " + args.c
                else:
                    c11 = "Matching Status Codes : 200 , 301, 302, 401, 403"
                if args.o:
                    o11 = "OUTPUT TO : " + args.o
                else:
                    o11 = "OUTPUT TO : NONE "
                u11 = "URL : " + base_url
                w11 = "Wordlist : " + args.w

                print(f'{u11}  |  {w11}  |  {s11}  |  {c11}   |  {o11}')

                time.sleep(1)
                print("\nCredax is heating itself ...\n\n")


                for line in filex:
                    l = []
                    word = line.strip()
                    word = str(word)
                    words = line.split()
                    num_words += len(words)

                    fuzz = base_url + word
                    l.append(fuzz)

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
                    for i in user_c:
                        if i == lst[1]:
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

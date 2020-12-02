cat $1 | while read domain;do python3 credax.py -d $domain -w $2 -s -o $domain_credax.txt; don

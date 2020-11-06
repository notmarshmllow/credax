echo "RUNNING GAU TO FETCH URLs"

gau $1 > gau.txt | cat gau.txt | grep -aoP "(?<=(\"|\'|\`))\/[a-zA-Z0-9_?&=\/\-\#\.]*(?=(\"|\'|\`))" | sort -u > endpoints.txt;

echo "ENDPOINTS FETCHED SUCCESSFULLY."

echo "RUNNING SPRAWL TO CREATE A WORDLISTS."

while read word;do echo $word | ./sprawl/sprawl.py -s >> wordlists.txt;done

cat endpoints.txt wordlists.txt | sort -u > wordlist.txt

echo "WORDLIST CREATED SUCCESSFULLY."
sleep(2)
echo "RUNNING CREDAX ..."
sleep(1)
python3 credax.py -d $1 -w wordlists.txt -o $1_credax_results.txt -s

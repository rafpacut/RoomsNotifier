#!/bin/bash
difference=`python scrape.py`
mailAddress=`cat mailAddress.txt`
if [ $difference != '[]' ]; then
	echo $mailAddress > mail.txt
	echo $difference >> mail.txt
	sendmail -vt < mail.txt
else
	echo "no differences"
fi

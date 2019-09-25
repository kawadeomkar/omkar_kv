#!/bin/bash
curl -vvv -X PUT -d first_test localhost:9090/test_first

HELLO=hello
FIRST_TEST="$(curl -vvv -X GET localhost:9090/test_first)"

if [ -z FIRST_TEST ];
then
	echo "FIRST_TEST FAILED"
fi

 

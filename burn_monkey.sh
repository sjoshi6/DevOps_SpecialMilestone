#!/bin/bash

#Usage  burn_monkey 'name.pem' 'public ip of the machine'

scp -i /Users/saurabh/Downloads/$1 burn_cpu_script.sh ubuntu@$2:/home/ubuntu/
ssh -i /Users/saurabh/Downloads/$1 ubuntu@$2 './burn_cpu_script.sh'
exit

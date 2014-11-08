#!/bin/bash

VM_NAMES=`vagrant ssh-config | egrep "^Host flocker-.*$" | awk '{print $2}'`
HOSTS_FILE=flocker.hosts
rm -f $HOSTS_FILE ; touch $HOSTS_FILE

for VM_NAME in $VM_NAMES; do
  VM_IP=`vagrant ssh $VM_NAME -c "ip -4 address show enp0s8 | egrep -o 'inet [0-9\.]+'" | egrep -o 'inet [0-9\.]+' | awk '{print $2}'`
  echo "$VM_IP flocker.cluster" >> $HOSTS_FILE
done

HOST_ENTRIES=`cat $HOSTS_FILE`
for VM_NAME in $VM_NAMES; do
  vagrant ssh $VM_NAME -c "echo \"$HOST_ENTRIES\" | sudo tee -a /etc/hosts"
done

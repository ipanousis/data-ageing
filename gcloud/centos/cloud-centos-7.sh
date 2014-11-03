#!/bin/bash
yum update
yum install -y docker
sed -i 's/OPTIONS=\(.*\)/OPTIONS=\1 -H tcp:\/\/0.0.0.0:4243 -H unix:\/\/\/var\/run\/docker.sock/g' /etc/sysconfig/docker
service docker restart

# install zfs for flocker-node
yum localinstall -y --nogpgcheck https://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-2.noarch.rpm
yum localinstall -y --nogpgcheck http://archive.zfsonlinux.org/epel/zfs-release.el7.noarch.rpm
yum install -y kernel-devel zfs 

# install flocker-node
yum install -y git
git clone https://github.com/ClusterHQ/flocker
cd flocker


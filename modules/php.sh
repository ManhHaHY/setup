#!/bin/bash
rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm
rpm -Uvh http://mirror.webtatic.com/yum/el5/latest.rpm
yum install -y php55w* --skip-broken

echo "no" | pecl install mongo
pecl install redis
pecl install memcache
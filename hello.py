#!/usr/bin/env python
#########################################################################
# -*- coding: utf-8 -*-
# File Name: hello.py
# Author :kite
# QQ : 987324339
# Email:987324339@qq.com
# Created Time: Thu 29 Oct 2020 06:19:03 PM CST
#########################################################################
import re
import requests


def say():
    print("hello world\n")


def getResponse():
    response = requests.get('https://www.baidu.com').text
    print(response)


getResponse()

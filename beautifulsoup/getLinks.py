#!/usr/bin/env python
# coding=utf8
# -*- coding: utf-8 -*-
# @File  : getLinks.py
# @Author: ChENMo
# @Contact:pishit2009@gmail.com
# @Date  : 2017/10/19
# @Desc  :


from urllib.parse import  urlparse
import requests
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://"+urlparse(includeUrl).netloc
    internalLinks = []
    #找出所有以/开头的连接
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有外链的列表
def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    #找出所有以http或www开头且不包含当前url的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*%")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLinks(startingPage):
    r = requests.get(startingPage)
    bsObj = BeautifulSoup(r.text,"html.parser")
    externalLinks = getExternalLinks(bsObj,startingPage)
    if len(externalLinks) == 0:
        print("No external links,looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj,domain)
        internalLinks = getInternalLinks(bsObj,startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])

    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print("random external link is: "+externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")


# r = requests.get("http://oreilly.com")
# bsObj = BeautifulSoup(r.text,"html.parser")
# interlinks = getInternalLinks(bsObj,"http://oreilly.com")
# print(interlinks)
# r = requests.get("http://oreilly.com")
# bsObj = BeautifulSoup(r.text,"html.parser")
# externallinks = getExternalLinks(bsObj,"http://oreilly.com")
# print(externallinks)

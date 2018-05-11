#coding:utf-8
import requests 
import urllib3  
import time
import re

def url_read(url):
    try:
        return requests.get(url).text
    except:
        return -1

def get_number(matched):
    global pending_tx
    pending_tx = int(matched.group('value'))

def log(fname, content):
    f = open(fname, 'a+')
    f.write(content)
    f.close()

if __name__ == '__main__':
    pending_tx = 0;
    #pattern = re.compile(r'A total of (?P<value>\d+) Pending txns found')
    while(True):
        s = url_read('https://etherscan.io/txsPending')
        re.sub('A total of (?P<value>\d+) Pending txns found', get_number, s)
        f = time.strftime("%Y-%m-%d", time.localtime())
        print (time.time(), pending_tx)
        log(f, str(time.time()) + ' ' + str(pending_tx) + '\n')
        pending_tx = 0
        time.sleep(60)

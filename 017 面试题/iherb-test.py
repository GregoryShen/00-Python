#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialDomains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY lines as parameter.
#
import re

def getPotentialDomains(lines):
    # Write your code here
    res = []
    for line in lines:
        if "http://" or "https://" in line:
            web_link = re.findall(r'https?://[a-z0-9.-]+[.-a-z0-9/]?, line)
            if web_link:
                for item in weblink:
                    tmp = web_link.split('.')
                    if 'www' in tmp:
                        tmp.pop(tmp.index('www'))
                    elif 'ww2' in tmp:
                        tmp.pop(tmp.index('ww2'))
                    elif 'web' in tmp:
                        tmp.pop(tmp.index('web'))
                res.append(tmp)
    result = ';'.join(res)
    return result
    
if __name__ == '__main__':
    

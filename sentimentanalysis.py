#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:44:28 2020

@author: Jumana
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
#General idea: we want to first read the urls from the link, and for each url, just read out
#the ending of the url-- convert url to a string and then extract out endings
#of the url to get the name of the subreddit. We can then run beautiful soup on the
#subreddit to get more information and to do sentiment analysis.

#step 1: find list of college subreddits

url = 'https://raw.githubusercontent.com/karlding/college-subreddits/master/data/colleges.csv'
df = pd.read_csv(url, error_bad_lines=False)
df = df[['subreddit']]
                
df.to_csv('sb.csv', index=True)



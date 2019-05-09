import webbrowser
import urllib.request
import bs4 as bs
import os, sys, subprocess
from sensitiveInfo import *

def wolfram_answer(query):
    import wolframalpha
    client = wolframalpha.Client(APP_ID)
    res = client.query(query)
    return next(res.results).text

def wiki_answer(query, sentences=3):
    import wikipedia
    summary = wikipedia.summary(query, sentences)
    return summary

def google_q(query, link_index=0):
    url = str('http://google.com/search?q={}'.format(query))

    req = urllib.request.Request(url, data=None, headers={'User-Agent':'Mozilla'})
    src = urllib.request.urlopen(req)

    soup = bs.BeautifulSoup(src, 'html.parser')

    results = []

    for elem in soup.find_all('cite'):
    	link = elem.text
    	results.append(link)

    webbrowser.open(results[link_index])

def map_q(query):
    url = 'https://www.google.com/maps/place/{}'.format(query)
    webbrowser.open(url)

def open_s(item):
    if 'google' in item:
    	webbrowser.open('https://www.google.com')

    elif 'youtube' in item or 'yt' in item:
    	webbrowser.open('https://www.youtube.com')

    elif 'gmail' in item or 'mail' in item:
    	webbrowser.open('https://www.gmail.com')

    elif 'chrome' in item or 'google chrome' in item:
    	subprocess.call(CHROME_PATH)

    elif 'python' in item:
    	subprocess.call(PYTHON_PATH)

    elif 'notepad' in item:
    	subprocess.call(NOTEPAD_PATH)

    else:
    	if 'https://' not in item:
    		arg = 'https://' + item 
    	webbrowser.open(item)

def yt_q(query):
    url = str('https://www.youtube.com/results?search_query={}'.format(query))

    req = urllib.request.Request(url, data=None, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})
    src = urllib.request.urlopen(req)

    soup = bs.BeautifulSoup(src, 'html.parser')

    results = []

    a = soup.find_all("a", "about-channel-link ")

    for elem in a:
    	link = elem.get(href)
    	results.append(link)

    webbrowser.open(results[0])
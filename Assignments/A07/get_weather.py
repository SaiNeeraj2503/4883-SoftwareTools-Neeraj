"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time      
import requests
import PySimpleGUI as sg
import numpy as np

import gui# needed for the sleep function

from bs4 import BeautifulSoup                           # used to parse the HTML
                         # used to render the web page
#from seleniumwire import webdriver                      
   # Service is only needed for ChromeDriverManager
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
        #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
        #service = Service(executable_path='/usr/local/bin/chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') 
        options.add_argument('--log-level=3')
        
        #driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(3)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML
    
if __name__=='__main__':
    
    

    # Could be a good idea to use the buildWeatherURL function from gui.py
    url,filter = gui.buildWeatherURL()
    
    
    

    # get the page source HTML from the URL
    page = asyncGetWeather(url)
    
    
    
    

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    if filter=="daily":
        history = soup.find('lib-city-history-observation')
        thead=history.find_all('thead')
        tbody=history.find_all('tbody')
        headers=[]
        for hd in thead:
            ntr=hd.find_all('tr')
            for nntr in ntr:
                nth=nntr.find_all('th') 
                for nnth in nth:
                    headers.append(nnth.text)
               
        rows = history.find_all('tr')
        data_rows=[]
        g=[]
        for row in rows:
            cells = row.find_all('td')
            s=""
            data_row=[]
            for cell in cells:
                
                data_row.append(cell.text)
            data_rows.append(data_row) 
        print("*"*20)  
        print(data_rows)
        
        
        
    else:
        history = soup.find('lib-city-history-observation')
        thead=history.find_all('thead')
        tbody=history.find_all('tbody')
        headers=[]
        for hd in thead:
            ntr=hd.find_all('tr')
            for nntr in ntr:
                nth=nntr.find_all('td') 
                for nnth in nth:
                    headers.append(nnth.text)
                    
        print(headers)
        print(("#"*30))
        
        data=[]
        for tb in tbody:
            rows = tb.find_all('tr')
            data_rows1=[]
            for row in rows:
                cells = row.find_all('td')
                data_row2=[]
                for cell in cells:
                    table1=cell.find_all('table') 
                    rows1=[]
                    for r1 in table1:
                        r01=r1.find_all('tr')
                        c2=[]
                        for r02 in r01:
                            t1=r02.find_all('td')
                            c1=[]
                            for t2 in t1:
                                if t2.text!="":
                                    c1.append(t2.text)
                            if len(c1)!=0:
                                c2.append(c1)
                        if len(c2)!=0:
                            rows1.append(c2)
                    if len(rows1)!=0:
                        data_row2.append(rows1)
                if len(data_row2)!=0:
                    data_rows1.append(data_row2)
            if len(data_rows1)!=0:
                data.append(data_rows1)
        
    
        print("*"*20)  
        
        a=[]
        for i in data:
            for j in i:
                for z in j:
                    for f in z:
                        for m in f:
                            str=""
                            das="  "
                            for n in m:
                                str=str+das+n
                            a.append(str)
                        
        
        print(a)
        d=0
        if len(headers)!=0:
            d=int(len(a)/len(headers))
        data_rows=[]
        for j in range(0,d):
            h=[]
            while(j<len(a)):
                h.append(a[j])
                j=j+d
            data_rows.append(h)
        print("*"*20)
        print(data_rows)
    
    
    



    # Define the table layout
    layout = [
        [sg.Table(values=data_rows, headings=headers, justification='left', auto_size_columns=True)],
        [sg.Button('Close')]
    ]

    # Create the window
    window = sg.Window('Table for weather data', layout)

    # Event loop
    while True:
        event, values = window.read()

        # Close the window if the Close button is clicked or the window is closed
        if event == sg.WINDOW_CLOSED or event == 'Close' or event == 'Submit':
            break

    # Close the window
    window.close()
    
    

    
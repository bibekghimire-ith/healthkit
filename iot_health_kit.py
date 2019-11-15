# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:20:08 2018

@author: bibekghimire_ith
"""

""" *** IOT Health Kit Monitoring System *** """

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    t = requests.get('https://api.thingspeak.com/channels/630324/fields/1/last.txt')
    tempr = float(t.text)
    hb = requests.get('https://api.thingspeak.com/channels/630324/fields/2/last.txt')
    heart_beat = int(hb.text)
    return render_template('project_main.html', tempr=tempr, heart_beat=heart_beat)

if __name__ == '__main__':
    app.run(debug=True)

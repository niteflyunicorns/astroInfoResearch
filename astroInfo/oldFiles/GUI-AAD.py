from pymongo import MongoClient
from pprint import pprint
import pandas as pd
import statistics as stat
#import ruptures as rpt
import matplotlib.pyplot as plt
import numpy as np
import random as rand
import sys
import PySimpleGUI as gui
import guiModForMatrix as mtrx
import pdb

print("----------------------------------------------------------------")
print("                   Asteroid Anomaly Detection                   ")
print("----------------------------------------------------------------")

# THEME
# DarkBlue14
# DarkGrey3
# Black
# DarkPurple4

gui.theme('DarkGrey3')

def homeScreen():
    homeLayout = [
        [gui.Text('Asteroid Anomaly Detection', justification='center', size=(100, 1))],
        [gui.Text('Menu:', justification='center', size=(12, 1))],
        [gui.Button('Run AAD', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Analyze Specific Asteroid', size = (35))], #button_color = '#FA8072')],
        [gui.Button('Help', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Close AAD', size = (22))] #button_color = 'dark red')]
    ]
    
    window = gui.Window('Asteroid Anomaly Detection Program', homeLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    event, values = window.read()
    
    #Runs the ERM function if the 'Run ERM' button is pressed
    if event in (None, 'Run AAD'): 
        #mtrx.runProgram()
        #window = gui.Window('Analyze Asteroids', size = (520, 520), element_justification='c', grab_anywhere=True)).Layout(runAllLayout)
        window = runAllScreen()
        #runAll = gui.Window('Analyze Asteroids', runAllLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    
    #Closes WRAP if the 'Close WRAP' button is pressed
    if event in (None, 'Analyze Specific Asteroid'):
        window = runOneScreen()
        #runOne = gui.Window('Analyze One Asteroid', runOneLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
        #mtrx.viewOne()

    #Provides the user with the authors information if the 'Help' button is pressed
    if event in (None, 'Help'):
        print('\n')
        print('                     **print help message**                     ')
        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')
        print('\n')

    # window.close()


def runAllScreen():
    runAllLayout = [
        [gui.Text('Run AAD', justification='center', size=(100, 1))],
        [gui.Text('Number of Asteroids (-1 if all):', justification='center', size=(100, 1))],
        [gui.InputText(key = 'maxIn', size = (70, 3), justification='center')],
        [gui.Text('Where to start in data: (-1 if random):', justification='center', size=(100, 1))],
        [gui.InputText(key = 'offset', size = (70, 3), justification='center')],
        [gui.Text('Level of Filter Intensity (1=None, 2=Low, 3=Med, 4=High):', justification='center', size=(100, 1))],
        [gui.InputText(key = 'fltrLvl', size = (70, 3), justification='center')],
        [gui.Button('Run & Display', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Run & Export', size = (35))], #button_color = '#FA8072')],
        [gui.Button('Clear All', size = (22))],  #button_color = '#FA8072')],
        [gui.Button('Back', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Help', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Close AAD', size = (22))] #button_color = 'dark red')]
        ]
    window = gui.Window('Analyze Asteroids', runAllLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    event, values = window.read()
    
    #Runs the ERM function if the 'Run ERM' button is pressed
    if event in (None, 'Run & Display'): 
        #window = runAllScreen()
        mtrx.runProgram('maxIn', 'offset', 'N', '', '', 'fltrLvl')
        #print("Run & Display")

    #Closes WRAP if the 'Close WRAP' button is pressed
    if event in (None, 'Run & Export'):
        #window = runOneScreen()
        fileName = gui.popup_get_text('Filename:', 'filename without extension')
        fileType = gui.popup_get_text('Filetype', 'filetype: .html, .csv, etc.')
        mtrx.runProgram('maxIn', 'offset', 'Y', fileType, fileName, 'fltrLvl')
        print("Run & Export")

    if event in (None, 'Clear All'):
        runAllScreen()

    if event in (None, 'Back'):
        homeScreen()
        
    #Provides the user with the authors information if the 'Help' button is pressed
    if event in (None, 'Help'):
        print('\n')
        print('                     **print help message**                     ')
        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')
        print('\n')

    window.close()


def runOneScreen():
    runOneLayout = [
        [gui.Text('Asteroid Anomaly Detection', justification='center', size=(100, 1))],
        [gui.Text('Menu:', justification='center', size=(12, 1))],
        [gui.Button('Run AAD', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Analyze Specific Asteroid', size = (35))], #button_color = '#FA8072')],
        [gui.Button('Run AAD', size = (22))],  #button_color = '#FA8072')],
        [gui.Button('Run AAD', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Help', size = (22))], #button_color = '#FA8072')],
        [gui.Button('Close AAD', size = (22))] #button_color = 'dark red')]
        ]
    window = gui.Window('Analyze One Asteroid', runOneLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    return window

#Makes the windows in the layout from above
#window = gui.Window('AAD', homeLayout, size = (520, 520), element_justification='c', grab_anywhere=True)

#while True:
    #Opens the window
    #window = homeScreen()

    # #Runs the ERM function if the 'Run ERM' button is pressed
    # if event in (None, 'Run AAD'): 
    #     #mtrx.runProgram()
    #     #window = gui.Window('Analyze Asteroids', size = (520, 520), element_justification='c', grab_anywhere=True)).Layout(runAllLayout)
    #     window = runAllScreen()
    #     #runAll = gui.Window('Analyze Asteroids', runAllLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    #     pass


    # #Closes WRAP if the 'Close WRAP' button is pressed
    # if event in (None, 'Analyze Specific Asteroid'):
    #     window = runOneScreen()
    #     #runOne = gui.Window('Analyze One Asteroid', runOneLayout, size = (520, 520), element_justification='c', grab_anywhere=True)
    #     #mtrx.viewOne()

    # #Provides the user with the authors information if the 'Help' button is pressed
    # if event in (None, 'Help'):
    #     print('\n')
    #     print('                     **print help message**                     ')
    #     print('----------------------------------------------------------------')
    #     print('----------------------------------------------------------------')
    #     print('\n')

#window.close()

def main():
    homeScreen()

main()

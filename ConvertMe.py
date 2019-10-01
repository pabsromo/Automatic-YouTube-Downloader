# Pablo Romo
# This is meant to be a graphic tool that implements the YouTube downloader
# I made earlier.

# This is only meant to help me learn python, please buy your music
# or buy a subscription like Spotify and support the artists!

# Using kivy for the UIX.
# Link for resources here: https://likegeeks.com/kivy-tutorial/#Kivy-vs-PyQt

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os
from os import listdir
from os.path import isfile, join
import eyed3
import csv
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

class StartPage(GridLayout):
    

class MainApp(App):

    def build(self):
        self.screen_manager = ScreenManager()

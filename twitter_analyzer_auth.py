#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:12:06 2020

@author: muqrizdevice
"""
import tweepy

api_key = ##your_api_key##
api_secret = ##your_api_secret##

access_token = ##your_access_token##
access_token_secret = ##access_token_secret##

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


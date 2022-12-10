#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:11:22 2022

@author: nicolas
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/home/nicolas/bin/chromedriver"

df = gs.get_jobs("data scientist", 15, False, path, 9)


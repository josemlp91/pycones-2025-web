# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath("config"))


from config.pelicanconf_common import *
from config.pelicanconf_event import *
from config.pelicanconf_flags import *

SITEURL = os.getenv("SITEURL")
GOOGLE_ANALYTICS_CODE = os.getenv("GOOGLE_ANALYTICS_CODE", "0000")

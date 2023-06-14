from datetime import datetime, date, timedelta

from django.conf import settings
import os
from os import remove
from urllib.parse import urlparse, parse_qs
from django.core.paginator import Paginator
from django.template import Context, Template
#token
import jwt
import time
#email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def numberFormat(numero):
    if numero == None:
        return 0
    else:
        return "{:,}".format(numero).replace(",",".")
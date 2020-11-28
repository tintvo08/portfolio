import requests
import os

from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()


def home(request):
    upcoming = _get_upcoming()
    earnings = upcoming['earnings']
    phases = upcoming['phases']
    return render(request, 'jobs/home.html', {'earnings': earnings})


def _get_upcoming():
    headers = {'api-key': os.getenv("TRADE_API_KEY")}
    resp = requests.get('https://t-trade-api.herokuapp.com/t_trade/upcoming', headers=headers)
    data = resp.json()
    return data





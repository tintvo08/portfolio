import requests
import os

from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()


def home(request):
    return render(request, 'jobs/home.html')


def earnings(request):
    upcoming = _get_upcoming()
    earnings = upcoming['earnings']
    return render(request, 'jobs/earnings.html', {'earnings': earnings})


def phases(request):
    upcoming = _get_upcoming()
    phases = upcoming['phases']
    return render(request, 'jobs/phases.html', {'phases': phases})


def aboutme(request):
    return render(request, 'jobs/aboutme.html')


def _get_upcoming():
    headers = {'api-key': os.getenv("TRADE_API_KEY")}
    resp = requests.get('https://t-trade-api.herokuapp.com/t_trade/upcoming', headers=headers)
    data = resp.json()
    return data





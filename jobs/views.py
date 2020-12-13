import requests
import os

from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()


def home(request):
    return render(request, 'jobs/home.html')


def earnings(request):
    upcoming = _get_upcoming()
    stock_earnings = upcoming['earnings']
    return render(request, 'jobs/earnings.html', {'earnings': stock_earnings})


def phases(request):
    upcoming = _get_upcoming()
    pharm_phases = upcoming['phases']
    return render(request, 'jobs/phases.html', {'phases': pharm_phases})


def search(request):
    key = {'key': os.getenv("TRADE_API_KEY")}
    return render(request, 'jobs/search.html', {'key': key})


def aboutme(request):
    return render(request, 'jobs/aboutme.html')


def _get_upcoming():
    headers = {'api-key': os.getenv("TRADE_API_KEY")}
    resp = requests.get('https://t-trade-api.herokuapp.com/t_trade/upcoming', headers=headers)
    data = resp.json()
    return data



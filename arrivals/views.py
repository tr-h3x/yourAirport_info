import json
from datetime import date, timedelta

import requests
from django.conf import settings
from django.shortcuts import render

AEROAPI_KEY = getattr(settings, "AEROAPI_KEY", None)
AEROAPI = requests.Session()
AEROAPI.headers.update({"x-apikey": AEROAPI_KEY})


def index(request):
    return render(request, "home.html")


def arrivals(request):
    if request.method == "POST":
        airport = request.POST["airport"]
        today = date.today()
        yesterday = today - timedelta(1)
        tomorrow = today + timedelta(1)
        results = AEROAPI.get(
            f"https://aeroapi.flightaware.com/aeroapi/airports/{airport}/flights/arrivals?start={today}&end={tomorrow}&max_pages=10"
        )

        schedule = results.json()
        # schedule = json.load(results)
        arrivals = schedule["arrivals"]

        context = {
            "arrivals": arrivals,
            "airport": airport,
        }

        print(arrivals)
    else:
        context = {}
    return render(request, "arrivals.html", context)

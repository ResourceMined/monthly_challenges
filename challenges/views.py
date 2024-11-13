from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes each day",
    "march": "learn django for 20 minutes a day",
    "april": "Challenge04",
    "may": "Challenge05",
    "june": "Challenge06",
    "july": "Challenge07",
    "august": "Challenge08",
    "september": "Challenge09",
    "october": "Challenge10",
    "november": "Challenge11",
    "december": None,
}
# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month - 1]
    # /challenge/ avoids having to fixe (name fixes)
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
            
        })
    except:
        return HttpResponseNotFound("<h1>this month is not supported</h1>")

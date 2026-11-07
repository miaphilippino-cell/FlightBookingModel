from flask import Flask, render_template, request, redirect, url_for, session # type: ignore
import random
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "flight-booking-secret-key"


# -----------------------------
# Airport Data
# -----------------------------

airports = {
    "ATL": "Atlanta, GA",
    "BOS": "Boston, MA",
    "DEN": "Denver, CO",
    "DFW": "Dallas, TX",
    "JFK": "New York, NY",
    "LAX": "Los Angeles, CA",
    "MCO": "Orlando, FL",
    "MIA": "Miami, FL",
    "ORD": "Chicago, IL",
    "SEA": "Seattle, WA",
    "SFO": "San Francisco, CA",
}


# -----------------------------
# Airlines
# -----------------------------

airlines = [
    {
        "name": "American Airlines",
        "code": "AA",
        "price": 250
    },
    {
        "name": "Delta",
        "code": "DL",
        "price": 280
    },
    {
        "name": "United",
        "code": "UA",
        "price": 260
    },
    {
        "name": "JetBlue",
        "code": "B6",
        "price": 230
    }
]


# -----------------------------
# Home Page
# -----------------------------

@app.route("/")
def index():

    return render_template(
        "index.html",
        airports=airports
    )


# -----------------------------
# Flight Search
# -----------------------------

@app.route("/search", methods=["POST"])
def search():

    origin = request.form["origin"]
    destination = request.form["destination"]
    date = request.form["date"]

    session["origin"] = origin
    session["destination"] = destination
    session["date"] = date


    flights = []

    for airline in airlines:

        flights.append({
            "airline": airline["name"],
            "flight": airline["code"] + str(random.randint(100,999)),
            "price": airline["price"],
            "departure": "8:30 AM",
            "arrival": "11:45 AM"
        })


    session["flights"] = flights


    return render_template(
        "search.html",
        flights=flights
    )


# -----------------------------
# Select Flight
# -----------------------------

@app.route("/select_flight/<flight>")
def select_flight(flight):

    session["flight"] = flight

    return redirect(
        url_for("passenger")
    )


# -----------------------------
# Passenger Page
# -----------------------------

@app.route("/passenger", methods=["GET","POST"])
def passenger():

    if request.method == "POST":

        session["name"] = request.form["name"]
        session["email"] = request.form["email"]
        session["phone"] = request.form["phone"]

        return redirect(
            url_for("seat_selection")
        )


    return render_template(
        "passenger.html"
    )


# -----------------------------
# Seat Selection
# -----------------------------

@app.route("/seats", methods=["GET","POST"])
def seat_selection():

    if request.method == "POST":

        session["seat"] = request.form["seat"]

        return redirect(
            url_for("payment")
        )


    return render_template(
        "seat_selection.html"
    )


# -----------------------------
# Payment
# -----------------------------

@app.route("/payment", methods=["GET","POST"])
def payment():

    if request.method == "POST":

        session["payment"] = request.form["payment"]

        session["booking_id"] = (
            "BK" + str(random.randint(10000,99999))
        )


        return redirect(
            url_for("confirmation")
        )


    return render_template(
        "payment.html"
    )


# -----------------------------
# Confirmation
# -----------------------------

@app.route("/confirmation")
def confirmation():

    return render_template(
        "confirmation.html",
        booking=session
    )



if __name__ == "__main__":

    app.run(debug=True)
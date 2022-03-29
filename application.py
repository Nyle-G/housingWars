import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///house.db")


@app.route("/")
@login_required
def index():
    #Adams:

    adamsTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Adams'")[0]['COUNT(rankID)']

    if adamsTotal > 0:
        adamsSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Adams'")[0]['SUM(spaciousness)']
        adamsConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Adams'")[0]['SUM(convenience)']
        adamsAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Adams'")[0]['SUM(amenities)']
        adamsClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Adams'")[0]['SUM(cleanliness)']
        adamsCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Adams'")[0]['SUM(community)']
        adamsDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Adams'")[0]['SUM(diningHall)']

        adamsSpaceAvg = round(adamsSpace / adamsTotal, 2)
        adamsConvAvg = round(adamsConv / adamsTotal, 2)
        adamsAmenAvg = round(adamsAmen / adamsTotal, 2)
        adamsCleanAvg = round(adamsClean / adamsTotal, 2)
        adamsComAvg = round(adamsCom / adamsTotal, 2)
        adamsDHallAvg = round(adamsDHall / adamsTotal, 2)

        adamsOverall = round((adamsSpaceAvg + adamsConvAvg + adamsAmenAvg + adamsCleanAvg + adamsComAvg + adamsDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Adams'", adamsOverall, adamsSpaceAvg, adamsConvAvg, adamsAmenAvg, adamsCleanAvg, adamsComAvg, adamsDHallAvg)

    #Cabot:

    cabotTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Cabot'")[0]['COUNT(rankID)']

    if cabotTotal > 0:
        cabotSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Cabot'")[0]['SUM(spaciousness)']
        cabotConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Cabot'")[0]['SUM(convenience)']
        cabotAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Cabot'")[0]['SUM(amenities)']
        cabotClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Cabot'")[0]['SUM(cleanliness)']
        cabotCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Cabot'")[0]['SUM(community)']
        cabotDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Cabot'")[0]['SUM(diningHall)']

        cabotSpaceAvg = round(cabotSpace / cabotTotal, 2)
        cabotConvAvg = round(cabotConv / cabotTotal, 2)
        cabotAmenAvg = round(cabotAmen / cabotTotal, 2)
        cabotCleanAvg = round(cabotClean / cabotTotal, 2)
        cabotComAvg = round(cabotCom / cabotTotal, 2)
        cabotDHallAvg = round(cabotDHall / cabotTotal, 2)

        cabotOverall = round((cabotSpaceAvg + cabotConvAvg + cabotAmenAvg + cabotCleanAvg + cabotComAvg + cabotDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Cabot'", cabotOverall, cabotSpaceAvg, cabotConvAvg, cabotAmenAvg, cabotCleanAvg, cabotComAvg, cabotDHallAvg)

    #Currier:

    currierTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Currier'")[0]['COUNT(rankID)']

    if currierTotal > 0:
        currierSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Currier'")[0]['SUM(spaciousness)']
        currierConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Currier'")[0]['SUM(convenience)']
        currierAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Currier'")[0]['SUM(amenities)']
        currierClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Currier'")[0]['SUM(cleanliness)']
        currierCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Currier'")[0]['SUM(community)']
        currierDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Currier'")[0]['SUM(diningHall)']

        currierSpaceAvg = round(currierSpace / currierTotal, 2)
        currierConvAvg = round(currierConv / currierTotal, 2)
        currierAmenAvg = round(currierAmen / currierTotal, 2)
        currierCleanAvg = round(currierClean / currierTotal, 2)
        currierComAvg = round(currierCom / currierTotal, 2)
        currierDHallAvg = round(currierDHall / currierTotal, 2)

        currierOverall = round((currierSpaceAvg + currierConvAvg + currierAmenAvg + currierCleanAvg + currierComAvg + currierDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Currier'", currierOverall, currierSpaceAvg, currierConvAvg, currierAmenAvg, currierCleanAvg, currierComAvg, currierDHallAvg)    #Duster:

    dunsterTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Dunster'")[0]['COUNT(rankID)']

    if dunsterTotal > 0:
        dunsterSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Dunster'")[0]['SUM(spaciousness)']
        dunsterConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Dunster'")[0]['SUM(convenience)']
        dunsterAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Dunster'")[0]['SUM(amenities)']
        dunsterClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Dunster'")[0]['SUM(cleanliness)']
        dunsterCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Dunster'")[0]['SUM(community)']
        dunsterDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Dunster'")[0]['SUM(diningHall)']

        dunsterSpaceAvg = round(dunsterSpace / dunsterTotal, 2)
        dunsterConvAvg = round(dunsterConv / dunsterTotal, 2)
        dunsterAmenAvg = round(dunsterAmen / dunsterTotal, 2)
        dunsterCleanAvg = round(dunsterClean / dunsterTotal, 2)
        dunsterComAvg = round(dunsterCom / dunsterTotal, 2)
        dunsterDHallAvg = round(dunsterDHall / dunsterTotal, 2)

        dunsterOverall = round((dunsterSpaceAvg + dunsterConvAvg + dunsterAmenAvg + dunsterCleanAvg + dunsterComAvg + dunsterDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Dunster'", dunsterOverall, dunsterSpaceAvg, dunsterConvAvg, dunsterAmenAvg, dunsterCleanAvg, dunsterComAvg, dunsterDHallAvg)
    #Eliot:

    eliotTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Eliot'")[0]['COUNT(rankID)']

    if eliotTotal > 0:
        eliotSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Eliot'")[0]['SUM(spaciousness)']
        eliotConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Eliot'")[0]['SUM(convenience)']
        eliotAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Eliot'")[0]['SUM(amenities)']
        eliotClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Eliot'")[0]['SUM(cleanliness)']
        eliotCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Eliot'")[0]['SUM(community)']
        eliotDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Eliot'")[0]['SUM(diningHall)']

        eliotSpaceAvg = round(eliotSpace / eliotTotal, 2)
        eliotConvAvg = round(eliotConv / eliotTotal, 2)
        eliotAmenAvg = round(eliotAmen / eliotTotal, 2)
        eliotCleanAvg = round(eliotClean / eliotTotal, 2)
        eliotComAvg = round(eliotCom / eliotTotal, 2)
        eliotDHallAvg = round(eliotDHall / eliotTotal, 2)

        eliotOverall = round((eliotSpaceAvg + eliotConvAvg + eliotAmenAvg + eliotCleanAvg + eliotComAvg + eliotDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Eliot'", eliotOverall, eliotSpaceAvg, eliotConvAvg, eliotAmenAvg, eliotCleanAvg, eliotComAvg, eliotDHallAvg)
    #Kirkland:

    kirklandTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Kirkland'")[0]['COUNT(rankID)']

    if kirklandTotal > 0:
        kirklandSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(spaciousness)']
        kirklandConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(convenience)']
        kirklandAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(amenities)']
        kirklandClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(cleanliness)']
        kirklandCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(community)']
        kirklandDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Kirkland'")[0]['SUM(diningHall)']

        kirklandSpaceAvg = round(kirklandSpace / kirklandTotal, 2)
        kirklandConvAvg = round(kirklandConv / kirklandTotal, 2)
        kirklandAmenAvg = round(kirklandAmen / kirklandTotal, 2)
        kirklandCleanAvg = round(kirklandClean / kirklandTotal, 2)
        kirklandComAvg = round(kirklandCom / kirklandTotal, 2)
        kirklandDHallAvg = round(kirklandDHall / kirklandTotal, 2)

        kirklandOverall = round((kirklandSpaceAvg + kirklandConvAvg + kirklandAmenAvg + kirklandCleanAvg + kirklandComAvg + kirklandDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Kirkland'", kirklandOverall, kirklandSpaceAvg, kirklandConvAvg, kirklandAmenAvg, kirklandCleanAvg, kirklandComAvg, kirklandDHallAvg)
    #Leverett:
    leverettTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Leverett'")[0]['COUNT(rankID)']

    if leverettTotal > 0:

        leverettSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Leverett'")[0]['SUM(spaciousness)']
        leverettConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Leverett'")[0]['SUM(convenience)']
        leverettAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Leverett'")[0]['SUM(amenities)']
        leverettClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Leverett'")[0]['SUM(cleanliness)']
        leverettCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Leverett'")[0]['SUM(community)']
        leverettDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Leverett'")[0]['SUM(diningHall)']

        leverettSpaceAvg = round(leverettSpace / leverettTotal, 2)
        leverettConvAvg = round(leverettConv / leverettTotal, 2)
        leverettAmenAvg = round(leverettAmen / leverettTotal, 2)
        leverettCleanAvg = round(leverettClean / leverettTotal, 2)
        leverettComAvg = round(leverettCom / leverettTotal, 2)
        leverettDHallAvg = round(leverettDHall / leverettTotal, 2)

        leverettOverall = round((leverettSpaceAvg + leverettConvAvg + leverettAmenAvg + leverettCleanAvg + leverettComAvg + leverettDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Leverett'", leverettOverall, leverettSpaceAvg, leverettConvAvg, leverettAmenAvg, leverettCleanAvg, leverettComAvg, leverettDHallAvg)
    #Lowell:
    lowellTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Lowell'")[0]['COUNT(rankID)']

    if lowellTotal > 0:
        lowellSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Lowell'")[0]['SUM(spaciousness)']
        lowellConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Lowell'")[0]['SUM(convenience)']
        lowellAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Lowell'")[0]['SUM(amenities)']
        lowellClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Lowell'")[0]['SUM(cleanliness)']
        lowellCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Lowell'")[0]['SUM(community)']
        lowellDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Lowell'")[0]['SUM(diningHall)']

        lowellSpaceAvg = round(lowellSpace / lowellTotal, 2)
        lowellConvAvg = round(lowellConv / lowellTotal, 2)
        lowellAmenAvg = round(lowellAmen / lowellTotal, 2)
        lowellCleanAvg = round(lowellClean / lowellTotal, 2)
        lowellComAvg = round(lowellCom / lowellTotal, 2)
        lowellDHallAvg = round(lowellDHall / lowellTotal, 2)

        lowellOverall = round((lowellSpaceAvg + lowellConvAvg + lowellAmenAvg + lowellCleanAvg + lowellComAvg + lowellDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Lowell'", lowellOverall, lowellSpaceAvg, lowellConvAvg, lowellAmenAvg, lowellCleanAvg, lowellComAvg, lowellDHallAvg)

    #Mather:
    matherTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Mather'")[0]['COUNT(rankID)']

    if matherTotal > 0:
        matherSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Mather'")[0]['SUM(spaciousness)']
        matherConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Mather'")[0]['SUM(convenience)']
        matherAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Mather'")[0]['SUM(amenities)']
        matherClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Mather'")[0]['SUM(cleanliness)']
        matherCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Mather'")[0]['SUM(community)']
        matherDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Mather'")[0]['SUM(diningHall)']

        matherSpaceAvg = round(matherSpace / matherTotal, 2)
        matherConvAvg = round(matherConv / matherTotal, 2)
        matherAmenAvg = round(matherAmen / matherTotal, 2)
        matherCleanAvg = round(matherClean / matherTotal, 2)
        matherComAvg = round(matherCom / matherTotal, 2)
        matherDHallAvg = round(matherDHall / matherTotal, 2)

        matherOverall = round((matherSpaceAvg + matherConvAvg + matherAmenAvg + matherCleanAvg + matherComAvg + matherDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Mather'", matherOverall, matherSpaceAvg, matherConvAvg, matherAmenAvg, matherCleanAvg, matherComAvg, matherDHallAvg)

    #Pforzheimer
    pforzheimerTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Pforzheimer'")[0]['COUNT(rankID)']

    if pforzheimerTotal > 0:
        pforzheimerSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(spaciousness)']
        pforzheimerConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(convenience)']
        pforzheimerAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(amenities)']
        pforzheimerClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(cleanliness)']
        pforzheimerCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(community)']
        pforzheimerDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Pforzheimer'")[0]['SUM(diningHall)']

        pforzheimerSpaceAvg = round(pforzheimerSpace / pforzheimerTotal, 2)
        pforzheimerConvAvg = round(pforzheimerConv / pforzheimerTotal, 2)
        pforzheimerAmenAvg = round(pforzheimerAmen / pforzheimerTotal, 2)
        pforzheimerCleanAvg = round(pforzheimerClean / pforzheimerTotal, 2)
        pforzheimerComAvg = round(pforzheimerCom / pforzheimerTotal, 2)
        pforzheimerDHallAvg = round(pforzheimerDHall / pforzheimerTotal, 2)

        pforzheimerOverall = round((pforzheimerSpaceAvg + pforzheimerConvAvg + pforzheimerAmenAvg + pforzheimerCleanAvg + pforzheimerComAvg + pforzheimerDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Pforzheimer'", pforzheimerOverall, pforzheimerSpaceAvg, pforzheimerConvAvg, pforzheimerAmenAvg, pforzheimerCleanAvg, pforzheimerComAvg, pforzheimerDHallAvg)

    #Quincy:
    quincyTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Quincy'")[0]['COUNT(rankID)']

    if quincyTotal > 0:
        quincySpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Quincy'")[0]['SUM(spaciousness)']
        quincyConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Quincy'")[0]['SUM(convenience)']
        quincyAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Quincy'")[0]['SUM(amenities)']
        quincyClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Quincy'")[0]['SUM(cleanliness)']
        quincyCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Quincy'")[0]['SUM(community)']
        quincyDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Quincy'")[0]['SUM(diningHall)']

        quincySpaceAvg = round(quincySpace / quincyTotal, 2)
        quincyConvAvg = round(quincyConv / quincyTotal, 2)
        quincyAmenAvg = round(quincyAmen / quincyTotal, 2)
        quincyCleanAvg = round(quincyClean / quincyTotal, 2)
        quincyComAvg = round(quincyCom / quincyTotal, 2)
        quincyDHallAvg = round(quincyDHall / quincyTotal, 2)

        quincyOverall = round((quincySpaceAvg + quincyConvAvg + quincyAmenAvg + quincyCleanAvg + quincyComAvg + quincyDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Quincy'", quincyOverall, quincySpaceAvg, quincyConvAvg, quincyAmenAvg, quincyCleanAvg, quincyComAvg, quincyDHallAvg)

    #Winthrop:
    winthropTotal = db.execute("SELECT COUNT(rankID) FROM ranks WHERE house = 'Winthrop'")[0]['COUNT(rankID)']

    if winthropTotal > 0:
        winthropSpace = db.execute("SELECT SUM(spaciousness) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(spaciousness)']
        winthropConv = db.execute("SELECT SUM(convenience) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(convenience)']
        winthropAmen = db.execute("SELECT SUM(amenities) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(amenities)']
        winthropClean = db.execute("SELECT SUM(cleanliness) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(cleanliness)']
        winthropCom = db.execute("SELECT SUM(community) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(community)']
        winthropDHall = db.execute("SELECT SUM(diningHall) FROM ranks WHERE house = 'Winthrop'")[0]['SUM(diningHall)']

        winthropSpaceAvg = round(winthropSpace / winthropTotal, 2)
        winthropConvAvg = round(winthropConv / winthropTotal, 2)
        winthropAmenAvg = round(winthropAmen / winthropTotal, 2)
        winthropCleanAvg = round(winthropClean / winthropTotal, 2)
        winthropComAvg = round(winthropCom / winthropTotal, 2)
        winthropDHallAvg = round(winthropDHall / winthropTotal, 2)

        winthropOverall = round((winthropSpaceAvg + winthropConvAvg + winthropAmenAvg + winthropCleanAvg + winthropComAvg + winthropDHallAvg) / 6, 2)

        db.execute("UPDATE rankings SET overall=?, spaciousness=?, convenience=?, amenities=?, cleanliness=?, community=?, dHall=? WHERE house='Winthrop'", winthropOverall, winthropSpaceAvg, winthropConvAvg, winthropAmenAvg, winthropCleanAvg, winthropComAvg, winthropDHallAvg)

    rankings = db.execute("SELECT * FROM rankings ORDER BY overall DESC")

    return render_template("index.html", rankings=rankings)


@app.route("/rank", methods=["GET", "POST"])
@login_required
def rank():
    if request.method == "POST":
        house = request.form.get("house")
        spaciousness = request.form.get("spaciousness")
        convenience = request.form.get("convenience")
        amenities = request.form.get("amenities")
        cleanliness = request.form.get("cleanliness")
        community = request.form.get("community")
        diningHall = request.form.get("diningHall")
        db.execute("INSERT INTO ranks (house, spaciousness, convenience, amenities, cleanliness, community, diningHall) VALUES (?, ?, ?, ?, ?, ?, ?)", house, spaciousness, convenience, amenities, cleanliness, community, diningHall)
        return index()
    else:
        return render_template("rank.html")

@app.route("/houseBios", methods=["GET"])
@login_required
def houseBios():
    return render_template("houseBios.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensures username doesn't already exist
        if len(rows) == 1:
            return apology("username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confirmation", 400)

        # Ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, password)

        return redirect("/")

    else:
        return render_template("register.html")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

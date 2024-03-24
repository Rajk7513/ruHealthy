from flask import Flask

from Campus.Busch.dining_hall.dh_breakfast import get_busch_dh_breakfast_items
from Campus.Busch.dining_hall.dh_lunch import get_busch_dh_lunch_items
from Campus.Busch.dining_hall.dh_dinner import get_busch_dh_dinner_items

from Campus.College_Ave.Atrium.atrium_breakfast import get_atrium_breakfast_items
from Campus.College_Ave.Atrium.atrium_lunch import get_atrium_lunch_items
from Campus.College_Ave.Atrium.atrium_dinner import get_atrium_dinner_items

from Campus.Livingston.dining_hall.dh_breakfast import get_livi_breakfast_items
from Campus.Livingston.dining_hall.dh_lunch import get_livi_lunch_items
from Campus.Livingston.dining_hall.dh_dinner import get_livi_dinner_items


app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello World! Server is active"

if(__name__ == "__main__"):
    app.run(debug=True)
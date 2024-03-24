import datetime
from flask import Flask

from Campus.Busch.dining_hall.dh_breakfast import get_busch_dh_breakfast_items
from Campus.Busch.dining_hall.dh_lunch import get_busch_dh_lunch_items
from Campus.Busch.dining_hall.dh_dinner import get_busch_dh_dinner_items

from Campus.College_Ave.Atrium.atrium_breakfast import get_atrium_breakfast_items
from Campus.College_Ave.Atrium.atrium_lunch import get_atrium_lunch_items
from Campus.College_Ave.Atrium.atrium_dinner import get_atrium_dinner_items

from Campus.Cook.neilson_dining_hall.neilson_breakfast import get_cd_breakfast_items
from Campus.Cook.neilson_dining_hall.neilson_lunch import get_cd_lunch_items
from Campus.Cook.neilson_dining_hall.neilson_dinner import get_cd_dinner_items

from Campus.Livingston.dining_hall.dh_breakfast import get_livi_breakfast_items
from Campus.Livingston.dining_hall.dh_lunch import get_livi_lunch_items
from Campus.Livingston.dining_hall.dh_dinner import get_livi_dinner_items


app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello World! Server is active"

def is_weekday_today():
    # Get the current date
    today = datetime.datetime.now().date()
    
    # Check if the day of the week is Monday to Friday (1 to 5)
    if today.isoweekday() < 6:
        return True
    else:
        return False


@app.route('/api/get-breakfast-items', methods=["POST"])
def get_all_breakfast_items():
    if(is_weekday_today()):
        all_breakfast_items = {
            "livi" : get_livi_breakfast_items(),
            "cook" : get_cd_breakfast_items(),
            "busch" : get_busch_dh_breakfast_items(),
            "atrium" : get_atrium_breakfast_items()
        }
        return all_breakfast_items
    else:
        return {}


@app.route('/api/get-lunch-items', methods=["POST"])
def get_all_lunch_items():
    all_lunch_items = {
        "livi" : get_livi_lunch_items(),
        "cook" : get_cd_lunch_items(),
        "busch" : get_busch_dh_lunch_items(),
        "atrium" : get_atrium_lunch_items()
    }
    return all_lunch_items

@app.route('/api/get-dinner-items', methods=["POST"])
def get_all_dinner_items():
    all_dinner_items = {
        "livi" : get_livi_dinner_items(),
        "cook" : get_cd_dinner_items(),
        "busch" : get_busch_dh_dinner_items(),
        "atrium" : get_atrium_dinner_items()
    }
    return all_dinner_items

    

if(__name__ == "__main__"):
    app.run(debug=True)
from flask import Blueprint, request
from databaseConnection import findCabinCrewsWithID
from databaseConnection import create_connection
from databaseConnection import findCabinCrewIDs
from databaseConnection import findCabinCrewLanguagesWithID
from databaseConnection import getMealsWithID
import json

views = Blueprint('views', __name__)


@views.route('/getCabinCrew', methods=['POST'])
def getCabinCrew():
    try:
        print("what")
        conn = create_connection("localhost", 3306, "myDB", "root", "1234")
        print("1")
        cabinCrewIDList = findCabinCrewIDs(conn, str(request.form.get('pnr')))
        print("sure?")
        returnList = []
        print("1")
        menuAdded = False
        menu = str()
        for cabinCrewID in cabinCrewIDList:

            print(cabinCrewID[0])
            languages = findCabinCrewLanguagesWithID(conn, cabinCrewID[0])
            cabinCrew = findCabinCrewsWithID(conn, cabinCrewID[0])
            if cabinCrew[5] == "Chef" and menuAdded == False:
                menuAdded = True
                menu = getMealsWithID(conn, cabinCrewID[0])[0]

            returnList.append({"id": cabinCrew[0], 'name': cabinCrew[1], 'age': cabinCrew[2], 'gender': cabinCrew[3],
                               'nationality': cabinCrew[4], 'type': cabinCrew[5], 'vehicle': cabinCrew[6],
                               "languages": languages})
        print("1")
        conn.close()
        return json.dumps({"menu": menu, "cabinCrews": returnList})
    except Exception as e:
        print(e)
        return e

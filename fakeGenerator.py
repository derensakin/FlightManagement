import random
import mysql.connector
from mysql.connector import Error
import faker


def create_connection(host, port, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        print("Connection to MySQL successful")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_fake_pilot(numPilot, connection):
    try:
        idList = []
        myFaker = faker.Faker()
        cursor = connection.cursor()
        for _ in range(numPilot):
            name = myFaker.first_name() + " " + myFaker.last_name()
            id = random.randrange(1000000, 9999999)
            while id in idList:
                id = random.randrange(1000000, 9999999)
            idList.append(id)
            age = random.randrange(25, 60)
            gender = random.choice(["Male", "Female"])

            nationality = myFaker.country()
            while (len(nationality) > 40):
                nationality = myFaker.country()
            vehicle = random.choice(["Airbus", "Boeing", "SeaPlane", "Wide-Body-AirCraft", "Turboprop"])
            distance = random.randrange(1, 30)
            seniority = random.choice(["senior", "junior", "trainee"])
            cursor.execute(
                """
                INSERT INTO FLIGHTCREW VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (id, name, age, gender, nationality, vehicle, seniority, distance)
            )
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting pilot values: {e}")


def create_fake_cabin_crew(numCabinCrew, connection):
    try:
        idList = []
        myFaker = faker.Faker()
        cursor = connection.cursor()
        for _ in range(numCabinCrew):
            name = myFaker.first_name() + " " + myFaker.last_name()
            id = random.randrange(1000000, 9999999)
            id = random.randrange(1000000, 9999999)
            while id in idList:
                id = random.randrange(1000000, 9999999)
            age = random.randrange(25, 60)
            gender = random.choice(["Male", "Female"])
            nationality = myFaker.country()
            while (len(nationality) > 50):
                nationality = myFaker.country()
            type = random.choice(["Chief", "Regular", "Chef"])
            vehicle = random.choice(["Airbus", "Boeing", "SeaPlane", "Wide-Body-AirCraft", "Turboprop"])
            cursor.execute("""
            INSERT INTO CABINCREW VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (id, name, age, gender, nationality, type, vehicle))
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting cabin crew values: {e}")


def create_fake_passenger(numPassenger, connection):
    try:
        idList = []
        myFaker = faker.Faker()
        cursor = connection.cursor()
        for _ in range(numPassenger):
            name = myFaker.first_name() + " " + myFaker.last_name()
            id = random.randrange(1000000, 9999999)
            id = random.randrange(1000000, 9999999)
            while id in idList:
                id = random.randrange(1000000, 9999999)
            age = random.randrange(0, 60)
            gender = random.choice(["Male", "Female"])
            nationality = myFaker.country()
            while (len(nationality) > 50):
                nationality = myFaker.country()
            cursor.execute("""
            INSERT INTO PASSANGERINFORMATION VALUES (%s, %s, %s, %s, %s)
            """, (id, name, age, gender, nationality)
                           )
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting passenger values: {e}")


def create_fake_flight_known_languages(connection):
    try:
        cursor = connection.cursor()
        myFaker = faker.Faker()
        cursor.execute(
            """
            SELECT ID FROM FLIGHTCREW"""
        )
        flight_crew_ids = cursor.fetchall()
        for id in flight_crew_ids:
            num_lang = random.randrange(1, 3)
            for _ in range(num_lang):
                language = myFaker.language_name()
                try:
                    cursor.execute("""
                    INSERT INTO FLIGHTCREWKNOWNLANGUAGES VALUES(%s,%s)
                    """, (str(id[0]), language)
                                   )

                    connection.commit()
                except Error as e:
                    print(f"Error inserting flight know language values: {str(id[0])} and {language}")
        cursor.close()
    except Error as e:
        print(f"Error inserting flight known languages values: {e}")


def create_fake_cabin_crew_known_languages(connection):
    try:
        cursor = connection.cursor()
        myFaker = faker.Faker()
        cursor.execute("""
        SELECT ID FROM CABINCREW
        """)
        cabin_crew_ids = cursor.fetchall()
        for id in cabin_crew_ids:
            num_lang = random.randrange(1, 3)
            for _ in range(num_lang):
                language = myFaker.language_name()
                try:
                    cursor.execute("""
                    INSERT INTO CABINCREWKNOWNLANGUAGES VALUES(%s,%s)
                    """, (str(id[0]), language)
                                   )
                    connection.commit()
                except Error as e:
                    print("Error inserting cabin crew known language values: " + str(language) + "and " + str(id[0]))
        cursor.close()
    except Error as e:
        print(f"Error inserting cabin crew known languages values: {e}")


def create_fake_cabin_crew_food(connection):
    try:
        cursor = connection.cursor()
        myFaker = faker.Faker()
        cursor.execute(
            """
            SELECT ID FROM CABINCREW WHERE TYPE = "Chef"
            """
        )
        chef_ids = cursor.fetchall()
        for id in chef_ids:
            num_food = random.randrange(2, 4)
            for _ in range(num_food):
                food = random.choice(
                    ["Kebab", "Chicken", "Doner", "Soup", "Meatball", "Burger", "Fries", "Fish", "Iguana Meat","Lamb","Lion Milk","Chinese","Japanese","Pizza","Steak","Eggplant","Brocoli","Sunflower","Garlic","Prmium","Chief's Special"])
                try:
                    cursor.execute(
                        """
                        INSERT INTO CABINCREWFOOD VALUES(%s,"%s")
                        """, (str(id[0]), food)

                    )
                    connection.commit()
                except Error as e:
                    print(f"Error inserting cabin crew food values: {str(id[0])} and {food} and {e}")
        cursor.close()
    except Error as e:
        print(f"Error inserting cabin crew food values: {e}")


def create_fake_flight(numberOfFlights, connection):
    try:
        cursor = connection.cursor()
        myFaker = faker.Faker()
        for _ in range(numberOfFlights):

            departureDate = myFaker.date_time()
            duration = random.randrange(60, 2000)
            distance = random.randrange(1, 25)
            source_country = myFaker.country()
            while len(source_country) > 50:
                source_country = myFaker.country()
            source_city = myFaker.city()
            while len(source_city) > 40:
                source_city = myFaker.city()
            source_airport = source_city + " airport"
            source_airport_code = source_airport[0] + source_airport[len(source_airport) // 2] + source_airport[
                len(source_airport) - 1]
            vehicle = random.choice(["Airbus", "Boeing", "SeaPlane", "Wide-Body-AirCraft", "Turboprop"])
            id = "CS" + str(random.randrange(1000, 9999))
            if random.randrange(1, 10) == 1:
                sharedFlight = random.choice(["TK", "PG", "AJ", "QA"]) + str(random.randrange(1000, 9999))
            else:
                sharedFlight = "XXXXXX"
            try:
                cursor.execute(
                    """
                    INSERT INTO FLIGHTINFORMATION VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (
                    id, departureDate, duration, distance, source_country, source_city, source_airport, source_airport_code,
                    vehicle, sharedFlight)
                )
            except Error as e:
                print(f"Error inserting flight values: {e}")
            connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting flight info values: {e}")


def create_fake_ticket(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT ID FROM FLIGHTINFORMATION
            """

        )
        flightList = cursor.fetchall()
        cursor.execute(
            """
            SELECT ID FROM PASSANGERINFORMATION WHERE AGE > 2
            """
        )
        mBiggerTwoList = cursor.fetchall()
        cursor.execute(
            """
            SELECT ID FROM PASSANGERINFORMATION WHERE AGE < 3
            """
        )
        mSmallerThreeList = cursor.fetchall()

        for flight in flightList:
            biggerTwoList = []
            for i in mBiggerTwoList:
                biggerTwoList.append(i)
            smallerThreeList = []
            for i in mSmallerThreeList:
                smallerThreeList.append(i)
            maxSeatNumber = random.choice([30, 60, 100])
            for seatNumber in range(maxSeatNumber):
                if seatNumber < 10:
                    seatType = "Business"
                else:
                    seatType = "Economy"
                sittingPassenger = random.choice(biggerTwoList)
                biggerTwoList.remove(sittingPassenger)
                try:
                    cursor.execute("""
                    INSERT INTO TICKET VALUES (%s,%s,%s,%s)
                    """, (str(flight[0]), seatNumber, seatType, str(sittingPassenger[0])))
                    connection.commit()
                except Error as e:
                    print(f"Error inserting ticket values: {e}")
                if random.randrange(0, 20) == 1:
                    child = random.choice(smallerThreeList)
                    smallerThreeList.remove(child)
                    try:
                        cursor.execute("""
                        INSERT INTO TICKET VALUES (%s,%s,"%s",%s)
                        """, (str(flight[0]), str(sittingPassenger[0]), seatType, str(child[0])))
                        connection.commit()
                    except Error as e:
                        print(f"Error inserting child ticket values: {e} and {str(flight[0])}")
        cursor.close()
    except Error as e:
        print(f"Error inserting ticket values: {e}")


def create_fake_flight_pilot(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT ID, DISTANCE, VEHICLE FROM FLIGHTINFORMATION
            """
        )
        flightList = cursor.fetchall()
        for flight in flightList:
            flightID = flight[0]
            flightDistance = flight[1]
            flightVehicle = flight[2]
            cursor.execute(
                """
                SELECT ID FROM FLIGHTCREW WHERE VEHICLE = %s AND FLIGHT_RANGE > %s AND SENIORITY = "senior"
                """
                , (flightVehicle, str(flightDistance))
            )
            appropriatePilots = cursor.fetchall()
            for _ in range(random.randrange(1, 2)):
                if len(appropriatePilots) > 0:
                    pilot = random.choice(appropriatePilots)
                    appropriatePilots.remove(pilot)
                    cursor.execute("""
                    INSERT INTO FLIGHTPILOT VALUES(%s,%s)
                    """, (flightID, str(pilot[0])))
                    connection.commit()
            cursor.execute(
                """
                SELECT ID FROM FLIGHTCREW WHERE VEHICLE = %s AND FLIGHT_RANGE > %s AND SENIORITY = "junior"
                """
                , (flightVehicle, int(flightDistance))
            )
            appropriatePilots = cursor.fetchall()

            for _ in range(random.randrange(1, 2)):
                if (len(appropriatePilots) > 0):
                    pilot = random.choice(appropriatePilots)
                    appropriatePilots.remove(pilot)
                    cursor.execute(
                        """
                        INSERT INTO FLIGHTPILOT VALUES(%s,%s)""",
                        (flightID, str(pilot[0]))
                    )
                    connection.commit()
            numTrainee = random.randrange(0, 2)
            if numTrainee != 0:
                cursor.execute(
                    """
                    SELECT ID FROM FLIGHTCREW WHERE VEHICLE = %s AND FLIGHT_RANGE > %s AND SENIORITY = "trainee"
                    """, (flightVehicle, int(flightDistance))
                )
                appropriatePilots = cursor.fetchall()
                for _ in range(numTrainee):
                    if len(appropriatePilots) > 0:
                        pilot = random.choice(appropriatePilots)
                        appropriatePilots.remove(pilot)
                        cursor.execute(
                            """
                            INSERT INTO FLIGHTPILOT VALUES(%s,%s)""",
                            (str(flightID), str(pilot[0]))
                        )
                        connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting flight-pilot values: {e}")


def create_fake_flight_cabin_crew(connection) :
    try:
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT ID, VEHICLE FROM FLIGHTINFORMATION
            """
        )
        flightList = cursor.fetchall()
        for flight in flightList:
            vehicle = flight[1]
            cursor.execute(
                f"""
                SELECT ID
                FROM CABINCREW
                WHERE VEHICLE = "{vehicle}" AND TYPE = "Chief"
                """
            )
            chiefList = cursor.fetchall()
            numChiefs = random.randrange(1, 4)
            for _ in range(numChiefs):
                if len(chiefList) > 0:
                    chief = random.choice(chiefList)
                    chiefList.remove(chief)
                    cursor.execute(

                        """
                        INSERT INTO FLIGHTCABINCREW VALUES(%s,%s)
                        """,(flight[0], str(chief[0]))
                    )
                    connection.commit()
            cursor.execute(
                f"""
                SELECT ID 
                FROM CABINCREW
                WHERE VEHICLE = "{vehicle}" AND TYPE = "Regular"
                """
            )
            regularList = cursor.fetchall()
            numRegulars = random.randrange(4, 16)
            for _ in range(numRegulars):
                if len(regularList) > 0:
                    regular = random.choice(regularList)
                    regularList.remove(regular)
                    cursor.execute(f"""
                    INSERT INTO FLIGHTCABINCREW VALUES(%s,%s)
                    """,
                    (flight[0], str(regular[0]))
                    )
                    connection.commit()
            cursor.execute(
                f"""
                SELECT ID FROM CABINCREW
                WHERE VEHICLE = "{vehicle}" AND TYPE = "Chef"
                """
            )
            chefList = cursor.fetchall()
            numChefs = random.randrange(0, 2)
            for _ in range(numChefs):
                if len(chefList) > 0:
                    chef = random.choice(chefList)
                    chefList.remove(chef)
                    cursor.execute(
                        """
                        INSERT INTO FLIGHTCABINCREW VALUES(%s,%s)
                        """
                        ,(flight[0], str(chef[0]))
                    )
                    connection.commit()
        cursor.close()
    except Error as e:
        print(f"Error inserting flight cabin crew values: {e}")




def main():
    host = 'localhost'
    port = 3306
    user = 'root'
    password = '1234'
    database = 'myDB'

    connection = create_connection(host, port, user, password, database)
    # create_fake_pilot(1000, connection)
    # create_fake_cabin_crew(1000, connection)
    # create_fake_passenger(1000, connection)
    # create_fake_flight_known_languages(connection)
    create_fake_cabin_crew_known_languages(connection)
    # create_fake_cabin_crew_food(connection)
    # create_fake_flight(100, connection)
    # create_fake_ticket(connection)
    # create_fake_flight_pilot(connection)
    # create_fake_flight_cabin_crew(connection)
    connection.close()


if __name__ == "__main__":
    main()

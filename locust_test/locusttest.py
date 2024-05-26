from locust import HttpUser, TaskSet, task, between
import json

class UserBehavior(TaskSet):

    @task(1)
    def get_flight(self):
        flightID = "CS2445"  # Replace with a valid flight ID
        self.client.post("/getFlight", data={'flightID': flightID})

    @task(2)
    def search_flights(self):
        filters = {
            'id': "CS1169",  # Replace with valid filter values
            'departure_date': "2007-10-21 03:10:25",
            'duration': "174",
            'distance': "14",
            'source_country': "Central African Republic",
            'source_city': "Mitchellhaven",
            'source_airport': "Mitchellhaven airport",
            'source_airport_code': "Mvt",
            'vehicle': "Wide-Body-AirCraft",
            'shared_flight': False
        }
        self.client.post("/searchFlights", data=json.dumps(filters), headers={'Content-Type': 'application/json'})

    @task(1)
    def get_tickets_by_flight(self):
        flightID = "CS1146"  # Replace with a valid flight ID
        self.client.post("/getTicketsByFlight", data={'flightID': flightID})

    @task(1)
    def get_flight_pilots_by_flight(self):
        flightID = "CS1146"  # Replace with a valid flight ID
        self.client.post("/getFlightPilotsByFlight", data={'flightID': flightID})

    @task(2)
    def get_passengers(self):
            flightID = "CS1146"  # Replace with a valid flight ID
            self.client.get(f"/getPassengers?flightID={flightID}")
    @task(2)
    def get_flight_crew_post(self):
        flightID = "CS1146"  # Replace with a valid flight ID
        self.client.post("/getFlightCrew", data={'flightID': flightID})

    @task(2)
    def get_flight_crew_get(self):
        flightID = "CS1146"  # Replace with a valid flight ID
        self.client.get(f"/getFlightCrew?flightID={flightID}")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

if __name__ == "__main__":
    import os

    os.system("locust -f locusttest.py")

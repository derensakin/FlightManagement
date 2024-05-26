from locust import HttpUser, task, between

class FlightAppUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def login(self):
        # Define the payload for the POST request
        payload = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        # Send the POST request to the /login endpoint
        response = self.client.post("/login", json=payload)



    @task
    def get_flight(self):
        # Define the payload for the POST request
        payload = {'flightID': 'CS1031'}

        # Send the POST request to the /getFlight endpoint
        response = self.client.post("/getFlight", data=payload)



    @task
    def search_flights(self):
        # Define the payload for the POST request
        payload = {
            'id': 'CS1031',
            'departure_date': '2024-06-01',
            'duration': 120,
            'distance': 1000,
            'source_country': 'USA',
            'source_city': 'New York',
            'source_airport': 'JFK',
            'source_airport_code': 'JFK',
            'vehicle': 'Boeing 737',
            'shared_flight': False
        }

        # Send the POST request to the /searchFlights endpoint
        response = self.client.post("/searchFlights", json=payload)



    @task
    def get_tickets_by_flight(self):
        # Define the payload for the POST request
        payload = {'flightID': 'CS1031'}

        # Send the POST request to the /getTicketsByFlight endpoint
        response = self.client.post("/getTicketsByFlight", data=payload)


    @task
    def get_flight_pilots_by_flight(self):
        # Define the payload for the POST request
        payload = {'flightID': 'CS1031'}

        # Send the POST request to the /getFlightPilotsByFlight endpoint
        response = self.client.post("/getFlightPilotsByFlight", data=payload)





if __name__ == "__main__":
    import os

    os.system("locust -f flight_locust.py")

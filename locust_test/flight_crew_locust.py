from locust import HttpUser, task, between

class FlightCrewUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def get_flight_crew(self):
        # Define the payload for the POST request
        payload = {'flightID': 'CS1031'}

        # Send the POST request to the /getFlightCrew endpoint
        response = self.client.post("/getFlightCrew", data=payload)

        # Print the response (optional, for debugging purposes)
        print(response.text)

        # Check that the response is successful
        if response.status_code != 200:
            print("Request failed: ", response.status_code)
        else:
            print("Request succeeded: ", response.status_code)



if __name__ == "__main__":
    import os

    os.system("locust -f flight_crew_locust.py")


# # Path: locust_test/flight_locust.py
# #http://localhost:5001  for the cabin crew api
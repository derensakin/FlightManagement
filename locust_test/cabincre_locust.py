from locust import HttpUser, TaskSet, task, between
import json
from locust import HttpUser, task, between

class CabinCrewUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def get_cabin_crew(self):
        # Define the payload for the POST request
        payload = {'pnr': 'example_pnr'}

        # Send the POST request to the /getCabinCrew endpoint
        response = self.client.post("/getCabinCrew", data=payload)

        # Print the response (optional, for debugging purposes)
        print(response.text)



if __name__ == "__main__":
    import os

    os.system("locust -f cabincre_locust.py")

# Path: locust_test/flight_locust.py



#http://localhost:5002  for the cabin crew api



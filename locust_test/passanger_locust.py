from locust import HttpUser, task, between

class FlightAppUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks

    @task
    def get_passenger(self):
        # Define the payload for the POST request
        payload = {'flight_id': 'CS1031'}

        # Send the POST request to the /getPassenger endpoint
        response = self.client.post("/getPassenger", data=payload)



    @task
    def change_seats(self):
        # Define the payload for the POST request
        payload = {
            'flight_id': 'CS1031',
            'passenger_id1': 1,
            'passenger_id2': 2
        }

        # Send the POST request to the /changeSeats endpoint
        response = self.client.post("/changeSeats", data=payload)





if __name__ == "__main__":

    import os

    os.system("locust -f passanger_locust.py")

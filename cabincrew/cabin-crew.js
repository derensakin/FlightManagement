// Selecting necessary elements
const cabinCrewMainContent = document.querySelector('main');

// Selecting necessary elements for navigation links
const cabinCrewHomeLink = document.getElementById('cabin-crew-home-link');
const cabinCrewSearchFlightLink = document.getElementById('cabin-crew-search-flight-link');
const cabinCrewSeatingPlanLink = document.getElementById('cabin-crew-seating-plan-link');
const cabinCrewFlightInfoLink = document.getElementById('cabin-crew-flight-info-link');
const cabinCrewInfoLink = document.getElementById('cabin-crew-info-link');
const cabinCrewPassengerInfoLink = document.getElementById('cabin-crew-passenger-info-link');
const cabinCrewUpdateSeatingLink = document.getElementById('cabin-crew-update-seating-link');

// Event listeners for navigation links
cabinCrewHomeLink.addEventListener('click', showCabinCrewWelcomePage);
cabinCrewSearchFlightLink.addEventListener('click', openCabinCrewSearchFlightView);
cabinCrewSeatingPlanLink.addEventListener('click', viewSeatingPlan);
cabinCrewFlightInfoLink.addEventListener('click', viewFlightInformation);
cabinCrewInfoLink.addEventListener('click', openCabinCrewInfoInput);
cabinCrewPassengerInfoLink.addEventListener('click', viewPassengerInformation);
cabinCrewUpdateSeatingLink.addEventListener('click', updateSeatingPlan);

// Functions to load different sections
function showCabinCrewWelcomePage() {
    cabinCrewMainContent.innerHTML = `<h2>Welcome to the Cabin Crew Dashboard</h2>
                                      <p>Use the sidebar to navigate through different sections.</p>`;
}

function openCabinCrewSearchFlightView() {
    cabinCrewMainContent.innerHTML = `<div class="search-container">
                                        <h2>Cabin Crew: Search Flight</h2>
                                        <input type="text" placeholder="Enter Flight Number" id="cabinCrewFlightNumber" class="form-control">
                                        <button type="button" class="btn btn-primary mt-2" onclick="cabinCrewSearchFlight()">Search</button>
                                      </div>`;
}

async function cabinCrewSearchFlight() {
    const flightNumber = document.getElementById('cabinCrewFlightNumber').value;
    const flightInfo = await fetchFlightInformation(flightNumber);
    const cabinCrewInfo = await fetchFlightCabinCrew(flightNumber);
    cabinCrewMainContent.innerHTML = `<h2>Flight Information for Flight: ${flightInfo.ID}</h2>
                                      <p><strong>Departure Date:</strong> ${flightInfo.DEPARTURE_DATE}</p>
                                      <p><strong>Duration:</strong> ${flightInfo.DURATION} minutes</p>
                                      <p><strong>Distance:</strong> ${flightInfo.DISTANCE} km</p>
                                      <p><strong>Source Country:</strong> ${flightInfo.SOURCE_COUNTRY}</p>
                                      <p><strong>Source City:</strong> ${flightInfo.SOURCE_CITY}</p>
                                      <p><strong>Source Airport:</strong> ${flightInfo.SOURCE_AIRPORT}</p>
                                      <p><strong>Source Airport Code:</strong> ${flightInfo.SOURCE_AIRPORT_CODE}</p>
                                      <p><strong>Vehicle:</strong> ${flightInfo.VEHICLE}</p>
                                      <p><strong>Shared Flight:</strong> ${flightInfo.SHARED_FLIGHT}</p>
                                      <h3>Cabin Crew</h3>
                                      <ul>
                                        ${cabinCrewInfo.map(crew => `<li>ID: ${crew.CABIN_CREW_ID}, Name: ${crew.name}</li>`).join('')}
                                      </ul>
                                      <button type="button" class="btn btn-secondary" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
}

function viewSeatingPlan() {
    cabinCrewMainContent.innerHTML = `<h2>Seating Plan</h2>
                                      <p>Seating plan details go here.</p>
                                      <button type="button" class="btn btn-secondary" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
}

function viewFlightInformation() {
    cabinCrewMainContent.innerHTML = `<h2>Flight Information</h2>
                                      <p>Flight information details go here.</p>
                                      <button type="button" class="btn btn-secondary" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
}

function openCabinCrewInfoInput() {
    cabinCrewMainContent.innerHTML = `<div class="search-container">
                                        <h2>Cabin Crew Information</h2>
                                        <input type="text" placeholder="Enter Flight Number" id="cabinCrewFlightInfoNumber" class="form-control">
                                        <button type="button" class="btn btn-primary mt-2" onclick="viewCabinCrewInformation()">View Information</button>
                                      </div>`;
}

async function viewCabinCrewInformation() {
    const flightNumber = document.getElementById('cabinCrewFlightInfoNumber').value;
    const cabinCrewInfo = await fetchFlightCabinCrew(flightNumber);
    cabinCrewMainContent.innerHTML = `<h2>Cabin Crew Information for Flight: ${flightNumber}</h2>
                                      <ul>
                                        ${cabinCrewInfo.map(crew => `<li>ID: ${crew.CABIN_CREW_ID}, Name: ${crew.name}</li>`).join('')}
                                      </ul>
                                      <button type="button" class="btn btn-secondary" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
}

function viewPassengerInformation() {
    cabinCrewMainContent.innerHTML = `<h2>Passenger Information</h2>
                                      <p>Passenger information details go here.</p>
                                      <button type="button" class="btn btn-secondary" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
}

function updateSeatingPlan() {
    cabinCrewMainContent.innerHTML = `<h2>Update Seating Plan</h2>
                                      <form id="updateSeatingPlanForm">
                                        <div class="form-group">
                                          <label for="seatNumber">Seat Number</label>
                                          <input type="text" class="form-control" id="seatNumber" placeholder="Enter Seat Number" required>
                                        </div>
                                        <div class="form-group">
                                          <label for="passengerName">Passenger Name</label>
                                          <input type="text" class="form-control" id="passengerName" placeholder="Enter Passenger Name" required>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Update Seat</button>
                                      </form>
                                      <button type="button" class="btn btn-secondary mt-2" onclick="showCabinCrewWelcomePage()">Back to Cabin Crew Dashboard</button>`;
    document.getElementById('updateSeatingPlanForm').addEventListener('submit', function(event) {
        event.preventDefault();
        alert("Seating plan updated successfully!");
        showCabinCrewWelcomePage();
    });
}

// Function to fetch flight information (simulated)
async function fetchFlightInformation(flightNumber) {
    // Replace with actual data fetching logic
    return {
        ID: flightNumber,
        DEPARTURE_DATE: '2024-06-01 12:30:00',
        DURATION: 180,
        DISTANCE: 1200,
        SOURCE_COUNTRY: 'Turkey',
        SOURCE_CITY: 'Istanbul',
        SOURCE_AIRPORT: 'Istanbul Airport',
        SOURCE_AIRPORT_CODE: 'IST',
        VEHICLE: 'Boeing 737',
        SHARED_FLIGHT: 'TK1234'
    };
}

// Function to fetch flight cabin crew information (simulated)
async function fetchFlightCabinCrew(flightNumber) {
    // Replace with actual data fetching logic
    return [
        { CABIN_CREW_ID: 1, name: 'Crew Member 1' },
        { CABIN_CREW_ID: 2, name: 'Crew Member 2' },
        { CABIN_CREW_ID: 3, name: 'Crew Member 3' }
    ];
}

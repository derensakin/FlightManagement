// Selecting necessary elements
const mainContent = document.querySelector('main');
const loginContainer = document.getElementById('login-container');
const loginForm = document.getElementById('login-form');
const flightCrewHomeLink = document.getElementById('flight-crew-home-link');
const flightCrewSearchFlightLink = document.getElementById('flight-crew-search-flight-link');
const flightCrewSeatingPlanLink = document.getElementById('flight-crew-seating-plan-link');
const flightCrewFlightInfoLink = document.getElementById('flight-crew-flight-info-link');
const flightCrewCabinCrewInfoLink = document.getElementById('flight-crew-cabin-crew-info-link');
const flightCrewFlightCrewInfoLink = document.getElementById('flight-crew-flight-crew-info-link');

let username = "";

// Event listener for the login form submission
loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (verifyCredentials(username, password)) {
        showWelcomePage();
        enableSidebarLinks();
    } else {
        alert('Invalid username or password');
    }
});

// Function to verify credentials (accepts any username and password)
function verifyCredentials(username, password) {
    return username !== '' && password !== '';
}

// Function to show the welcome page
function showWelcomePage() {
    loginContainer.style.display = 'none';
    mainContent.innerHTML = `<h2>Welcome ${username}</h2><p>We hope you have a nice day!</p>`;
}

// Function to enable sidebar links after login
function enableSidebarLinks() {
    flightCrewHomeLink.addEventListener('click', showWelcomePage);
    flightCrewSearchFlightLink.addEventListener('click', openFlightCrewSearchFlightView);
    flightCrewSeatingPlanLink.addEventListener('click', viewSeatingPlan);
    flightCrewFlightInfoLink.addEventListener('click', viewFlightInformation);
    flightCrewCabinCrewInfoLink.addEventListener('click', openFlightCrewCabinCrewInfoInput);
    flightCrewFlightCrewInfoLink.addEventListener('click', openFlightCrewFlightCrewInfoInput);
}

// Function to open the search flight view
function openFlightCrewSearchFlightView() {
    mainContent.innerHTML = `<div class="search-container">
                                <h2>Search Flight</h2>
                                <input type="text" placeholder="Enter Flight Number" id="flightNumber" class="form-control">
                                <button type="button" class="btn btn-primary mt-2" onclick="searchFlight()">Search</button>
                             </div>`;
}

// Function to search for flight information (simulated)
async function searchFlight() {
    const flightNumber = document.getElementById('flightNumber').value;
    const flightInfo = await fetchFlightInformation(flightNumber);
    mainContent.innerHTML = `<h2>Flight Information for Flight: ${flightInfo.ID}</h2>
                             <p><strong>Departure Date:</strong> ${flightInfo.DEPARTURE_DATE}</p>
                             <p><strong>Duration:</strong> ${flightInfo.DURATION} minutes</p>
                             <p><strong>Distance:</strong> ${flightInfo.DISTANCE} km</p>
                             <p><strong>Source Country:</strong> ${flightInfo.SOURCE_COUNTRY}</p>
                             <p><strong>Source City:</strong> ${flightInfo.SOURCE_CITY}</p>
                             <p><strong>Source Airport:</strong> ${flightInfo.SOURCE_AIRPORT}</p>
                             <p><strong>Source Airport Code:</strong> ${flightInfo.SOURCE_AIRPORT_CODE}</p>
                             <p><strong>Vehicle:</strong> ${flightInfo.VEHICLE}</p>
                             <p><strong>Shared Flight:</strong> ${flightInfo.SHARED_FLIGHT}</p>`;
}

// Function to view the seating plan (placeholder)
function viewSeatingPlan() {
    mainContent.innerHTML = `<h2>Seating Plan</h2>
                             <p>Seating plan details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Dashboard</button>`;
}

// Function to view flight information (placeholder)
function viewFlightInformation() {
    mainContent.innerHTML = `<h2>Flight Information</h2>
                             <p>Flight information details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Dashboard</button>`;
}

// Function to open the cabin crew information input view
function openFlightCrewCabinCrewInfoInput() {
    mainContent.innerHTML = `<div class="search-container">
                                <h2>Cabin Crew Information</h2>
                                <input type="text" placeholder="Enter Flight Number" id="cabinCrewFlightInfoNumber" class="form-control">
                                <button type="button" class="btn btn-primary mt-2" onclick="viewCabinCrewInformation()">View Information</button>
                             </div>`;
}

// Function to view cabin crew information (simulated)
async function viewCabinCrewInformation() {
    const flightNumber = document.getElementById('cabinCrewFlightInfoNumber').value;
    const cabinCrewInfo = await fetchFlightCabinCrew(flightNumber);
    mainContent.innerHTML = `<h2>Cabin Crew Information for Flight: ${flightNumber}</h2>
                             <ul>
                               ${cabinCrewInfo.map(crew => `<li>ID: ${crew.CABIN_CREW_ID}, Name: ${crew.name}</li>`).join('')}
                             </ul>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Dashboard</button>`;
}

// Function to open the flight crew information input view
function openFlightCrewFlightCrewInfoInput() {
    mainContent.innerHTML = `<div class="search-container">
                                <h2>Flight Crew Information</h2>
                                <input type="text" placeholder="Enter Flight Number" id="flightCrewFlightInfoNumber" class="form-control">
                                <button type="button" class="btn btn-primary mt-2" onclick="viewFlightCrewInformation()">View Information</button>
                             </div>`;
}

// Function to view flight crew information (simulated)
async function viewFlightCrewInformation() {
    const flightNumber = document.getElementById('flightCrewFlightInfoNumber').value;
    const flightCrewInfo = await fetchFlightCrew(flightNumber);
    mainContent.innerHTML = `<h2>Flight Crew Information for Flight: ${flightNumber}</h2>
                             <ul>
                               ${flightCrewInfo.map(crew => `<li>ID: ${crew.FLIGHT_CREW_ID}, Name: ${crew.name}</li>`).join('')}
                             </ul>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Dashboard</button>`;
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

// Function to fetch flight crew information (simulated)
async function fetchFlightCrew(flightNumber) {
    // Replace with actual data fetching logic
    return [
        { FLIGHT_CREW_ID: 1, name: 'Flight Crew Member 1' },
        { FLIGHT_CREW_ID: 2, name: 'Flight Crew Member 2' },
        { FLIGHT_CREW_ID: 3, name: 'Flight Crew Member 3' }
    ];
}

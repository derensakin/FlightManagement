// Selecting necessary elements
const mainContent = document.querySelector('main');
const loginContainer = document.getElementById('login-container');
const loginForm = document.getElementById('login-form');
const welcomeLink = document.getElementById('welcome-link');

// Add a variable to store the username
let username = "";

// Event listener for the login form submission
loginForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting
    username = document.getElementById('username').value;
    showWelcomePage();
});

// Event listener for the home link
welcomeLink.addEventListener('click', showWelcomePage);

// Selecting necessary elements for navigation links
const flightManagementLink = document.getElementById('flight-management-link');
const addUpdateFlightLink = document.getElementById('add-update-flight-link');
const addUpdatePassengerLink = document.getElementById('add-update-passenger-link');

// Event listeners for navigation links
flightManagementLink.addEventListener('click', loadFlightManagement);
addUpdateFlightLink.addEventListener('click', loadAddUpdateFlight);
addUpdatePassengerLink.addEventListener('click', loadAddUpdatePassenger);

// Functions to load different sections
function showWelcomePage() {
    loginContainer.style.display = 'none';
    mainContent.innerHTML = `<h2>Welcome ${username}</h2><p>We hope you have a nice day!</p>`;
}

function loadFlightManagement() {
    mainContent.innerHTML = "<h2>Flight Management</h2><p>Manage flights here!</p>";
    addSearchFlightButton();
}

function addSearchFlightButton() {
    const searchFlightButton = document.createElement('button');
    searchFlightButton.innerText = 'Search Flight';
    searchFlightButton.classList.add('btn', 'btn-primary'); // Add Bootstrap classes
    searchFlightButton.addEventListener('click', openSearchFlightView);
    mainContent.appendChild(searchFlightButton);
}

function openSearchFlightView() {
    mainContent.innerHTML = `<div class="search-container">
                                <h2>Search Flight</h2>
                                <input type="text" placeholder="Enter Flight Number" id="flightNumber" class="form-control">
                                <button type="button" class="btn btn-primary mt-2" onclick="searchFlight()">Search</button>
                             </div>`;
}

// Assuming you have a function to fetch flight information
async function fetchFlightInformation(flightNumber) {
    // For demonstration purposes, we'll use static data
    // Replace this with actual data fetching logic
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
                             <p><strong>Shared Flight:</strong> ${flightInfo.SHARED_FLIGHT}</p>
                             <button type="button" class="btn btn-secondary" onclick="editFlightCrew()">Edit Crew</button>
                             <button type="button" class="btn btn-info" onclick="viewFlightCrewAttendants('${flightInfo.ID}')">View Flight Crew Attendants</button>`;
}

function editFlightCrew() {
    const currentCrewName = document.getElementById('flightCrew').textContent;
    mainContent.innerHTML = `<h2>Edit Flight Crew</h2>
                             <form id="editCrewForm">
                               <div class="form-group">
                                 <label for="newCrewName">New Crew Name</label>
                                 <input type="text" class="form-control" id="newCrewName" value="${currentCrewName}" required>
                               </div>
                               <button type="submit" class="btn btn-primary">Save Changes</button>
                             </form>`;
    document.getElementById('editCrewForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const newCrewName = document.getElementById('newCrewName').value;
        document.getElementById('flightCrew').textContent = newCrewName;
        displayChangesSavedMessage();
    });
}

function displayChangesSavedMessage() {
    mainContent.innerHTML = `<h2>Admin Flight Info View</h2>
                             <p>Flight crew updated successfully.</p>
                             <p>Changes saved!</p>
                             <button type="button" class="btn btn-primary" onclick="loadFlightManagement()">Return to Flight Management</button>`;
}

function viewFlightCrewAttendants(flightNumber) {
    // For demo purposes, we're using static data. Replace with actual data fetching logic as needed.
    const attendants = ["Attendant 1", "Attendant 2", "Attendant 3"];
    mainContent.innerHTML = `<h2>Flight Crew Attendants for Flight ${flightNumber}</h2>
                             <ul id="crewAttendantsList">
                               ${attendants.map(attendant => `<li>${attendant}</li>`).join('')}
                             </ul>
                             <button type="button" class="btn btn-primary" onclick="loadFlightManagement()">Return to Flight Management</button>`;
}

function loadAddUpdateFlight() {
    mainContent.innerHTML = `<h2>Add/Update Flight</h2>
                             <form onsubmit="submitAddUpdateFlight(event)">
                               <div class="form-group">
                                 <label for="flightNumber">Flight Number</label>
                                 <input type="text" class="form-control" id="flightNumber" placeholder="Enter Flight Number" required>
                               </div>
                               <div class="form-group">
                                 <label for="destination">Destination</label>
                                 <input type="text" class="form-control" id="destination" placeholder="Enter Destination" required>
                               </div>
                               <button type="submit" class="btn btn-primary">Submit</button>
                             </form>`;
}

function submitAddUpdateFlight(event) {
    event.preventDefault();
    const flightNumber = document.getElementById('flightNumber').value;
    const destination = document.getElementById('destination').value;
    alert(`Flight ${flightNumber} to ${destination} has been added/updated successfully.`);
    loadFlightManagement();
}

function loadAddUpdatePassenger() {
    mainContent.innerHTML = `<h2>Add/Update Passenger</h2>
                             <form onsubmit="submitAddUpdatePassenger(event)">
                               <div class="form-group">
                                 <label for="passengerName">Passenger Name</label>
                                 <input type="text" class="form-control" id="passengerName" placeholder="Enter Passenger Name" required>
                               </div>
                               <button type="submit" class="btn btn-primary">Submit</button>
                             </form>`;
}

function submitAddUpdatePassenger(event) {
    event.preventDefault();
    const passengerName = document.getElementById('passengerName').value;
    alert(`Passenger ${passengerName} has been added/updated successfully.`);
    loadFlightManagement();
}

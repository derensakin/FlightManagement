// Selecting necessary elements
const mainContent = document.querySelector('main');
const loginContainer = document.getElementById('login-container');
const loginForm = document.getElementById('login-form');
const passengerHomeLink = document.getElementById('passenger-home-link');
const passengerSearchFlightLink = document.getElementById('passenger-search-flight-link');
const passengerSeatingPlanLink = document.getElementById('passenger-seating-plan-link');
const passengerFlightInfoLink = document.getElementById('passenger-flight-info-link');
const passengerCabinCrewInfoLink = document.getElementById('passenger-cabin-crew-info-link');
const passengerFlightCrewInfoLink = document.getElementById('passenger-flight-crew-info-link');

let username = "";

loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (verifyCredentials(username, password)) {
        showWelcomePage();
    } else {
        alert('Invalid username or password');
    }
});

function verifyCredentials(username, password) {
    return username === 'passenger' && password === 'passenger';
}

passengerHomeLink.addEventListener('click', showWelcomePage);
passengerSearchFlightLink.addEventListener('click', openPassengerSearchFlightView);
passengerSeatingPlanLink.addEventListener('click', viewSeatingPlan);
passengerFlightInfoLink.addEventListener('click', viewFlightInformation);
passengerCabinCrewInfoLink.addEventListener('click', viewCabinCrewInformation);
passengerFlightCrewInfoLink.addEventListener('click', viewFlightCrewInformation);

// Functions to load different sections
function showWelcomePage() {
    loginContainer.style.display = 'none';
    mainContent.innerHTML = `<h2>Welcome ${username}</h2><p>We hope you have a nice day!</p>`;
}

function openPassengerSearchFlightView() {
    mainContent.innerHTML = `<div class="search-container">
                                <h2>Search Flight</h2>
                                <input type="date" id="departureDate" class="form-control" placeholder="Enter Departure Date">
                                <input type="text" id="departurePlace" class="form-control" placeholder="Enter Departure Place">
                                <button type="button" class="btn btn-primary mt-2" onclick="searchFlight()">Search</button>
                             </div>`;
}

async function fetchFlightInformation(departureDate, departurePlace) {
    return [
        { flightNumber: 'TK1234', departureDate: '2024-06-01 12:30:00', departurePlace: 'Istanbul' },
        { flightNumber: 'TK5678', departureDate: '2024-06-02 15:00:00', departurePlace: 'Ankara' }
    ];
}

async function searchFlight() {
    const departureDate = document.getElementById('departureDate').value;
    const departurePlace = document.getElementById('departurePlace').value;
    const results = await fetchFlightInformation(departureDate, departurePlace);
    displayResults(results);
}

function displayResults(results) {
    let resultsHtml = '<table class="table"><thead><tr><th>Flight Number</th><th>Departure Date</th><th>Departure Place</th></tr></thead><tbody>';
    results.forEach(result => {
        resultsHtml += `<tr><td>${result.flightNumber}</td><td>${result.departureDate}</td><td>${result.departurePlace}</td></tr>`;
    });
    resultsHtml += '</tbody></table>';
    mainContent.innerHTML = resultsHtml;
}

function viewSeatingPlan() {
    mainContent.innerHTML = `<h2>Seating Plan</h2>
                             <p>Seating plan details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Home</button>`;
}

function viewFlightInformation() {
    mainContent.innerHTML = `<h2>Flight Information</h2>
                             <p>Flight information details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Home</button>`;
}

function viewCabinCrewInformation() {
    mainContent.innerHTML = `<h2>Cabin Crew Information</h2>
                             <p>Cabin crew information details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Home</button>`;
}

function viewFlightCrewInformation() {
    mainContent.innerHTML = `<h2>Flight Crew Information</h2>
                             <p>Flight crew information details go here.</p>
                             <button type="button" class="btn btn-secondary" onclick="showWelcomePage()">Back to Home</button>`;
}

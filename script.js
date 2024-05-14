// Selecting necessary elements
const loginForm = document.getElementById('login-form');
const loginContainer = document.querySelector('.login-container');
const mainContent = document.querySelector('main');

// Event listener for the login form submission
loginForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Hide the login container and show the main content after login
    loginContainer.style.display = 'none';
    mainContent.style.display = 'block';
    loadDashboard();
});

// Selecting necessary elements for navigation links after login
const dashboardLink = document.getElementById('dashboard-link');
const flightManagementLink = document.getElementById('flight-management-link');
const bookingManagementLink = document.getElementById('booking-management-link');
const customerManagementLink = document.getElementById('customer-management-link');

// Event listeners for navigation links
dashboardLink.addEventListener('click', loadDashboard);
flightManagementLink.addEventListener('click', loadFlightManagement);
bookingManagementLink.addEventListener('click', loadBookingManagement);
customerManagementLink.addEventListener('click', loadCustomerManagement);

// Functions to load different sections
function loadDashboard() {
    mainContent.innerHTML = "<h2>Dashboard</h2><p>Welcome to the dashboard!</p>";
}

function loadFlightManagement() {
    mainContent.innerHTML = "<h2>Flight Management</h2><p>Manage flights here!</p>";
    // Append the search flight button specifically for this section
    addSearchFlightButton();
}

function addSearchFlightButton() {
    const searchFlightButton = document.createElement('button');
    searchFlightButton.innerText = 'Search Flight';
    searchFlightButton.addEventListener('click', openSearchFlightView);
    mainContent.appendChild(searchFlightButton);
}

function loadBookingManagement() {
    mainContent.innerHTML = "<h2>Booking Management</h2><p>Manage bookings here!</p>";
}

function loadCustomerManagement() {
    mainContent.innerHTML = "<h2>Customer Management</h2><p>Manage customers here!</p>";
}

function openSearchFlightView() {
    mainContent.innerHTML = `<h2>Search Flight</h2>
                             <input type="text" placeholder="Enter Flight Number" id="flightNumber">
                             <button onclick="searchFlight()">Search</button>`;
}

function searchFlight() {
    const flightNumber = document.getElementById('flightNumber').value;
    mainContent.innerHTML = `<h2>Admin Flight Info View</h2>
                             <p>Results for Flight: ${flightNumber}</p>
                             <div>Flight Crew: <span id="flightCrew">Osmail</span></div>
                             <button onclick="editFlightCrew()">Edit Crew</button>`;
}

function editFlightCrew() {
    const crewName = prompt("Change Crew Name", "Osmail");
    if (crewName !== null) {
        document.getElementById('flightCrew').textContent = crewName;
        mainContent.innerHTML += `<button onclick="commitChanges()">Commit Changes</button>`;
    }
}

function commitChanges() {
    mainContent.innerHTML = `<h2>Admin Flight Info View</h2>
                             <p>Flight crew updated successfully.</p>
                             <button onclick="loadDashboard()">Return to Dashboard</button>`;
}

// Selecting necessary elements
const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (verifyCredentials(username, password)) {
        // Redirect to the main portal page after successful login
        window.location.href = 'flight-crew.html';
    } else {
        alert('Invalid username or password');
    }
});

// Function to verify credentials (accepts any username and password)
function verifyCredentials(username, password) {
    return username !== '' && password !== '';
}

function togglePasswordVisibility(passwordFieldId, toggleButtonId) {

    /**
     * Funkcija, lai pārslēgtu paroles redzamību ievades laukā.
     * 
     * @param {string} passwordFieldId - Paroles lauka elementa ID.
     * @param {string} toggleButtonId - Pogas elementa ID, lai pārslēgtu redzamību.
     */

    try {
        const passwordField = document.getElementById(passwordFieldId);
        const toggleButton = document.getElementById(toggleButtonId);

        if (!passwordField || !toggleButton) {
            throw new Error("Password field or toggle button not found. Please check the element IDs.");
        }

        if (passwordField.type === "password") {
            passwordField.type = "text";
            toggleButton.textContent = "Hide";
        } else {
            passwordField.type = "password";
            toggleButton.textContent = "Show";
        }
    } catch (error) {
        console.error("Error in togglePasswordVisibility:", error);
        alert("An error occurred while toggling password visibility. Please try again.");
    }
}

async function validateForm(event) {

    /**
     * Validē reģistrācijas formu, pārbaudot e-pastu un paroles atbilstību.
     * 
     * @param {Event} event - Notikums, kas aktivizē funkciju (piem., pogas nospiešana).
     * @returns {boolean} - Atgriež false, ja validācija neizdodas, pretējā gadījumā iesniedz formu.
     */

    event.preventDefault();

    const email = document.getElementById('email').value;
    const emailError = document.getElementById('emailError');

    const response = await fetch('/auth/check_email?email=' + encodeURIComponent(email));
    const data = await response.json();

    if (data.exists) {
        emailError.textContent = "This email is already in use!";
        return false;
    } else {
        emailError.textContent = "";
    }

    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm_password').value;
    if (password !== confirmPassword) {
        alert('Passwords do not match!');
        return false;
    }

    event.target.submit();
}
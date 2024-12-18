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

function validateForm(event) {

    /**
     * Funkcija, lai pārbaudītu reģistrācijas formas derīgumu.
     * Pārbauda, vai paroles lauki ir aizpildīti un vai paroles sakrīt.
     * 
     * @param {Event} event - Formas iesniegšanas notikums, lai to apturētu, ja validācija neizdodas.
     */

    try {
        const passwordField = document.getElementById("password");
        const confirmPasswordField = document.getElementById("confirm_password");

        if (!passwordField || !confirmPasswordField) {
            throw new Error("Password or confirm password field not found. Please check the element IDs.");
        }

        const password = passwordField.value;
        const confirmPassword = confirmPasswordField.value;

        if (!password || !confirmPassword) {
            event.preventDefault();
            alert("Both password fields are required.");
            return;
        }

        if (password !== confirmPassword) {
            event.preventDefault();
            alert("Passwords do not match. Please try again.");
        }
    } catch (error) {
        console.error("Error in validateForm:", error);
        alert("An unexpected error occurred during form validation. Please try again.");
    }
}

let excludedProducts = new Set();

function prepareLimits() {

    /**
     * Funkcija, lai sagatavotu un validētu produktu minimālos un maksimālos ierobežojumus.
     * Saglabā ierobežojumus JSON formātā un apstrādā kļūdas.
     */

    try {
        const minLimits = {};
        const maxLimits = {};
        let hasError = false;
        let errorMessage = "";

        document.querySelectorAll("input[name^='min_limit_']").forEach(input => {
            try {
                const id = input.name.split('_')[2];
                const productName = input.closest("tr").querySelector("td:first-child").textContent.trim(); // Название продукта
                const value = parseFloat(input.value.trim());

                if (!isNaN(value) && value <= 0) {
                    errorMessage += `Error: Min limit for product "${productName}" cannot be 0 or less.\n`;
                    input.value = "";
                    hasError = true;
                } else {
                    minLimits[id] = input.value.trim() === "" ? null : value;
                }
            } catch (innerError) {
                console.error("Error processing min limit for input:", input, innerError);
                errorMessage += "An unexpected error occurred while processing min limits.\n";
                hasError = true;
            }
        });

        document.querySelectorAll("input[name^='max_limit_']").forEach(input => {
            try {
                const id = input.name.split('_')[2];
                const productName = input.closest("tr").querySelector("td:first-child").textContent.trim(); // Название продукта
                const value = parseFloat(input.value.trim());

                if (!isNaN(value) && value <= 0) {
                    errorMessage += `Error: Max limit for product "${productName}" cannot be 0 or less.\n`;
                    input.value = "";
                    hasError = true;
                } else {
                    maxLimits[id] = input.value.trim() === "" ? null : value;
                }
            } catch (innerError) {
                console.error("Error processing max limit for input:", input, innerError);
                errorMessage += "An unexpected error occurred while processing max limits.\n";
                hasError = true;
            }
        });

        for (const id in minLimits) {
            try {
                const productRow = document.querySelector(`input[name="min_limit_${id}"]`).closest("tr");
                const productName = productRow.querySelector("td:first-child").textContent.trim(); // Название продукта

                if (minLimits[id] !== null && maxLimits[id] !== null && minLimits[id] > maxLimits[id]) {
                    errorMessage += `Error: Min limit for product "${productName}" (${minLimits[id]}) is greater than Max limit (${maxLimits[id]}).\n`;
                    hasError = true;
                }

                if (minLimits[id] !== null && maxLimits[id] !== null && minLimits[id] === maxLimits[id]) {
                    errorMessage += `Error: Min and Max limits cannot be the same for product "${productName}".\n`;
                    hasError = true;
                }
            } catch (innerError) {
                console.error("Error validating limits for product ID:", id, innerError);
                errorMessage += "An unexpected error occurred while validating limits.\n";
                hasError = true;
            }
        }

        if (hasError) {
            alert(errorMessage.trim());
            setTimeout(() => {
                location.reload();
            }, 100);
            return;
        }

        document.getElementById('min_limits_input').value = JSON.stringify(minLimits);
        document.getElementById('max_limits_input').value = JSON.stringify(maxLimits);
        document.getElementById('excluded_products_input').value = JSON.stringify([...excludedProducts]);

    } catch (error) {
        console.error("Error in prepareLimits:", error);
        alert("An unexpected error occurred while preparing limits. Please try again.");
    }
}

function renderRows(products) {

    /**
     * Funkcija, lai dinamiski attēlotu produktu rindas HTML tabulā.
     * Apstrādā produktu sarakstu, ģenerē rindu katram produktam un pievieno to tabulai.
     */

    try {
        if (!Array.isArray(products)) {
            throw new Error("Invalid products data: expected an array.");
        }
    tableBody.innerHTML = "";

    products.forEach(product => {
        try {
            const row = document.createElement("tr");

            const nameCell = document.createElement("td");
            nameCell.textContent = product.nosaukums;

            const minCell = document.createElement("td");
            const minInput = document.createElement("input");
            minInput.type = "number";
            minInput.name = `min_limit_${product.id}`;
            minInput.step = "0.0001";
            minInput.value = minLimits[product.id] || "";
            minInput.disabled = excludedProducts.has(product.id);
            minCell.appendChild(minInput);

            const maxCell = document.createElement("td");
            const maxInput = document.createElement("input");
            maxInput.type = "number";
            maxInput.name = `max_limit_${product.id}`;
            maxInput.step = "0.0001";
            maxInput.value = maxLimits[product.id] || "";
            maxInput.disabled = excludedProducts.has(product.id);
            maxCell.appendChild(maxInput);

            const excludeCell = document.createElement("td");
            const excludeCheckbox = document.createElement("input");
            excludeCheckbox.type = "checkbox";
            excludeCheckbox.name = `exclude_product_${product.id}`;
            excludeCheckbox.checked = excludedProducts.has(product.id);
            excludeCheckbox.addEventListener("change", () => {
                if (excludeCheckbox.checked) {
                    excludedProducts.add(product.id);
                    minInput.disabled = true;
                    maxInput.disabled = true;
                    minInput.value = "";
                    maxInput.value = "";
                } else {
                    excludedProducts.delete(product.id);
                    minInput.disabled = false;
                    maxInput.disabled = false;
                }
            });
            excludeCell.appendChild(excludeCheckbox);

            row.appendChild(nameCell);
            row.appendChild(minCell);
            row.appendChild(maxCell);
            row.appendChild(excludeCell);

            tableBody.appendChild(row);

        } catch (productError) {
            console.error(`Error rendering product with ID ${product.id}:`, productError);
        }
    });

    } catch (error) {
        console.error("Error in renderRows:", error);
        alert("An error occurred while rendering rows. Please check the console for details.");
    }
}

function applyFilters(allProducts) {

    /**
     * Funkcija, lai filtrētu produktu sarakstu pēc lietotāja ievadītajiem kritērijiem.
     * Filtrētie produkti tiek attēloti tabulā.
     * 
     * @param {Array} allProducts - Produktu saraksts, kas tiks filtrēts.
     * @returns {Array} - Filtrētais produktu saraksts.
     */

    try {
        if (!Array.isArray(allProducts)) {
            throw new Error("Invalid allProducts data: expected an array.");
        }

        if (!allProducts || allProducts.length === 0) {
            console.error("No products available to filter.");
            return [];
        }

        const categoryValue = document.getElementById("categoryFilter").value.trim();
        const veganValue = document.getElementById("veganFilter").value.trim();
        const searchValue = document.getElementById("productSearch").value.toLowerCase().trim();

        const filteredProducts = allProducts.filter(product => {
            const matchesSearch = product.nosaukums.toLowerCase().includes(searchValue);
            const matchesCategory = categoryValue === "" || product.kategorija_key == categoryValue;
            const matchesVegan = veganValue === "" || (veganValue === "1" ? product.vegan : !product.vegan);
            return matchesSearch && matchesCategory && matchesVegan;
        });

        renderRows(filteredProducts);
        return filteredProducts;

    } catch (error) {
        console.error("Error in applyFilters:", error);
        alert("An error occurred while filtering products. Please check the console for details.");
        return [];
    }
}


function setLimitsForFiltered() {

    /**
     * Funkcija, lai uzstādītu minimālos un maksimālos limitus visiem filtrētajiem produktiem.
     * 
     * Ievadītās vērtības (Min un/vai Max) tiek piemērotas visiem produktiem, 
     * kas atbilst pašreizējiem filtriem, izņemot produktus, kuri ir izslēgti (excluded).
     * 
     * Nosacījumi:
     * - Min un Max nevar būt mazāki vai vienādi ar 0.
     * - Min nevar būt lielāks par Max.
     */

    try {
        const minInputValue = parseFloat(document.getElementById("massMinLimit").value.trim());
        const maxInputValue = parseFloat(document.getElementById("massMaxLimit").value.trim());

        if ((isNaN(minInputValue) || minInputValue <= 0) && (isNaN(maxInputValue) || maxInputValue <= 0)) {
            alert("Please enter valid values greater than 0 for Min and/or Max limits.");
            return;
        }

        const filteredProducts = applyFilters(allProducts);

        filteredProducts.forEach(product => {
            if (excludedProducts.has(product.id)) return;

            const minInput = document.querySelector(`input[name="min_limit_${product.id}"]`);
            const maxInput = document.querySelector(`input[name="max_limit_${product.id}"]`);

            if (!isNaN(minInputValue) && minInputValue > 0) {
                if (isNaN(maxInputValue) || minInputValue <= parseFloat(maxInput.value) || maxInput.value === "") {
                    minInput.value = minInputValue;
                } else {
                    console.warn(`Min limit is greater than Max limit for product ID ${product.id}.`);
                }
            }

            if (!isNaN(maxInputValue) && maxInputValue > 0) {
                if (isNaN(minInputValue) || maxInputValue >= parseFloat(minInput.value) || minInput.value === "") {
                    maxInput.value = maxInputValue;
                } else {
                    console.warn(`Max limit is less than Min limit for product ID ${product.id}.`);
                }
            }
        });

    } catch (error) {
        console.error("Error in setLimitsForFiltered:", error);
    }
}


function clearLimitsForFiltered() {

    /**
     * Funkcija, lai notīrītu minimālos un maksimālos limitus visiem filtrētajiem produktiem.
     * 
     * Attīra Min un Max ievades laukus visiem produktiem, kas atbilst pašreizējiem filtriem,
     * izņemot produktus, kuri ir izslēgti (excluded).
     */

    try {
        const filteredProducts = applyFilters(allProducts);

        filteredProducts.forEach(product => {
            if (excludedProducts.has(product.id)) return;

            const minInput = document.querySelector(`input[name="min_limit_${product.id}"]`);
            const maxInput = document.querySelector(`input[name="max_limit_${product.id}"]`);

            if (minInput) minInput.value = "";
            if (maxInput) maxInput.value = "";
        });

    } catch (error) {
        console.error("Error in clearLimitsForFiltered:", error);
    }
}



function excludeFilteredProducts() {

    /**
     * Funkcija, lai izslēgtu filtrētos produktus no turpmākās apstrādes.
     * Pievieno produktu ID sarakstam `excludedProducts` un atjauno tabulu.
     */

    try {
        const filteredProducts = applyFilters(allProducts);
        filteredProducts.forEach(product => excludedProducts.add(product.id));
        renderRows(filteredProducts);
    } catch (error) {
        console.error("Error in excludeFilteredProducts:", error);
        alert("An error occurred while excluding filtered products. Please try again.");
    }
}

function clearExcludedFilteredProducts() {

    /**
     * Funkcija, lai notīrītu izslēgto produktu sarakstu `excludedProducts`.
     * Noņem produktu ID no saraksta un atjauno tabulu.
     */

    try {
        const filteredProducts = applyFilters(allProducts);
        filteredProducts.forEach(product => excludedProducts.delete(product.id));
        renderRows(filteredProducts);
    } catch (error) {
        console.error("Error in clearExcludedFilteredProducts:", error);
        alert("An error occurred while clearing excluded products. Please try again.");
    }
}

function deleteProduct(productId) {

    /**
     * Funkcija, lai dzēstu produktu pēc tā ID.
     * Sūta POST pieprasījumu uz serveri un pārbauda atbildi.
     */

    if (!productId) {
        alert("Invalid product ID. Cannot delete.");
        return;
    }

    if (confirm('Are you sure you want to delete this product?')) {
        fetch('/product_bp/delete_product', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `product_id=${productId}`,
        })
        .then(response => {
            if (response.ok) {
                alert('Product deleted successfully!');
                location.reload();
            } else {
                response.text().then(text => {
                    console.error(`Failed to delete product: ${text}`);
                    alert(`Failed to delete the product. Server responded with: ${text}`);
                });
            }
        })
        .catch(error => {
            console.error('Network or server error:', error);
            alert('A network or server error occurred while deleting the product. Please try again later.');
        });
    }
}

function saveRow(productId) {

    /**
     * Funkcija, lai saglabātu izmaiņas produktam, pamatojoties uz lietotāja ievadītajiem datiem.
     * Veic validāciju un nosūta atjauninātos datus uz serveri.
     * 
     * @param {number} productId - Produkta unikālais identifikators.
     */

    try {
        const row = document.querySelector(`[data-id="${productId}"]`).parentElement.parentElement;
        if (!row) {
            throw new Error(`Row not found for product ID: ${productId}`);
        }

        const formData = new FormData();

        function parseOrNull(value) {
            if (!value || value.trim() === '' || isNaN(value)) {
                return null;
            }
            return parseFloat(value);
        }

        const productName = row.querySelector('input[data-field="nosaukums"]').value.trim();
        const maximaLink = row.querySelector('input[data-field="saite_maxima"]').value.trim();
        const rimiLink = row.querySelector('input[data-field="saite_rimi"]').value.trim();

        if (!productName) {
            alert("Product name cannot be empty.");
            return;
        }

        const existingNames = allProducts
            .filter(product => product.id !== productId)
            .map(product => product.nosaukums.toLowerCase());

        if (existingNames.includes(productName.toLowerCase())) {
            alert("A product with this name already exists. Please use a different name.");
            return;
        }

        if (maximaLink && !maximaLink.startsWith("https://www.barbora.lv/")) {
            alert("Maxima link must start with 'https://www.barbora.lv/'.");
            return;
        }

        if (rimiLink && !rimiLink.startsWith("https://www.rimi.lv/")) {
            alert("Rimi link must start with 'https://www.rimi.lv/'.");
            return;
        }

        formData.append('id', productId);
        formData.append('nosaukums', productName);
        formData.append('kalorijas', parseOrNull(row.querySelector('input[data-field="kalorijas"]').value));
        formData.append('olbaltumvielas', parseOrNull(row.querySelector('input[data-field="olbaltumvielas"]').value));
        formData.append('tauki', parseOrNull(row.querySelector('input[data-field="tauki"]').value));
        formData.append('oglhidrati', parseOrNull(row.querySelector('input[data-field="oglhidrati"]').value));
        formData.append('cena_maxima', parseOrNull(row.querySelector('input[data-field="cena_maxima"]').value));
        formData.append('cena_rimi', parseOrNull(row.querySelector('input[data-field="cena_rimi"]').value));
        formData.append('saite_maxima', maximaLink || null);
        formData.append('saite_rimi', rimiLink || null);
        formData.append('meris_vieniba', row.querySelector('input[data-field="meris_vieniba"]').value.trim() || null);
        formData.append('kategorija_key', row.querySelector('select[data-field="kategorija_key"]').value || null);
        formData.append('vegan', row.querySelector('select[data-field="vegan"]').value || null);

        fetch('/product_bp/update_product', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (response.ok) {
                alert('Product updated successfully!');
                location.reload();
            } else {
                response.text().then(text => alert(`Failed to update the product: ${text}`));
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the product.');
        });

    } catch (error) {
        console.error('Error in saveRow:', error);
        alert(`Failed to save the product. Error: ${error.message}`);
    }
}


function renderRows(products) {

    /**
     * Funkcija, lai attēlotu produktu sarakstu HTML tabulā.
     * Apstrādā produktu sarakstu un dinamiski pievieno rindu katram produktam.
     */

    try {
        const tableBody = document.getElementById("productTable").querySelector("tbody");
        if (!tableBody) {
            throw new Error("Table body element not found. Please ensure the table structure is correct.");
        }
    tableBody.innerHTML = "";

    products.forEach(product => {
        try {
        const hasFailedUrls = product.failed_urls && product.failed_urls.length > 0;

        const row = document.createElement("tr");
        row.innerHTML = `
            <td><input type="text" value="${product.nosaukums || ''}" data-id="${product.id}" data-field="nosaukums"></td>
            <td><input type="number" step="0.01" value="${product.kalorijas !== null ? product.kalorijas : ''}" data-id="${product.id}" data-field="kalorijas"></td>
            <td><input type="number" step="0.01" value="${product.olbaltumvielas !== null ? product.olbaltumvielas : ''}" data-id="${product.id}" data-field="olbaltumvielas"></td>
            <td><input type="number" step="0.01" value="${product.tauki !== null ? product.tauki : ''}" data-id="${product.id}" data-field="tauki"></td>
            <td><input type="number" step="0.01" value="${product.oglhidrati !== null ? product.oglhidrati : ''}" data-id="${product.id}" data-field="oglhidrati"></td>
            <td>
                <input 
                    type="text" 
                    value="${product.saite_maxima || ''}" 
                    class="${hasFailedUrls && product.failed_urls.includes(product.saite_maxima) ? 'highlight-error' : ''}" 
                    data-id="${product.id}" 
                    data-field="saite_maxima">
            </td>
            <td><input type="number" step="0.01" value="${product.cena_maxima !== null ? product.cena_maxima : ''}" data-id="${product.id}" data-field="cena_maxima"></td>
            <td>
                <input 
                    type="text" 
                    value="${product.saite_rimi || ''}" 
                    class="${hasFailedUrls && product.failed_urls.includes(product.saite_rimi) ? 'highlight-error' : ''}" 
                    data-id="${product.id}" 
                    data-field="saite_rimi">
            </td>
            <td><input type="number" step="0.01" value="${product.cena_rimi !== null ? product.cena_rimi : ''}" data-id="${product.id}" data-field="cena_rimi"></td>
            <td><input type="text" value="${product.meris_vieniba || ''}" data-id="${product.id}" data-field="meris_vieniba"></td>
            <td>
                <select data-id="${product.id}" data-field="kategorija_key">
                    ${categories.map(cat => `
                        <option value="${cat.kategorija_key}" ${product.kategorija_key == cat.kategorija_key ? 'selected' : ''}>
                            ${cat.nosaukums}
                        </option>
                    `).join('')}
                </select>
            </td>
            <td>
                <select data-id="${product.id}" data-field="vegan">
                    <option value="1" ${product.vegan ? 'selected' : ''}>Yes</option>
                    <option value="0" ${!product.vegan ? 'selected' : ''}>No</option>
                </select>
            </td>
            <td>
                <button class="save-button" onclick="saveRow(${product.id})">Save</button>
                <button class="delete-button" onclick="deleteProduct(${product.id})" style="margin-left: 10px;">Delete</button>
            </td>
        `;
        tableBody.appendChild(row);
        } catch (productError) {
            console.error(`Error rendering product ID ${product.id}:`, productError);
        }
    });
    } catch (error) {
        console.error("Error in renderRows:", error);
        alert("An error occurred while rendering the table rows. Please try again later.");
    }
}

function applyFilters() {

    /**
     * Funkcija, lai piemērotu filtrus produktu sarakstam.
     * Atlasītie produkti tiek attēloti tabulā pēc norādītajiem filtriem.
     */

    try {
        const searchValue = document.getElementById("productSearch").value.toLowerCase().trim();
        const categoryValue = document.getElementById("categoryFilter").value;
        const veganValue = document.getElementById("veganFilter").value;
        const failedUrlsValue = document.getElementById("failedUrlsFilter").value;

        if (!allProducts || allProducts.length === 0) {
            console.warn("No products available to filter.");
            alert("No products found for filtering.");
            return;
        }

        const filteredProducts = allProducts.filter(product => {
            const matchesSearch = product.nosaukums.toLowerCase().includes(searchValue);
            const matchesCategory = !categoryValue || parseInt(product.kategorija_key) === parseInt(categoryValue);
            const matchesVegan = !veganValue || product.vegan.toString() === veganValue;
            const matchesFailedUrls = !failedUrlsValue || (failedUrlsValue === "1" && product.failed_urls?.length > 0);

            return matchesSearch && matchesCategory && matchesVegan && matchesFailedUrls;
        });

        renderRows(filteredProducts);

    } catch (error) {
        console.error("Error in applyFilters:", error);
        alert("An error occurred while applying filters. Please try again.");
    }
}

document.addEventListener("DOMContentLoaded", () => {

    /**
     * Noklusējuma funkcija, kas tiek izsaukta, kad lapa ir pilnībā ielādēta.
     * Inicializē pogas darbības un pievieno apstrādātājus.
     */

    const container = document.getElementById("productTablesContainer");
    const addTableButton = document.getElementById("addTable");

    async function validateProduct(table, existingNames = []) {

        /**
         * Funkcija, lai validētu ievadītos produkta datus.
         * 
         * @param {HTMLElement} table - Tabulas rinda ar produkta datiem.
         * @param {Array} existingNames - Saraksts ar jau esošajiem produktu nosaukumiem.
         * @returns {boolean} - True, ja dati ir derīgi; False, ja nav.
         */

        const name = table.querySelector('input[name="nosaukums"]').value.trim();
        const maximaLink = table.querySelector('input[name="saite_maxima"]').value.trim();
        const rimiLink = table.querySelector('input[name="saite_rimi"]').value.trim();

        if (!name) { // Pārbauda, vai nosaukums nav tukšs.
            alert("Product name cannot be empty.");
            return false;
        }

        // Pārbauda, vai nosaukums jau eksistē.
        if (existingNames.includes(name.toLowerCase())) {
            alert(`A product with the name "${name}" already exists. Please use a different name.`);
            return false;
        }

        // Pārbauda, vai saites atbilst prasītajam formātam.
        if (maximaLink && !maximaLink.startsWith("https://www.barbora.lv/")) {
            alert("Maxima link must start with 'https://www.barbora.lv/'.");
            return false;
        }
        if (rimiLink && !rimiLink.startsWith("https://www.rimi.lv/")) {
            alert("Rimi link must start with 'https://www.rimi.lv/'.");
            return false;
        }
        return true;
    }

    async function addSingleProduct(table) {

        /**
         * Funkcija, lai pievienotu vienu produktu.
         * Validē datus un sūta POST pieprasījumu serverim.
         * 
         * @param {HTMLElement} table - Tabulas rinda ar produkta datiem.
         */

        const existingNames = await fetch('/product_bp/get_existing_names')
            .then(response => response.json())
            .catch(() => []);

        if (!await validateProduct(table, existingNames)) return;

        const formData = new FormData();
        table.querySelectorAll("input, select").forEach(input => {
            formData.append(input.name, input.value.trim());
        });

        fetch('/product_bp/add_single_product', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                alert(result.error || "Failed to add product.");
            } else {
                alert("Product added successfully!");
                window.location.href = '/product_bp/manage_products';
            }
        })
        .catch(error => alert("Network error: " + error.message));
    }

    async function addAllProducts(event) {

        /**
         * Funkcija, lai pievienotu visus produktus no tabulas.
         * Validē katru produktu un sūta datus serverim.
         * 
         * @param {Event} event - Formas iesniegšanas notikums.
         */

        event.preventDefault();

        const existingNames = await fetch('/product_bp/get_existing_names')
            .then(response => response.json())
            .catch(() => []);

        const tables = container.querySelectorAll(".product-table");
        const products = [];
        let errors = [];

        for (let index = 0; index < tables.length; index++) {
            const table = tables[index];
            const isValid = await validateProduct(table, existingNames);

            if (!isValid) {
                errors.push(`Table ${index + 1}: Validation failed.`);
                continue;
            }

            const product = {};
            table.querySelectorAll("input, select").forEach(input => {
                product[input.name] = input.value.trim();
            });
            products.push(product);
        }

        if (errors.length > 0) {
            alert(errors.join("\n"));
            return;
        }

        // Nosūta visus produktus serverim.
        try {
            const response = await fetch('/product_bp/add_product', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(products)
            });

            const result = await response.json();

            if (!response.ok) {
                alert(result.errors ? result.errors.join("\n") : result.error);
            } else {
                alert("All products added successfully!");
                window.location.href = '/product_bp/manage_products';
            }
        } catch (error) {
            alert("Failed to add products due to a network error.");
        }
    }

    function setupTableActions(table) {

        /**
         * Funkcija, lai pievienotu darbības pogām tabulā.
         * 
         * @param {HTMLElement} table - Tabulas rinda ar produktiem.
         */

        const addProductButton = table.querySelector(".addProduct");
        addProductButton.addEventListener("click", () => addSingleProduct(table));

        const deleteButton = table.querySelector(".deleteRow");
        deleteButton.disabled = false;
        deleteButton.addEventListener("click", () => {
            if (container.children.length > 1) {
                container.removeChild(table); // Dzēš tabulu, ja ir vairāk par vienu.
            } else {
                alert("At least one table must remain!"); 
            }
        });
    }

    addTableButton.addEventListener("click", () => {

        /**
         * Pievieno jaunu tabulu un inicializē tās darbības pogas.
         */

        const newTable = container.querySelector(".product-table").cloneNode(true);
        newTable.querySelectorAll("input").forEach(input => input.value = "");
        newTable.querySelectorAll("select").forEach(select => select.selectedIndex = 0);
        setupTableActions(newTable);
        container.appendChild(newTable);
    });

    setupTableActions(container.querySelector(".product-table"));
    document.getElementById("productForm").addEventListener("submit", addAllProducts);
});

document.addEventListener("DOMContentLoaded", () => {

    // Saites uz HTML elementiem
    const addCategoryButton = document.getElementById("addCategoryButton");
    const deleteCategoryButton = document.getElementById("deleteCategoryButton");
    const newCategoryInput = document.getElementById("newCategoryInput");
    const categoryDropdown = document.getElementById("categoryDropdown");

    /**
     * Funkcija, lai sakārtotu kategoriju nolaižamo sarakstu pēc vērtībām augošā secībā.
     */
    function sortDropdown() {
        const options = Array.from(categoryDropdown.options).slice(1);
        options.sort((a, b) => parseInt(a.value) - parseInt(b.value));

        categoryDropdown.innerHTML = '<option value="all">All</option>';
        options.forEach(option => categoryDropdown.appendChild(option));
    }

    /**
     * Pievieno jaunu kategoriju, validē nosaukumu un nosūta pieprasījumu serverim.
     */
    addCategoryButton.addEventListener("click", () => {
        const categoryName = newCategoryInput.value.trim();

        if (!categoryName) {
            alert("Category name cannot be empty.");
            return;
        }

        const existingCategories = Array.from(categoryDropdown.options).map(opt => opt.textContent.toLowerCase());
        if (existingCategories.includes(categoryName.toLowerCase())) {
            alert("This category already exists.");
            return;
        }

        fetch('/product_bp/add_category', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: categoryName })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert("Category added successfully!");
                window.location.href = '/product_bp/manage_products';
            } else {
                alert(`Failed to add category: ${data.error}`);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while adding the category.");
        });
    });

    /**
     * Dzēš izvēlēto kategoriju pēc apstiprinājuma un nosūta pieprasījumu serverim.
     */
    deleteCategoryButton.addEventListener("click", () => {
        const selectedCategory = categoryDropdown.value;

        if (selectedCategory === "all") {
            alert("Please select a category to delete.");
            return;
        }

        if (!confirm("Are you sure you want to delete this category? This action cannot be undone.")) {
            return;
        }

        fetch(`/product_bp/delete_category/${selectedCategory}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert("Category deleted successfully!");
                window.location.href = '/product_bp/manage_products';
            } else {
                alert(`Failed to delete category: ${data.error}`);
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while deleting the category.");
        });
    });

    sortDropdown();
});

document.addEventListener("DOMContentLoaded", () => {
    const downloadTemplate = document.getElementById("download-template");
    const downloadExample = document.getElementById("download-example");
    const uploadFile = document.getElementById("upload-file");
    const uploadData = document.getElementById("upload-data");
    const uploadStatus = document.getElementById("upload-status");
    const fileNameDisplay = document.getElementById("file-name");

    uploadFile.addEventListener("change", () => {
        if (uploadFile.files.length > 0) {
            fileNameDisplay.textContent = uploadFile.files[0].name;
        } else {
            fileNameDisplay.textContent = "No file chosen";
        }
    });

    /**
     * Lejupielādē veidni.
     * Virzīšana uz servera maršrutu, lai lejupielādētu failu "template".
     */
    downloadTemplate.addEventListener("click", () => {
        window.location.href = '/product_bp/download_template';
    });

    /**
     * Lejupielādē piemēra failu.
     * Virzīšana uz servera maršrutu, lai lejupielādētu failu "example".
     */
    downloadExample.addEventListener("click", () => {
        window.location.href = '/product_bp/download_example';
    });

    /**
     * Augšupielādē izvēlēto failu un nosūta to serverim apstrādei.
     */
    uploadData.addEventListener("click", () => {
        const file = uploadFile.files[0];

        if (!file) {
            uploadStatus.textContent = "Please select a file to upload.";
            return;
        }

        const formData = new FormData();
        formData.append("file", file);

        fetch("/product_bp/upload_products", {
            method: "POST",
            body: formData 
        })
        .then(response => response.json())
        .then(data => {
            if (data.errors && data.errors.length > 0) {
                uploadStatus.textContent = "Errors: " + data.errors.join(", ");
            } else {
                uploadStatus.style.color = "green";
                uploadStatus.textContent = "Products uploaded successfully!";
                window.location.reload();
            }
        })
        .catch(error => {
            console.error("Upload error:", error);
            uploadStatus.textContent = "An error occurred during upload.";
        });
    });
});
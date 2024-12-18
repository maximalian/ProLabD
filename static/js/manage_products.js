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
     * Funkcija, lai saglabātu atjauninātu produkta informāciju.
     * Sūta POST pieprasījumu ar produkta datiem uz serveri.
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

    formData.append('id', productId);
    formData.append('nosaukums', row.querySelector('input[data-field="nosaukums"]').value.trim());
    formData.append('kalorijas', parseOrNull(row.querySelector('input[data-field="kalorijas"]').value));
    formData.append('olbaltumvielas', parseOrNull(row.querySelector('input[data-field="olbaltumvielas"]').value));
    formData.append('tauki', parseOrNull(row.querySelector('input[data-field="tauki"]').value));
    formData.append('oglhidrati', parseOrNull(row.querySelector('input[data-field="oglhidrati"]').value));
    formData.append('cena_maxima', parseOrNull(row.querySelector('input[data-field="cena_maxima"]').value));
    formData.append('cena_rimi', parseOrNull(row.querySelector('input[data-field="cena_rimi"]').value));
    formData.append('saite_maxima', row.querySelector('input[data-field="saite_maxima"]').value.trim() || null);
    formData.append('saite_rimi', row.querySelector('input[data-field="saite_rimi"]').value.trim() || null);
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
    
    }  catch (error) {
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
                <button onclick="saveRow(${product.id})">Save</button>
                <button onclick="deleteProduct(${product.id})" style="margin-left: 10px;">Delete</button>
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
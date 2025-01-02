function validateStoreSelection() {

    /**
     * Funkcija, lai pārbaudītu, vai lietotājs ir izvēlējies vismaz vienu veikalu.
     * 
     * @returns {boolean} - True, ja veikals ir izvēlēts; False, ja nav.
     */

    try {
        const maximaCheckbox = document.getElementById('store_maxima');
        const rimiCheckbox = document.getElementById('store_rimi');

        if (!maximaCheckbox || !rimiCheckbox) {
            throw new Error("One or both store selection checkboxes are missing.");
        }

        if (!maximaCheckbox.checked && !rimiCheckbox.checked) {
            alert("Please select at least one store (Maxima or Rimi).");
            return false;
        }
        return true;
    } catch (error) {
        console.error("Error in validateStoreSelection:", error.message);
        alert("An unexpected error occurred while validating store selection.");
        return false;
    }
}

try {
    const chartDataDiv = document.getElementById('chartData');
    if (!chartDataDiv) {
        throw new Error("Chart data div is missing in the DOM.");
    }

    let nutrientsObtained, normsData;

    try {
        nutrientsObtained = JSON.parse(chartDataDiv.getAttribute('data-nutrients-obtained'));
        normsData = JSON.parse(chartDataDiv.getAttribute('data-daily-norms'));

        if (!nutrientsObtained || !normsData) {
            throw new Error("Chart data attributes are invalid or missing.");
        }
    } catch (parseError) {
        console.error("Error parsing chart data:", parseError.message);
        alert("Invalid chart data format. Please contact support.");
        throw parseError;
    }

    const ctx = document.getElementById('nutrientChart');
    if (!ctx) {
        throw new Error("Canvas element for the chart is missing.");
    }

    new Chart(ctx.getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Proteins (g)', 'Fats (g)', 'Carbohydrates (g)', 'Calories (kcal)'],
            datasets: [
                {
                    label: 'Obtained',
                    data: [
                        nutrientsObtained.Proteins || 0,
                        nutrientsObtained.Fats || 0,
                        nutrientsObtained.Carbohydrates || 0,
                        nutrientsObtained.Calories || 0
                    ],
                    backgroundColor: 'rgba(54, 162, 235, 0.6)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                },
                {
                    label: 'Daily Norms',
                    data: [
                        normsData.Protein || 0,
                        normsData.Fat || 0,
                        normsData.Carbs || 0,
                        normsData.Calories || 0
                    ],
                    backgroundColor: 'rgba(255, 99, 132, 0.6)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: (context) => `${context.dataset.label}: ${context.raw.toFixed(2)}`,
                    },
                },
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Grams / Calories',
                    },
                },
            },
        },
    });
} catch (error) {
    console.error("Error while rendering the chart:", error.message);
    alert("An error occurred while generating the chart. Please try again later.");
}


document.addEventListener("DOMContentLoaded", () => {

    // === Sagatavo pogu DOCX dokumenta lejupielādei ===
    const downloadDocButton = document.getElementById("downloadDoc");

    /**
     * Noklausīšanās notikuma pievienošana pogai lejupielādei.
     * Pēc noklikšķināšanas sāk DOCX dokumenta ģenerēšanas procesu.
     */
    downloadDocButton.addEventListener("click", () => {
        console.log("DOCX generation started...");

        const firstName = document.documentElement.getAttribute('data-first-name') || "Unknown";
        const lastName = document.documentElement.getAttribute('data-last-name') || "User";
        const fileName = `${firstName}_${lastName}_results.docx`; // Veido faila nosaukumu

        // === 2. Pārbauda, vai ir dati eksportam ===
        const element = document.getElementById("results");
        const chart = document.getElementById('nutrientChart');

        if (!element || !chart) {
            alert("Error: Content not found!");
            return;
        }

        const exportElement = document.createElement('div');
        exportElement.innerHTML = element.outerHTML;

        exportElement.querySelector(".button-container")?.remove();

        const headings = exportElement.querySelectorAll('h2');
        let comparisonHeading = null;

        headings.forEach(heading => {
            if (heading.textContent.includes("Daily Nutrient Comparison")) {
                comparisonHeading = heading;
            }
        });

        if (comparisonHeading) {
            const chartImage = chart.toDataURL('image/png');

            const img = document.createElement('img');
            img.src = chartImage;
            img.setAttribute("width", "650");
            img.setAttribute("height", "400");
            img.style.marginTop = "10px";
            img.style.display = "block";

            comparisonHeading.insertAdjacentElement('afterend', img);
        }

        const htmlContent = `
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Diet Calculation Results</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 20px;
                        padding: 20px;
                        background-color: #f4f4f9;
                        position: relative;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                    }
                    th, td {
                        border: 1px solid #ddd;
                        padding: 8px;
                        text-align: center;
                        min-width: 120px;
                        white-space: nowrap;
                    }
                    th {
                        background-color: #f2f2f2;
                        font-weight: bold;
                    }
                    .highlight {
                        background-color: lightgreen;
                    }
                    .daily-obtained td:first-child {
                        background-color: #86c7f3;
                        font-weight: bold;
                    }
                    .daily-norms td:first-child {
                        background-color: #ffa1b5;
                        font-weight: bold;
                    }

                    .header-logo {
                        position: absolute;
                        top: 10px;
                        right: 10px;
                        display: flex;
                        align-items: center;
                        gap: 10px;
                    }
                    .header-logo img {
                        width: 40px;
                        height: 40px;
                    }
                    .header-logo span {
                        font-size: 16px;
                        font-weight: bold;
                        color: #333;
                    }
                </style>
            </head>
            <body>
                ${exportElement.innerHTML}
            </body>
            </html>
            `;



        const docx = htmlDocx.asBlob(htmlContent); // Ģenerē DOCX failu no HTML

        const link = document.createElement("a");
        link.href = URL.createObjectURL(docx);
        link.download = fileName;
        link.click();
    });
});

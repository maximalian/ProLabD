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

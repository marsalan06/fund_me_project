const financeData = [
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "1",
        "Cycle/ Frequency": "4 Quarters",
        "Length of Inv.(Months)": "4",
        "Profit Rate": "20%",
        "Principal plus Profit": "1,215,506.25 Rs",
        "Profit Earned": "215,506.25 Rs",
        "Taxes 2%": "4,310.13 Rs",
        "NET PROFIT": "211,196.13 Rs",
        "Category": "Quarterly",
        "Subcategory": "1 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "3",
        "Cycle/ Frequency": "4 Quarters",
        "Length of Inv.(Months)": "12",
        "Profit Rate": "20%",
        "Principal plus Profit": "1,795,856.33 Rs",
        "Profit Earned": "795,856.33 Rs",
        "Taxes 2%": "15,917.13 Rs",
        "NET PROFIT": "779,939.20 Rs",
        "Category": "Quarterly",
        "Subcategory": "3 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "5",
        "Cycle/ Frequency": "4 Quarters",
        "Length of Inv.(Months)": "20",
        "Profit Rate": "20%",
        "Principal plus Profit": "2,653,297.71 Rs",
        "Profit Earned": "1,653,297.71 Rs",
        "Taxes 2%": "33,065.95 Rs",
        "NET PROFIT": "1,620,231.75 Rs",
        "Category": "Quarterly",
        "Subcategory": "5 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "10",
        "Cycle/ Frequency": "4 Quarters",
        "Length of Inv.(Months)": "40",
        "Profit Rate": "20%",
        "Principal plus Profit": "7,039,988.71 Rs",
        "Profit Earned": "6,039,988.71 Rs",
        "Taxes 2%": "120,799.77 Rs",
        "NET PROFIT": "5,919,188.94 Rs",
        "Category": "Quarterly",
        "Subcategory": "10 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "15",
        "Cycle/ Frequency": "4 Quarters",
        "Length of Inv.(Months)": "60",
        "Profit Rate": "20%",
        "Principal plus Profit": "18,679,185.89 Rs",
        "Profit Earned": "17,679,185.89 Rs",
        "Taxes 2%": "353,583.72 Rs",
        "NET PROFIT": "17,325,602.18 Rs",
        "Category": "Quarterly",
        "Subcategory": "15 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "1",
        "Rate of Profit": "20%",
        "Profit for the period": "16,666.67 Rs",
        "Taxes 2%": "333.33 Rs",
        "NET PROFIT": "16,333.33 Rs",
        "Category": "Monthly",
        "Subcategory": "Monthly"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "3",
        "Rate of Profit": "20%",
        "Profit for the period": "50,000.00 Rs",
        "Taxes 2%": "1,000.00 Rs",
        "NET PROFIT": "49,000.00 Rs",
        "Category": "Monthly",
        "Subcategory": "Quarterly"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "6",
        "Rate of Profit": "20%",
        "Profit for the period": "100,000.00 Rs",
        "Taxes 2%": "2,000.00 Rs",
        "NET PROFIT": "98,000.00 Rs",
        "Category": "Monthly",
        "Subcategory": "6 Months"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "12",
        "Rate of Profit": "20%",
        "Principal plus Profit": "1,219,391.08 Rs",
        "Profit for the period": "219,391.08 Rs",
        "Taxes 2%": "4,387.82 Rs",
        "NET PROFIT": "215,003.26 Rs",
        "Category": "Monthly",
        "Subcategory": "12 Months"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "36",
        "Rate of Profit": "20%",
        "Principal plus Profit": "1,813,130.43 Rs",
        "Profit for the period": "813,130.43 Rs",
        "Taxes 2%": "16,262.61 Rs",
        "NET PROFIT": "796,867.82 Rs",
        "Category": "Monthly",
        "Subcategory": "3 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "60",
        "Rate of Profit": "20%",
        "Principal plus Profit": "2,695,970.14 Rs",
        "Profit for the period": "1,695,970.14 Rs",
        "Taxes 2%": "33,919.40 Rs",
        "NET PROFIT": "1,662,050.74 Rs",
        "Category": "Monthly",
        "Subcategory": "5 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "120",
        "Rate of Profit": "20%",
        "Principal plus Profit": "7,268,254.99 Rs",
        "Profit for the period": "6,268,254.99 Rs",
        "Taxes 2%": "125,365.10 Rs",
        "NET PROFIT": "6,142,889.89 Rs",
        "Category": "Monthly",
        "Subcategory": "10 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "180",
        "Rate of Profit": "20%",
        "Principal plus Profit": "19,594,998.42 Rs",
        "Profit for the period": "18,594,998.42 Rs",
        "Taxes 2%": "371,899.97 Rs",
        "NET PROFIT": "18,223,098.46 Rs",
        "Category": "Monthly",
        "Subcategory": "15 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Months)": "240",
        "Rate of Profit": "20%",
        "Principal plus Profit": "52,827,530.63 Rs",
        "Profit for the period": "51,827,530.63 Rs",
        "Taxes 2%": "1,036,550.61 Rs",
        "NET PROFIT": "50,790,980.02 Rs",
        "Category": "Monthly",
        "Subcategory": "20 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "1",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "2 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "1,210,000.00 Rs",
        "Profit Earned": "210,000.00 Rs",
        "TAX": "2%",
        "NET PROFIT": "205,800.00 Rs",
        "Category": "Bi-annual",
        "Subcategory": "1 Year"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "3",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "6 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "1,771,561.00 Rs",
        "Profit Earned": "771,561.00 Rs",
        "TAX": "2%",
        "NET PROFIT": "756,129.78 Rs",
        "Category": "Bi-annual",
        "Subcategory": "3 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "5",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "10 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "2,593,742.46 Rs",
        "Profit Earned": "1,593,742.46 Rs",
        "TAX": "2%",
        "NET PROFIT": "1,561,867.61 Rs",
        "Category": "Bi-annual",
        "Subcategory": "5 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "10",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "20 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "6,727,499.95 Rs",
        "Profit Earned": "5,727,499.95 Rs",
        "TAX": "2%",
        "NET PROFIT": "5,612,949.95 Rs",
        "Category": "Bi-annual",
        "Subcategory": "10 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "15",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "30 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "17,449,402.27 Rs",
        "Profit Earned": "16,449,402.27 Rs",
        "TAX": "2%",
        "NET PROFIT": "16,120,414.22 Rs",
        "Category": "Bi-annual",
        "Subcategory": "15 Years"
    },
    {
        "Inv. Amount": "1,000,000.00 Rs",
        "Length of Inv.(Years)": "20",
        "Cycle/ Frequency": "2 Bi-annual",
        "Number of times profit paid": "40 Bi-annual",
        "Profit Rate": "20%",
        "Principal plus Profit": "45,259,255.57 Rs",
        "Profit Earned": "44,259,255.57 Rs",
        "TAX": "2%",
        "NET PROFIT": "43,374,070.46 Rs",
        "Category": "Bi-annual",
        "Subcategory": "20 Years"
    }
];

document.addEventListener("DOMContentLoaded", function() {
    const financeTable = document.getElementById("finance-table");
    const categoryFilter = document.getElementById("category-filter");
    const subcategoryFilter = document.getElementById("subcategory-filter");

    // Function to populate the table with data
    function populateTable(category, subcategory) {
        financeTable.innerHTML = ""; // Clear the table
        let filteredData = financeData;

        if (category) {
            filteredData = filteredData.filter(item => item.Category === category);
        }

        if (subcategory && subcategory !== 'All Subcategories') {
            filteredData = filteredData.filter(item => item.Subcategory === subcategory);
        }

        if (filteredData.length === 0) {
            financeTable.innerHTML = "<tr><td colspan='10'>No data available</td></tr>";
            return;
        }

        const keys = Object.keys(filteredData[0]);

        const headerRow = financeTable.insertRow();
        keys.forEach(key => {
            const cell = headerRow.insertCell();
            cell.innerHTML = key;
        });

        filteredData.forEach(item => {
            const row = financeTable.insertRow();
            keys.forEach(key => {
                const cell = row.insertCell();
                cell.innerHTML = item[key];
            });
        });
    }

    // Function to populate filter options
    function populateFilterOptions() {
        const categories = [...new Set(financeData.map(item => item.Category))];
        categoryFilter.innerHTML = "";

        subcategoryFilter.innerHTML = "<option value='All Subcategories'>All Subcategories</option>";

        categories.forEach(category => {
            const option = document.createElement("option");
            option.value = category;
            option.textContent = category;
            categoryFilter.appendChild(option);
        });

        subcategoryFilter.value = "All Subcategories";
    }

    // Function to populate subcategories based on selected category
    function populateSubcategories() {
        const selectedCategory = categoryFilter.value;
        const subcategories = [...new Set(financeData
            .filter(item => item.Category === selectedCategory)
            .map(item => item.Subcategory))];

        subcategoryFilter.innerHTML = "<option value='All Subcategories'>All Subcategories</option>";

        subcategories.forEach(subcategory => {
            const option = document.createElement("option");
            option.value = subcategory;
            option.textContent = subcategory;
            subcategoryFilter.appendChild(option);
        });
    }

    // Initial population of the table and filter options
    populateTable("Quarterly", "All Subcategories");
    populateFilterOptions();

    // Initial population of subcategories
    populateSubcategories();

    // Filter data on category change
    categoryFilter.addEventListener("change", function() {
        const selectedCategory = categoryFilter.value;
        const selectedSubcategory = subcategoryFilter.value;
        populateSubcategories(); // Populate subcategories based on the selected category
        populateTable(selectedCategory, selectedSubcategory);
    });

    subcategoryFilter.addEventListener("change", function() {
        const selectedCategory = categoryFilter.value;
        const selectedSubcategory = subcategoryFilter.value;
        populateTable(selectedCategory, selectedSubcategory);
    });
});
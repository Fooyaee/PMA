// Sorting Function
// Code generated by ChatGPT

// By rating
function sortByRating() {
    var restaurantList = document.getElementById('restaurantList');
    var items = Array.from(restaurantList.children);

    items.sort(function (a, b) {
        var ratingA = parseInt(a.getAttribute('data-rating'));
        var ratingB = parseInt(b.getAttribute('data-rating'));
        return ratingA - ratingB;
    });

    // Clear the present list
    restaurantList.innerHTML = '';

    // Renew the list after sorting
    items.forEach(function (item) {
        restaurantList.appendChild(item);
    });
}

// By average price
function sortByPrice() {
    var restaurantList = document.getElementById('restaurantList');
    var items = Array.from(restaurantList.children);

    items.sort(function (a, b) {
        var priceA = parseInt(a.getAttribute('data-price'));
        var priceB = parseInt(b.getAttribute('data-price'));
        return priceA - priceB;
    });

    // Clear the present list
    restaurantList.innerHTML = '';

    // Renew the list after sorting
    items.forEach(function (item) {
        restaurantList.appendChild(item);
    });
}


// Filter Function
// Code generated by ChatGPT

function filterByLocation(location) {
    var restaurantList = document.getElementById('restaurantList');
    var items = Array.from(restaurantList.children);

    items.forEach(function (item) {
        var itemLocation = item.getAttribute('data-location');

        if (itemLocation === location) {
            item.style.display = 'block'; // Show eligible restaurants
        } else {
            item.style.display = 'none'; // Show ineligible restaurants
        }
    });
}

function resetFilter() {
    var restaurantList = document.getElementById('restaurantList');
    var items = Array.from(restaurantList.children);

    items.forEach(function (item) {
        item.style.display = 'block'; // Reset to show all restaurants
    });
}



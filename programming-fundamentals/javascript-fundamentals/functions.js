// Example: Input Object and return string
function getFirstName(user) {
    return user.firstName;
}

// Example: Conditional return boolean
function isFrontendDeveloper(user) {
    if (user.frontend.html && user.frontend.css && user.frontend.javascript) {
        return true;
    } else {
        return false;
    }
}

function meanSquareError(actual, predicted) {
    return actual.map((value, index) => Math.pow(value - predicted[index], 2)).reduce((sum, value) => sum + value, 0) / actual.length;
}

// a function which calculates the area below a curve using the Riemann sum





/**
 * Removes an item from the shopping cart by its id.
 * @param {Array} cart - The shopping cart array.
 * @param {string|number} itemId - The id of the item to remove.
 * @returns {Array} - A new cart array with the item removed.
 */
function removeItemFromCart(cart, itemId) {
    return cart.filter(item => item.id !== itemId);
}

// Example: Simple for loop to count total items in shopping cart
function countCartItems(cart) {
    let totalItems = 0;
    for (let i = 0; i < cart.length; i++) {
        totalItems += cart[i].quantity;
    }
    return totalItems;
}

function calculateAverage(numbers) {
    return numbers.reduce((sum, num) => sum + num, 0) / numbers.length;
}

function calculateAverageWithLoop(numbers) {
    let total = 0;
    let count = 0;
    for (const num of numbers) {
        total += num;
        count++;
    }
    return total / count;
}

module.exports = {
    calculateAverage,
    calculateAverageWithLoop
};



//this will be rather put to the tests section 
// Example object
const sampleUser = {
    firstName: "Jane",
    lastName: "Wilson",
    age: 28,
    frontend: {
        html: true,
        css: true,
        javascript: true
    },
    backend: {
        node: true,
        golang: true,
        python: true,   
        java: false
    },
    automation: {
        selenium: true,
        cypress: true,
        playwright: true,
        kubernetes: true,
        terraform: true,
        docker: true,
        cicd: true,
        linux: true
    }
};

const shoppingCart = [
    { name: "T-shirt", quantity: 2 },
    { name: "Jeans", quantity: 1 },
    { name: "Socks", quantity: 3 }
];












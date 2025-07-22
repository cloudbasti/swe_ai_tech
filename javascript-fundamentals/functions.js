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












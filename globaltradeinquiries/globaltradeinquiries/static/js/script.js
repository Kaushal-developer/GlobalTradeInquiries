// Sample product categories and top-selling products
const productData = {
    categories: ["Electronics", "Clothing", "Books", "Home Appliances", "Toys"],
    topSoldProducts: {
        Electronics: "Smartphone XYZ",
        Clothing: "Men's Casual Shirt",
        Books: "Learn Programming in Python",
        Home: "Vacuum Cleaner V20",
        Toys: "Kids Racing Car Set"
    }
};

// Toggle chat window visibility
function toggleChat() {
    const chatWindow = document.getElementById("chat-window");
    chatWindow.style.display =
        chatWindow.style.display === "block" ? "none" : "block";

    if (chatWindow.style.display === "block") {
        sendBotMessage("Hello! I'm here to help. Ask me about products, categories, or top-selling items.");
    }
}

// Send a message to the chatbot
function sendMessage() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value.trim();

    if (message) {
        displayMessage("You", message);
        userInput.value = "";

        setTimeout(() => {
            const botReply = getBotResponse(message);
            displayMessage("Chatbot", botReply);
        }, 1000);
    }
}

// Display messages in the chat window
function displayMessage(sender, message) {
    const chatContent = document.getElementById("chat-content");
    const msgDiv = document.createElement("div");
    msgDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatContent.appendChild(msgDiv);
    chatContent.scrollTop = chatContent.scrollHeight;
}

// Send initial message when chatbot opens
function sendBotMessage(msg) {
    displayMessage("Chatbot", msg);
}

// Generate chatbot responses
function getBotResponse(userMsg) {
    const msg = userMsg.toLowerCase();

    if (msg.includes("hello")) return "Hi! How can I assist you today?";
    if (msg.includes("products")) return `We have a wide range of products across various categories: ${productData.categories.join(", ")}.`;
    if (msg.includes("category")) return `We have the following categories: ${productData.categories.join(", ")}. Which category are you interested in?`;
    if (msg.includes("top-selling")) return `Our top-selling products include: 
    - Electronics: ${productData.topSoldProducts.Electronics}
    - Clothing: ${productData.topSoldProducts.Clothing}
    - Books: ${productData.topSoldProducts.Books}
    - Home Appliances: ${productData.topSoldProducts.Home}
    - Toys: ${productData.topSoldProducts.Toys}`;

    if (msg.includes("goodbye") || msg.includes("exit")) return "Goodbye! Let me know if you have any questions in the future.";

    return "I'm not sure I understand that. Could you ask something about products, categories, or our top-selling items?";
}

function getQueryParam(name) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(name) ? urlParams.get(name) : 0;
}
let currentPage = 1;

function fetchProducts(page = 1) {
  const category = document.getElementById("categoryFilter").value;
  fetch(`/filtered-products?page=${page}&category=${category}`)
    .then((response) => response.text())
    .then((data) => {
      document.getElementById("modalContent").innerHTML = data;
      setupPagination(page);
    });
}

document.getElementById("openModal").addEventListener("click", function () {
  document.getElementById("productModal").classList.remove("hidden");
  fetchProducts();
});

document.getElementById("closeModal").addEventListener("click", function () {
  document.getElementById("productModal").classList.add("hidden");
});

document.getElementById("applyFilter").addEventListener("click", function () {
  fetchProducts();
});

function setupPagination(page) {
  const pagination = document.getElementById("pagination");
  pagination.innerHTML = "";

  if (page > 1) {
    const firstBtn = `<button onclick="fetchProducts(1)" class="bg-gray-200 px-4 py-2 rounded">First</button>`;
    const prevBtn = `<button onclick="fetchProducts(${
      page - 1
    })" class="bg-gray-200 px-4 py-2 rounded">Previous</button>`;
    pagination.innerHTML += firstBtn + prevBtn;
  }

  const currentSpan = `<span class="px-4 py-2 bg-gray-100 rounded">Page ${page}</span>`;
  pagination.innerHTML += currentSpan;

  const nextBtn = `<button onclick="fetchProducts(${
    page + 1
  })" class="bg-gray-200 px-4 py-2 rounded">Next</button>`;
  const lastBtn = `<button onclick="fetchProducts(5)" class="bg-gray-200 px-4 py-2 rounded">Last</button>`;
  pagination.innerHTML += nextBtn + lastBtn;
}

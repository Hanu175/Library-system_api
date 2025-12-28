const API_URL = "http://127.0.0.1:5000/api/books";

document.addEventListener("DOMContentLoaded", loadBooks);

function loadBooks() {
    fetch(API_URL)
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("bookList");
            list.innerHTML = "";

            data.forEach(book => {
                const li = document.createElement("li");
                li.innerHTML = `
                    ${book.title} by ${book.author} (Qty: ${book.quantity})
                    <button onclick="deleteBook(${book.id})">Delete</button>
                `;
                list.appendChild(li);
            });
        });
}

function addBook() {
    const title = document.getElementById("title").value;
    const author = document.getElementById("author").value;
    const quantity = document.getElementById("quantity").value;

    fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, author, quantity })
    })
    .then(() => {
        loadBooks();
        document.querySelectorAll("input").forEach(i => i.value = "");
    });
}

function deleteBook(id) {
    fetch(`${API_URL}/${id}`, {
        method: "DELETE"
    }).then(loadBooks);
}

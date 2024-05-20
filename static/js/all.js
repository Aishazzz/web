function validateForm() {
    var inputs = document.querySelectorAll('input[required]');
    for (var i = 0; i < inputs.length; i++) {
        if (!inputs[i].value) {
            alert("Please fill out all required fields.");
            return false; // Prevent form submission
        }
    }
    return true; // Allow form submission if all required fields are filled
}


addBtn.addEventListener1("click", (e) => {
    e.preventDefault();
    addBook();
    bookForm.reset();
});

var editBtn = document.getElementById("editBtn");

editBtn.addEventListener("click", (e) => {
    e.preventDefault();
    editBook();
    window.location.href = "{ % url 'homeadmin' %}";
});

function deleteBook() {
    var link = window.location.href;
    var url = new URL(link);
    var id = url.searchParams.get("id");
    var book = data.find((book) => book.id == id);
    var index = data.indexOf(book);
    data.splice(index, 1);
    setDataToStorage(data);
    window.location.href = "{% url 'homeadmin' %}";
}

var deleteBtn = document.getElementById("deleteBtn");

deleteBtn.addEventListener("click", (e) => {
    e.preventDefault();
    deleteBook();
    window.location.href = "{% url 'homeadmin' %}";
});

document.addEventListener('DOMContentLoaded', function() {
    let profileLink = document.querySelector("#PRofile");
    let sidebar = document.querySelector("#side_bar");

    profileLink.addEventListener("click", function() {
        // Show the sidebar
        sidebar.style.visibility = "visible";

        // Set a timeout to hide the sidebar after 3 seconds
        setTimeout(function() {
            sidebar.style.visibility = "hidden";
        }, 3000); // 3000 milliseconds = 3 seconds
    });
});

var deleteButtons = document.querySelectorAll('.B2');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            var bookId = parseInt(this.getAttribute('data-book-id'));
            var confirmDelete = confirm("Are you sure you want to delete this book?");
            if (confirmDelete) {
                deleteBook(bookId);
                displayAllBooks();
            }
        });
    });

    if (passwordInput !== confirmPasswordInput) {
        alert("Passwords do not match. Please try again.");
        return;
    }

    window.location.href = "{% url 'login' %}";

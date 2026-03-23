const textarea = document.getElementById('ask_me');
const counterSpan = document.querySelector('#counter span');
const form = document.querySelector('#writing form');
const maxChars = 150;

if (textarea) {
    textarea.addEventListener('input', function() {
        const remaining = maxChars - this.value.length;
        if (counterSpan) counterSpan.textContent = remaining;
        if (counterSpan) counterSpan.style.color = remaining <= 10 ? 'red' : '#7c7c7c';
    });

    textarea.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    });
}

if (form && textarea) {
    form.addEventListener('submit', function(e) {
        if (textarea.value.trim() === "") {
            e.preventDefault();
            alert("The text field cannot be empty. Please write something first.");
        }
    });
}

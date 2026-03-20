const textarea = document.getElementById('ask_me');
const counterSpan = document.querySelector('#counter span');
const maxChars = 150;

if (textarea) { // Dobra praktyka: sprawdź, czy element istnieje
    textarea.addEventListener('input', function() {
        const remaining = maxChars - this.value.length;
        if (counterSpan) counterSpan.textContent = remaining;
        if (counterSpan) counterSpan.style.color = remaining <= 10 ? 'red' : '#666';
    });

    textarea.addEventListener('keydown', function(e) {
        const lines = this.value.split('\n');
        if (e.key === 'Enter') {
            e.preventDefault();
        }
    });
}
const btn = document.getElementById('submit_btn');

if (btn) {
    btn.addEventListener('click', function() {
        const userText = textarea.value;

        if (userText.trim() === "") {
            alert("Please, write first something....");
        } else {
            alert("Message Sent!\n\nYour message: " + userText + "\n\n(This is a test box; the send function will be added shortly)");
        }
    });
}

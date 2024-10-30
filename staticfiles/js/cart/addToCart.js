document.getElementById('add-to-cart-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const form = event.target;
    const url = form.action;
    const formData = new FormData(form);

    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const messageElement = document.getElementById('message');
        if (messageElement) {  
            if (data.success) {
                messageElement.textContent = data.message;
                messageElement.style.color = 'green';
            } else {
                messageElement.textContent = data.message;
                messageElement.style.color = 'red';
            }
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

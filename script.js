document.getElementById('labForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const labResults = document.getElementById('labResults').value;

    fetch('/interpret', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ lab_results: labResults })
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.textContent = data.interpreted_text;
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

// scripts.py

document.getElementById('mergeForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const folderPath = document.getElementById('folder_path').value;
    const outputPath = document.getElementById('output_path').value;

    fetch('/merger_app/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ folder_path: folderPath, output_path: outputPath })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').textContent = data.message;
        if (data.status === 'success') {
            document.getElementById('mergeForm').reset();
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

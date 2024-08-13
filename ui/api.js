function generateDialog(jsonObject) {
  console.log('making a request...')
  fetch('http://localhost:8080/npc', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify(jsonObject)
  })
  .then(response => response.text())
  .then(data => {
    console.log(typeof data)
      document.getElementById('responseOutput').textContent = data;
  })
  .catch(error => {
      console.error('Error:', error);
      document.getElementById('responseOutput').textContent = 'An error occurred. Try again.';
  });
}

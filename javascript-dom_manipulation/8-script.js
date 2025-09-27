// Fetch hello translation and display it
document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.getElementById('hello');
  
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error fetching hello:', error);
    });
});

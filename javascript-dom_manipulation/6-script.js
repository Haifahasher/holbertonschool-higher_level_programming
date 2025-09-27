// Fetch Star Wars character name and display it
document.addEventListener('DOMContentLoaded', function () {
  const characterElement = document.getElementById('character');
  
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching character:', error);
    });
});

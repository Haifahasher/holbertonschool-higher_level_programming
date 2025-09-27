// Update the text of the header element to "New Header!!!" when clicking on update_header
document.addEventListener('DOMContentLoaded', function () {
  const updateHeader = document.getElementById('update_header');
  const header = document.querySelector('header');
  
  updateHeader.addEventListener('click', function () {
    header.textContent = 'New Header!!!';
  });
});

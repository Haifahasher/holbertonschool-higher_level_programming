// Add a li element to the list when clicking on add_item
document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');
  
  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});

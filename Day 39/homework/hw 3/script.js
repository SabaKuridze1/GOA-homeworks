// Example: Add a click event to each movie poster
document.querySelectorAll('.movie').forEach(movie => {
    movie.addEventListener('click', () => {
        alert('You clicked on: ' + movie.querySelector('h2').textContent);
    });
});

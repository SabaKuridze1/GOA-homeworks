// Simple Play/Pause functionality
const playPauseButton = document.querySelector('.play-pause');
let isPlaying = false;

playPauseButton.addEventListener('click', () => {
    if (isPlaying) {
        playPauseButton.textContent = 'Play';
        isPlaying = false;
    } else {
        playPauseButton.textContent = 'Pause';
        isPlaying = true;
    }
});

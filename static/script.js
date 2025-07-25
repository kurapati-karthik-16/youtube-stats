document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  form.addEventListener('submit', () => {
    const statsDiv = document.querySelector('.result');
    if (statsDiv) statsDiv.innerHTML = "<p>Loading...</p>";
  });
});

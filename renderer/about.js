document.getElementById('aboutName').textContent = window.constants.app_name + " - About Us";
document.getElementById('appName').textContent = window.constants.app_name;
document.getElementById('appVersion').textContent = window.constants.app_version;


document.getElementById('homeButton').addEventListener('click', () => {
    window.location.href = '../pages/index.html';
  });
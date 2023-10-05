
document.getElementById('appName').textContent = window.constants.app_name;
document.getElementById('appWelcome').textContent = window.constants.app_welcome;
document.getElementById('appVersion').textContent = window.constants.app_version;

document.getElementById('getStartedButton').addEventListener('click', () => {
  window.location.href = '../pages/setup.html';
});

document.getElementById('aboutButton').addEventListener('click', () => {
  window.location.href = '../pages/about.html';
});


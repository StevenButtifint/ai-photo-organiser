
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Setup";
document.getElementById('appName').textContent = window.constants.app_name;
document.getElementById('appVersion').textContent = window.constants.app_version;

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = '../pages/index.html';
});

ipcRenderer.on('organise-result', (event, result) => {
});

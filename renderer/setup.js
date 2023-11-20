
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Setup";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

const processButton = document.getElementById('processButton');

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = '../pages/index.html';
});

processButton.addEventListener('click', () => {
  const folder = document.getElementById("folder-entry").value;
  if (folder === '') {
  } else {
    window.location.href = '../pages/processing.html';
    ipcRenderer.send('organise-folder', folder);
  }
});

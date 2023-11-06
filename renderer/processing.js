
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Processing";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = '../pages/index.html';
});
 

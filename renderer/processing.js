
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Processing";
document.getElementById('appName').textContent = window.constants.app_name;
document.getElementById('appVersion').textContent = window.constants.app_version;

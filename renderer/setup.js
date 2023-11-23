
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Setup";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

const INDEX_PAGE_PATH = "../pages/index.html";
const PROCESS_PAGE_PATH = "../pages/processing.html";

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = INDEX_PAGE_PATH;
});

document.getElementById('processButton').addEventListener('click', () => {
  const folder = document.getElementById("folder-entry").value;
  if (folder === '') {
  } else {
    window.location.href = PROCESS_PAGE_PATH;
    ipcRenderer.send('organise-folder', folder);
  }
});

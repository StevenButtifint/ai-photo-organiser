
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Processing";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = '../pages/index.html';
});
 
ipcRenderer.on('organise-result', (event, result) => {

  const returned = JSON.parse(result);
  const returned_message = returned[0];
  const returned_state = returned[1];
  const returned_done = returned[2];
  const returned_state_message = returned[3];

});
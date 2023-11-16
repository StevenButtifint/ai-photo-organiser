
const { ipcRenderer } = require('electron');

document.getElementById('setupName').textContent = window.constants.app_name + " - Processing";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

const notice = document.getElementById('organise-notice');
const home_button = document.getElementById('homeButton');

document.getElementById('homeButton').addEventListener('click', () => {
  window.location.href = '../pages/index.html';
});
 
ipcRenderer.on('organise-result', (event, result) => {

  const returned = JSON.parse(result);
  const returned_message = returned[0];
  const returned_state = returned[1];
  const returned_done = returned[2];
  const returned_state_message = returned[3];

  notice.textContent = `${returned_message}`;


  if (returned_state != "200"){
    setHomeButtonText("Close");
    home_button.className = "button";
  }

  if (returned_state == "900"){
    notice.textContent = `${returned_state_message}`;
  } else {
    notice.textContent = `${returned_message}`;
  }

  if (returned_done == true) {
    setHomeButtonText("Finish");
    home_button.className = "button";
  }

});

function setHomeButtonText(text) {
  home_button.textContent = text;
}
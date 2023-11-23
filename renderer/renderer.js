
document.getElementById('appName').textContent = window.constants.app_name;
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appWelcome').textContent = window.constants.app_welcome;
document.getElementById('appVersion').textContent = window.constants.app_version;

const SETUP_PAGE_PATH = "../pages/setup.html";
const ABOUT_PAGE_PATH = "../pages/about.html";


document.getElementById('getStartedButton').addEventListener('click', () => {
  window.location.href = SETUP_PAGE_PATH;
});

document.getElementById('aboutButton').addEventListener('click', () => {
  window.location.href = ABOUT_PAGE_PATH;
});


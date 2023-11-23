document.getElementById('aboutName').textContent = window.constants.app_name + " - About Us";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;

const INDEX_PAGE_PATH = "../pages/index.html";

document.getElementById('homeButton').addEventListener('click', () => {
    window.location.href = INDEX_PAGE_PATH;
  });
document.getElementById('aboutName').textContent = window.constants.app_name + " - About Us";
document.getElementById('appCredit').textContent = window.constants.app_credit;
document.getElementById('appVersion').textContent = window.constants.app_version;


document.getElementById('homeButton').addEventListener('click', () => {
    window.location.href = '../pages/index.html';
  });
const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

app.on('ready', () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  mainWindow.loadFile('pages/index.html');

  ipcMain.on('run-python-script', (event) => {
    const pythonProcess = spawn('python', ['./backend/photo_organiser.py', '2', '3']);
    pythonProcess.stdout.on('data', (data) => {
      console.log(data.toString());
      event.sender.send('python-script-result', data.toString());
    });
  });
});

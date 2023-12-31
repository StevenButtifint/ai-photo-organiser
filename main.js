const { app, BrowserWindow, ipcMain, Menu } = require('electron');
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

  Menu.setApplicationMenu(null);

  mainWindow.loadFile('pages/index.html');

  ipcMain.on('organise-folder', (event, folder_location) => {
    const pythonProcess = spawn('python', ['./backend/photo_organiser.py', folder_location]);
    pythonProcess.stdout.on('data', (data) => {
      console.log(data.toString());
      event.sender.send('organise-result', data.toString());
    });
  });
});

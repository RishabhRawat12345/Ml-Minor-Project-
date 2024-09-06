const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');

const app = express();
const port = 3001;

app.use(cors());
app.use(bodyParser.json());

app.post('/predict', (req, res) => {
    const { text } = req.body;

    // Use Python to predict personality type
    const pythonProcess = spawn('python3', ['predict.py', text]);

    pythonProcess.stdout.on('data', (data) => {
        // Send the prediction back to the client
        res.json({ prediction: data.toString() });
    }); 

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
        res.status(500).send(data.toString());
    });
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

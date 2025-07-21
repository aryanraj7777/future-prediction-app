document.getElementById('astroForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    name: document.getElementById('name').value,
    dob: document.getElementById('dob').value,
    tob: document.getElementById('tob').value,
    pob: document.getElementById('pob').value,
  };

  const response = await fetch('https://your-backend-url.onrender.com/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'future_prediction.pdf';
  a.click();
});

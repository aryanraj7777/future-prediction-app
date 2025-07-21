<script>
document.getElementById("predict-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value;
  const dob = document.getElementById("dob").value;
  const time = document.getElementById("time").value;
  const place = document.getElementById("place").value;

  const response = await fetch("https://future-prediction-app.onrender.com/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ name, dob, time, place }),
  });

  if (!response.ok) {
    alert("Something went wrong with the prediction.");
    return;
  }

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "future_prediction.pdf";
  a.click();
});
</script>


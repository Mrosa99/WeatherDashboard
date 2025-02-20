const weatherForm = document.getElementById("weatherForm");

weatherForm.addEventListener("submit", function (event) {
  event.preventDefault();

  const input = document.getElementById("city").value;
  console.log("It's not raining in " + input);
});

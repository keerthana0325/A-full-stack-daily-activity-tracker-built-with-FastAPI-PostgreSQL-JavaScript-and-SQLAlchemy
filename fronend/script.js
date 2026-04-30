console.log("JS loaded");

const form = document.getElementById('habit-form');
form.addEventListener("submit", function(event) {
    event.preventDefault()
    // console.log("submitted");
    // console.log(document.getElementById("date").value);
    // console.log(document.getElementById("title").value);    
    const date = document.getElementById("date").value; 
    const title = document.getElementById("title").value;
    const category = document.getElementById("category").value;
    const didIt = document.getElementById("did_it").checked;
    const notes = document.getElementById("notes").value;

    const habit = {
        date: date,
        title: title,
        category: category,
        did_it: didIt,
        notes: notes
    }
    console.log(habit);
    // console.log("HERE");
    fetch("http://127.0.0.1:8000/entries", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify(habit)
}).then(response => response.json())
  .then(data => {
    console.log("Success:", data);
    // document.getElementById("message").innerText = data.message;
    const popup = document.getElementById("popup");
popup.innerText = data.message;
popup.style.display = "block";

// hide after 2 seconds
setTimeout(function() {
  popup.style.display = "none";
}, 2000);
    //document.getElementById("message").innerText = "";
     form.reset();
    // Optionally, you can clear the form or provide feedback to the user here
  })
  .catch((error) => {
    console.error("Error:", error);
  });
})

const viewHabitsButton = document.getElementById("view-habits");

viewHabitsButton.addEventListener("click", function() {
  fetch("http://127.0.0.1:8000/entries")
    .then(response => response.json())
    .then(data => {
      console.log("Habits:", data);
      const habitsList = document.getElementById("habits-list");
  //     habitsList.innerHTML = "";
  //     data.entries.forEach(function(entry) {
  // const status = entry.did_it ? "done" : "not done";

  // habitsList.innerHTML +=
  //   entry.date + " | " +
  //   entry.title + " | " +
  //   entry.category + " | " +
  //   status + "<br>";
  let table = "<table>";

table += `
<tr>
  <th>Date</th>
  <th>Activity</th>
  <th>Category</th>
  <th>Status</th>
</tr>
`;

data.entries.forEach(function(entry) {
  const status = entry.did_it ? "Done" : "Not Done";

  table += `
  <tr>
    <td>${entry.date}</td>
    <td>${entry.title}</td>
    <td>${entry.category}</td>
    <td>${status}</td>
  </tr>
  `;
});

table += "</table>";

habitsList.innerHTML = table;
});
    });


const viewStatsButton = document.getElementById("view-stats");

viewStatsButton.addEventListener("click", function() {
  fetch("http://127.0.0.1:8000/stats")
    .then(response => response.json())
    .then(data => {
      console.log("Stats:", data);

      const statlist = document.getElementById("stats");
      let table = "<table>";
      table += `
      <tr>
        <th>Total Entries</th>
        <th>Completed Entries</th>
        <th>Completion Rate</th>
      </tr>
      `;

      if (data.message) {
        statlist.innerHTML = data.message;
      } else {
        table += `
        <tr>
          <td>${data.total_entries}</td>
          <td>${data.completed_entries}</td>
          <td>${data.completion_rate.toFixed(2)}%</td>
        </tr>
        `;
        statlist.innerHTML = table;
      }
    });
});
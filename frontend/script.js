const API_BASE_URL = "http://127.0.0.1:8000/api/book/";

function fetchSlots() {
  const date = document.getElementById("dateInput").value;
  if (!date) {
    alert("Please select a date");
    return;
  }

  fetch(`${API_BASE_URL}available_slots/${date}/`)
    .then((response) => {
      if (!response.ok) throw new Error("Failed to fetch slots");
      return response.json();
    })
    .then((data) => {
      const slotList = document.getElementById("slotList");
      const timeSelect = document.getElementById("time");
      slotList.innerHTML = "";
      timeSelect.innerHTML = '<option value="">Select a time</option>';

      if (data.slots && data.slots.length > 0) {
        data.slots.forEach((slot) => {
          const li = document.createElement("li");
          li.textContent = slot;
          slotList.appendChild(li);

          const option = document.createElement("option");
          option.value = slot;
          option.textContent = slot;
          timeSelect.appendChild(option);
        });
      } else {
        slotList.innerHTML = "<li>No available slots</li>";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      document.getElementById("slotList").innerHTML =
        '<li class="bg" style="color: red;">Error loading slots</li>';
    });
}

document
  .getElementById("bookingForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;
    const date = document.getElementById("date").value;
    const time = document.getElementById("time").value;
    const message = document.getElementById("formMessage");

    const bookingData = { name, phone, date, time };

    fetch(`${API_BASE_URL}book_appointment/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(bookingData),
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((err) => {
            throw new Error(err.error || "Booking failed");
          });
        }
        return response.json();
      })
      .then((data) => {
        message.textContent = data.message;
        message.style.color = "#28a745";
        document.getElementById("bookingForm").reset();
        fetchSlots(); // Refresh slots
      })
      .catch((error) => {
        console.error("Error:", error);
        message.textContent = error.message;
        message.style.color = "#d9534f";
      });
  });

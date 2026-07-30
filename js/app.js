let ostanSelect = document.getElementById("ostan");
let shahrSelect = document.getElementById("shahr");

let ostans = [];
let shahrs = [];

// گرفتن استان ها
fetch("static/data/ostan.json")
  .then((res) => res.json())
  .then((data) => {
    ostans = data;
    console.log(ostans)

    data.forEach((item) => {
      let option = document.createElement("option");

      option.value = item.id;
      option.textContent = item.name;

      ostanSelect.appendChild(option);
    });
  });

// وقتی استان انتخاب شد
ostanSelect.addEventListener("change", function () {
  let ostanId = this.value;

  shahrSelect.innerHTML = "<option>انتخاب شهر</option>";

  let filteredshahrs = shahrs.filter((shahr) => shahr.ostan == ostanId);

  filteredshahrs.forEach((shahr) => {
    let option = document.createElement("option");

    option.value = shahr.id;
    option.textContent = shahr.name;

    shahrSelect.appendChild(option);
  });
});

// گرفتن شهرها
fetch("static/data/shahr.json")
  .then((res) => res.json())
  .then((data) => {
    shahrs = data;
  });

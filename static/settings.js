function settingsInit() {
    // initialization code, called from openModule()
    console.log("settingsInit() called!");
    let paramId = 0;
    let paramsTableBody = document.getElementById("paramsTableBody");
    let paramsTableSubmit = document.getElementById("paramsTableSubmit");
    paramsTableSubmit.onclick = onSubmitAppParamChangeForm;
    let uploadTimesCsvFile = document.getElementById("uploadTimesCsvFile");
    let uploadTimesCsvSubmit = document.getElementById("uploadTimesCsvSubmit");
    uploadTimesCsvSubmit.onclick = onSubmitUploadTimesCsv;

    // fetch application parameters
    fetch(/*"http://localhost:5000*/ "/params", {
        method: "GET",
        mode: "no-cors"
    })
    .then(response => response.json())
    .then(json => {
        // Empty the table body first
        paramsTableBody.innerHTML = "";

        for (param of json) {
            paramId++;

            let row = document.createElement("tr");

            let keyCell = row.insertCell();
            let keyId = paramId + "_key";
            let keyInput = document.createElement("input");
            keyInput.setAttribute("id", keyId);
            keyInput.setAttribute("name", keyId);
            keyInput.setAttribute("type", "text");
            keyInput.setAttribute("disabled", "disabled");
            keyInput.setAttribute("value", param.key);
            keyCell.appendChild(keyInput);

            let valueCell = row.insertCell();
            let valueId = paramId + "_value";
            let valueInput = document.createElement("input");
            valueInput.setAttribute("id", valueId);
            valueInput.setAttribute("name", valueId);
            valueInput.setAttribute("type", "text");
            valueInput.setAttribute("value", param.value);
            valueCell.appendChild(valueInput);

            let typeCell = row.insertCell();
            typeCell.innerText = param.type;

            paramsTableBody.appendChild(row);
        }
    });
}

function onSubmitAppParamChangeForm(event) {
    console.log("submit clicked, event: ", event);

    let newValues = {};
    let i = 1;
    while (true) {
        console.log("looking for field with id", i.toString() + "_key");
        let keyField = document.getElementById(i.toString() + "_key");
        if (null == keyField) break;
        let key = keyField.value;
        let val = document.getElementById(i.toString() + "_value").value;
        newValues[key] = val;
        i++;
    }

    console.log("call parameters POST /config: ", newValues);
    // call POST /config
    fetch(/*"http://localhost:5000*/ "/params", {
        method: "POST",
        body: JSON.stringify(newValues)
    })
    .then(response => response.json())
    .then(json => {
        console.log("call to POST /params returned", json);
    });

    event.preventDefault();
    return false;
}

function onSubmitUploadTimesCsv(event) {
    console.log("submit UploadTimesCsv clicked, event: ", event);
    console.log("file uploaded", uploadTimesCsvFile.files[0]);

    // call POST /upload_times_csv
    fetch("/upload_times_csv", {
        method: "POST",
        body: uploadTimesCsvFile.files[0]
    })
    .then(response => response.json())
    .then(json => {
        console.log("call to POST /upload_times_csv returned", json);
    });

    event.preventDefault();
    return false;
}
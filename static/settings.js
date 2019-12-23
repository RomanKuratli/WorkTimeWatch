function settingsInit() {
    // initialization code, called from openModule()
    console.log('settingsInit() called!');
    let paramId = 0;
    let paramsTableBody = document.getElementById('paramsTableBody');
    let paramsTableSubmit = document.getElementById('paramsTableSubmit');
    paramsTableSubmit.onclick = onSubmitAppParamChangeForm;

    // fetch application parameters
    fetch(/*'http://localhost:5000*/ '/params', {
        method: 'GET',
        mode: 'no-cors'
    })
    .then(response => response.json())
    .then(json => {
        // Empty the table body first
        paramsTableBody.innerHTML = '';

        for (param of json) {
            paramId++;

            let row = document.createElement('tr');

            let keyCell = row.insertCell();
            let keyId = paramId + '_key';
            let keyInput = document.createElement("input");
            keyInput.setAttribute("id", keyId);
            keyInput.setAttribute("name", keyId);
            keyInput.setAttribute("type", "text");
            keyInput.setAttribute("disabled", "disabled");
            keyInput.setAttribute("value", param.key);
            keyCell.appendChild(keyInput);

            let valueCell = row.insertCell();
            let valueId = paramId + '_value';
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
    console.log('submit clicked, event: ', event);

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

    event.preventDefault();
    return false;
}
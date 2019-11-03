function settingsInit() {
    // initialization code, called from openModule()
    console.log('settingsInit() called!');
    let paramsTableBody = document.getElementById('paramsTableBody');
    fetch(/*'http://localhost:5000*/ '/params', {
        method: 'GET',
        mode: 'no-cors'
    })
    .then(response => {
        console.log('response: ', response);
        return response.json();
    })
    .then(json => {
        for (param of json) {
            let row = document.createElement('tr');

            let keyCell = row.insertCell();
            keyCell.innerText = param.key;

            let valueCell = row.insertCell();
            valueCell.appendChild(createAppParamChangeForm(param.key, param.value));

            let typeCell = row.insertCell();
            typeCell.innerText = param.type;

            paramsTableBody.appendChild(row);
        }
    });
}

function onSubmitAppParamChangeForm(event) {
    event.preventDefault();
    console.log('submit clicked, event: ', event);
}

function createAppParamChangeForm(key, currentValue) {
    let form = document.createElement('form');
    form.setAttribute('method', 'POST');
    form.setAttribute('action', '/params');
    
    let keyField = document.createElement('input');
    keyField.setAttribute('type', 'hidden');
    keyField.setAttribute('value', key);
    form.appendChild(keyField);

    let valueField = document.createElement('input');
    valueField.setAttribute('type', 'text');
    valueField.setAttribute('value', currentValue);
    form.appendChild(valueField);

    let changeBtn = document.createElement('button');
    changeBtn.setAttribute('type', 'submit');
    changeBtn.setAttribute('value', 'Change');
    changeBtn.onclick = onSubmitAppParamChangeForm;
    form.appendChild(changeBtn);

    return form;
}
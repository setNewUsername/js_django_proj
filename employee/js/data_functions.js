async function getData(){
    let response = await fetch('http://127.0.0.1:8000/employee/list/');
    if (response.ok) {
        let json = await response.json();
        json.forEach(element => {
            let fio = element['name'] + ' ' + element['second_name'] + ' ' + element['last_name'];
            data.push({'fio':fio, 'picture':element['picture'], 'dep':element['emp_department'], 'title':element['emp_title'], 'number':element['number']})
            tableContElement.insertAdjacentHTML('beforeend', appendInfoRow(element['picture'], fio, element['emp_title'], element['emp_department'], element['number']));
        });
    } else {
        alert("Ошибка HTTP: " + response.status);
    }
}

function searchByInput(string, array){
    tableContElement.innerHTML = '';
    array.forEach(element => {
        if((element['fio']).indexOf(string) != -1 || 
           element['title'].indexOf(string) != -1 || 
           element['dep'].indexOf(string) != -1 || 
           String(element['number']).indexOf(string) != -1){
            
            tableContElement.insertAdjacentHTML('beforeend', appendInfoRow(element['picture'], element['fio'], element['dep'], element['title'], element['number']));
        }
    });
}
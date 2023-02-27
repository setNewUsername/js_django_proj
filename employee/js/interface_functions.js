function appendInfoRow(picture, fio, title, department, number){
    return `<div class="row content_row">
                <img class="profile_image" src=${picture == 'none'? "./image/profile.png" : picture}>
                <div class="table_column_row">
                    <p>
                        ${fio}
                    </p>
                </div>
                <div class="table_column_row">
                    <p>
                        ${title}
                    </p>
                </div>
                <div class="table_column_row">
                    <p>
                        ${department}
                    </p>
                </div>
                <div class="table_column_row" style="width: auto;">
                    <p>
                        ${number}
                    </p>
                </div>
            </div>`
}

function checkSelected(id, sortButtons){
    sortButtons.forEach(element => {
        if(element.id == id){
            if(Array.from(element.classList).includes('selected')){
                console.log(`already sorted by ${element.id}`);
                return false;
            } else {
                element.classList.add('selected');
            }
        } else {
            element.classList.remove('selected');
        }
    });
}

function setListenerToSortColumnsHeaders(columnHeader, array){   
    if(columnHeader.id != ''){
        columnHeader.addEventListener('click', ()=>{
            sortBy(columnHeader.id, array);
            checkSelected(columnHeader.id, sortButtons);
        });
    }
}
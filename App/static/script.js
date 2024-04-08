data_list = []

document.getElementById('pastData').innerHTML += data_list

function upload_sheet(id){
    url = document.location.href
    switch(id){
        case 1:
            document.location.href = url  + "upload_data2excel";
            break;
        case  2:
            document.location.href = url  + "passage2excel";
            break;
    }
}

function make_disabled(){
    document.getElementById('nodataform').disabled = true;
}
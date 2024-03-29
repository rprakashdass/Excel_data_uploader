let nofdata = 0
let data = []

function upload_sheet(){
    url = document.location.href
    document.location.href = url  + "upload_data2excel"
    alert(url)
}

function display_len(value) {
    nofdata = value
    document.getElementById('display_len').innerHTML = value
}

function display_data(data){
    input_data += data
    document.getElementById('display_data').innerHTML = data;
}

function displayPast(nofdata, input_data){
    document.getElementById('past-nofdata').innerHTML = nofdata;
    document.getElementById('past-data').innerHTML = input_data;
}

function getInputs(data){
    const nofdata =  data[0].value;
    const input_data =  data[1].value;
    data += input_data;
    displayPast(nofdata,input_data);
    // data.submit();
}

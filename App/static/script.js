
function upload_sheet(){
    url = document.location.href
    document.location.href = url  + "upload_data2excel"
    alert(url)
}

function display(value) {
    document.getElementById('display_input').innerHTML = value
}
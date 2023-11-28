function tableCreate(id,url,values) {
    const tbody = document.getElementById('Table-'+id);
    tbody.innerHTML = ""
    $.ajax({
        method: 'GET',
        url: url,
        dataType: "json",
        success: function(data){
            for (var row=0; row<data['results'].length; row++) {
                var tr = tbody.insertRow();
                colValues = values.split(',').slice(0, -1)
                for (var col=0; col<colValues.length;col++) {
                    var td = tr.insertCell();
                    td.style.textAlign = colValues[col].split(';')[1];
                    td.style.verticalAlign = colValues[col].split(';')[2];
                    td.id = 'Table-'+id+'-'+row+'-'+col;
                    td.appendChild(document.createTextNode(''));
                    td.innerHTML = data['results'][row][colValues[col].split(';')[0]];
                }
                tbody.appendChild(tr)
            };
        },
        error: function(error_data){
            console.log('error');
            console.log(error_data);
        },
    });
}

function tableUpdate(id,url,values) {
    $.ajax({
        method: 'GET',
        url: url,
        dataType: "json",
        success: function(data){
            for (var row=0; row<data['results'].length; row++) {
                colValues = values.split(',').slice(0, -1);
                for (var col=0; col<colValues.length;col++) {
                    document.getElementById('Table-'+id+'-'+row+'-'+col).innerHTML = data['results'][row][colValues[col].split(';')[0]]
                };
            };
        },
        error: function(error_data){
            console.log('error');
            console.log(error_data);
        },
    });
}

function runTableUpdate(id,url,values,time){
    tableCreate(id,url,values);
    if (time != "None"){
    setInterval(function(){
        tableUpdate(id,url,values);
    },Math.imul(parseInt(time),1000)
    );
  };
}
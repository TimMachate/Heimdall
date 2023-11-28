function createTable(tableData,tableHead,tableID) {
    $.ajax({
        url: tableData,
        type: 'get',
        dataType: "json",
        success: function(data) {
            console.log(data)
            const table = JSON.parse(tableHead);
            const body = document.getElementById(table['id']+"-body");
            for (var i = 0; i < data.length; i++){
                var row = document.createElement("tr");
                row.setAttribute("id",table['id']+"-body-row"+data[i].id);
                for (var headItem in table['head']){
                    var cell = document.createElement("td");
                    cell.setAttribute('id',table['id'] +'-body-row'+data[i].id+"-col"+headItem);
                    if ( table['head'][headItem]['type'] == "icon" ) {
                        var link = document.createElement('a');
                        link.setAttribute('href',data[i][table['head'][headItem]['data_url']]);
                        link.setAttribute('class',table['head'][headItem]['class']);
                        link.innerHTML = "<img src=" + table['head'][headItem]['data'] + " alt='Icon'>";
                        cell.appendChild(link);
                    } else if ( table['head'][headItem]['type'] == "time" ) {
                        if (data[i][table['head'][headItem]['data']] != null){
                            var date = new Date(data[i][table['head'][headItem]['data']]);
                            year = date.getFullYear();
                            month = date.getMonth()+1;
                            day = date.getDate();
                            hour = date.getHours();
                            minute = date.getMinutes();
                            if (day < 10) {
                            day = '0' + day;
                            }
                            if (month < 10) {
                            month = '0' + month;
                            }
                            if (hour < 10) {
                            hour = '0' + hour;
                            }
                            if (minute < 10) {
                            minute = '0' + minute;
                            }
                            cell.innerHTML = year+"."+month+"."+day+" "+hour+":"+minute;
                        } else {
                            cell.innerHTML = "";
                        }
                    } else if ( table['head'][headItem]['type'] == "hyperlink" ) {
                        var link = document.createElement('a');
                        link.setAttribute('href',data[i][table['head'][headItem]['data_url']]);
                        link.innerHTML = data[i][table['head'][headItem]['data']];
                        cell.appendChild(link);
                    } else {
                        cell.innerHTML = data[i][table['head'][headItem]['data']];
                    };
                    row.appendChild(cell);
                };
                body.appendChild(row);
            };
            /* Spaltenbreite */
            var colWidth = [];
            for (var headItem in table['head']) {
                colWidth.push({"width":table['head'][headItem]["width"]})
            };
            /* Tabelle Formatieren */
            $("#"+tableID).DataTable({
                "columns": colWidth,
                paging: true,
                searching: true,
                ordering: true,
                order: [[1, 'desc']],
                language: {
                    decimal: ',',
                    thousands: '.',
                },
            }
            );
        },
        failure: function(data) { 
            alert("Die Daten konnten nicht geladen werden!");
        }
    });
}
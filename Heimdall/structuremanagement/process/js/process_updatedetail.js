function process_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                // define all items
                if(dataset.url){
                    if(dataset.url.detail && document.getElementById("id_url_detail")){
                        document.getElementById("id_url_detail").setAttribute("href",dataset.url.detail);
                    };
                };

                if(dataset.reference_number && document.getElementById("id_reference_number")){
                    document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                };

                if(dataset.name && document.getElementById("id_name")){
                    document.getElementById("id_name").setAttribute("value",dataset.name);
                };

                if(dataset.count){
                    if(dataset.count.total && document.getElementById('id_count_total')){
                        document.getElementById('id_count_total').innerHTML = dataset.count.total;
                    };
                    if(dataset.count.average && document.getElementById('id_count_average')){
                        document.getElementById('id_count_average').innerHTML = dataset.count.average;
                    };
                };

                if(dataset.utilization){
                    if(dataset.utilization.average && document.getElementById('id_utilization_average')){
                        document.getElementById('id_utilization_average').innerHTML = dataset.utilization.average+' %';
                    };
                };

                if(dataset.create){
                    if(dataset.create.date && dataset.create.time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create.date+' '+dataset.create.time);
                    };
                    if(dataset.create.username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create.username);
                    };
                };

                if(dataset.update){
                    if(dataset.update.date && dataset.create.time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.create.time);
                    };
                    if(dataset.update.username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update.username);
                    };
                };

                if(dataset.duration){
                    if(dataset.duration.average && document.getElementById('id_duration_average')){
                        document.getElementById('id_duration_average').innerHTML = dataset.duration.average;
                    };
                    if(dataset.duration.days && document.getElementById('id_duration_days')){
                        document.getElementById('id_duration_days').setAttribute('value',dataset.duration.days);
                    };
                    if(dataset.duration.hours && document.getElementById('id_duration_hours')){
                        document.getElementById('id_duration_hours').setAttribute('value',dataset.duration.hours);
                    };
                    if(dataset.duration.minutes && document.getElementById('id_duration_minutes')){
                        document.getElementById('id_duration_minutes').setAttribute('value',dataset.duration.minutes);
                    };
                    if(dataset.duration.seconds && document.getElementById('id_duration_seconds')){
                        document.getElementById('id_duration_seconds').setAttribute('value',dataset.duration.seconds);
                    };
                };

                if(dataset.picture){
                    if(dataset.picture.url_file && document.getElementById('id_picture_url_file')){
                        document.getElementById('id_picture_url_file').setAttribute('href',dataset.picture.url_file);
                    };
                    if(dataset.picture.name && document.getElementById('id_picture')){
                        document.getElementById('id_picture').setAttribute('value',dataset.picture.name);
                    };
                    if(dataset.picture.url_detail && document.getElementById('id_picture_url_detail')){
                        document.getElementById('id_picture_url_detail').setAttribute('href',dataset.picture.url_detail);
                    };
                };

                if(dataset.technical_data_sheet){
                    if(dataset.technical_data_sheet.url_file && document.getElementById('id_technical_data_sheet_url_file')){
                        document.getElementById('id_technical_data_sheet_url_file').setAttribute('href',dataset.technical_data_sheet.url_file);
                    };
                    if(dataset.technical_data_sheet.name && document.getElementById('id_technical_data_sheet')){
                        document.getElementById('id_technical_data_sheet').setAttribute('value',dataset.technical_data_sheet.name);
                    };
                    if(dataset.technical_data_sheet.url_detail && document.getElementById('id_technical_data_sheet_url_detail')){
                        document.getElementById('id_technical_data_sheet_url_detail').setAttribute('href',dataset.technical_data_sheet.url_detail);
                    };
                };

                document.getElementById('id_processes_count').innerHTML = dataset.processes.count;
                if(dataset.url){
                    if(dataset.url.data_create){
                        document.getElementById("id_url_data_create").setAttribute("href",dataset.url.data_create)
                    };
                    if(dataset.url.data_list){
                        document.getElementById("id_url_data_list").setAttribute("href",dataset.url.data_list)
                    };
                    if(dataset.url.data_table){
                        document.getElementById("id_url_data_table").setAttribute("href",dataset.url.data_table)
                    };
                };
                
                // define table processdata
                if(dataset.processes.data[0]){
                    let col = [
                        {
                            "name":"id",
                            "data":"",
                            "defaultContent": "",
                            "width":"10px",
                            "className":"",
                            "visible":true,
                        },
                        {
                            "name":"begin",
                            "data":"dataset.processes.begin",
                            "defaultContent": "",
                            "className":"",
                            "visible": "begin" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.begin){return row.begin.date}}
                        },
                        {
                            "name":"begin",
                            "data":"dataset.processes.begin",
                            "defaultContent": "",
                            "className":"",
                            "visible": "begin" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){if(row.begin){return row.begin.time}}
                        },
                        {
                            "name":"begin",
                            "data":"dataset.processes.begin",
                            "defaultContent": "",
                            "className":"",
                            "visible": "begin" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.begin){
                                if (row.begin.url_detail){
                                    return '<a class="link-dark" href="'+ row.begin.url_detail +'">'+row.begin.username+'</a>'
                                } else {
                                    return row.begin.username
                                }
                            }}
                        },
                        {
                            "name":"duration_formated",
                            "data":"dataset.processes.duration_formated",
                            "defaultContent": "",
                            "className":"",
                            "visible": "duration_formated" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){return row.duration_formated}
                        },
                        {
                            "name":"reference_number",
                            "data":"dataset.processes.reference_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "reference_number" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_detail){
                                    return '<a class="link-dark" href="'+ row.url_detail +'">'+row.reference_number+'</a>'
                                } else {
                                    return row.reference_number
                                }
                            }
                        },
                        {
                            "name":"device",
                            "data":"dataset.processes.device",
                            "defaultContent": "",
                            "className":"",
                            "visible": "device" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.device.url_detail){
                                    return '<a class="link-dark" href="'+ row.url_detail +'">'+row.device.name+' ('+row.device.reference_number+')</a>'
                                } else {
                                    return row.device.name
                                }
                            }
                        },
                        {
                            "name":"count",
                            "data":"count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "count" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){return row.count}
                        },
                        {
                            "name":"utilization_percentage_formated",
                            "data":"utilization_percentage_formated",
                            "defaultContent": "",
                            "className":"",
                            "visible": "utilization_percentage_formated" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){return row.utilization_percentage_formated}
                        },
                        {
                            "name":"url",
                            "data":"url",
                            "defaultContent": "",
                            "width":"35px",
                            "className":"",
                            "visible": "url" in dataset.processes.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url){
                                    if (row.url.detail){
                                        detail = '<a class="btn btn-primary" href="'+ row.url.detail +'"><i class="fas fa-search"></i></a>'
                                    } else {detail = ""};
                                    if (row.url.update){
                                        update = '<a class="btn btn-primary" href="'+ row.url.update +'"><i class="fas fa-pen"></i></a>'
                                    } else {update = ""};
                                    if (row.url.data_create){
                                        data_create = '<a class="btn btn-success" href="'+ row.url.data_create +'"><i class="fas fa-plus"></i></a>'
                                    } else {data_create = ""};
                                    if (row.url.delete){
                                        del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                    } else {del = ""};
                                    return '<div class="btn-group">'+detail+update+data_create+del+'</div>'
                                };
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createTable("processes",dataset.processes.data,col,[[1,'desc'],[2,'desc']],print);
                };
            },
        });
        
    });
}
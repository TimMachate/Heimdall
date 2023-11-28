function device_updatedetail(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset.picture){
                    document.getElementById("id_image_file_url").setAttribute("src",dataset.picture.url_file);
                };
                if(dataset.reference_number){
                    document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                };
                if(dataset.url_detail && document.getElementById("id_url_detail")){
                    document.getElementById("id_url_detail").setAttribute("href",dataset.url_detail);
                };
                if(dataset.url_update && document.getElementById("id_url_update")){
                    document.getElementById("id_url_update").setAttribute("href",dataset.url_update);
                };
                if(dataset.url_delete){
                    document.getElementById("id_url_delete").setAttribute("href",dataset.url_delete);
                };
                if(dataset.name){
                    document.getElementById("id_name").setAttribute("value",dataset.name);
                };
                if(dataset.voltage){
                    document.getElementById("id_voltage").setAttribute("value",dataset.voltage);
                };
                if(dataset.power){
                    document.getElementById("id_power").setAttribute("value",dataset.power);
                };
                if(dataset.count){
                    document.getElementById("id_count").setAttribute("value",dataset.count);
                };
                if(dataset.fabricator){
                    document.getElementById("id_fabricator_id").setAttribute("value",dataset.fabricator.name);
                    document.getElementById("id_fabricator_id_url_detail").setAttribute("href",dataset.fabricator.url_detail);
                };
                if(dataset.fabricator_label){
                    document.getElementById("id_fabricator_label").setAttribute("value",dataset.fabricator_label);
                };
                if(dataset.serial_number){
                    document.getElementById("id_serial_number").setAttribute("value",dataset.serial_number);
                };
                if(dataset.year_of_manufacture){
                    document.getElementById("id_year_of_manufacture").setAttribute("value",dataset.year_of_manufacture);
                };
                if(dataset.create){
                    if(dataset.create.date && dataset.create.time){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create.date+' '+dataset.create.time);
                    };
                    if(dataset.create.username){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create.username);
                    };
                };
                if(dataset.update){
                    if(dataset.update.date && dataset.create.time){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update.date+' '+dataset.create.time);
                    };
                    if(dataset.update.username){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update.username);
                    };
                };
                if(dataset.processdata.data){
                    let processdata = [
                        {
                            "name":"id",
                            "data":"",
                            "defaultContent": "",
                            "width":"10px",
                            "className":"",
                            "visible":true,
                        },
                        {
                            "name":"begin_datetime",
                            "data":"begin_datetime",
                            "defaultContent": "",
                            "className":"",
                            "visible": "begin" in dataset.processdata.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.begin.date && row.begin.time){
                                    return row.begin.date +' '+ row.begin.time
                                } else {
                                    return ""
                                }
                            }
                        },
                        {
                            "name":"end_datetime",
                            "data":"end_datetime",
                            "defaultContent": "",
                            "className":"",
                            "visible": "end" in dataset.processdata.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.end.date && row.end.time){
                                    return row.end.date + ' ' + row.end.time
                                } else {
                                    return ""
                                }
                            }
                        },
                        {
                            "name":"processdata",
                            "data":"processdata",
                            "defaultContent": "",
                            "className":"",
                            "visible": "process" in dataset.processdata.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.process){
                                    return '<a class="link-dark text-decoration-none" href="'+row.process.url_detail+'">'+row.process.name+'</a>'
                                } else {
                                    return ""
                                }
                            }
                        },
                        {
                            "name":"count",
                            "data":"count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "count" in dataset.processdata.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.count){
                                    return row.count
                                } else {
                                    return ""
                                }
                            }
                        },
                        {
                            "name":"utilization",
                            "data":"count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "utilization_percentage_formated" in dataset.processdata.data[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.utilization_percentage_formated){
                                    return row.utilization_percentage_formated
                                } else {
                                    return ""
                                }
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < processdata.length; i++){
                        if (processdata[i]["visible"] === true) {print.push(i)};
                    };
                    transformTable("id_processdata",dataset.processdata.data,processdata,[[1,'desc']],print);
                };
            },
        });
        
    });
}
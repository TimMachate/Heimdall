function maintenance_list(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
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
                        "name":"reference_number",
                        "data":"reference_number",
                        "defaultContent": "",
                        "className":"",
                        "visible": "reference_number" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark" href="'+ row.url_detail +'">'+row.reference_number+'</a>'
                            } else {
                                return row.reference_number
                            }
                        }
                    },
                    {
                        "name":"name",
                        "data":"name",
                        "defaultContent": "",
                        "className":"",
                        "visible": "name" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.url_detail){
                                return '<a class="link-dark" href="'+ row.url_detail +'">'+row.name+'</a>'
                            } else {
                                return row.name
                            }
                        }
                    },
                    {
                        "name":"device",
                        "data":"device",
                        "defaultContent": "",
                        "className":"",
                        "visible": "device" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.device){
                                return '<a class="link-dark" href="'+ row.device.url_detail +'">'+row.device.name+'</a>'
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"protocol",
                        "data":"protocol",
                        "defaultContent": "",
                        "className":"",
                        "visible": "protocol" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.protocol){
                                return '<a class="link-dark" href="'+ row.protocol.url_detail +'">'+row.protocol.name+'</a>'
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"warning",
                        "data":"warning",
                        "defaultContent": "",
                        "className":"",
                        "visible": "warning" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.warning) {
                                return row.warning.formated
                            } else {
                                return ''
                            }                            
                        }
                    },
                    {
                        "name":"warning",
                        "data":"warning",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "warning" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.warning) {
                                if(row.warning.days){
                                    return row.warning.days
                                };
                            };
                        }
                    },
                    {
                        "name":"warning",
                        "data":"warning",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "warning" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.warning) {
                                if(row.warning.hours){
                                    return row.warning.hours
                                };
                            };
                        }
                    },
                    {
                        "name":"warning",
                        "data":"warning",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "warning" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.warning) {
                                if(row.warning.minutes){
                                    return row.warning.minutes
                                };
                            }                           
                        }
                    },
                    {
                        "name":"warning",
                        "data":"warning",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "warning" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.warning) {
                                if(row.warning.seconds){
                                    return row.warning.seconds
                                };
                            }                            
                        }
                    },
                    {
                        "name":"repetition",
                        "data":"repetition",
                        "defaultContent": "",
                        "className":"",
                        "visible": "repetition" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.repetition) {
                                return row.repetition.formated
                            } else {
                                return ''
                            }
                        }
                    },
                    {
                        "name":"repetition",
                        "data":"repetition",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "repetition" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.repetition) {
                                if(row.repetition.days){
                                    return row.repetition.days
                                };
                            };
                        }
                    },
                    {
                        "name":"repetition",
                        "data":"repetition",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "repetition" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.repetition) {
                                if(row.repetition.hours){
                                    return row.repetition.hours
                                };
                            };
                        }
                    },
                    {
                        "name":"repetition",
                        "data":"repetition",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "repetition" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.repetition) {
                                if(row.repetition.minutes){
                                    return row.repetition.minutes
                                };
                            }                           
                        }
                    },
                    {
                        "name":"repetition",
                        "data":"repetition",
                        "defaultContent": "0",
                        "className":"",
                        "visible": "repetition" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.repetition) {
                                if(row.repetition.seconds){
                                    return row.repetition.seconds
                                };
                            }                            
                        }
                    },
                    {
                        "name":"maintenance_last",
                        "data":"maintenance_last",
                        "defaultContent": "",
                        "className":"",
                        "visible": "maintenance_last" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.maintenance_last){
                                return row.maintenance_last.create.datetime_formated
                            }                           
                        }
                    },
                    {
                        "name":"maintenance_next",
                        "data":"maintenance_next",
                        "defaultContent": "",
                        "className":"",
                        "visible": "maintenance_next" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.maintenance_next){
                                return row.maintenance_next.datetime_formated
                            }
                        }
                    },
                    {
                        "name":"status",
                        "data":"status",
                        "defaultContent": "",
                        "className":"",
                        "visible": "status" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if (row.status=='alarm'){
                                return '<button type="button" class="btn btn-danger" disabled>&emsp;</button>'
                            } else if (row.status=='warning') {
                                return '<button type="button" class="btn btn-warning" disabled>&emsp;</button>'
                            } else if (row.status=='OK') {
                                return '<button type="button" class="btn btn-success" disabled>&emsp;</button>'
                            } else {
                                return '<button type="button" class="btn btn-secondary" disabled>&emsp;</button>'
                            };
                        }
                    },
                    {
                        "name":"maintenance_count",
                        "data":"maintenance_count",
                        "defaultContent": "",
                        "className":"",
                        "visible": "maintenance_count" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            return row.maintenance_count
                        }
                    },
                    {
                        "name":"create_date",
                        "data":"create_date",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.date}}
                    },
                    {
                        "name":"create_time",
                        "data":"create_time",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.create){return row.create.time}}
                    },
                    {
                        "name":"create_username",
                        "data":"create_username",
                        "defaultContent": "",
                        "className":"",
                        "visible": "create" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.create){
                            if (row.create.url_detail){
                                return '<a class="link-dark" href="'+ row.create.url_detail +'">'+row.create.username+'</a>'
                            } else {
                                return row.create.username
                            }
                        }}
                    },
                    {
                        "name":"update_date",
                        "data":"update_date",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.update){return row.update.date}}
                    },
                    {
                        "name":"update_time",
                        "data":"update_time",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){if(row.update){return row.update.time}}
                    },
                    {
                        "name":"update_username",
                        "data":"update_username",
                        "defaultContent": "",
                        "className":"",
                        "visible": "update" in dataset[0] ? true : false,
                        "render":function(data,type,row,meta){
                            if(row.update){
                            if (row.update.url_detail){
                                return '<a class="link-dark" href="'+ row.update.url_detail +'">'+row.update.username+'</a>'
                            } else {
                                return row.update.username
                            }
                        }}
                    },
                    {
                        "name":"url",
                        "data":"url",
                        "defaultContent": "",
                        "width":"35px",
                        "className":"",
                        "visible": "url" in dataset[0] ? true : false,
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
                createList(model,dataset,col,[[6,'desc']],print);
            },
        });
        
    });
}

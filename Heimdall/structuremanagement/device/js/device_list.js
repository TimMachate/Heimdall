function device_list(api_data_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_data_url,
            success: function(dataset){
                if(dataset){
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
                            "name":"fabricator",
                            "data":"fabricator",
                            "defaultContent": "",
                            "className":"",
                            "visible": "fabricator" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.fabricator){
                                    if (row.fabricator.url_detail){
                                        return '<a class="link-dark" href="'+ row.fabricator.url_detail +'">'+row.fabricator.name+'</a>'
                                    } else {
                                        return row.fabricator.name
                                    }
                                } else {
                                    return ""
                                };
                            }
                        },
                        {
                            "name":"fabricator_label",
                            "data":"fabricator_label",
                            "defaultContent": "",
                            "className":"",
                            "visible": "fabricator_label" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.fabricator_label){
                                    return row.fabricator_label
                                } else {
                                    return row.fabricator_label
                                }
                            }
                        },
                        {
                            "name":"serial_number",
                            "data":"serial_number",
                            "defaultContent": "",
                            "className":"",
                            "visible": "serial_number" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.serial_number){
                                    return row.serial_number
                                } else {
                                    return row.serial_number
                                }
                            }
                        },
                        {
                            "name":"year_of_manufacture",
                            "data":"year_of_manufacture",
                            "defaultContent": "",
                            "className":"",
                            "visible": "year_of_manufacture" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.year_of_manufacture){
                                    return row.year_of_manufacture
                                } else {
                                    return row.year_of_manufacture
                                }
                            }
                        },
                        {
                            "name":"voltage",
                            "data":"voltage",
                            "defaultContent": "",
                            "className":"",
                            "visible": "voltage" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.voltage){
                                    return row.voltage
                                } else {
                                    return row.voltage
                                }
                            }
                        },
                        {
                            "name":"power",
                            "data":"power",
                            "defaultContent": "",
                            "className":"",
                            "visible": "power" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.power){
                                    return row.power
                                } else {
                                    return row.power
                                }
                            }
                        },
                        {
                            "name":"processes_count",
                            "data":"processes_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "processes_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.processes_count){
                                    return row.processes_count
                                } else {
                                    return row.processes_count
                                }
                            }
                        },
                        {
                            "name":"count",
                            "data":"count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.count){
                                    return row.count
                                } else {
                                    return row.count
                                }
                            }
                        },
                        {
                            "name":"status_count",
                            "data":"status_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "status_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.status_count){
                                    return row.status_count
                                } else {
                                    return row.status_count
                                }
                            }
                        },
                        {
                            "name":"errors_count",
                            "data":"errors_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "errors_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.errors_count){
                                    return row.errors_count
                                } else {
                                    return row.errors_count
                                }
                            }
                        },
                        {
                            "name":"manuals_count",
                            "data":"manuals_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "manuals_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.manuals_count){
                                    return row.manuals_count
                                } else {
                                    return row.manuals_count
                                }
                            }
                        },
                        {
                            "name":"documents_count",
                            "data":"documents_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "documents_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_detail){
                                    return row.documents_count
                                } else {
                                    return row.documents_count
                                }
                            }
                        },
                        {
                            "name":"working_instructions_count",
                            "data":"working_instructions_count",
                            "defaultContent": "",
                            "className":"",
                            "visible": "working_instructions_count" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if (row.url_detail){
                                    return row.working_instructions_count
                                } else {
                                    return row.working_instructions_count
                                }
                            }
                        },
                        {
                            "name":"picture",
                            "data":"picture",
                            "defaultContent": "",
                            "className":"",
                            "visible": "picture" in dataset[0] ? true : false,
                            "render":function(data,type,row,meta){
                                if(row.picture){
                                    if (row.picture.url_file){
                                        return '<a class="btn btn-primary" href="'+ row.picture.url_file +'"><i class="fas fa-file-image"></i></a>'
                                    } else {
                                        return row.picture.name
                                    }
                                } else {
                                    return ""
                                };
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
                                    if(row.url.status){
                                        if (row.url.status.overview){
                                            overview = '<a class="btn btn-primary" href="'+ row.url.status.overview +'"><i class="fas fa-signal"></i></a>'
                                        } else {overview = ""};
                                        if (row.url.status.data_create){
                                            data_create = '<a class="btn btn-success" href="'+ row.url.status.data_create +'"><i class="fas fa-plus"></i></a>'
                                        } else {data_create = ""};
                                        return '<div class="btn-group">'+overview+data_create+'</div>'
                                    };
                                };
                            }
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
                                    if(row.url.process){
                                        if (row.url.process.overview){
                                            overview = '<a class="btn btn-primary" href="'+ row.url.process.overview +'"><i class="fas fa-cogs"></i></a>'
                                        } else {overview = ""};
                                        if (row.url.process.data_create){
                                            data_create = '<a class="btn btn-success" href="'+ row.url.process.data_create +'"><i class="fas fa-plus"></i></a>'
                                        } else {data_create = ""};
                                        return '<div class="btn-group">'+overview+data_create+'</div>'
                                    };
                                };
                            }
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
                                    if(row.url.error){
                                        if (row.url.error.overview){
                                            overview = '<a class="btn btn-primary" href="'+ row.url.error.overview +'"><i class="fas fa-exclamation-circle"></i></a>'
                                        } else {overview = ""};
                                        if (row.url.error.data_create){
                                            data_create = '<a class="btn btn-success" href="'+ row.url.error.data_create +'"><i class="fas fa-plus"></i></a>'
                                        } else {data_create = ""};
                                        return '<div class="btn-group">'+overview+data_create+'</div>'
                                    };
                                };
                            }
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
                                    if(row.url.maintenance){
                                        if (row.url.maintenance.overview){
                                            overview = '<a class="btn btn-primary" href="'+ row.url.maintenance.overview +'"><i class="fas fa-tools"></i></a>'
                                        } else {overview = ""};
                                        if (row.url.maintenance.data_create){
                                            data_create = '<a class="btn btn-success" href="'+ row.url.maintenance.data_create +'"><i class="fas fa-plus"></i></a>'
                                        } else {data_create = ""};
                                        return '<div class="btn-group">'+overview+data_create+'</div>'
                                    };
                                };
                            }
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
                                    if (row.url.delete){
                                        del = '<a class="btn btn-danger" href="'+ row.url.delete +'"><i class="fas fa-trash"></i></a>'
                                    } else {del = ""};
                                    return '<div class="btn-group">'+detail+update+del+'</div>'
                                };
                            }
                        },
                    ];
                    let print = [];
                    for (let i = 0; i < col.length; i++){
                        if (col[i]["visible"] === true) {print.push(i)};
                    };
                    createList(model,dataset,col,[[1,'asc']],print);
                };
            },
        });
        
    });
}

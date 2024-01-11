function supplieritem_updatedetail(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset){
                    if(dataset.reference_number && document.getElementById("id_reference_number")){
                        document.getElementById("id_reference_number").innerHTML = dataset.reference_number;
                    };
                    if(dataset.name && document.getElementById("id_name")){
                        document.getElementById("id_name").setAttribute("value",dataset.name);
                    };
                    if(dataset.item_number && document.getElementById("id_item_number")){
                        document.getElementById("id_item_number").setAttribute("value",dataset.item_number);
                    };
                    if(dataset.supplier_name && document.getElementById("id_company")){
                        document.getElementById("id_company").setAttribute("value",dataset.supplier_name);
                    };
                    if(dataset.supplier_url_detail && document.getElementById("id_company_url_detail")){
                        document.getElementById("id_company_url_detail").setAttribute("href",dataset.supplier_url_detail);
                    };
                    if(dataset.storageitem_name && document.getElementById("id_storageitem")){
                        document.getElementById("id_storageitem").setAttribute("value",dataset.storageitem_name);
                    };
                    if(dataset.storageitem_url_detail && document.getElementById("id_storageitem_url_detail")){
                        document.getElementById("id_storageitem_url_detail").setAttribute("href",dataset.storageitem_url_detail);
                    };
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    if(dataset.update_date && dataset.create_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    if(dataset.unit && document.getElementById("id_unit")){
                        document.getElementById("id_unit").setAttribute("value",dataset.unit);
                    };
                    if(dataset.price && document.getElementById("id_price")){
                        document.getElementById("id_price").setAttribute("value",dataset.price);
                    };
                    if(dataset.stock_value && document.getElementById("id_stock_value")){
                        document.getElementById("id_stock_value").setAttribute("value",dataset.stock_value);
                    };
                    if(dataset.stock_count && document.getElementById("id_stock_count")){
                        document.getElementById("id_stock_count").innerHTML = dataset.stock_count
                    };
                    if(dataset.stock_data){
                        if(dataset.stock_data.length != 0){
                            let stock = [
                                {
                                    "name":"id",
                                    "data":"",
                                    "defaultContent": "",
                                    "width":"10px",
                                    "className":"",
                                    "visible":true,
                                },
                                {
                                    "name":"create_date",
                                    "data":"create_date",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "create_date" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if(row.create_date){return row.create_date};}
                                },
                                {
                                    "name":"create_time",
                                    "data":"create_time",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "create_time" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if(row.create_time){return row.create_time};}
                                },
                                {
                                    "name":"value",
                                    "data":"value",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "value" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if (row.value){return row.value + " €"};}
                                },
                                {
                                    "name":"notice",
                                    "data":"notice",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "notice" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.notice){
                                            return '<div class="btn btn-danger disabled"><i class="fas fa-exclamation-triangle"></i></div>'
                                        };
                                    }
                                },
                                {
                                    "name":"url_detail",
                                    "data":"url_detail",
                                    "defaultContent": "",
                                    "width":"35px",
                                    "className":"",
                                    "visible": "url_detail" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.url_detail){
                                            return '<a class="btn btn-primary" href="'+ row.url_detail + "?next=" + dataset.url_detail +'"><i class="fas fa-search"></i></a>'
                                        };
                                    }
                                },
                                {
                                    "name":"url_unload",
                                    "data":"url_unload",
                                    "defaultContent": "",
                                    "width":"35px",
                                    "className":"",
                                    "visible": "url_unload" in dataset.stock_data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.url_unload){
                                            return '<a class="btn btn-danger" href="'+ row.url_unload + "?next=" + dataset.url_detail +'"><i class="fas fa-angle-up"></i></a>'
                                        };
                                    }
                                },
                            ];
                            let print = [];
                            for (let i = 0; i < stock.length; i++){
                                if (stock[i]["visible"] === true) {print.push(i)};
                            };
                            transformTable("id_stock",dataset.stock_data,stock,[[1,'desc'],[2,'desc']],print);
                        };
                    };
                    if(dataset.booking_count && document.getElementById("id_booking_count")){
                        document.getElementById("id_booking_count").innerHTML = dataset.booking_count
                    };
                    if(dataset.booking_data){
                        if(dataset.booking_data.length != 0){
                            let bookings = [
                                {
                                    "name":"id",
                                    "data":"",
                                    "defaultContent": "",
                                    "width":"10px",
                                    "className":"",
                                    "visible":true,
                                },
                                {
                                    "name":"create_date",
                                    "data":"create_date",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "create_date" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if(row.create_date){return row.create_date};}
                                },
                                {
                                    "name":"create_time",
                                    "data":"create_time",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "create_time" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if(row.create_time){return row.create_time};}
                                },
                                {
                                    "name":"create_username",
                                    "data":"create_username",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "create_username" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if(row.create_username){return row.create_username};}
                                },
                                {
                                    "name":"amount",
                                    "data":"amount",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "amount" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if (row.amount){return row.amount};}
                                },
                                {
                                    "name":"price",
                                    "data":"price",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "price" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if (row.price){return row.price + " €"};}
                                },
                                {
                                    "name":"value",
                                    "data":"value",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "value" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){if (row.value){return row.value + " €"};}
                                },
                                {
                                    "name":"notice",
                                    "data":"notice",
                                    "defaultContent": "",
                                    "className":"",
                                    "visible": "notice" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                        if (row.notice){
                                            return '<div class="btn btn-danger disabled"><i class="fas fa-exclamation-triangle"></i></div>'
                                        };
                                    }
                                },
                                {
                                    "name":"url_detail",
                                    "data":"url_detail",
                                    "defaultContent": "",
                                    "width":"35px",
                                    "className":"",
                                    "visible": "url_detail" in dataset.booking_data[0] ? true : false,
                                    "render":function(data,type,row,meta){
                                            if (row.url_detail){
                                                return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                            };
                                    }
                                },
                            ];
                            let print = [];
                            for (let i = 0; i < bookings.length; i++){
                                if (bookings[i]["visible"] === true) {print.push(i)};
                            };
                            transformTable("id_booking",dataset.booking_data,bookings,[[1,'desc'],[2,'desc']],print);
                        };
                    };
                };
            },
        });
        
    });
}

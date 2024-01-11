function storageitem_updatedetail(api_url,model) {
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
                    // Create
                    if(dataset.create_date && dataset.create_time && document.getElementById('id_create_datetime')){
                        document.getElementById('id_create_datetime').setAttribute('value',dataset.create_date+' '+dataset.create_time);
                    };
                    if(dataset.create_username && document.getElementById('id_create_username')){
                        document.getElementById('id_create_username').setAttribute('value',dataset.create_username);
                    };
                    // Update
                    if(dataset.update_date && dataset.create_time && document.getElementById('id_update_datetime')){
                        document.getElementById('id_update_datetime').setAttribute('value',dataset.update_date+' '+dataset.update_time);
                    };
                    if(dataset.update_username && document.getElementById('id_update_username')){
                        document.getElementById('id_update_username').setAttribute('value',dataset.update_username);
                    };
                    // Company
                    if(dataset.supplier_name && document.getElementById('id_supplier')){
                        document.getElementById('id_supplier').setAttribute('value',dataset.supplier_name);
                    };
                    if(dataset.supplier_url_detail && document.getElementById('id_supplier_url_detail')){
                        document.getElementById('id_supplier_url_detail').setAttribute('href',dataset.supplier_url_detail);
                    };
                    // Company Item
                    if(dataset.supplieritem_name && document.getElementById('id_supplieritem')){
                        document.getElementById('id_supplieritem').setAttribute('value',dataset.supplieritem_name);
                    };
                    if(dataset.supplieritem_url_detail && document.getElementById('id_supplieritem_url_detail')){
                        document.getElementById('id_supplieritem_url_detail').setAttribute('href',dataset.supplieritem_url_detail);
                    };
                    // Min / Warning / Max
                    if(dataset.minimum && document.getElementById("id_minimum")){
                        document.getElementById("id_minimum").setAttribute("value",dataset.minimum);
                    };
                    if(dataset.warning && document.getElementById("id_warning")){
                        document.getElementById("id_warning").setAttribute("value",dataset.warning);
                    };
                    if(dataset.maximum && document.getElementById("id_maximum")){
                        document.getElementById("id_maximum").setAttribute("value",dataset.maximum);
                    };
                    // Stock
                    if(dataset.stock_count && document.getElementById("id_stock_count")){
                        document.getElementById("id_stock_count").innerHTML = dataset.stock_count;
                    };
                    if(dataset.stock_value && document.getElementById("id_stock_value")){
                        document.getElementById("id_stock_value").innerHTML=dataset.stock_value;
                    };
                    // Progress Bar
                    if(dataset.stock_percentage && document.getElementById("id_progressbar")){
                        document.getElementById("id_progressbar").setAttribute('aria-valuenow',dataset.stock_percentage);
                        document.getElementById("id_progressbar").style.width = dataset.stock_percentage+"%"
                    };
                    if(dataset.stock_percentage && document.getElementById("id_stock_percentage")){
                        document.getElementById("id_stock_percentage").innerHTML = dataset.stock_percentage+" %"
                    };
                    // Status
                    if(dataset.status && document.getElementById("id_progressbar")){
                        if(dataset.status == 'overload'){
                            document.getElementById("id_progressbar").setAttribute("class",'progress-bar bg-secondary');
                        };
                        if(dataset.status == 'ok'){
                            document.getElementById("id_progressbar").setAttribute("class",'progress-bar bg-success');
                        };
                        if(dataset.status == 'warning'){
                            document.getElementById("id_progressbar").setAttribute("class",'progress-bar bg-warning');
                        };
                        if(dataset.status == 'alarm'){
                            document.getElementById("id_progressbar").setAttribute("class",'progress-bar bg-danger');
                        };
                    };
                    // Suppliers
                    if(dataset.supplier_count && document.getElementById("id_supplier_count")){
                        document.getElementById("id_supplier_count").innerHTML = dataset.supplier_count
                    };
                    if(dataset.supplier_data.length != 0){
                        let suppliers = [
                            {
                                "name":"id",
                                "data":"",
                                "defaultContent": "",
                                "width":"10px",
                                "className":"",
                                "visible":true,
                            },
                            {
                                "name":"company_name",
                                "data":"company_name",
                                "defaultContent": "-",
                                "className":"",
                                "visible": "company_name" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.company_name){
                                        return row.company_name
                                    };
                                }
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "-",
                                "className":"",
                                "visible": "name" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.name){return row.name};}
                            },
                            {
                                "name":"item_number",
                                "data":"item_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "item_number" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.item_number){return row.item_number};}
                            },
                            {
                                "name":"price",
                                "data":"price",
                                "defaultContent": "",
                                "className":"",
                                "visible": "price" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.price){return row.price + " €"};}
                            },
                            {
                                "name":"url_request_create",
                                "data":"url_request_create",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_request_create" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_request_create){
                                        return '<a class="btn btn-success" href="'+ row.url_request_create +'?next='+dataset.url_detail+'"><i class="fas fa-cart-plus"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_booking_remove",
                                "data":"url_booking_remove",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_booking_remove" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_booking_remove){
                                        return '<a class="btn btn-danger" href="'+ row.url_booking_remove +'?next='+dataset.url_detail+'"><i class="fas fa-minus"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_booking_add",
                                "data":"url_booking_add",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_booking_add" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_booking_add){
                                        return '<a class="btn btn-success" href="'+ row.url_booking_add +'?next='+dataset.url_detail+'"><i class="fas fa-plus"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_detail",
                                "data":"url_detail",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_detail" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_detail){
                                        return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_update",
                                "data":"url_update",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_update" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_update){
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'?next='+dataset.url_detail+'"><i class="fas fa-pen"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_delete",
                                "data":"url_delete",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_delete" in dataset.supplier_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_delete){
                                        return '<a class="btn btn-danger" href="'+ row.url_delete +'?next='+dataset.url_detail+'"><i class="fas fa-trash"></i></a>'
                                    };
                                }
                            },
                        ];
                        let print = [];
                        for (let i = 0; i < suppliers.length; i++){
                            if (suppliers[i]["visible"] === true) {print.push(i)};
                        };
                        transformTable("id_supplier",dataset.supplier_data,suppliers,[[1,'desc'],[2,'desc']],print);
                    };
                    // Stock
                    if(dataset.stock_count && document.getElementById("id_stocks_count")){
                        document.getElementById("id_stocks_count").innerHTML = dataset.stock_count
                    };
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
                                "name":"company_name",
                                "data":"company_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "company_name" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.company_name){return row.company_name};}
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
                                        return '<a class="btn btn-primary" href="'+ row.url_detail +'"><i class="fas fa-search"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_update",
                                "data":"url_update",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_update" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_update){
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'?next='+dataset.url_detail+'"><i class="fas fa-pen"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_delete",
                                "data":"url_delete",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_delete" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_delete){
                                        return '<a class="btn btn-danger" href="'+ row.url_delete +'?next='+dataset.url_detail+'"><i class="fas fa-trash"></i></a>'
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
                                        return '<a class="btn btn-danger" href="'+ row.url_unload +'?next='+dataset.url_detail+'"><i class="fas fa-angle-up"></i></a>'
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
                    // Booking
                    if(dataset.booking_count && document.getElementById("id_booking_count")){
                        document.getElementById("id_booking_count").innerHTML = dataset.booking_count
                    };
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
                                "name":"company_name",
                                "data":"company_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "company_name" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.company_name){return row.company_name};}
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
                            {
                                "name":"url_update",
                                "data":"url_update",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_update" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_update){
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'?next='+dataset.url_detail+'"><i class="fas fa-pen"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_delete",
                                "data":"url_delete",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_delete" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_delete){
                                        return '<a class="btn btn-danger" href="'+ row.url_delete +'?next='+dataset.url_detail+'"><i class="fas fa-trash"></i></a>'
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
            },
        });
        
    });
}

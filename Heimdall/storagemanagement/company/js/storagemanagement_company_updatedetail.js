function company_updatedetail(api_url,model) {
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
                    if(dataset.street && document.getElementById("id_street")){
                        document.getElementById("id_street").setAttribute("value",dataset.street);
                    };
                    if(dataset.house_number && document.getElementById("id_house_number")){
                        document.getElementById("id_house_number").setAttribute("value",dataset.house_number);
                    };
                    if(dataset.post_code && document.getElementById("id_post_code")){
                        document.getElementById("id_post_code").setAttribute("value",dataset.post_code);
                    };
                    if(dataset.city && document.getElementById("id_city")){
                        document.getElementById("id_city").setAttribute("value",dataset.city);
                    };
                    if(dataset.country && document.getElementById("id_country")){
                        document.getElementById("id_country").setAttribute("value",dataset.country);
                    };
                    if(dataset.telephone){
                        if(dataset.telephone && document.getElementById("id_telephone")){
                            document.getElementById("id_telephone").setAttribute('value',dataset.telephone);
                        };
                    };
                    if(dataset.email){
                        if(dataset.email && document.getElementById("id_email")){
                            document.getElementById("id_email").setAttribute('value',dataset.email);
                        };
                    };
                    if(dataset.supplier && document.getElementById("id_supplier")){
                        document.getElementById("id_supplier").setAttribute("checked",true)
                    };
                    if(dataset.notice && document.getElementById("id_notice")){
                        document.getElementById("id_notice").innerHTML=dataset.notice;
                    };
                    // Company Contact
                    if(dataset.companycontact_count && document.getElementById("id_companycontact_count")){
                        document.getElementById("id_companycontact_count").innerHTML = dataset.companycontact_count
                    };
                    if(dataset.companycontact_data.length != 0){
                        let companycontacts = [
                            {
                                "name":"id",
                                "data":"",
                                "defaultContent": "",
                                "width":"10px",
                                "className":"",
                                "visible":true,
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "name" in dataset.companycontact_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.name){return row.name};}
                            },
                            {
                                "name":"telephone_data",
                                "data":"telephone_data",
                                "defaultContent": "",
                                "className":"",
                                "visible": "telephone_data" in dataset.companycontact_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.telephone_data){
                                        string = ""
                                        row.telephone_data.forEach(phone => {
                                            string+='<div>'+phone.number+'</div>'
                                        })
                                        return string
                                    };
                                }
                            },
                            {
                                "name":"email_data",
                                "data":"email_data",
                                "defaultContent": "",
                                "className":"",
                                "visible": "email_data" in dataset.companycontact_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.email_data){
                                        string = ""
                                        row.email_data.forEach(email => {
                                            string+='<div>'+email.email+'</div>'
                                        })
                                        return string
                                    };
                                }
                            },
                            {
                                "name":"url_detail",
                                "data":"url_detail",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_detail" in dataset.companycontact_data[0] ? true : false,
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
                                "visible": "url_update" in dataset.companycontact_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_update){
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_delete",
                                "data":"url_delete",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_delete" in dataset.companycontact_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_delete){
                                        return '<a class="btn btn-danger" href="'+ row.url_delete + "?next=" + dataset.url_detail +'"><i class="fas fa-trash"></i></a>'
                                    };
                                }
                            },
                        ];
                        let print = [];
                        for (let i = 0; i < companycontacts.length; i++){
                            if (companycontacts[i]["visible"] === true) {print.push(i)};
                        };
                        transformTable("id_companycontact",dataset.companycontact_data,companycontacts,[[1,'asc']],print);
                    };
                    // Company Item
                    if(dataset.companyitem_count && document.getElementById("id_companyitem_count")){
                        document.getElementById("id_companyitem_count").innerHTML = dataset.companyitem_count
                    };
                    if(dataset.companyitem_data.length != 0){
                        let companyitems = [
                            {
                                "name":"id",
                                "data":"",
                                "defaultContent": "",
                                "width":"10px",
                                "className":"",
                                "visible":true,
                            },
                            {
                                "name":"name",
                                "data":"name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "name" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.name){return row.name};}
                            },
                            {
                                "name":"item_number",
                                "data":"item_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "item_number" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.item_number){return row.item_number};}
                            },
                            {
                                "name":"unit_package",
                                "data":"unit_package",
                                "defaultContent": "",
                                "className":"",
                                "visible": "unit_package" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.unit_package){return row.unit_package};}
                            },
                            {
                                "name":"unit",
                                "data":"unit",
                                "defaultContent": "",
                                "className":"",
                                "visible": "unit" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.unit){return row.unit};}
                            },
                            {
                                "name":"price",
                                "data":"price",
                                "defaultContent": "",
                                "className":"",
                                "visible": "price" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.price){return row.price+" €"};}
                            },
                            {
                                "name":"url_detail",
                                "data":"url_detail",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_detail" in dataset.companyitem_data[0] ? true : false,
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
                                "visible": "url_update" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_update){
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
                                    };
                                }
                            },
                            {
                                "name":"url_delete",
                                "data":"url_delete",
                                "defaultContent": "",
                                "width":"35px",
                                "className":"",
                                "visible": "url_delete" in dataset.companyitem_data[0] ? true : false,
                                "render":function(data,type,row,meta){
                                    if (row.url_delete){
                                        return '<a class="btn btn-danger" href="'+ row.url_delete + "?next=" + dataset.url_detail +'"><i class="fas fa-trash"></i></a>'
                                    };
                                }
                            },
                        ];
                        let print = [];
                        for (let i = 0; i < companyitems.length; i++){
                            if (companyitems[i]["visible"] === true) {print.push(i)};
                        };
                        transformTable("id_companyitem",dataset.companyitem_data,companyitems,[[1,'asc']],print);
                    };
                    // Stock
                    if(dataset.stock_count && document.getElementById("id_stock_count")){
                        document.getElementById("id_stock_count").innerHTML = dataset.stock_count
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
                                "name":"storageitem_name",
                                "data":"storageitem_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "storageitem_name" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.storageitem_name){return row.storageitem_name};}
                            },
                            {
                                "name":"storageitem_reference_number",
                                "data":"storageitem_reference_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "storageitem_reference_number" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.storageitem_reference_number){return row.storageitem_reference_number};}
                            },
                            {
                                "name":"companyitem_name",
                                "data":"companyitem_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "companyitem_name" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.companyitem_name){return row.companyitem_name};}
                            },
                            {
                                "name":"item_number",
                                "data":"item_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "companyitem_item_number" in dataset.stock_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.companyitem_item_number){return row.companyitem_item_number};}
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
                                "render":function(data,type,row,meta){if (row.notice){return '<i class="fas fa-exclamation-triangle"></i>'};}
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
                                "name":"companyitem_name",
                                "data":"companyitem_name",
                                "defaultContent": "",
                                "className":"",
                                "visible": "companyitem_name" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.companyitem_name){return row.companyitem_name};}
                            },
                            {
                                "name":"item_number",
                                "data":"item_number",
                                "defaultContent": "",
                                "className":"",
                                "visible": "companyitem_item_number" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.companyitem_item_number){return row.companyitem_item_number};}
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
                                "name":"notice",
                                "data":"notice",
                                "defaultContent": "",
                                "className":"",
                                "visible": "notice" in dataset.booking_data[0] ? true : false,
                                "render":function(data,type,row,meta){if (row.notice){return '<i class="fas fa-exclamation-triangle"></i>'};}
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
                                        return '<a class="btn btn-primary" href="'+ row.url_update +'"><i class="fas fa-pen"></i></a>'
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
                                        return '<a class="btn btn-danger" href="'+ row.url_delete + "?next=" + dataset.url_detail +'"><i class="fas fa-trash"></i></a>'
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

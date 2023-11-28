function storageitem_overview(api_url,model) {
    $(document).ready(function(){
        $.ajax({
            url: api_url.replaceAll("=&amp;", '=&').replaceAll("&amp;", '&'),
            success: function(dataset){
                if(dataset.length != 0){
                    dataset.forEach(element => {
                        // Name
                        if(element.name && document.getElementById("id_name-"+element.id)){
                            document.getElementById("id_name-"+element.id).innerHTML = element.name;
                        };
                        if(element.url_detail){
                            document.getElementById("id_name-"+element.id).setAttribute("href",element.url_detail);
                        };
                        // Stock
                        if(element.stock_count && document.getElementById("id_stock-"+element.id)){
                            document.getElementById("id_stock-"+element.id).innerHTML = element.stock_count;
                        } else {
                            document.getElementById("id_stock-"+element.id).innerHTML = "0"
                        };
                        // Progressbar
                        if(element.stock_percentage && document.getElementById("id_stock_percentage-"+element.id)){
                            document.getElementById("id_stock_percentage-"+element.id).innerHTML = element.stock_percentage+" %";
                        } else {
                            document.getElementById("id_stock_percentage-"+element.id).innerHTML = "0%"
                        };
                        if(element.stock_percentage && document.getElementById("id_progressbar-"+element.id)){
                            document.getElementById("id_progressbar-"+element.id).setAttribute('aria-valuenow',element.stock_percentage);
                            document.getElementById("id_progressbar-"+element.id).style.width = element.stock_percentage+"%"
                        };
                        // Status
                        if(element.status && document.getElementById("id_progressbar-"+element.id)){
                            if(element.status == 'overload'){
                                document.getElementById("id_progressbar-"+element.id).setAttribute("class",'progress-bar bg-secondary');
                            };
                            if(element.status == 'ok'){
                                document.getElementById("id_progressbar-"+element.id).setAttribute("class",'progress-bar bg-success');
                            };
                            if(element.status == 'warning'){
                                document.getElementById("id_progressbar-"+element.id).setAttribute("class",'progress-bar bg-warning');
                            };
                            if(element.status == 'alarm'){
                                document.getElementById("id_progressbar-"+element.id).setAttribute("class",'progress-bar bg-danger');
                            };
                        };
                        if(element.status && document.getElementById("id_status-"+element.id)){
                            if(element.status == 'overload'){
                                document.getElementById("id_status-"+element.id).setAttribute("class",'card mt-1 mb-1 ms-1 me-1 pt-1 pe-1 pb-1 ps-1 bg-secondary');
                            };
                            if(element.status == 'ok'){
                                document.getElementById("id_status-"+element.id).setAttribute("class",'card mt-1 mb-1 ms-1 me-1 pt-1 pe-1 pb-1 ps-1 bg-success');
                            };
                            if(element.status == 'warning'){
                                document.getElementById("id_status-"+element.id).setAttribute("class",'card mt-1 mb-1 ms-1 me-1 pt-1 pe-1 pb-1 ps-1 bg-warning');
                            };
                            if(element.status == 'alarm'){
                                document.getElementById("id_status-"+element.id).setAttribute("class",'card mt-1 mb-1 ms-1 me-1 pt-1 pe-1 pb-1 ps-1 bg-danger');
                            };
                        };
                        // Booking Urls
                        if(element.url_booking_add){
                            document.getElementById("id_booking_add-"+element.id).setAttribute("href",element.url_booking_add+"?next=storagemanagement:storageitem_overview");
                        };
                        if(element.url_booking_create){
                            document.getElementById("id_stock-"+element.id).setAttribute("href",element.url_booking_create+"?next=storagemanagement:storageitem_overview");
                        };
                        if(element.url_booking_remove){
                            document.getElementById("id_booking_rm-"+element.id).setAttribute("href",element.url_booking_remove+"?next=storagemanagement:storageitem_overview");
                        };
                        // Order
                        if(element.url_order){
                            document.getElementById("id_order-"+element.id).setAttribute("href",element.url_order+"?next=storagemanagement:storageitem_overview");
                        };
                        if(element.order_count){
                            document.getElementById("id_order_count-"+element.id).innerHTML = element.order_count
                        };
                        // Request
                        if(element.url_request_create && document.getElementById("id_request-"+element.id)){
                            document.getElementById("id_request-"+element.id).setAttribute("href",element.url_request_create+"?next=storagemanagement:storageitem_overview");
                        };
                        if(element.request_count){
                            document.getElementById("id_request_count-"+element.id).innerHTML = element.request_count
                        };
                    });
                };
            },
        });
        
    });
}

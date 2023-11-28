function group_overview(api_data_url){
    $(document).ready(function(){
        $.ajax({
            url:api_data_url,
            success: function(dataset){
                string=""
                dataset.forEach(element => {
                     string+= '<div class="col-xxl-3 col-xl-4 col-lg-5 col-md-6 col-sm-12 col-12 mt-3">'+
                                    '<div class="card h-100">'+
                                        '<div class="card-body">'+
                                            '<h1 id="card-title-{{ obj.id }}" class="card-title"></h1>'+
                                            '<p class="card-text">'+
                                                '<div class="mb-3">'+
                                                    '<h5>'+
                                                        '<a class="link-dark text-decoration-none" href="'+element.url_detail+'">'+
                                                            element.name+
                                                        '</a>'+
                                                    '</h5>'+
                                                    '<div>'+
                                                        '<span id="responsible-{{ obj.id }}">'+
                                                            element.reference_number+
                                                        '</span><br>'+
                                                    '</div>'+
                                                '</div>'+
                                            '</p>'+
                                        '</div>'+
                                    '</div>'+
                                '</div>'
                });
                document.getElementById('content').innerHTML = string
            },
        });
    });
}
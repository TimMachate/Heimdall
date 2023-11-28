function transformTable(id,dataset,col,order,print_list){
    /* Tabelle Formatieren */
    $("#"+id).DataTable({
        /* Column Data */
        data: dataset,
        columns: col,
        /* Button Copy, Excel, Print & PDF */
        dom: 'flBrtip',
        buttons:[
            // Copy Button
            {
                extend: 'copy',
                text:'<i class="fas fa-copy"></i>',
                className:"btn btn-primary",
                titleAttr: 'Copy',
                // Chose the columns you wish to copy
                exportOptions: {
                    columns:print_list
                }
            },
            // Excel Button
            {
                extend: 'excel',
                text:'<i class="fas fa-file-excel"></i>',
                className:"btn btn-primary",
                titleAttr: 'Excel',
                // Disable Caption
                messageTop: false,
                // Chose the columns you wish to copy
                exportOptions: {
                    columns:print_list
                }
            },
            // Print Button
            {
                extend: 'print',
                text:'<i class="fas fa-print"></i>',
                className:"btn btn-primary",
                titleAttr: 'Print',
                // Chose the columns you wish to copy
                exportOptions: {
                    columns:print_list
                }
            },
            // PDF Button
            {
                extend: 'pdf',
                text:'<i class="fas fa-file-pdf"></i>',
                className:"btn btn-primary",
                titleAttr: 'PDF',
                // Disable Caption
                messageTop: false,
                // Chose the columns you wish to copy
                exportOptions: {
                    columns:print_list
                }
            }
        ],
        /* Responsive Design */
        responsive:true,
        /* Paging True or False */
        info: true,
        paging: true,
        /* scrollX */
        //"sScrollX": "100%",
        //"sScrollXInner": '100%',
        //"bScrollCollapse": true,
        /* Searching True or False */
        searching: true,
        /* Ordering True or False */
        ordering: true,
        order: order,
        /* Ordersymbols in the Top Line Header */
        orderCellsTop: true,
        /* Auto Width True or False */
        autoWidth: true,
        /* Change Language to German */
        language: {
            "aria": {
                "sortAscending": ": Aufsteigende Sortierung",
                "sortDescending": ": Absteigende Sortierung"
            },
            "decimal": ',',
            "emptyTable": "Keine Daten vorhanden in der Tabelle",
            "info": "Seite _PAGE_ von _PAGES_",
            "infoEmpty": "Seite 0 von 0",
            "infoFiltered": "(gefiltert von _MAX_ totalen Einträgen)",
            "infoPostFix": "",
            "lengthMenu": "Zeige _MENU_ Einträge pro Seite",
            "loadingRecords": "Laden ...",
            "paginate": {
                "first": "Erste",
                "last": "Letzte",
                "next": "Nächste",
                "previous": "Vorherige"
                },
            "processing":     "",
            "search": "Suche:",
            "thousands": '.',
            "zeroRecords": "Keine Einträge gefunden!"
        },
        /* Filters */
        fixedHeader: false,
    })
}
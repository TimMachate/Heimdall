function createList(id,dataset,col,order,print_list){
    /* Tabelle Formatieren */
    $("#"+id).DataTable({
        /* Responsive Design */
        responsive:true,
        /* Paging True or False */
        info: false,
        paging: false,
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
        /* Column Data */
        data:dataset,
        columns: col,
        /* Filters */
        fixedHeader: false,
    })
}
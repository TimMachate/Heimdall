function createTable(id,dataset,col,order,print_list){
    /* Tabelle Formatieren */
    $("#"+id).DataTable({
        /* Responsive Design */
        responsive:true,
        /* Paging True or False */
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
        autoWidth: false,
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
        /* Filters */
        fixedHeader: false,
        initComplete: function () {
                var api = this.api();
                // For each column
                api
                    .columns()
                    .eq(0)
                    .each(function (colIdx) {
                        $(
                            'input',
                            $('.filters th').eq($(api.column(colIdx).footer()).index())
                        )
                        .off('keyup change')
                        .on('change', function (e) {
                            // Get the search value
                            $(this).attr('title', $(this).val());
                            var regexr = '({search})'; //$(this).parents('th').find('select').val();

                            var cursorPosition = this.selectionStart;
                            // Search the column for that value
                            api
                                .column(colIdx)
                                .search(
                                    this.value != ''
                                        ? regexr.replace('{search}', '(((' + this.value + ')))')
                                        : '',
                                    this.value != '',
                                    this.value == ''
                                )
                                .draw();
                        })
                        .on('keyup', function (e) {
                            e.stopPropagation();

                            $(this).trigger('change');
                            $(this)
                                .focus()[0]
                                .setSelectionRange(cursorPosition, cursorPosition);
                        });
                    });
            },
    })
}
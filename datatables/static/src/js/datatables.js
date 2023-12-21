$(document).ready(function () {
    console.log("datatables ready!");
// Константы забираемые с шаблона
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    // Словарь с url
    const urls = JSON.parse(document.getElementById('urls').textContent);
    console.log(urls);

//  Данные при раскрытии
    function format(data) {
        console.log(data);
        var html = '<table class="table">';
        html += '<thead>';
        html += '<tr><th scope="col">Записи</th>';
        html += '</thead>';
        html += '<tbody>';
        html += '<tr>';
        html += '<td>' + data.name + '</td>';
        html += '</tr>';
        html += '</tbody>';
        return html;
    }


//  Pipelining function for DataTables. To be used to the `ajax` option of DataTables

    $.fn.dataTable.pipeline = function (opts) {
        // Configuration options
        var conf = $.extend(
            {
                pages: 5, // number of pages to cache
                url: '', // script url
                data: null, // function or object with parameters to send to the server
                // matching how `ajax.data` works in DataTables
                method: 'GET', // Ajax HTTP method
            },
            opts
        );

        // Private variables for storing the cache
        var cacheLower = -1;
        var cacheUpper = null;
        var cacheLastRequest = null;
        var cacheLastJson = null;

        return function (request, drawCallback, settings) {
            var ajax = false;
            var requestStart = request.start;
            var drawStart = request.start;
            var requestLength = request.length;
            var requestEnd = requestStart + requestLength;

            if (settings.clearCache) {
                // API requested that the cache be cleared
                ajax = true;
                settings.clearCache = false;
            } else if (cacheLower < 0 || requestStart < cacheLower || requestEnd > cacheUpper) {
                // outside cached data - need to make a request
                ajax = true;
            } else if (
                JSON.stringify(request.order) !== JSON.stringify(cacheLastRequest.order) ||
                JSON.stringify(request.columns) !== JSON.stringify(cacheLastRequest.columns) ||
                JSON.stringify(request.search) !== JSON.stringify(cacheLastRequest.search)
            ) {
                // properties changed (ordering, columns, searching)
                ajax = true;
            }
            // Store the request for checking next time around
            cacheLastRequest = $.extend(true, {}, request);

            var json;
            if (ajax) {
                // Need data from the server
                if (requestStart < cacheLower) {
                    requestStart = requestStart - requestLength * (conf.pages - 1);

                    if (requestStart < 0) {
                        requestStart = 0;
                    }
                }

                cacheLower = requestStart;
                cacheUpper = requestStart + requestLength * conf.pages;

                request.start = requestStart;
                request.length = requestLength * conf.pages;

                // Provide the same `data` options as DataTables.
                if (typeof conf.data === 'function') {
                    //  As a function it is executed with the data object as an arg
                    //  for manipulation. If an object is returned, it is used as the
                    //  data object to submit
                    var d = conf.data(request);
                    if (d) {
                        $.extend(request, d);
                    }
                } else if ($.isPlainObject(conf.data)) {
                    //  As an object, the data given extends the default
                    $.extend(request, conf.data);
                }

                return $.ajax({
                    type: conf.method,
                    url: conf.url,
                    data: request,
                    dataType: 'json',
                    cache: false,
                    success: function (json) {
                        cacheLastJson = $.extend(true, {}, json);

                        if (cacheLower !== drawStart) {
                            json.data.splice(0, drawStart - cacheLower);
                        }
                        if (requestLength >= -1) {
                            json.data.splice(requestLength, json.data.length);
                        }

                        drawCallback(json);
                    },
                });
            } else {
                json = $.extend(true, {}, cacheLastJson);
                json.draw = request.draw; // Update the echo for each response
                json.data.splice(0, requestStart - cacheLower);
                json.data.splice(requestLength, json.data.length);

                drawCallback(json);
            }
        };
    };

//  Register an API method that will empty the pipelined data, forcing an Ajax
//  fetch on the next draw (i.e. `table.clearPipeline().draw()`)
    $.fn.dataTable.Api.register('clearPipeline()', function () {
        return this.iterator('table', function (settings) {
            settings.clearCache = true;
        });
    });

//  DataTables initialisation
    let table = null;
    $(document).ready(function () {
        table = $('#users_table').DataTable({
            responsive: true,
            search: {return: true},
            dom: 'lBfrtip',
            order: [],
            orderCellsTop: true,
            deferRender: true,
            processing: true,
            serverSide: true,
            ajax: $.fn.dataTable.pipeline({
                url: urls['data_url'],
                type: 'GET',
                contentType: 'application/json',
                pages: 5   // Number of cache pages
            }),
            columns: [
                {target: 0, title: "id", data: "id"},
                {target: 1, title: "name", data: "name",},
                {target: 2, title: "code", data: "code"},
                {
                    target: 3,
                    title: "url",
                    data: "url",
                    render: function (data, type) {
                        return '<a href="' + data + '">' + data + '</a>';
                    }
                },
                {target: 4, title: "description", data: "description"},
                {target: 5, title: "cost", data: "cost"},
                {
                    target: 6,
                    title: "count",
                    data: null,
                    orderable: false,
                    defaultContent: '<div class="number " data-step="1" data-min="1" data-max="100">' +
                        '<button class="btn btn-outline-secondary number-minus buttons-html5">−</button>' +
                        '<input class="number-text" type="text" name="count" value="1">' +
                        '<button class="btn btn-outline-secondary number-plus buttons-html5">+</button></div>',
                    width: "10%"
                },
                {
                    target: 7,
                    title: "action",
                    data: null,
                    orderable: false,
                    defaultContent: '<button class="btn btn-outline-secondary add_to_cart buttons-html5">go!</button>'
                },
            ],
            buttons: {
                buttons: [
                    'print',
                    'copy',
                    {extend: 'excel', text: 'Save as Excel'},
                    {text: 'Expand all', className: 'btn-show-all-children buttons-html5'},
                    {text: 'Hide all', className: 'btn-hide-all-children buttons-html5'},
                ]
            },

            // createdRow: function (row, data, dataIndex) {
            //     $(row).attr("id", data.id);
            //     // Редактируем 2ую колонку
            //     $('td', row).eq(1).html('<a href=' + data.url + '>' + data.name + '</a>');
            // },
            lengthMenu: [
                [10, 25, 50, 100],
                ["10", "25", "50", "100"],
            ],
            pageLength: 10,
        });


//  Обрабатывем кнопку клик
        table.on("click", ".add_to_cart", function (e) {
            // Находим сообщение
            const cart_message = $('#cart_message');
            // Данные строки
            let data = table.row(e.target.closest("tr")).data();
            console.log(data);
            // Получаем текст из инпута в строке
            let cart_count = $(e.target.closest("tr")).find("input.number-text").val();
            console.log(cart_count);

            //  Обрабатывем ответ
            function add_to_cart_response(response) {
                if (response['success']) {
                    cart_message.fadeIn().removeClass('cardmess_red').addClass('cardmess_green');
                } else {
                    cart_message.fadeIn().removeClass('cardmess_green').addClass('cardmess_red');
                }
                cart_message.text(response['message']);
                setTimeout(function () {
                    cart_message.fadeOut();
                }, 1200);
            }

            //  Отправляем данные
            $.ajax({
                type: 'POST',
                url: urls['add_to_cart_url'],
                headers: {'X-CSRFToken': csrftoken},
                data: {'id': data.id, 'count': cart_count},
            })
                .done(add_to_cart_response);
        });

        //  Обрабатываем счетчик +-1
        $(document).ready(function () {
            $('body').on('click', '.number-minus, .number-plus', function () {
                var $row = $(this).closest('.number');
                var $input = $row.find('.number-text');
                var step = $row.data('step');
                var val = parseFloat($input.val());
                if ($(this).hasClass('number-minus')) {
                    val -= step;
                } else {
                    val += step;
                }
                $input.val(val);
                $input.change();
                return false;
            });

            $('body').on('change', '.number-text', function () {
                var $input = $(this);
                var $row = $input.closest('.number');
                var step = $row.data('step');
                var min = parseInt($row.data('min'));
                var max = parseInt($row.data('max'));
                var val = parseFloat($input.val());
                if (isNaN(val)) {
                    val = step;
                } else if (min && val < min) {
                    val = min;
                } else if (max && val > max) {
                    val = max;
                }
                $input.val(val);
            });
        });

//  Array to track the ids of the details displayed rows
        const detailRows = [];

        table.on('click', 'tbody td.dt-control', function () {
            let tr = event.target.closest('tr');
            let row = table.row(tr);
            let idx = detailRows.indexOf(tr.id);

            if (row.child.isShown()) {
                tr.classList.remove('details');
                row.child.hide();

                // Remove from the 'open' array
                detailRows.splice(idx, 1);
            } else {
                tr.classList.add('details');
                row.child(format(row.data())).show();

                // Add to the 'open' array
                if (idx === -1) {
                    detailRows.push(tr.id);
                }
            }
        });

//  On each draw, loop over the `detailRows` array and show any child rows
        table.on('draw', () => {
            detailRows.forEach((id, i) => {
                let el = document.querySelector('#' + id + ' td.dt-control');

                if (el) {
                    el.dispatchEvent(new Event('click', {bubbles: true}));
                }
            });
        });

        // Handle click on "Expand All" button
        $('.btn-show-all-children').on('click', function () {
            // Enumerate all rows
            table.rows().every(function () {
                // If row has details collapsed
                if (!this.child.isShown()) {
                    // Open this row
                    this.child(format(this.data())).show();
                    $(this.node()).addClass('shown');
                }
            });
        });

        // Handle click on "Collapse All" button
        $('.btn-hide-all-children').on('click', function () {
            // Enumerate all rows
            table.rows().every(function () {
                // If row has details expanded
                if (this.child.isShown()) {
                    // Collapse row details
                    this.child.hide();
                    $(this.node()).removeClass('shown');
                }
            });
        });
    });
});

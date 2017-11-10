$(document).ready(function(){
    var acount = 0;
    var scount = 0;
    var name_length = 0;
    var assemblyMetrics = assembly_metrics.dimension(function(d){
        acount++;
        if (d.assembly_name.length > name_length){
            name_length = d.assembly_name.length;
        }
        return d.assembly_name;
    });
    var left_margin = name_length * 5 + 20;
    var bottom_margin = name_length * 4 + 10;
    var wa = acount * 30 + left_margin + 60;
    var assemblyMetricsTable = $('#metrics-datatable').dataTable({
        "data": assembly_data_table,
        "columns": assembly_header,
        "colReorder" : {
            fixedColumnsLeft: 1
        },
        "search": {
            "caseInsensitive": true,
            "regex": true
        },
        "select" : true
    });
    var scaffoldContiguity = dc.barChart("#scaffoldContiguity-chart");
    var scaffold_N50 = assemblyMetrics.group().reduceSum(function(d){
        return d.scaffold_N50;
    });
    scaffoldContiguity
        .width(wa)
        .height(600)
        .dimension(assemblyMetrics)
        .margins({top: 50, right: 50, bottom: bottom_margin, left: left_margin})
        .colors('green')
        .group(scaffold_N50, "Scaffold N50")
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Assembly Identifier")
        .yAxisLabel("Scaffold N50")
        .transitionDuration(10)
        .legend((dc.legend().x(120).y(0).itemHeight(16).gap(4)))
        .on('renderlet', function(chart){
        chart.selectAll('rect').on('click.custom', function(d){
            var chartI = dc.chartRegistry.list('assemblymetrics_group');
            var table = $('#metrics-datatable').DataTable();
            var rows = $("#metrics-datatable").dataTable()._('tr');
            for (var r = 0; r < rows.length; r++){
                if (rows[r][0] === d.x){
                    var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                        return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                    });
                    if (table.rows(indexes).nodes().to$().hasClass('selected') === false){
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .addClass('selected');
                        console.log(rows[r], indexes);
                    } else {
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .removeClass('selected');
                    }
                }
            }
            for (var i = 0; i < chartI.length; i++) {
                if (chartI[i].chartName !== 'scaffoldcontiguity'){
                    chartI[i].filter(d.x);
                    console.log(chartI[i].chartName);
                }
            }
            dc.renderAll();
            console.log(d.x + "thing" + chartI);
        });	
    });
    scaffoldContiguity.chartName = 'scaffoldcontiguity';
    dc.chartRegistry.register(scaffoldContiguity, 'assemblymetrics_group');

    var assemblyBases = dc.barChart("#assemblyBases-chart");
    var contig_bases = assemblyMetrics.group().reduceSum(function(d){
        return d.contig_length;
    });
    var gap_bases = assemblyMetrics.group().reduceSum(function(d){
        return d.gap_length;
    });
    assemblyBases
        .width(wa)
        .height(600)
        .dimension(assemblyMetrics)
        .margins({top: 50, right: 50, bottom: bottom_margin, left: left_margin})
        .title(function(d){
            return d.key + ' ' + this.layer + ' ' + d.value;
        })
        .group(contig_bases, "Bases in Contigs")
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Assembly Identifier")
        .yAxisLabel("Assembly Bases")
        .stack(gap_bases, "Bases in Gaps")
        .transitionDuration(10)
        .legend((dc.legend().x(120).y(0).itemHeight(16).gap(4)))
        .on('renderlet', function(chart){
        chart.selectAll('rect').on('click.custom', function(d){
            var chartI = dc.chartRegistry.list('assemblymetrics_group');
            var table = $('#metrics-datatable').DataTable();
            var rows = $("#metrics-datatable").dataTable()._('tr');
            for (var r = 0; r < rows.length; r++){
                if (rows[r][0] === d.x){
                    var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                        return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                    });
                    if (table.rows(indexes).nodes().to$().hasClass('selected') === false){
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .addClass('selected');
                        console.log(rows[r], indexes);
                    } else {
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .removeClass('selected');
                    }
                }
            }
            for (var i = 0; i < chartI.length; i++) {
                if (chartI[i].chartName !== 'assemblybases'){
                    chartI[i].filter(d.x);
                    console.log(chartI[i].chartName);
                }
            }
            dc.renderAll();
            console.log(d.x + "thing" + chartI);
        });	
    });
    assemblyBases.chartName = 'assemblybases';
    dc.chartRegistry.register(assemblyBases, 'assemblymetrics_group');
    var buscoComplete = dc.barChart("#buscoComplete-chart");
    var busco_complete = assemblyMetrics.group().reduceSum(function(d){
        return d.busco_complete;
    });
    var busco_fragmented = assemblyMetrics.group().reduceSum(function(d){
        return d.busco_fragmented;
    });
    var busco_missing = assemblyMetrics.group().reduceSum(function(d){
        return d.busco_missing;
    });
    buscoComplete
        .width(wa)
        .height(600)
        .dimension(assemblyMetrics)
        .margins({top: 50, right: 50, bottom: bottom_margin, left: left_margin})
        .title(function(d){
            return d.key + ' ' + this.layer + ' ' + d.value;
        })
        .group(busco_complete, "Complete BUSCOs")
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Assembly Identifier")
        .yAxisLabel("Percentage")
        .stack(busco_fragmented, "Fragmented BUSCOs")
        .stack(busco_missing, "Missing BUSCOs")
        .transitionDuration(10)
        .legend((dc.legend().x(120).y(0).itemHeight(16).gap(4)))
        .on('renderlet', function(chart){
        chart.selectAll('rect').on('click.custom', function(d){
            var chartI = dc.chartRegistry.list('assemblymetrics_group');
            var table = $('#metrics-datatable').DataTable();
            var rows = $("#metrics-datatable").dataTable()._('tr');
            for (var r = 0; r < rows.length; r++){
                if (rows[r][0] === d.x){
                    var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                        return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                    });
                    if (table.rows(indexes).nodes().to$().hasClass('selected') === false){
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .addClass('selected');
                        console.log(rows[r], indexes);
                    } else {
                        table.rows(indexes)
                             .nodes()
                             .to$()
                             .removeClass('selected');
                    }
                }
            }
            for (var i = 0; i < chartI.length; i++) {
                if (chartI[i].chartName !== 'buscocomplete'){
                    chartI[i].filter(d.x);
                    console.log(chartI[i].chartName);
                }
            }
            dc.renderAll();
            console.log(d.x + "thing" + chartI);
        });	
    });
    buscoComplete.chartName = 'buscocomplete';
    dc.chartRegistry.register(buscoComplete, 'assemblymetrics_group');
    dc.renderAll();

    $("#reset-metrics").click(function(){
        var table = $('#metrics-datatable').DataTable();
        var chartI = dc.chartRegistry.list('assemblymetrics_group');
        table.rows('.selected').deselect();
        table.search("").draw();
        var len = $("#metrics-datatable").dataTable()._('tr').length;
        var w = len * 30 + left_margin + 60;
        for (var i = 0; i < chartI.length; i++) {
            if (chartI[i].chartName === 'scaffoldcontiguity'){
                var contiguity= assemblyMetrics.group().reduceSum(function(d){
                    return d.scaffold_N50;
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(contiguity, "Scaffold N50");
                chartI[i].filter(null);
            }
            else if (chartI[i].chartName === 'assemblybases') {
                var contig_bases = assemblyMetrics.group().reduceSum(function(d){
                    return d.contig_length;
                });
                var gap_bases = assemblyMetrics.group().reduceSum(function(d){
                    return d.gap_length;							
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(contig_bases, "Bases in Contigs");
                chartI[i].stack(gap_bases, "Bases in Gaps")
                chartI[i].filter(null);
            }
            else if (chartI[i].chartName === 'buscocomplete') {
                var busco_complete = assemblyMetrics.group().reduceSum(function(d){
                    return d.busco_complete;
                });
                var busco_fragmented = assemblyMetrics.group().reduceSum(function(d){
                    return d.busco_fragmented;
                });
                var busco_missing = assemblyMetrics.group().reduceSum(function(d){
                    return d.busco_missing;
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(busco_complete, "Complete BUSCOs")
                chartI[i].stack(busco_fragmented, "Fragmented BUSCOs")
                chartI[i].stack(busco_missing, "Missing BUSCOs")
                chartI[i].filter(null);
            }
        }
        dc.redrawAll();
        table.order([0, 'asc']).draw();
    });

    $('#metrics-datatable tbody').on('click', 'tr', function(){
        var chartI = dc.chartRegistry.list('assemblymetrics_group');
        var rows = $('#metrics-datatable').DataTable().rows('.selected').data();
        console.log($(this)[0].getElementsByTagName('td')[0].innerText);
        var filtered_samples = assemblyMetrics.top(Infinity);
        console.log(filtered_samples);
        for (var j = 0;j<chartI.length; j++){
            chartI[j].filter(null)
            for (var i = 0;i<rows.length; i++){
                chartI[j].filter(rows[i][0]);
            }
        }
        dc.redrawAll();
    });

    $('#metrics-datatable thead').on('click', 'th', function(){
        var s = [];
        var chartI = dc.chartRegistry.list('assemblymetrics_group');
        var rows = $("#metrics-datatable").dataTable()._('tr', {"filter": "applied"});
        for (var i = 0;i<rows.length;i++){
            s.push(rows[i][0]);
        }
        for (var i = 0;i<chartI.length; i++){
            chartI[i].x(d3.scale.ordinal().domain(s));
        }
        dc.redrawAll();
    });
    $("#metrics-datatable_filter input").on('keyup', function(k){
        var rows = $("#metrics-datatable").dataTable()._('tr', {"filter": "applied"});
        var chartI = dc.chartRegistry.list('assemblymetrics_group');
        var s = [];
        var r = {};
        for (var i = 0;i<rows.length;i++){
            s.push(rows[i][0]);
            r[rows[i][0]] = 1;
        }
        for (var i = 0;i<chartI.length; i++){
            if (chartI[i].chartName === 'scaffoldcontiguity'){
                var contiguity_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.scaffold_N50;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(contiguity_filter, "Scaffold N50");
            }
            else if (chartI[i].chartName === 'assemblybases') {
                var contig_bases_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.contig_length;
                    }
                });
                var gap_bases_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.gap_length;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(contig_bases_filter, "Bases in Contigs");
                chartI[i].stack(gap_bases_filter, "Bases in Gaps")
            }
            else if (chartI[i].chartName === 'buscocomplete') {
                var busco_complete_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_complete;
                    }
                });
                var busco_fragmented_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_fragmented;
                    }
                });
                var busco_missing_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_missing;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(busco_complete_filter, "Complete BUSCOs");
                chartI[i].stack(busco_fragmented_filter, "Fragmented BUSCOs");
                chartI[i].stack(busco_missing_filter, "Missing BUSCOs");
                chartI[i].filter(null);
            }
        }
        dc.renderAll();
    });

    $("#filter-metrics").click(function(d){
        var searchstr = "";
        var s = [];
        var r = {};
        var rows = $('#metrics-datatable').DataTable().rows('.selected').data();
        var table = $('#metrics-datatable').DataTable();
        var chartI = dc.chartRegistry.list('assemblymetrics_group');
        if (rows.length === 0){
            return 0
        }
        for (var i=0;i<rows.length;i++){
            s.push(rows[i][0]);
            r[rows[i][0]] = 1;
            if (searchstr.length < 1){
                searchstr = rows[i][0] + '[^\\S+]';
            } else {
                searchstr += "|" + rows[i][0] + '[^\\S+]';
            }
        }
        table.search(searchstr, 1, true, false).draw();
        for (var i = 0;i<chartI.length; i++){
            if (chartI[i].chartName === 'scaffoldcontiguity'){
                var contiguity_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.scaffold_N50;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(contiguity_filter, "Scaffold N50");
                chartI[i].filter(null);
            }
            else if (chartI[i].chartName === 'assemblybases') {
                var contig_bases_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.contig_length;
                    }
                });
                var gap_bases_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.gap_length;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(contig_bases_filter, "Bases in Contigs");
                chartI[i].stack(gap_bases_filter, "Bases in Gaps");
                chartI[i].filter(null);
            }
            else if (chartI[i].chartName === 'buscocomplete') {
                var busco_complete_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_complete;
                    }
                });
                var busco_fragmented_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_fragmented;
                    }
                });
                var busco_missing_filter = assemblyMetrics.group().reduceSum(function(d){
                    if (r[d.assembly_name] === 1){
                        return d.busco_missing;
                    }
                });
                var len = rows.length;
                wa = (len * 30) + left_margin + 60;
                chartI[i].width(wa);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(busco_complete_filter, "Complete BUSCOs")
                chartI[i].stack(busco_fragmented_filter, "Fragmented BUSCOs")
                chartI[i].stack(busco_missing_filter, "Missing BUSCOs")
                chartI[i].filter(null);
            }
        }
        table.rows('.selected').deselect();
        dc.renderAll();
    });

    $('a.toggle-vis-metrics').on('click', function(e){
        e.preventDefault();
        var column = $("#metrics-datatable").DataTable().column(':contains(' + $(this).attr('data-column') + ')');
        column.visible(! column.visible());
        color_anchors($(this));
    });
});

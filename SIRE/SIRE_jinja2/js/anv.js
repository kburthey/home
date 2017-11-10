$(document).ready(function(){
    $('a.toggle-vis-aln').on('click', function(e){
        e.preventDefault();
        var column = $("#anv-datatable").DataTable().column(':contains(' + $(this).attr('data-column') + ')');
        column.visible(! column.visible());
        color_anchors($(this));
    });
    var count = 0;
    var longest = 0;
    var anvSamples = anvData.dimension(function(d){
        count++;
        if (d.sample.length > longest){
            longest = d.sample.length;
        }
        return d.sample;
    });
    var left_m = longest * 5 + 30;
    var bottom_m = longest * 5 + 30;
    var w = count * 30 + left_m + 60;
    var anvTable = $('#anv-datatable').dataTable({
        "data": anv_table_data,
        "columns": anv_header,
        "colReorder" : {
            "fixedColumnsLeft" : 1
        },
        "search": {
            "caseInsensitive": true,
            "regex": true
        },
        "select" : true
    });
    var anvAligned = anvSamples.group().reduceSum(function(d){
        return d.aligned;
    });
    var anvUnique =  anvSamples.group().reduceSum(function(d){
        return d.unique;
    });
    var anvAmbig = anvSamples.group().reduceSum(function(d){
        return d.aligned - d.unique;
    });
    var anvUnaligned = anvSamples.group().reduceSum(function(d){
        return d.total - d.aligned;
    });
    var anvIndels = anvSamples.group().reduceSum(function(d){
        return d.indels;
    });
    var anvSNPs = anvSamples.group().reduceSum(function(d){
        return d.snps;
    });
    var anvHets = anvSamples.group().reduceSum(function(d){
        return d.hets;
    });
    var anvnHom = anvSamples.group().reduceSum(function(d){
        return d.nref_hom;
    });
    var anvHom = anvSamples.group().reduceSum(function(d){
        return d.ref_hom;
    });

    var anvAlign = dc.barChart("#anvalign-chart");
    anvAlign
        .width(w)
        .height(400)
        .dimension(anvSamples)
        .margins({top: 100, right: 50, bottom: bottom_m, left: left_m})
        .group(anvUnique, "Unique")
        .title(function(d){
            return d.key + ' ' + this.layer + ' ' + d.value;
        })
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Sample")
        .yAxisLabel("Alignments")
        .stack(anvAmbig, "Ambiguous")
        .stack(anvUnaligned, "Unmapped")
        .legend((dc.legend().x(120).y(30).itemHeight(16).gap(4)))
        .transitionDuration(10)
        .on('renderlet', function(chart){
            chart.selectAll('rect').on('click.custom', function(d){
                var chartI = dc.chartRegistry.list('anvsample_group');
                var table = $('#anv-datatable').DataTable();
                var rows = $("#anv-datatable").dataTable()._('tr');
                for (var r = 0; r < rows.length; r++){
                    if (rows[r][0] === d.x){
                        var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                            return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                        } );
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
                    if (chartI[i].chartName !== 'anvalign'){
                        chartI[i].filter(d.x);
                        console.log(chartI[i].chartName);
                    }
                }
                dc.renderAll();
                console.log(d.x + "thing" + chartI);
            });
        });
    anvAlign.chartName = 'anvalign';
    dc.chartRegistry.register(anvAlign, 'anvsample_group');

    var anvByType = dc.barChart("#anvbytype-chart");
    anvByType
        .width(w)
        .height(400)
        .dimension(anvSamples)
        .margins({top: 100, right: 50, bottom: bottom_m, left: left_m})
        .group(anvIndels, "InDels")
        .title(function(d){
            return d.key + ' ' + this.layer + ' ' + d.value;
        })
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Sample")
        .yAxisLabel("Total Variants")
        .stack(anvSNPs, "SNPs")
        .legend((dc.legend().x(120).y(30).itemHeight(16).gap(4)))
        .transitionDuration(10)
        .on('renderlet', function(chart){
            chart.selectAll('rect').on('click.custom', function(d){
                var chartI = dc.chartRegistry.list('anvsample_group');
                var table = $('#anv-datatable').DataTable();
                var rows = $("#anv-datatable").dataTable()._('tr');
                for (var r = 0; r < rows.length; r++){
                    if (rows[r][0] === d.x){
                        var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                            return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                        } );
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
                    if (chartI[i].chartName !== 'anvbytype'){
                        chartI[i].filter(d.x);
                        console.log(chartI[i].chartName);
                    }
                }
                dc.renderAll();
                console.log(d.x + "thing" + chartI);
            });
        });
    anvByType.chartName = 'anvbytype';
    dc.chartRegistry.register(anvByType, 'anvsample_group');

    var varByType = dc.barChart("#varbytype-chart");
    varByType
        .width(w)
        .height(400)
        .dimension(anvSamples)
        .margins({top: 100, right: 50, bottom: bottom_m, left: left_m})
        .group(anvHom, "Homozygous Ref")
        .title(function(d){
            return d.key + ' ' + this.layer + ' ' + d.value;
        })
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel("Sample")
        .yAxisLabel("Total Variants")
        .stack(anvnHom, "Homozygous Alt")
        .stack(anvHets, "Heterozygous")
        .legend((dc.legend().x(120).y(30).itemHeight(16).gap(4)))
        .transitionDuration(10)
        .on('renderlet', function(chart){
            chart.selectAll('rect').on('click.custom', function(d){
                var chartI = dc.chartRegistry.list('anvsample_group');
                var table = $('#anv-datatable').DataTable();
                var rows = $("#anv-datatable").dataTable()._('tr');
                for (var r = 0; r < rows.length; r++){
                    if (rows[r][0] === d.x){
                        var indexes = table.rows().eq( 0 ).filter( function (rowIdx) {
                            return table.cell( rowIdx, 0 ).data() === d.x ? true : false;
                        } );
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
                    if (chartI[i].chartName !== 'varbytype'){
                        chartI[i].filter(d.x);
                        console.log(chartI[i].chartName);
                    }
                }
                dc.renderAll();
                console.log(d.x + "thing" + chartI);
            });
        });
    varByType.chartName = 'varbytype';
    dc.chartRegistry.register(varByType, 'anvsample_group');

    dc.renderAll();
    $('#anv-datatable thead').on('click', 'th', function(){
        var s = [];
        var chartI = dc.chartRegistry.list('anvsample_group');
        var rows = $("#anv-datatable").dataTable()._('tr', {"filter": "applied"});
        for (var i = 0;i<rows.length;i++){
            s.push(rows[i][0]);
        }
        for (var i = 0;i<chartI.length; i++){
            chartI[i].x(d3.scale.ordinal().domain(s));
        }
        dc.redrawAll();
    });
    $('#anv-datatable tbody').on('click', 'tr', function(){
        var chartI = dc.chartRegistry.list('anvsample_group');
        var rows = $('#anv-datatable').DataTable().rows('.selected').data();
        console.log($(this)[0].getElementsByTagName('td')[0].innerText);
        var filtered_samples = anvSamples.top(Infinity);
        console.log(filtered_samples);
        for (var j = 0;j<chartI.length; j++){
            chartI[j].filter(null)
            for (var i = 0;i<rows.length; i++){
                chartI[j].filter(rows[i][0]);
            }
        }
        dc.redrawAll();
    });
    $("#reset-anv").click(function(){
        var table = $('#anv-datatable').DataTable();
        var chartI = dc.chartRegistry.list('anvsample_group');
        table.rows('.selected').deselect();
        table.search("").draw();
        var len = $("#anv-datatable").dataTable()._('tr').length;
        var w = len * 30 + left_m + 60;
        for (var i = 0; i < chartI.length; i++) {
            if (chartI[i].chartName === 'anvbytype'){
                var indels_filter = anvSamples.group().reduceSum(function(d){
                    return d.indels;
                });
                var snps_filter = anvSamples.group().reduceSum(function(d){
                    return d.snps;
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(indels_filter, "InDels");
                chartI[i].stack(snps_filter, "SNPs");
                chartI[i].filter(null);
            }
            if (chartI[i].chartName === 'varbytype'){
                var homs_filter = anvSamples.group().reduceSum(function(d){
                    return d.ref_hom;
                });
                var nhoms_filter = anvSamples.group().reduceSum(function(d){
                    return d.nref_hom;
                });
                var hets_filter = anvSamples.group().reduceSum(function(d){
                    return d.hets;
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(homs_filter, "Homozygous Ref");
                chartI[i].stack(nhoms_filter, "Homozygous Alt");
                chartI[i].stack(hets_filter, "Heterozygous");
                chartI[i].filter(null);
            }
            if (chartI[i].chartName === 'anvalign'){
                var anvAligned_filter = anvSamples.group().reduceSum(function(d){
                    return d.aligned;
                });
                var anvUnaligned_filter = anvSamples.group().reduceSum(function(d){
                    return d.total - d.aligned;
                });
                var anvUnique_filter =  anvSamples.group().reduceSum(function(d){
                    return d.unique;
                });
                var anvAmbig_filter = anvSamples.group().reduceSum(function(d){
                    return d.aligned - d.unique;
                });
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal());
                chartI[i].group(anvUnique_filter, "Unique");
                chartI[i].stack(anvAmbig_filter, "Ambiguous");
                chartI[i].stack(anvUnaligned_filter, "Unmapped");
                chartI[i].filter(null);
            }
        }
        dc.redrawAll();
        table.order([0, 'asc']).draw();
    });

    $("#filter-anv").click(function(d){
        var searchstr = "";
        var s = [];
        var r = {};
        var rows = $('#anv-datatable').DataTable().rows('.selected').data();
        var table = $('#anv-datatable').DataTable();
        var chartI = dc.chartRegistry.list('anvsample_group');
        if (rows.length === 0){
            return 0
        }
        for (var i=0;i<rows.length;i++){
            s.push(rows[i][0]);
            r[rows[i][0]] = 1;
            if (searchstr.length < 1){
                searchstr = '(' + rows[i][0] + ')[^\\S+]';
            } else {
                searchstr += '|(' + rows[i][0] + ')[^\\S+]';
            }
        }
        table.search(searchstr, 1, true, true).draw();
        for (var i = 0;i<chartI.length; i++){
            if (chartI[i].chartName === 'anvbytype'){
                var indels_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.indels;
                    }
                });
                var snps_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.snps;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(indels_filter, "InDels");
                chartI[i].stack(snps_filter, "SNPs");
                chartI[i].filter(null);
            }
            if (chartI[i].chartName === 'varbytype'){
                var homs_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.ref_hom;
                    }
                });
                var nhoms_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.nref_hom;
                    }
                });
                var hets_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.hets;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(homs_filter, "Homozygous Ref");
                chartI[i].stack(nhoms_filter, "Homozygous Alt");
                chartI[i].stack(hets_filter, "Heterozygous");
                chartI[i].filter(null);
            }
            if (chartI[i].chartName === 'anvalign'){
                var anvAligned_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.aligned;
                    }
                });
                var anvUnaligned_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.total - d.aligned;
                    }
                });
                var anvUnique_filter =  anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.unique;
                    }
                });
                var anvAmbig_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.aligned - d.unique;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(anvUnique_filter, "Unique");
                chartI[i].stack(anvAmbig_filter, "Ambiguous");
                chartI[i].stack(anvUnaligned_filter, "Unmapped");
                chartI[i].filter(null);
            }
        }
        table.rows('.selected').deselect();
        dc.renderAll();
    });
    $("#anv-datatable_filter input").on('keyup', function(k){
        var rows = $("#anv-datatable").dataTable()._('tr', {"filter": "applied"});
        var chartI = dc.chartRegistry.list('anvsample_group');
        var s = [];
        var r = {};
        if (rows.length === 0){
            return;
        }
        for (var i = 0;i<rows.length;i++){
            s.push(rows[i][0]);
            r[rows[i][0]] = 1;
        }
        for (var i = 0;i<chartI.length; i++){
            if (chartI[i].chartName === 'anvbytype'){
                var indels_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.indels;
                    }
                });
                var snps_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.snps;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(indels_filter, "InDels");
                chartI[i].stack(snps_filter, "SNPs");
            }
            if (chartI[i].chartName === 'varbytype'){
                var homs_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.ref_hom;
                    }
                });
                var nhoms_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.nref_hom;
                    }
                });
                var hets_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.hets;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(homs_filter, "Homozygous Ref");
                chartI[i].stack(nhoms_filter, "Homozygous Alt");
                chartI[i].stack(hets_filter, "Heterozygous");
            }
            if (chartI[i].chartName === 'anvalign'){
                var anvAligned_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.aligned;
                    }
                });
                var anvUnaligned_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.total - d.aligned;
                    }
                });
                var anvUnique_filter =  anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.unique;
                    }
                });
                var anvAmbig_filter = anvSamples.group().reduceSum(function(d){
                    if (r[d.sample] === 1){
                        return d.aligned - d.unique;
                    }
                });
                var len = rows.length;
                w = len * 30 + left_m + 60;
                chartI[i].width(w);
                chartI[i].x(d3.scale.ordinal().domain(s));
                chartI[i].group(anvUnique_filter, "Unique");
                chartI[i].stack(anvAmbig_filter, "Ambiguous");
                chartI[i].stack(anvUnaligned_filter, "Unmapped");
            }
        }
        dc.renderAll();
    });
});

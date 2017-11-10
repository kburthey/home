#!/usr/bin/env python

import os, sys
import re
import argparse
import json
import datetime
import textwrap
#import simplejson as json
from tools import fstools, stats_parser
from jinja2 import Environment, FileSystemLoader
from shutil import copyfile

parser = argparse.ArgumentParser(description="""
Reports Wrapper for Syngenta NGS Projects
""", formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--description', metavar = '<"Some Title">',
help="""Study Description\n\n""")

parser.add_argument('--study_id', metavar = '<NGS-000XXX>',
help="""ID of the study. Ex: NGS-000332\n\n""")

parser.add_argument('--analyst', metavar = '<"Analyst McGee">',
help="""Analyst who completed analysis\n\n""")

parser.add_argument('--sample_table', metavar = '<samples_metadata.tab>',
help="""Sample Table.\nTable must begin with # as the first character of row 1.\nColumns can contain any number and type of identifier.\n\n""")

parser.add_argument('--alpheus_table', metavar = '<alpheus_alignments.tab>',
help="""Alignments Table.\nTable must begin with # as the first character of row 1.\nFor now, total, reads_aligned, and uniquely_aligned,\ncolumns are detected.\n\n""")

parser.add_argument('--vcfstats', metavar = '<my_file.vcfstats>',
help="""Alignments Table.\nTable must begin with # as the first character of row 1.\nFor now, total, reads_aligned, and uniquely_aligned,\ncolumns are detected.\n\n""")

parser.add_argument('--metrics', metavar = '<metrics_metadata.json>',
help="""Metrics Metadata file in json format\n\n""")

parser.add_argument('--additional_figures', metavar = '<imageobj>',
help="""image objects, see example image.json\n\n""")

parser.add_argument('--summary', metavar = '<summary.txt>',
help="""Text file containing summary text\n\n""")

parser.add_argument('--references', metavar = '<references.txt>',
help="""Text file containing references\n\n""")

parser.add_argument('--custom_methods', metavar = '<methods.txt>',
help="""Text file containing custom methods text\n\n""")

parser.add_argument('--standard_methods', metavar = '<INT>',
help="""Standard Methods: transcriptome (1), Variants (2)\n\n""")

parser.add_argument('--conclusion', metavar = '<conclusion.txt>', 
help="""Text file containing conclusion text\n\n""")

parser.add_argument('--checklist', action='store_true',
help="""Whether or not to include analysis checklist\n\n""")

parser._optionals.title = "Program Options"

args = parser.parse_args()


if __name__ == '__main__':
    metrics = ''
    metadata = ''
    alignments = ''
    vcf_stats = ''
    all_results = []
    if args.sample_table:
        metadata = args.sample_table
        if not fstools.check_file(metadata):
            print 'could not find {}'.format(metadata)
            sys.exit(1)
    if args.alpheus_table:
        alignments = args.alpheus_table
        if not fstools.check_file(alignments):
            print 'could not find {}'.format(alignments)
            sys.exit(1)
    if args.vcfstats:
        vcf_stats = args.vcfstats
        if not fstools.check_file(vcf_stats):
            print 'could not find {}'.format(vcf_stats)
            sys.exit(1)
    if metadata or alignments or vcf_stats:
        if not (metadata and alignments and vcf_stats):
            print 'sample_table and alpheus_table and vcfstats required for anv'
            sys.exit(1)
    sys.stderr.write('imported\n')
    desc = args.description
    analyst = args.analyst
    study_id = args.study_id
    references = []
    if args.references:
        fstools.check_file(args.references)
        references = fstools.load_text_file(args.references, True)
    for i,v in enumerate(references):
        if not v:
            del references[i]
    summary = ''
    conclusion = ''
    if args.summary:
        if fstools.check_file(args.summary):
            summary = fstools.load_text_file(args.summary)
    if args.conclusion:
        if fstools.check_file(args.conclusion):
            conclusion = fstools.load_text_file(args.conclusion)
    add_figs = []
    if args.additional_figures:
        fstools.check_file(args.additional_figures)
        add_figs = json.loads(open(args.additional_figures).read())
        count = 3
        for a in add_figs:
            a['figure_number'] = count
            count += 1
    methods = ''
    if args.custom_methods:
        fstools.check_file(args.custom_methods)
        methods = fstools.load_text_file(args.custom_methods)
    else:
        methods = ''
    report_data = stats_parser.reportData()
    if metadata:
        report_data.sample_metadata(metadata)
        report_data.alpheus(alignments)
        report_data.vcfstats(vcf_stats)
#    print report_data.sample_data
#    print report_data.aln_data
#    print report_data.vcf_data['header']
#    print report_data.vcf_data['sample_vcfstats']
        samples = len(report_data.sample_data['data'])
        if not (samples == len(report_data.aln_data['data']) and \
                samples == len(report_data.vcf_data['sample_vcfstats'])):
            print 'samples detected in metadata do not equal alignments or stats'
            sys.exit(1)
#    print len(report_data.sample_data['data']), len(report_data.aln_data['data']), len(report_data.vcf_data['sample_vcfstats'])
        sorted_samples = sorted(
                         report_data.sample_data['data'],
                         key=lambda s: s['sample']
                     )
        sorted_vcf = sorted(
                     report_data.vcf_data['sample_vcfstats'], 
                     key=lambda s: s['sample']
                 )
        sorted_aln = sorted(report_data.aln_data['data'], key=lambda s: s['sample'])
        all_data = []
        for i, v in enumerate(sorted_samples):
            z = v.copy()
            z.update(sorted_aln[i])
            z.update(sorted_vcf[i])
            all_data.append(z)
#   print all_data
#    print len(all_data)
        
        header = report_data.sample_data['header']
        header += report_data.aln_data['header']
        header += report_data.vcf_data['header']
        table_data = []
        for d in all_data:
            datum = []
            count = 0
            datum.append(d['sample'])
            for h in header:
                if not count:
                    count += 1
                    continue
                if h == 'Total Reads':
                    break
                datum.append(d[h])
            datum += [d['total'], d['aligned'], d['unique'], d['snps'], d['indels'], d['ref_hom'], d['nref_hom'], d['hets']]
            table_data.append(datum)
        header = [{'title' : h} for h in header]
#    print header
        json_header = json.dumps(header)
        json_data = json.dumps(all_data)
        json_table_data = json.dumps(table_data)
        if json_table_data and json_data and json_header:
            datum = {'type' : 'anv', 'json_data' : json_data,
                    'json_header' : json_header,
                    'json_table_data' : json_table_data,
                    'data' : all_data, 'header' : header}
            all_results.append(datum)
    metrics = args.metrics
    if metrics:
        if not fstools.check_file(metrics):
            print 'could not find {}'.format(metrics)
            sys.exit(1)
        metrics_data = report_data.fasta_metrics(metrics)
        metrics_header = metrics_data[0]['header']
        metrics_table_data = []
        simplified_data = []
        for v in metrics_data:
            datum = []
            s = v['basic_stats']
            for h in metrics_header:
                if h == 'Total BUSCOs':
                    break
                datum.append(s[h])
            datum += [s['total'], s['busco_complete'], s['busco_single'],
                      s['busco_dup'], s['busco_fragmented'], s['busco_missing'],
                      s['scaffolds'], s['scaffold_length'], s['scaffold_N50'],
                      s['scaffold_N90'], s['max_scaffold'], s['min_scaffold'],
                      s['contigs'], s['contig_length'], s['contig_N50'],
                      s['contig_N90'], s['max_contig'], s['min_contig'],
                      s['gaps'], s['gap_length'], s['gap_N50'], s['max_gap'],
                      s['min_gap']]
            simplified_data.append(s)
            metrics_table_data.append(datum)
        js_metrics_header = [{'title' : h.replace('assembly_name', 'Assembly Name')} for h in metrics_header]
        #print metrics_table_data, metrics_header, simplified_data
        #sys.exit(1)
        if metrics_table_data and js_metrics_header and simplified_data:
            datum = {'type' : 'metrics', 'json_data' : json.dumps(simplified_data),
                     'json_header' : json.dumps(js_metrics_header),
                     'json_table_data' : json.dumps(metrics_table_data),
                     'data' : metrics_data, 'header' : js_metrics_header}
            all_results.append(datum)
    env = Environment(loader=FileSystemLoader('/thirdparty/ncgr/interactive_reporting/SIRE/SIRE_jinja2'), lstrip_blocks=True, trim_blocks=True)
    template = env.get_template('templates/js.jinja')
    toc = []
    if summary:
        toc.append({'label' : 'Summary'})
    if references:
        toc.append({'label' : 'References'})
    if methods:
        toc.append({'label' : 'Methods'})
    if all_results:
        toc.append({'label' : 'Results'})
    if conclusion:
        toc.append({'label' : 'Conclusion'})
    data={
      'analyst' : analyst,
      'study_id' : study_id,
      'checklist' : False,
      'description' : desc,
      'summary' : {'text' : summary,
                   'data_objects' : []},
      'methods' : {'text' : methods,
                   'data_objects' : []},
      'conclusion' : {'text' : conclusion,
                   'data_objects' : []},
      'references' : references,
      'toc' : toc,
      'results' : all_results,
      'additional_figures' : add_figs
    }
    if args.checklist:
        data['checklist'] = True
    #print data
    #print json_header
    #print data['results'][0]['data'][0]
    print template.render(data=data)

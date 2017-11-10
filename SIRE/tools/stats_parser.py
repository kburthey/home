#!/usr/bin/env python

import os, sys
import string
import argparse
import re
import json
from glob import glob
from tools import fstools
from math import log

class reportData:
    def __init__(self):
#        self.sample_data = {'header' : ['Clarity ID',
#                                        'Common Name',
#                                        'Phenotype'], 
        self.sample_data = {'header' : [],
                            'data' : []}
        self.vcf_data = {'header' : ['SNPs',
                                     'InDels',
                                     'Homozygous Ref',
                                     'Homozygous Alt',
                                     'Heterozygous'
                                    ],
                         'af_vcfstats' : [], 
                         'sample_vcfstats' : []}
        self.aln_data = {'header' : ['Total Reads',
                                     'Reads Aligned',
                                     'Unique Alignments',
                                    ], 
                        'data' : []}
        self.metrics_data = {'header' : [],
                             'data' : []}
        self.samples_seen = {}

    class FilterObjects:
        af = re.compile('^AF')
        sm = re.compile('^PSC')

    def sample_metadata(self, file):
        self.samples_seen = {}
        with open(file) as mopen:
            for line in mopen:
                line = line.rstrip()
#                if line.isspace() or line.startswith('#'):
#                    continue
                if line.startswith('#'):
                    self.sample_data['header'] = line.replace('#', '').split('\t')
                    continue
                datum = {}
                fields = line.split('\t')
                sample = fields[0]
                if sample in self.samples_seen:
                    continue
                self.samples_seen[sample] = 1
                count = 0
                datum['sample'] = fields[0]
                for f in fields:
                    if not count:
                        count += 1
                        continue
                    datum[self.sample_data['header'][count]] = f
                    count += 1
#                cname = fields[1]
#                geno = fields[2]
#                pheno = fields[3]
#                datum = {'sample' : sample, 'cname' : cname,
#                         'phenotype' : pheno}
                self.sample_data['data'].append(datum)

    def vcfstats(self, file):
        filters = self.FilterObjects
        with open(file) as vopen:
            for line in vopen:
                line = line.rstrip()
                if line.isspace():
                    continue
                if filters.af.match(line):
                    fields = line.split('\t')
                    af = float(fields[2])
                    sites = '{0:.6f}'.format(log(int(fields[3]), 10))
                    ts = float(fields[4])
                    tv = float(fields[5])
                    indels = int(fields[6])
                    ts_tv = '{0:.6f}'.format(ts/tv)
                    datum = {'af' : af, 'sites' : float(sites),
                             'ts_tv' : float(ts_tv), 'indels' : indels}
                    self.vcf_data['af_vcfstats'].append(datum)
                elif filters.sm.match(line):
                    fields = line.split('\t')
                    sample = fields[2]
                    if sample not in self.samples_seen:
                        print "Error cannot find sample: {} in samples metadata".format(sample)
                        sys.exit(1)
                    ref_hom = int(fields[3])
                    non_ref_hom = int(fields[4])
                    hets = int(fields[5])
                    ts = float(fields[6])
                    tv = float(fields[7])
                    indels = int(fields[8])
                    depth = float(fields[9])
                    single = int(fields[10])
                    snps = non_ref_hom + hets - indels
                    ts_tv = '{0:.6f}'.format(ts/tv)
#                    datum = {'sample' : sample, 'ref_hom' : ref_hom,
#                             'nref_hom' : non_ref_hom, 'hets' : hets,
#                             'ts_tv' : ts_tv, 'single' : single,
#                             'indels' : indels, 'snps' : snps,
#                             'depth' : depth}
                    datum = {'sample' : sample, 'ref_hom' : ref_hom,
                             'nref_hom' : non_ref_hom, 'hets' : hets,
                             'indels' : indels, 'snps' : snps}
                    self.vcf_data['sample_vcfstats'].append(datum)

    def alpheus(self, file):
        with open(file) as aopen:
            for line in aopen:
                line = line.rstrip()
                if line.isspace() or line.startswith('sample') or line.startswith('#'):
                    continue
                fields = line.split('\t')
                sample = fields[0]
                if sample not in self.samples_seen:
                    print "Error cannot find sample: {} in samples metadata".format(sample)
                    sys.exit(1)
                total = fields[1]
                aln = fields[3]
                unq = fields[5]
                ambig = fields[11]
                datum = {'aligned' : aln, 'unique' : unq, 
                         'total' : total, 'ambiguous' : ambig,
                         'sample' : sample}
                self.aln_data['data'].append(datum)

    def fasta_metrics(self, file):

        def parse_config(config):
            config_object = config
            assert 'metrics_targets' in config_object
            hold = []
            for m in config_object['metrics_targets']:
                assert 'assembly_name' in m
                assert 'directory' in m
                hold.append({'assembly_name' : m['assembly_name']})
            #name = m['name']
                for i in m:
                    if i == 'directory':
                        continue
                    if i == 'assembly_name':
                        continue
                    hold.append({i : m[i]})
                directory = m['directory']
                yield directory, hold

        def scrape_directories(directory, metadata):
            header = re.compile('^#')
            data = {'basic_stats' : {'scaffolds' : 0,
                             'scaffold_N50' : 0, 'scaffold_N90' : 0,
                             'contig_N50' : 0, 'gap_N50' : 0, 'contig_N90' : 0,
                             'contigs' : 0, 'gaps' : 0, 'max_scaffold' : 0,
                             'min_scaffold' : 0, 'max_contig' : 0,
                             'min_contig' : 0, 'max_gap' : 0, 'min_gap' : 0,
                             'gap_length' : 0, 'scaffold_length' : 0,
                             'contig_length' : 0, 'assembly_gc' : 0.0,
                             'busco_complete' : 0.0, 'busco_fragmented' : 0.0,
                             'busco_missing' : 0.0, 'busco_single' : 0.0,
                             'busco_dup' : 0.0, 'total' : 0
                            },
                    'header' : []
                   }
            fstools.check_directory(directory)
            for d in metadata:
                for v in d:
                    data['basic_stats'][str(v)] = str(d[v])
                    data['header'].append(str(v))
            data['header'] += ['Total BUSCOs', 'BUSCO Complete', 'BUSCO Complete Single', 'BUSCO Complete Duplicate', 'BUSCO Fragmented', 'Busco Missing', 'Scaffolds', 'Bases in Scaffolds', 'Scaffold N50', 'Scaffold N90', 'Max Scaffold', 'Min Scaffold', 'Contigs', 'Bases in Contigs', 'Contig N50', 'Contig N90', 'Max Contig', 'Min Contig', 'Gaps', 'Bases in Gaps', 'Gap N50', 'Max Gap', 'Min Gap']
                
            #data['header'] += ['Scaffolds', 'Bases in Scaffolds', 'Scaffold N50', 'Scaffold N90', 'Max Scaffold', 'Min Scaffold', 'Contigs', 'Bases in Contigs', 'Contig N50', 'Contig N90', 'Max Contig', 'Min Contig', 'Gaps', 'Bases in Gaps', 'Gap N50', 'Max Gap', 'Min Gap']
            for parent, sub, files in os.walk(directory):
                metric = parent.split('/')[-1]
                if metric == 'basic_stats_out':
                    file = glob(parent + '/basic_stats.basic_assembly_stats.table.txt')[0]
                    if not fstools.check_file(file):
                        print 'could not find {}'.format(file)
                        sys.exit(1)
                    with open(file) as fopen:
                        for line in fopen:
                            if header.match(line):
                                continue
                            line = line.rstrip()
                            fields = line.split(' | ')
                            stat = fields[0]
                            value = fields[1].replace(',', '')
                            if stat == 'Assembler':
                                continue
                            elif stat == 'Contigs':
                                data['basic_stats']['contigs'] = int(value)
                            elif stat == 'Max Contig':
                                data['basic_stats']['max_contig'] = int(value)
                            elif stat == 'Min Contig':
                                data['basic_stats']['min_contig'] = int(value)
                            elif stat == 'Contig N50':
                                data['basic_stats']['contig_N50'] = int(value)
                            elif stat == 'Contig N90':
                                data['basic_stats']['contig_N90'] = int(value)
                            elif stat == 'Total Contig Length':
                                data['basic_stats']['contig_length'] = int(value)
                            elif stat == 'Assembly GC':
                                data['basic_stats']['assembly_gc'] = float(
                                                              '{0:.2f}'.format(
                                                                float(value)
                                                               )
                                                             )
                            elif stat == 'Scaffolds':
                                data['basic_stats']['scaffolds'] = int(value)
                            elif stat == 'Max Scaffold':
                                data['basic_stats']['max_scaffold'] = int(value)
                            elif stat == 'Min Scaffold':
                                data['basic_stats']['min_scaffold'] = int(value)
                            elif stat == 'Scaffold N50':
                                data['basic_stats']['scaffold_N50'] = int(value)
                            elif stat == 'Scaffold N90':
                                data['basic_stats']['scaffold_N90'] = int(value)
                            elif stat == 'Total Scaffold Length':
                                data['basic_stats']['scaffold_length'] = int(value)
                            elif stat == 'Captured Gaps':
                                data['basic_stats']['gaps'] = int(value)
                            elif stat == 'Max Gap':
                                data['basic_stats']['max_gap'] = int(value)
                            elif stat == 'Min Gap':
                                data['basic_stats']['min_gap'] = int(value)
                            elif stat == 'Gap N50':
                                data['basic_stats']['gap_N50'] = int(value)
                            elif stat == 'Total Gap Length':
                                data['basic_stats']['gap_length'] = int(value)
                elif metric.startswith('run_busco'):
                    file = glob(parent + '/short_summary_busco_*_out.txt')[0]
                    with open(file) as fopen:
                        for line in fopen:
                            line = line.rstrip()
                            if line.startswith('#') or not line:
                                continue
                            if line.startswith('\tC:'):
                                line = line.replace('\t', '')
                                busco_parse = re.compile('C:(.+)\%\[S:(.+)\%,D:(.+)\%\],F:(.+)\%,M:(.+)\%,n:(\d+)')
                                percentages = busco_parse.search(line)
                                total = int(percentages.group(6))
                                complete = float(percentages.group(1))
                                frag = float(percentages.group(4))
                                single = float(percentages.group(2))
                                duplicate = float(percentages.group(3))
                                missing = float(percentages.group(5))
                                data['basic_stats']['total'] = total
                                data['basic_stats']['busco_complete'] = complete
                                data['basic_stats']['busco_fragmented'] = frag
                                data['basic_stats']['busco_missing'] = missing
                                data['basic_stats']['busco_single'] = single
                                data['basic_stats']['busco_dup'] = duplicate
            return data

        if not fstools.check_file(file):
            print 'could not find {}'.format(file)
            sys.exit(1)
        self.samples_seen = {}
        with open(file) as fopen:
            for line in fopen:
                line = line.rstrip()
                if line.startswith('#'):
                    self.metrics_data['header'] = line.replace('#', '').split('\t')
                    continue
                datum = {}
                fields = line.split('\t')
                sample = fields[0]
                if sample in self.samples_seen:
                    continue
                self.samples_seen[sample] = 1
                datum['assembly_name'] = fields[0]
                datum['directory'] = fields[1]
                if not fstools.check_directory(datum['directory']):
                    print 'could not find directory {}'.format(
                                                          datum['directory'])
                    sys.exit(1)
                count = 0
                for f in fields:
                    if count < 2:
                        count += 1
                        continue
                    datum[self.metrics_data['header'][count]] = f
                    count += 1
#                datum = {'sample' : sample, 'cname' : cname,
#                         'phenotype' : pheno}
                self.metrics_data['data'].append(datum)
        config = {'metrics_targets' : self.metrics_data['data']}
        json_data = {'basic_stats' : []}
        for directory, metadata in parse_config(config):
            all_data = scrape_directories(directory, metadata)
            json_data['basic_stats'].append(all_data)
        return json_data['basic_stats']



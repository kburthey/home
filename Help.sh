cp -R /scratch/4-quarterly/ANA-24/DONE /project/out_to_NCGR/ANA-24_DONE

cp -R /repository/ngs/run_archive/DON1348/150317_SN1123_0384_AC6CE3ACXX /repository/automated_transfer/out_to_USRE/DON1348
cp -R /repository/ngs/run_archive/DON1348/150317_SN1123_0384_AC6CE3ACXX/DON1348A1_CGTATGCA_L001_R2_001.fastq.gz /repository/automated_transfer/out_to_USRE/DON1348

cp -R /project/in_from_USET/DON1348/150317_SN1123_0384_AC6CE3ACXX

cp -R /project/in_from_USET/DON1348/150317_SN1123_0384_AC6CE3ACXX /project/out_to_NCGR/DON1348

cp -R /data/ngs/NES1801 /project/out_to_USET/NES1801

cp /scratch-large/4-quarterly/STI885_tophat/work/data

cp /scratch-large/4-quarterly/STI885_tophat/work/data/index17_GTAGAG_L001-L002_R1_001.fastq.gz /data/ngs/STI885/Index17_OtA8807_Davide.Sosso_600-804e-rep2_Corn_RNAseq-40M_05082015/index17_GTAGAG_L001-L002_R1_001.fastq.gz

cp -R /data/ngs/NGS-000245 /project/out_to_NCGR/WEB1957

ls -1| wc -l #(counts files in current directory)

find /project/DID714/ -type f -printf "%p\n">DID714.txt

find /home/u781084/NGS_work/KEL2052 -type f -printf "%p\n">KEL2052.txt

find /data/ngs/PI0009493/SD02457899/DAN877-Data -type f -printf "%p\n">DAN877.txt

cp -R /project/KRA2105/work/data/pasteuria_penetrans_illumina_reads/Pp-GSP-2/100806_SNPSTER5_0661_61RTUAAXX_PE /data/ngs/KRA2105/100806_SNPSTER5_0661_61RTUAAXX_PE

cp -R /data/ngs/DIE852/cornell /project/out_to_NCGR/DIE2204

cp /repository/automated_transfer/in_from_NCGR/s_6_2_sequence.txt.gz /userhome/u591556/misc/for_elhan

nohup cp -R /location/location /some/directory &      #(PID will pop up, will run in the background)

rm *gz #(removes all files with gz extension)

python ngs_verify.py -i LIU2108_HDtoUSRE_111115.csv --no_log  #FYI you can use –-no_log if you just want to try or run it with out writing to the log files.

find /repository/ngs/run_archive/KRA753/141230_700177R_0461_AC5YMNACXX -type f -printf "%p\n">KRA753.txt

find /data/ngs/DAC706/151112_M00831_0055_000000000-AJY0K -type f -printf "%p\n">DAC706.txt

cp -R /data/ngs/DAC706/151112_M00831_0055_000000000-AJY0K project/out_to_NCGR/DAC706

find /repository/automated_transfer/in_from_NCGR/ELM2206 -type f -printf "%p\n">ELM2206.txt 

cp -R /repository/automated_transfer/in_from_NCGR/LOK1805 /repository/ngs/analysis_results/LOK1805/2016

mv ./*../    - #this will move the files from the current directory into the previous directory

find /data/ngs/SCA1610 -type f -printf "%p\n">SCA1610.txt

find /repository/automated_transfer/in_from_NCGR/NGS-000226 -type f -printf "%p\n">NGS226.txt

cp -R /repository/automated_transfer/in_from_NCGR/WEB1957/2016_02_09 /repository/ngs/analysis_results/WEB1957/2016_02_09

find /repository/automated_transfer/in_from_NCGR/DAC706 -type f -printf "%p\n">DAC706.txt

cp -R /home/u483357/crops/Maize/NUC2303/ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/SRA049/SRA049773 /data/ngs/NUC2303

find /home/u483357/crops/Maize/NUC2303/ftp.ddbj.nig.ac.jp/ddbj_database/dra/fastq/SRA049/SRA049773 -type f -printf "%p\n">NUC2303.txt

cp -R /data/ngs/BRI2051/160308_SN1123_0499_BHL22MBCXX /project/out_to_NCGR/BRI2051

cp -R /project/in_from_NCGR/USRE/DIE2201 /project/DIE2201

cp -R /data/ngs/DAN878/DAN878_quiver_consensus.fasta.gz /project/DAN878

find /data/ngs/DIE1755 -type f -printf "%p\n">DIE1755_Filelist.txt

find /ngs_archive/2013-01-NGS/NGS-000251 -type f -printf "%p\n">NGS251_filelist.txt

find /ngs_archive/2013-02-NGS/NGS-000220 -type f -printf "%p\n">NGS220_filelist.txt

find /data/ngs/BRI2101/ -type f -printf "%p\n">BRI2101_filelist.txt

find /data/ngs/BRI2051/ -type f -printf "%p\n">BRI2051_filelist.txt

find /repository/ngs/analysis_results/ELM2206 -type f -printf "%p\n">ELM2206.txt

cp -R /project/BON2256/S_ARCANUM/BON2256_S_ARCANUM.CONTIGS.10_20_2uniq.vcf /project/out_to_USET/BON2256

cp -R /project/BON2256/S_ARCANUM/BON2256_S_ARCANUM.ORGANELLES.10_20_2uniq.vcf /project/out_to_USET/BON2256

bgzip cucumber_raw_vcf_file.vcf  #zips

bgzip –d cucumber_raw_vcf_file.vcf.gz #unzips

cp -R /repository/automated_transfer/in_from_USRE/BON2256 /repository/ngs/analysis_results/BON2256

mv dir/dir/* . #moves files from second dir into first (i dont think this works)

mv * ../ #moves files current dir into parent dir

find /data/ngs/DAN2452/ -type f -printf "%p\n">DAN2452_filelist.txt

find /data/ngs/LIU2559/ -type f -printf "%p\n">LIU2559.txt

~moughto1/bin/ngs_verify.py -i ELM2206_USETtoUSRE_091916.csv -c "Result files from NCGR"

find /data/ngs// -type f -printf "%p\n">LIU2559.txt

python C:/Users/t862537/Python/Python36-32/excelreportV3.py C:/Users/t862537/Python/Python36-32/named_resource_breakdown4.py

cp -R /scratch-large/5-biannual/LIU2558_TR /project/LIU2558/

cp /scratch-large/5-biannual/DIE2703/161216_phase_genomics/PI446958_A2/G_Tomentella_446958_A2_PGA_assembly_V2/PBJelly_out/ G_TOMENTELLA_446958_A2_version2.PBJELLY2.fasta
cp /scratch-large/5-biannual/DIE2703/161216_phase_genomics/PI509501_A3/A3_RoundI_PGA_Assembly/PGA_assembly_PI509501_A3.fasta
cp -R /scratch-large/5-biannual/DIE2703/161216_phase_genomics/PI446958_A2/G_Tomentella_446958_A2_PGA_assembly_V2/BLASTN/ 
cp -R /scratch-large/5-biannual/DIE2703/161216_phase_genomics/PI509501_A3/ 
#!/usr/bin/env python
from __future__ import print_function
import sys
import tldextract
import json

# how to use: python CP3_eval_script.py ground_truth_sample_CP3.json submission_sample_CP3.json output_sample_CP3.txt
output_file = open(sys.argv[3], "w")


def get_domain(url):
    return tldextract.extract(url).registered_domain.lower()


################################################
# ground truth data
gt_outputs = open(sys.argv[1], "r")
gt_sites = [line.rstrip('\n') for line in gt_outputs]
gt_domains = set([get_domain(url) for url in gt_sites])
gt_urls = set([url.split("://")[-1] for url in gt_sites])
################################################

################################################
# submission data
sub_outputs = open(sys.argv[2], "r")
sub_docs = [json.loads(line) for line in sub_outputs]
sub_sites =[doc['url'] for doc in sub_docs]
sub_domains = set([get_domain(url) for url in sub_sites])
sub_urls = set([url.split("://")[-1] for url in sub_sites])
################################################


################################################
# Domain level recall
domains = gt_domains & sub_domains
print("Host Names", file=output_file)
print("Ground truth Host Names:\t", len(gt_domains), file=output_file)
print("HostName Overlap:\t", len(domains), file=output_file)
print("Recall:\t", (len(domains) * 100)/float(len(gt_domains)), file=output_file)
################################################ 

################################################
# URL level recall
results = gt_urls & sub_urls
print("\nURLs", file=output_file)
print("Ground truth Sample Size:\t", len(gt_urls), file=output_file)
print("Overlap:\t", len(results), file=output_file)
print("Recall:\t", (len(results) * 100)/float(len(gt_urls)), file=output_file)
################################################ 

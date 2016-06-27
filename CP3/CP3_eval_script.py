#!/usr/bin/env python
import sys
import tldextract
import json

# how to use: python CP3_eval_script.py ground_truth_sample_CP3.json submission_sample_CP3.json

################################################
# ground truth data
gt_outputs = open(sys.argv[1], "r")
gt_sites = [line.rstrip('\n') for line in gt_outputs]
gt_domains = set([tldextract.extract(url).registered_domain for url in gt_sites])
gt_urls = set([url.split("://")[-1] for url in gt_sites])
################################################

################################################
# submission data
sub_outputs = open(sys.argv[2], "r")
sub_docs = [json.loads(line) for line in sub_outputs]
sub_sites =[doc['url'] for doc in sub_docs]
sub_domains = set([tldextract.extract(url).registered_domain for url in sub_sites])
sub_urls = set([url.split("://")[-1] for url in sub_sites])
################################################

################################################
# Domain level recall
domains = gt_domains & sub_domains
print "\nHost Names"
print "Ground truth Host Names:\t", len(gt_domains)
print "HostName Overlap:\t", len(domains)
print "Recall:\t", (len(domains) * 100)/float(len(gt_domains))
################################################ 

################################################
# URL level recall
results = gt_urls & sub_urls
print "\nURLs"
print "Ground truth Sample Size:\t", len(gt_urls)
print "Overlap:\t", len(results)
print "Recall:\t", (len(results) * 100)/float(len(gt_urls))
################################################ 
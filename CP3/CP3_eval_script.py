#!/usr/bin/env python
from __future__ import print_function
import re
import sys

import tldextract
from six.moves.urllib.parse import urlparse
try:
    from tqdm import tqdm
except ImportError:
    tqdm = lambda it, *args: it
# it requires w3lib >= 1.15.0
from w3lib.url import canonicalize_url


# how to use: python CP3_eval_script.py ground_truth_sample_CP3.json submission_sample_CP3.json output_sample_CP3.txt
output_file = open(sys.argv[3], "w")


# XXX: copied from Scrapy
def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url


def get_domain(url):
    return tldextract.extract(url).registered_domain.lower()


def normalize_url(url):
    url = add_http_if_no_scheme(url)
    return canonicalize_url(url).replace('https://', 'http://', 1)


################################################
# ground truth data
gt_outputs = open(sys.argv[1], "r")
gt_sites = [line.rstrip('\n') for line in gt_outputs]
gt_domains = {get_domain(url) for url in gt_sites}
gt_urls = {normalize_url(url) for url in gt_sites}
################################################

################################################
# submission data
sub_outputs = open(sys.argv[2], "r")
sub_sites = [line.rstrip('\n') for line in tqdm(sub_outputs, "reading submission")]
sub_domains = {get_domain(url) for url in tqdm(sub_sites, "extracting domains")}
sub_urls = {normalize_url(url) for url in tqdm(sub_sites, "normalizing urls")}
################################################


################################################
# Domain level recall
domains = gt_domains & sub_domains
print("Host Names", file=output_file)
print("Ground truth Host Names:\t", len(gt_domains), file=output_file)
print("Submission Host Names:\t", len(sub_domains), file=output_file)
print("HostName Overlap:\t", len(domains), file=output_file)
print("Recall:\t", (len(domains) * 100)/float(len(gt_domains)), file=output_file)
print("Harvest Rate:\t", (len(domains) * 100)/float(len(sub_domains)), file=output_file)
################################################ 

################################################
# URL level recall
results = gt_urls & sub_urls
print("\nURLs", file=output_file)
print("Ground truth Sample Size:\t", len(gt_urls), file=output_file)
print("Submission URLs Set Size:\t", len(sub_urls), file=output_file)
print("Overlap:\t", len(results), file=output_file)
print("Recall:\t", (len(results) * 100)/float(len(gt_urls)), file=output_file)
print("Harvest Rate:\t", (len(results) * 100)/float(len(sub_urls)), file=output_file)
################################################ 

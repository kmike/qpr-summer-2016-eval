#!/usr/bin/env python

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import sys
import json

# how to use: python CP2_eval_script.py ground_truth_sample_CP2.json submission_sample_CP2.json output_sample_CP2.pdf

################################################
# ground truth data
gt_id = []
gt_scores = []
gt_outputs = open(sys.argv[1], "r")
# set of difficulty levels to evaluate
if len(sys.argv) > 4:
    difficulties = sys.argv[4:]
    print 'Scoring difficulty levels:'
    print difficulties
else:
    print 'No difficulty arguments given.'
    print 'Scoring will be done on all difficulty levels (i.e., "easy", "medium", and "hard")'
difficulties = ['easy', 'medium', 'hard']
for line in gt_outputs:
    entry = json.loads(line)
    if entry['type'] in difficulties:
        gt_id.append(entry['id'])
        gt_scores.append(entry['class'])
gt_outputs.close()
################################################

################################################
# submission data
sub_id = []
sub_scores = []
sub_outputs = open(sys.argv[2], "r")
for line in sub_outputs:
    entry = json.loads(line)
    if entry['id'] in gt_id:
        sub_id.append(entry['id'])
        sub_scores.append(entry['score'])
sub_outputs.close()
################################################

################################################
# ids should be well-ordered, but just in case...
# note that if you did not include ids but instead only phone numbers in your file, the below needs modification
if any([a != b for a, b in zip(sub_id, gt_id)]):
    print 'submission ids do not match ground truth ids, please check submission data'   
################################################ 

else:
    fpr ,tpr, thresholds = roc_curve(gt_scores, sub_scores)
    auc = roc_auc_score(gt_scores, sub_scores)
    fig = plt.figure()
    plt.plot(fpr, tpr, '.-')
    plt.xlim(-0.01, 1.01)
    plt.ylim(-0.01, 1.01)
    title = 'ROC-AUC = {0}'.format(auc)
    plt.title(title)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.savefig(sys.argv[3])
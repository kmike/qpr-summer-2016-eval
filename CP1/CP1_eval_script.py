#!/usr/bin/env python

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score
import sys
import json

# how to use: python CP1_eval_script.py ht_evaluation_UPDATED your_group-s_cool_data_file.txt
#
################################################
# do not edit - eval data
eval_id = []
eval_phones = []
eval_scores = []
eval_outputs = open(sys.argv[1], "r")
for line in eval_outputs:
    eval_id.append(json.loads(line)['cdr_id'])
    eval_phones.append(json.loads(line)["phone"])
    score = json.loads(line)['class']
    eval_scores.append(score)
eval_outputs.close()
################################################

################################################
# group data ingest - edit to fit your data as needed
group_id = []
group_phones = []
group_scores = []
group_outputs = open(sys.argv[2], "r")
for line in group_outputs:
    line = json.loads(line)
    group_phones.append(line["phone"])
    group_id.append(line["cdr_id"])
    group_scores.append(line["score"])
group_outputs.close()
################################################

################################################
# ids should be well-ordered, but just in case...
# note that if you did not include ids but instead only phone numbers in your file, the below needs modification
if any([a != b for a, b in zip(group_id, eval_id)]):
    print 'submission ids do not match ground truth ids, please check submission data'   
################################################ 

else:
    fpr ,tpr, thresholds = roc_curve(eval_scores, group_scores)
    auc = roc_auc_score(eval_scores, group_scores)
    print 'ROC-AUC is:', auc
    print 'ROC curve plotting'
    plt.plot(fpr, tpr, '.-')
    plt.xlim(-0.01, 1.01)
    plt.ylim(-0.01, 1.01)
    plt.show()
# Challenge Problem 3

In this directory, the following files are provided towards the goal of evaluating team submission data against ground truth data for Challenge Problem #3:

### CP3_eval_script.py
This is the Python script that will be used to compare team submission data against ground truth data.

### ground_truth_sample_CP3.json
This file contains the known ground truth data against which team submissions will be compared.  Each line of this file is a string indicating the full URL path to a website used in the investigation of a question.

### submission_sample_CP3.json
This file contains the data submitted by the team, which is to be compared against the known ground truth data.  Each line of this file is a JSON formatted dictionary which exactly matches the CDR source document containing information about the crawl which was used in the investigation of the question.

**NOTE:** The JSON formatted dictionary should reflect the CDR **source** document.  Therefore, it should contain **top-level** dictionary keys that include: `crawl_data`, `url`, `timestamp`, `team`, `raw_content`, etc.  These keys are expected at the top-level of the dictionary, and no other keys above this level should be present in the dictionary.

The value associated with the `url` key will be the URL path that is compared to the ground truth URL data.

### output_sample_CP1.pdf
This file provides a sample of expected output of the evaluation script when run on the sample data files provided with the example usage command shown below.

The file contains the calculated values of ground truth sample size, number of overlapping instances between the submitted data and the ground truth data, and the recall of the submitted data as measured against the ground truth data.  These calculations are provided two times; once for the assessment of full URL paths and once for the assessment of top level domain names which are extracted from the submitted URL paths in the evlaulation script.

### Example Usage
Note that the file names given in the example usage command below (i.e., `ground_truth_sample_CP3.json submission_sample_CP3.json output_sample_CP3.pdf`) are example file names and can be substituted for the appropriate file names.

To run the evaluation of submission data contained in a file named `submission_sample_CP3.json` against ground truth data contained in a file named `ground_truth_sample_CP3.json` and save the output to a new file named `output_sample_CP3.txt` use:

`python CP3_eval_script.py ground_truth_sample_CP3.json submission_sample_CP3.json output_sample_CP3.txt`

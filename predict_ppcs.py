# Copyright (c) 2023 brainlife.io
#
# This file is a template for a python-based brainlife.io App
# brainlife stages this git repo, writes `config.json` and execute this script.
# this script reads the `config.json` and execute pynets container through singularity
#
# you can run this script(main) without any parameter to test how this App will run outside brainlife
# you will need to copy config.json.brainlife-sample to config.json before running `main` as `main`
# will read all parameters from config.json
#
# Author: Giulia Bertò
# The University of Texas at Austin

import argparse
import pandas as pd
import numpy as np
import json
import pickle


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-profiles', nargs='?', const=1, default='',
	                    help='profiles')  
    args = parser.parse_args()

    # Generate a json.product to display messages on Brainlife UI
    dict_json_product = {'brainlife': []}

    with open('tract_name_list.txt') as f:
        tract_name_list = f.read().splitlines()

    n_nodes = 100
    metric = 'fa'
    n_tracts = len(tract_name_list)
    fa_profiles = np.zeros((n_tracts, n_nodes))

    df = pd.read_csv(args.profiles,index_col=0)

    print("Extracting only FA tract profiles...")
    for t in range(len(tract_name_list)):
        #select only the block related to the current tract
        row_start = t*n_nodes
        row_end = t*n_nodes + n_nodes
        current_block = df.iloc[row_start:row_end]
        current_profile = current_block[metric]
        fa_profiles[t,:] = current_profile

    print("Computing the mean FA profile...")
    mean_profile = np.mean(fa_profiles[:,10:90], axis=1)

    print("Loading precomputed weights...")
    clf_LR_optimal = pickle.load(open('clf_LR_optimal', 'rb'))

    print("Predicting PPCS...")
    y_pred = clf_LR_optimal.predict(mean_profile.reshape(1, -1))

    if y_pred == 0:
        msg = 'This injury is at low risk of developing PPCS.'
        print("---> %s" %msg)
    else:
        msg = 'This injury is at high risk of developing PPCS.'
        print("---> %s" %msg)
    
    dict_json_product['brainlife'].append({'type': 'warning', 'msg': '%s' %msg})

    # Save the dict_json_product in a json file
    with open('product.json', 'w') as outfile:
        json.dump(dict_json_product, outfile)

    




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Description: A script to produce high-resolution ocean topography maps using the BFN-QG data assimilation method (F. Le Guillou).
This algorithm takes care of downloading the input observations, pre-processing the boundary ∏, plotting the data to be used,
performing the assimilation using MASSH, processing results, making various diagnostics on the output, and sending the maps 
and results to an external FTP server. It can be used both for near-real-time and reanalysis applications.

Author: adrienstella
Date: 2023-07-19
"""

import os
from datetime import timedelta
import sys

destination = None # Available options: 'ifremer'
make_lagrangian_diags = False # True or False
draw_L3 = False # True or False
make_alongtrack_rmse = False # True or False
make_duacs_comp = 'today' # Available options: 'today', 'YYYY-MM-DD' (choose a date), 'interactive', 'none'

output_maps_interval = 6 # final averaging of ssh, in hours - default = 24

dir_massh = '../MASSH/mapping'
path_config = './NRT_BFN_main_config.py'  

sys.path.append(dir_massh)
currdir=os.getcwd()

from src import exp
config = exp.Exp(path_config)
name_experiment = config.EXP.name_experiment
today = config.EXP.final_date
numdays = int((today-config.EXP.init_date)/timedelta(days = 1))

lon_min = config.GRID.lon_min                            
lon_max = config.GRID.lon_max                               
lat_min = config.GRID.lat_min                                 
lat_max = config.GRID.lat_max
bbox = [lon_min, lon_max, lat_min, lat_max]   

from tools.ftp_transfer import download_nadirs_cmems, download_swot_nadir
from tools.processing import make_mdt

# What datasets to download
datasets = [
    'dataset-duacs-nrt-global-al-phy-l3', 
    'dataset-duacs-nrt-global-c2n-phy-l3', 
    'dataset-duacs-nrt-global-h2b-phy-l3',
    'dataset-duacs-nrt-global-s3a-phy-l3',
    'dataset-duacs-nrt-global-s3b-phy-l3',
    'cmems_obs-sl_glo_phy-ssh_nrt_j3n-l3-duacs_PT1S',
    'cmems_obs-sl_glo_phy-ssh_nrt_s6a-hr-l3-duacs_PT1S',
]

dataset_l4 = 'dataset-duacs-nrt-global-merged-allsat-phy-l4'

# FTP connection to CMEMS server and observational data download
download_nadirs_cmems(name_experiment, currdir, today, numdays, datasets, dataset_l4)
download_swot_nadir(name_experiment, currdir, today)

# If needed, download and properly formats mdt file
make_mdt(name_experiment, currdir,bbox)
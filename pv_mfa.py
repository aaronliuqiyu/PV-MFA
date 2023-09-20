# Import required packages #
# These packages needs to be installed and imported for the script to run #
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Import ODYM dynamic stock model #
# This package is used to carry out the MFA calculations #
# ODYM has other modules, but I am currently only using the dynamic stock model module, see https://github.com/IndEcol/ODYM for detailed documentation #
from dynamic_stock_model import DynamicStockModel as DSM

# Set option so that pandas does not create a copy of the dataframe #
pd.set_option('mode.chained_assignment', None)

# Create an object for easier index slicing #
idx = pd.IndexSlice

# Set working directory #
# Change the directory in the bracket to where your data files are located #
# This does not have to be the same location as the git clone #
os.chdir("C:\\Users\\qiyu\\OneDrive - Chalmers\\PV MFA") # Change this to your directory# 

# Suppress scientific notation so the output is easier to read #
pd.set_option('display.float_format', lambda x: '%.3f' % x)

# Read in input data from excel file #
file_loc = 'PV_input.xlsx'

# Installed capacity with years as index #
Capacity = pd.read_excel(file_loc, sheet_name='Capacity', usecols='A:D', index_col=0)
DR_capacity = Capacity.iloc[:,0] # DR scenario  installed capacity #
DE_capacity = Capacity.iloc[:,1] # DE scenario  installed capacity #
RE_capacity = Capacity.iloc[:,2] # RE scenario  installed capacity #

# Read in lifetime parameter from excel #
lifetime = pd.read_excel(file_loc, sheet_name='Lifetime', usecols='A:C', index_col=0)

# Read in material intensity values #
cSi_MI = pd.read_excel(file_loc, sheet_name='MI cSi', index_col=0) 
CdTe_MI = pd.read_excel(file_loc, sheet_name='MI CdTe', index_col=0) 
aSi_MI = pd.read_excel(file_loc, sheet_name='MI aSi', index_col=0) 
CIGS_MI = pd.read_excel(file_loc, sheet_name='MI CIGS', index_col=0) 

# Market share variables #
market_share = pd.read_excel(file_loc, sheet_name='Market share', usecols='A:E', index_col=0, header=None)

# Apply market share to installed capacity #
DR_cSi_capacity = np.multiply(market_share.iloc[:,0], DR_capacity)
DR_CdTe_capacity = np.multiply(market_share.iloc[:,1], DR_capacity)
DR_aSi_capacity = np.multiply(market_share.iloc[:,2], DR_capacity)
DR_CIGS_capacity = np.multiply(market_share.iloc[:,3], DR_capacity)

DE_cSi_capacity = np.multiply(market_share.iloc[:,0], DE_capacity)
DE_CdTe_capacity = np.multiply(market_share.iloc[:,1], DE_capacity)
DE_aSi_capacity = np.multiply(market_share.iloc[:,2], DE_capacity)
DE_CIGS_capacity = np.multiply(market_share.iloc[:,3], DE_capacity)

RE_cSi_capacity = np.multiply(market_share.iloc[:,0], RE_capacity)
RE_CdTe_capacity = np.multiply(market_share.iloc[:,1], RE_capacity)
RE_aSi_capacity = np.multiply(market_share.iloc[:,2], RE_capacity)
RE_CIGS_capacity = np.multiply(market_share.iloc[:,3], RE_capacity)

# stock driven #
from pv_helper import stock_driven

# DR scenario #
DR_cSi_outflow, DR_cSi_inflow = stock_driven(DR_cSi_capacity, lifetime)
DR_CdTe_outflow, DR_CdTe_inflow = stock_driven(DR_CdTe_capacity, lifetime)
DR_aSi_outflow, DR_aSi_inflow = stock_driven(DR_aSi_capacity, lifetime)
DR_CIGS_outflow, DR_CIGS_inflow = stock_driven(DR_CIGS_capacity, lifetime)

# DE scenario #
DE_cSi_outflow, DE_cSi_inflow = stock_driven(DE_cSi_capacity, lifetime)
DE_CdTe_outflow, DE_CdTe_inflow = stock_driven(DE_CdTe_capacity, lifetime)
DE_aSi_outflow, DE_aSi_inflow = stock_driven(DE_aSi_capacity, lifetime)
DE_CIGS_outflow, DE_CIGS_inflow = stock_driven(DE_CIGS_capacity, lifetime)

# RE scenario #
RE_cSi_outflow, RE_cSi_inflow = stock_driven(RE_cSi_capacity, lifetime)
RE_CdTe_outflow, RE_CdTe_inflow = stock_driven(RE_CdTe_capacity, lifetime)
RE_aSi_outflow, RE_aSi_inflow = stock_driven(RE_aSi_capacity, lifetime)
RE_CIGS_outflow, RE_CIGS_inflow = stock_driven(RE_CIGS_capacity, lifetime)

# inflow materials #
DR_cSi_inflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DR_cSi_inflow.values.flatten())
DR_cSi_inflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * DR_cSi_inflow.values.flatten())
DR_cSi_inflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DR_cSi_inflow.values.flatten())
DR_cSi_inflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * DR_cSi_inflow.values.flatten())
DR_cSi_inflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DR_cSi_inflow.values.flatten())
DR_cSi_inflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * DR_cSi_inflow.values.flatten())

DR_CdTe_inflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DR_CdTe_inflow.values.flatten())
DR_CdTe_inflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DR_CdTe_inflow.values.flatten())
DR_CdTe_inflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DR_CdTe_inflow.values.flatten())
DR_CdTe_inflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DR_CdTe_inflow.values.flatten())
DR_CdTe_inflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DR_CdTe_inflow.values.flatten())
DR_CdTe_inflow_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * DR_CdTe_inflow.values.flatten())

DR_aSi_inflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DR_aSi_inflow.values.flatten())
DR_aSi_inflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * DR_aSi_inflow.values.flatten())
DR_aSi_inflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DR_aSi_inflow.values.flatten())
DR_aSi_inflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * DR_aSi_inflow.values.flatten())
DR_aSi_inflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DR_aSi_inflow.values.flatten())
DR_aSi_inflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DR_aSi_inflow.values.flatten())

DR_CIGS_inflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DR_CIGS_inflow.values.flatten())
DR_CIGS_inflow_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * DR_CIGS_inflow.values.flatten())

DE_cSi_inflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DE_cSi_inflow.values.flatten())
DE_cSi_inflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * DE_cSi_inflow.values.flatten())
DE_cSi_inflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DE_cSi_inflow.values.flatten())
DE_cSi_inflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * DE_cSi_inflow.values.flatten())
DE_cSi_inflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DE_cSi_inflow.values.flatten())
DE_cSi_inflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * DE_cSi_inflow.values.flatten())

DE_CdTe_inflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DE_CdTe_inflow.values.flatten())
DE_CdTe_inflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DE_CdTe_inflow.values.flatten())
DE_CdTe_inflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DE_CdTe_inflow.values.flatten())
DE_CdTe_inflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DE_CdTe_inflow.values.flatten())
DE_CdTe_inflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DE_CdTe_inflow.values.flatten())
DE_CdTe_inflow_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * DE_CdTe_inflow.values.flatten())

DE_aSi_inflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DE_aSi_inflow.values.flatten())
DE_aSi_inflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * DE_aSi_inflow.values.flatten())
DE_aSi_inflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DE_aSi_inflow.values.flatten())
DE_aSi_inflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * DE_aSi_inflow.values.flatten())
DE_aSi_inflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DE_aSi_inflow.values.flatten())
DE_aSi_inflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DE_aSi_inflow.values.flatten())

DE_CIGS_inflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_inflow.values.flatten())
DE_CIGS_inflow_selenium = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_inflow.values.flatten())

RE_cSi_inflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * RE_cSi_inflow.values.flatten())
RE_cSi_inflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * RE_cSi_inflow.values.flatten())
RE_cSi_inflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * RE_cSi_inflow.values.flatten())
RE_cSi_inflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * RE_cSi_inflow.values.flatten())
RE_cSi_inflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * RE_cSi_inflow.values.flatten())
RE_cSi_inflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * RE_cSi_inflow.values.flatten())

RE_CdTe_inflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * RE_CdTe_inflow.values.flatten())
RE_CdTe_inflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * RE_CdTe_inflow.values.flatten())
RE_CdTe_inflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * RE_CdTe_inflow.values.flatten())
RE_CdTe_inflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * RE_CdTe_inflow.values.flatten())
RE_CdTe_inflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * RE_CdTe_inflow.values.flatten())
RE_CdTe_inflow_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * RE_CdTe_inflow.values.flatten())

RE_aSi_inflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * RE_aSi_inflow.values.flatten())
RE_aSi_inflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * RE_aSi_inflow.values.flatten())
RE_aSi_inflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * RE_aSi_inflow.values.flatten())
RE_aSi_inflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * RE_aSi_inflow.values.flatten())
RE_aSi_inflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * RE_aSi_inflow.values.flatten())
RE_aSi_inflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * RE_aSi_inflow.values.flatten())

RE_CIGS_inflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * RE_CIGS_inflow.values.flatten())
RE_CIGS_inflow_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * RE_CIGS_inflow.values.flatten())

# Outflows #

DR_cSi_outflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DR_cSi_outflow.values.flatten())
DR_cSi_outflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * DR_cSi_outflow.values.flatten())
DR_cSi_outflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DR_cSi_outflow.values.flatten())
DR_cSi_outflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * DR_cSi_outflow.values.flatten())
DR_cSi_outflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DR_cSi_outflow.values.flatten())
DR_cSi_outflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * DR_cSi_outflow.values.flatten())

DR_CdTe_outflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DR_CdTe_outflow.values.flatten())
DR_CdTe_outflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DR_CdTe_outflow.values.flatten())
DR_CdTe_outflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DR_CdTe_outflow.values.flatten())
DR_CdTe_outflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DR_CdTe_outflow.values.flatten())
DR_CdTe_outflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DR_CdTe_outflow.values.flatten())
DR_CdTe_outflow_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * DR_CdTe_outflow.values.flatten())

DR_aSi_outflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DR_aSi_outflow.values.flatten())
DR_aSi_outflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * DR_aSi_outflow.values.flatten())
DR_aSi_outflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DR_aSi_outflow.values.flatten())
DR_aSi_outflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * DR_aSi_outflow.values.flatten())
DR_aSi_outflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DR_aSi_outflow.values.flatten())
DR_aSi_outflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DR_aSi_outflow.values.flatten())

DR_CIGS_outflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DR_CIGS_outflow.values.flatten())
DR_CIGS_outflow_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * DR_CIGS_outflow.values.flatten())

DE_cSi_outflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DE_cSi_outflow.values.flatten())
DE_cSi_outflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * DE_cSi_outflow.values.flatten())
DE_cSi_outflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DE_cSi_outflow.values.flatten())
DE_cSi_outflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * DE_cSi_outflow.values.flatten())
DE_cSi_outflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DE_cSi_outflow.values.flatten())
DE_cSi_outflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * DE_cSi_outflow.values.flatten())

DE_CdTe_outflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DE_CdTe_outflow.values.flatten())
DE_CdTe_outflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DE_CdTe_outflow.values.flatten())
DE_CdTe_outflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DE_CdTe_outflow.values.flatten())
DE_CdTe_outflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DE_CdTe_outflow.values.flatten())
DE_CdTe_outflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DE_CdTe_outflow.values.flatten())
DE_CdTe_outflow_tellurium= pd.DataFrame(CdTe_MI.iloc[5].values * DE_CdTe_outflow.values.flatten())

DE_aSi_outflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DE_aSi_outflow.values.flatten())
DE_aSi_outflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * DE_aSi_outflow.values.flatten())
DE_aSi_outflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DE_aSi_outflow.values.flatten())
DE_aSi_outflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * DE_aSi_outflow.values.flatten())
DE_aSi_outflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DE_aSi_outflow.values.flatten())
DE_aSi_outflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DE_aSi_outflow.values.flatten())

DE_CIGS_outflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_outflow.values.flatten())
DE_CIGS_outflow_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * DE_CIGS_outflow.values.flatten())

RE_cSi_outflow_concrete = pd.DataFrame(cSi_MI.iloc[0].values * RE_cSi_outflow.values.flatten())
RE_cSi_outflow_steel = pd.DataFrame(cSi_MI.iloc[1].values * RE_cSi_outflow.values.flatten())
RE_cSi_outflow_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * RE_cSi_outflow.values.flatten())
RE_cSi_outflow_copper = pd.DataFrame(cSi_MI.iloc[3].values * RE_cSi_outflow.values.flatten())
RE_cSi_outflow_silicon = pd.DataFrame(cSi_MI.iloc[4].values * RE_cSi_outflow.values.flatten())
RE_cSi_outflow_silver = pd.DataFrame(cSi_MI.iloc[5].values * RE_cSi_outflow.values.flatten())

RE_CdTe_outflow_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * RE_CdTe_outflow.values.flatten())
RE_CdTe_outflow_steel = pd.DataFrame(CdTe_MI.iloc[1].values * RE_CdTe_outflow.values.flatten())
RE_CdTe_outflow_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * RE_CdTe_outflow.values.flatten())
RE_CdTe_outflow_copper = pd.DataFrame(CdTe_MI.iloc[3].values * RE_CdTe_outflow.values.flatten())
RE_CdTe_outflow_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * RE_CdTe_outflow.values.flatten())
RE_CdTe_outflow_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * RE_CdTe_outflow.values.flatten())

RE_aSi_outflow_concrete = pd.DataFrame(aSi_MI.iloc[0].values * RE_aSi_outflow.values.flatten())
RE_aSi_outflow_steel = pd.DataFrame(aSi_MI.iloc[1].values * RE_aSi_outflow.values.flatten())
RE_aSi_outflow_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * RE_aSi_outflow.values.flatten())
RE_aSi_outflow_copper = pd.DataFrame(aSi_MI.iloc[3].values * RE_aSi_outflow.values.flatten())
RE_aSi_outflow_silicon = pd.DataFrame(aSi_MI.iloc[4].values * RE_aSi_outflow.values.flatten())
RE_aSi_outflow_germanium = pd.DataFrame(aSi_MI.iloc[5].values * RE_aSi_outflow.values.flatten())

RE_CIGS_outflow_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_steel = pd.DataFrame(CIGS_MI.iloc[1].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_copper = pd.DataFrame(CIGS_MI.iloc[3].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_indium = pd.DataFrame(CIGS_MI.iloc[4].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * RE_CIGS_outflow.values.flatten())
RE_CIGS_outflow_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * RE_CIGS_outflow.values.flatten())

# Calculate capacity expansion #
DR_cSi_capacity_expansion = DR_cSi_capacity.diff()
DR_CdTe_capacity_expansion = DR_CdTe_capacity.diff()
DR_aSi_capacity_expansion = DR_aSi_capacity.diff()
DR_CIGS_capacity_expansion = DR_CIGS_capacity.diff()

DE_cSi_capacity_expansion = DE_cSi_capacity.diff()
DE_CdTe_capacity_expansion = DE_CdTe_capacity.diff()
DE_aSi_capacity_expansion = DE_aSi_capacity.diff()
DE_CIGS_capacity_expansion = DE_CIGS_capacity.diff()

RE_cSi_capacity_expansion = RE_cSi_capacity.diff()
RE_CdTe_capacity_expansion = RE_CdTe_capacity.diff()
RE_aSi_capacity_expansion = RE_aSi_capacity.diff()
RE_CIGS_capacity_expansion = RE_CIGS_capacity.diff()

# Material expansion #

DR_cSi_concrete_expansion = pd.DataFrame(cSi_MI.iloc[0].values * DR_cSi_capacity_expansion.values.flatten())
DR_cSi_steel_expansion = pd.DataFrame(cSi_MI.iloc[1].values * DR_cSi_capacity_expansion.values.flatten())
DR_cSi_aluminium_expansion = pd.DataFrame(cSi_MI.iloc[2].values * DR_cSi_capacity_expansion.values.flatten())
DR_cSi_copper_expansion = pd.DataFrame(cSi_MI.iloc[3].values * DR_cSi_capacity_expansion.values.flatten())
DR_cSi_silicon_expansion = pd.DataFrame(cSi_MI.iloc[4].values * DR_cSi_capacity_expansion.values.flatten())
DR_cSi_silver_expansion = pd.DataFrame(cSi_MI.iloc[5].values * DR_cSi_capacity_expansion.values.flatten())

DR_CdTe_concrete_expansion = pd.DataFrame(CdTe_MI.iloc[0].values * DR_CdTe_capacity_expansion.values.flatten())
DR_CdTe_steel_expansion = pd.DataFrame(CdTe_MI.iloc[1].values * DR_CdTe_capacity_expansion.values.flatten())
DR_CdTe_aluminium_expansion = pd.DataFrame(CdTe_MI.iloc[2].values * DR_CdTe_capacity_expansion.values.flatten())
DR_CdTe_copper_expansion = pd.DataFrame(CdTe_MI.iloc[3].values * DR_CdTe_capacity_expansion.values.flatten())
DR_CdTe_cadmium_expansion = pd.DataFrame(CdTe_MI.iloc[4].values * DR_CdTe_capacity_expansion.values.flatten())
DR_CdTe_tellurium_expansion = pd.DataFrame(CdTe_MI.iloc[5].values * DR_CdTe_capacity_expansion.values.flatten())

DR_aSi_concrete_expansion = pd.DataFrame(aSi_MI.iloc[0].values * DR_aSi_capacity_expansion.values.flatten())
DR_aSi_steel_expansion = pd.DataFrame(aSi_MI.iloc[1].values * DR_aSi_capacity_expansion.values.flatten())
DR_aSi_aluminium_expansion = pd.DataFrame(aSi_MI.iloc[2].values * DR_aSi_capacity_expansion.values.flatten())
DR_aSi_copper_expansion = pd.DataFrame(aSi_MI.iloc[3].values * DR_aSi_capacity_expansion.values.flatten())
DR_aSi_silicon_expansion = pd.DataFrame(aSi_MI.iloc[4].values * DR_aSi_capacity_expansion.values.flatten())
DR_aSi_germanium_expansion = pd.DataFrame(aSi_MI.iloc[5].values * DR_aSi_capacity_expansion.values.flatten())

DR_CIGS_concrete_expansion = pd.DataFrame(CIGS_MI.iloc[0].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_steel_expansion = pd.DataFrame(CIGS_MI.iloc[1].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_aluminium_expansion = pd.DataFrame(CIGS_MI.iloc[2].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_copper_expansion = pd.DataFrame(CIGS_MI.iloc[3].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_indium_expansion = pd.DataFrame(CIGS_MI.iloc[4].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_gallium_expansion = pd.DataFrame(CIGS_MI.iloc[5].values * DR_CIGS_capacity_expansion.values.flatten())
DR_CIGS_selenium_expansion = pd.DataFrame(CIGS_MI.iloc[6].values * DR_CIGS_capacity_expansion.values.flatten())

DE_cSi_concrete_expansion = pd.DataFrame(cSi_MI.iloc[0].values * DE_cSi_capacity_expansion.values.flatten())
DE_cSi_steel_expansion = pd.DataFrame(cSi_MI.iloc[1].values * DE_cSi_capacity_expansion.values.flatten())
DE_cSi_aluminium_expansion = pd.DataFrame(cSi_MI.iloc[2].values * DE_cSi_capacity_expansion.values.flatten())
DE_cSi_copper_expansion = pd.DataFrame(cSi_MI.iloc[3].values * DE_cSi_capacity_expansion.values.flatten())
DE_cSi_silicon_expansion = pd.DataFrame(cSi_MI.iloc[4].values * DE_cSi_capacity_expansion.values.flatten())
DE_cSi_silver_expansion = pd.DataFrame(cSi_MI.iloc[5].values * DE_cSi_capacity_expansion.values.flatten())

DE_CdTe_concrete_expansion = pd.DataFrame(CdTe_MI.iloc[0].values * DE_CdTe_capacity_expansion.values.flatten())
DE_CdTe_steel_expansion = pd.DataFrame(CdTe_MI.iloc[1].values * DE_CdTe_capacity_expansion.values.flatten())
DE_CdTe_aluminium_expansion = pd.DataFrame(CdTe_MI.iloc[2].values * DE_CdTe_capacity_expansion.values.flatten())
DE_CdTe_copper_expansion = pd.DataFrame(CdTe_MI.iloc[3].values * DE_CdTe_capacity_expansion.values.flatten())
DE_CdTe_cadmium_expansion = pd.DataFrame(CdTe_MI.iloc[4].values * DE_CdTe_capacity_expansion.values.flatten())
DE_CdTe_tellurium_expansion = pd.DataFrame(CdTe_MI.iloc[5].values * DE_CdTe_capacity_expansion.values.flatten())

DE_aSi_concrete_expansion = pd.DataFrame(aSi_MI.iloc[0].values * DE_aSi_capacity_expansion.values.flatten())
DE_aSi_steel_expansion = pd.DataFrame(aSi_MI.iloc[1].values * DE_aSi_capacity_expansion.values.flatten())
DE_aSi_aluminium_expansion = pd.DataFrame(aSi_MI.iloc[2].values * DE_aSi_capacity_expansion.values.flatten())
DE_aSi_copper_expansion = pd.DataFrame(aSi_MI.iloc[3].values * DE_aSi_capacity_expansion.values.flatten())
DE_aSi_silicon_expansion = pd.DataFrame(aSi_MI.iloc[4].values * DE_aSi_capacity_expansion.values.flatten())
DE_aSi_germanium_expansion = pd.DataFrame(aSi_MI.iloc[5].values * DE_aSi_capacity_expansion.values.flatten())

DE_CIGS_concrete_expansion = pd.DataFrame(CIGS_MI.iloc[0].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_steel_expansion = pd.DataFrame(CIGS_MI.iloc[1].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_aluminium_expansion = pd.DataFrame(CIGS_MI.iloc[2].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_copper_expansion = pd.DataFrame(CIGS_MI.iloc[3].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_indium_expansion = pd.DataFrame(CIGS_MI.iloc[4].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_gallium_expansion = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_capacity_expansion.values.flatten())
DE_CIGS_selenium_expansion = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_capacity_expansion.values.flatten())

RE_cSi_concrete_expansion = pd.DataFrame(cSi_MI.iloc[0].values * RE_cSi_capacity_expansion.values.flatten())
RE_cSi_steel_expansion = pd.DataFrame(cSi_MI.iloc[1].values * RE_cSi_capacity_expansion.values.flatten())
RE_cSi_aluminium_expansion = pd.DataFrame(cSi_MI.iloc[2].values * RE_cSi_capacity_expansion.values.flatten())
RE_cSi_copper_expansion = pd.DataFrame(cSi_MI.iloc[3].values * RE_cSi_capacity_expansion.values.flatten())
RE_cSi_silicon_expansion = pd.DataFrame(cSi_MI.iloc[4].values * RE_cSi_capacity_expansion.values.flatten())
RE_cSi_silver_expansion = pd.DataFrame(cSi_MI.iloc[5].values * RE_cSi_capacity_expansion.values.flatten())

RE_CdTe_concrete_expansion = pd.DataFrame(CdTe_MI.iloc[0].values * RE_CdTe_capacity_expansion.values.flatten())
RE_CdTe_steel_expansion = pd.DataFrame(CdTe_MI.iloc[1].values * RE_CdTe_capacity_expansion.values.flatten())
RE_CdTe_aluminium_expansion = pd.DataFrame(CdTe_MI.iloc[2].values * RE_CdTe_capacity_expansion.values.flatten())
RE_CdTe_copper_expansion = pd.DataFrame(CdTe_MI.iloc[3].values * RE_CdTe_capacity_expansion.values.flatten())
RE_CdTe_cadmium_expansion = pd.DataFrame(CdTe_MI.iloc[4].values * RE_CdTe_capacity_expansion.values.flatten())
RE_CdTe_tellurium_expansion = pd.DataFrame(CdTe_MI.iloc[5].values * RE_CdTe_capacity_expansion.values.flatten())

RE_aSi_concrete_expansion = pd.DataFrame(aSi_MI.iloc[0].values * RE_aSi_capacity_expansion.values.flatten())
RE_aSi_steel_expansion = pd.DataFrame(aSi_MI.iloc[1].values * RE_aSi_capacity_expansion.values.flatten())
RE_aSi_aluminium_expansion = pd.DataFrame(aSi_MI.iloc[2].values * RE_aSi_capacity_expansion.values.flatten())
RE_aSi_copper_expansion = pd.DataFrame(aSi_MI.iloc[3].values * RE_aSi_capacity_expansion.values.flatten())
RE_aSi_silicon_expansion = pd.DataFrame(aSi_MI.iloc[4].values * RE_aSi_capacity_expansion.values.flatten())
RE_aSi_germanium_expansion = pd.DataFrame(aSi_MI.iloc[5].values * RE_aSi_capacity_expansion.values.flatten())

RE_CIGS_concrete_expansion = pd.DataFrame(CIGS_MI.iloc[0].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_steel_expansion = pd.DataFrame(CIGS_MI.iloc[1].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_aluminium_expansion = pd.DataFrame(CIGS_MI.iloc[2].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_copper_expansion = pd.DataFrame(CIGS_MI.iloc[3].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_indium_expansion = pd.DataFrame(CIGS_MI.iloc[4].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_gallium_expansion = pd.DataFrame(CIGS_MI.iloc[5].values * RE_CIGS_capacity_expansion.values.flatten())
RE_CIGS_selenium_expansion = pd.DataFrame(CIGS_MI.iloc[6].values * RE_CIGS_capacity_expansion.values.flatten())

# replacement #
DR_cSi_concrete_replacement = pd.DataFrame(DR_cSi_inflow_concrete - DR_cSi_concrete_expansion)
DR_cSi_steel_replacement = pd.DataFrame(DR_cSi_inflow_steel - DR_cSi_steel_expansion)
DR_cSi_aluminium_replacement = pd.DataFrame(DR_cSi_inflow_aluminium - DR_cSi_aluminium_expansion)
DR_cSi_copper_replacement = pd.DataFrame(DR_cSi_inflow_copper - DR_cSi_copper_expansion)
DR_cSi_silicon_replacement = pd.DataFrame(DR_cSi_inflow_silicon - DR_cSi_silicon_expansion)
DR_cSi_silver_replacement = pd.DataFrame(DR_cSi_inflow_silver - DR_cSi_silver_expansion)

DR_CdTe_concrete_replacement = pd.DataFrame(DR_CdTe_inflow_concrete - DR_CdTe_concrete_expansion)
DR_CdTe_steel_replacement = pd.DataFrame(DR_CdTe_inflow_steel - DR_CdTe_steel_expansion)
DR_CdTe_aluminium_replacement = pd.DataFrame(DR_CdTe_inflow_aluminium - DR_CdTe_aluminium_expansion)
DR_CdTe_copper_replacement = pd.DataFrame(DR_CdTe_inflow_copper - DR_CdTe_copper_expansion)
DR_CdTe_cadmium_replacement = pd.DataFrame(DR_CdTe_inflow_cadmium - DR_CdTe_cadmium_expansion)
DR_CdTe_tellurium_replacement = pd.DataFrame(DR_CdTe_inflow_tellurium - DR_CdTe_tellurium_expansion)

DR_aSi_concrete_replacement = pd.DataFrame(DR_aSi_inflow_concrete - DR_aSi_concrete_expansion)
DR_aSi_steel_replacement = pd.DataFrame(DR_aSi_inflow_steel - DR_aSi_steel_expansion)
DR_aSi_aluminium_replacement = pd.DataFrame(DR_aSi_inflow_aluminium - DR_aSi_aluminium_expansion)
DR_aSi_copper_replacement = pd.DataFrame(DR_aSi_inflow_copper - DR_aSi_copper_expansion)
DR_aSi_silicon_replacement = pd.DataFrame(DR_aSi_inflow_silicon - DR_aSi_silicon_expansion)
DR_aSi_germanium_replacement = pd.DataFrame(DR_aSi_inflow_germanium - DR_aSi_germanium_expansion)

DR_CIGS_concrete_replacement = pd.DataFrame(DR_CIGS_inflow_concrete - DR_CIGS_concrete_expansion)
DR_CIGS_steel_replacement = pd.DataFrame(DR_CIGS_inflow_steel - DR_CIGS_steel_expansion)
DR_CIGS_aluminium_replacement = pd.DataFrame(DR_CIGS_inflow_aluminium - DR_CIGS_aluminium_expansion)
DR_CIGS_copper_replacement = pd.DataFrame(DR_CIGS_inflow_copper - DR_CIGS_copper_expansion)
DR_CIGS_indium_replacement = pd.DataFrame(DR_CIGS_inflow_indium - DR_CIGS_indium_expansion)
DR_CIGS_gallium_replacement = pd.DataFrame(DR_CIGS_inflow_gallium - DR_CIGS_gallium_expansion)
DR_CIGS_selenium_replacement = pd.DataFrame(DR_CIGS_inflow_selenium - DR_CIGS_selenium_expansion)


DE_cSi_concrete_replacement = pd.DataFrame(DE_cSi_inflow_concrete - DE_cSi_concrete_expansion)
DE_cSi_steel_replacement = pd.DataFrame(DE_cSi_inflow_steel - DE_cSi_steel_expansion)
DE_cSi_aluminium_replacement = pd.DataFrame(DE_cSi_inflow_aluminium - DE_cSi_aluminium_expansion)
DE_cSi_copper_replacement = pd.DataFrame(DE_cSi_inflow_copper - DE_cSi_copper_expansion)
DE_cSi_silicon_replacement = pd.DataFrame(DE_cSi_inflow_silicon - DE_cSi_silicon_expansion)
DE_cSi_silver_replacement = pd.DataFrame(DE_cSi_inflow_silver - DE_cSi_silver_expansion)

DE_CdTe_concrete_replacement = pd.DataFrame(DE_CdTe_inflow_concrete - DE_CdTe_concrete_expansion)
DE_CdTe_steel_replacement = pd.DataFrame(DE_CdTe_inflow_steel - DE_CdTe_steel_expansion)
DE_CdTe_aluminium_replacement = pd.DataFrame(DE_CdTe_inflow_aluminium - DE_CdTe_aluminium_expansion)
DE_CdTe_copper_replacement = pd.DataFrame(DE_CdTe_inflow_copper - DE_CdTe_copper_expansion)
DE_CdTe_cadmium_replacement = pd.DataFrame(DE_CdTe_inflow_cadmium - DE_CdTe_cadmium_expansion)
DE_CdTe_tellurium_replacement = pd.DataFrame(DE_CdTe_inflow_tellurium - DE_CdTe_tellurium_expansion)

DE_aSi_concrete_replacement = pd.DataFrame(DE_aSi_inflow_concrete - DE_aSi_concrete_expansion)
DE_aSi_steel_replacement = pd.DataFrame(DE_aSi_inflow_steel - DE_aSi_steel_expansion)
DE_aSi_aluminium_replacement = pd.DataFrame(DE_aSi_inflow_aluminium - DE_aSi_aluminium_expansion)
DE_aSi_copper_replacement = pd.DataFrame(DE_aSi_inflow_copper - DE_aSi_copper_expansion)
DE_aSi_silicon_replacement = pd.DataFrame(DE_aSi_inflow_silicon - DE_aSi_silicon_expansion)
DE_aSi_germanium_replacement = pd.DataFrame(DE_aSi_inflow_germanium - DE_aSi_germanium_expansion)

DE_CIGS_concrete_replacement = pd.DataFrame(DE_CIGS_inflow_concrete - DE_CIGS_concrete_expansion)
DE_CIGS_steel_replacement = pd.DataFrame(DE_CIGS_inflow_steel - DE_CIGS_steel_expansion)
DE_CIGS_aluminium_replacement = pd.DataFrame(DE_CIGS_inflow_aluminium - DE_CIGS_aluminium_expansion)
DE_CIGS_copper_replacement = pd.DataFrame(DE_CIGS_inflow_copper - DE_CIGS_copper_expansion)
DE_CIGS_indium_replacement = pd.DataFrame(DE_CIGS_inflow_indium - DE_CIGS_indium_expansion)
DE_CIGS_gallium_replacement = pd.DataFrame(DE_CIGS_inflow_gallium - DE_CIGS_gallium_expansion)
DE_CIGS_selenium_replacement = pd.DataFrame(DE_CIGS_inflow_selenium - DE_CIGS_selenium_expansion)

RE_cSi_concrete_replacement = pd.DataFrame(RE_cSi_inflow_concrete - RE_cSi_concrete_expansion)
RE_cSi_steel_replacement = pd.DataFrame(RE_cSi_inflow_steel - RE_cSi_steel_expansion)
RE_cSi_aluminium_replacement = pd.DataFrame(RE_cSi_inflow_aluminium - RE_cSi_aluminium_expansion)
RE_cSi_copper_replacement = pd.DataFrame(RE_cSi_inflow_copper - RE_cSi_copper_expansion)
RE_cSi_silicon_replacement = pd.DataFrame(RE_cSi_inflow_silicon - RE_cSi_silicon_expansion)
RE_cSi_silver_replacement = pd.DataFrame(RE_cSi_inflow_silver - RE_cSi_silver_expansion)

RE_CdTe_concrete_replacement = pd.DataFrame(RE_CdTe_inflow_concrete - RE_CdTe_concrete_expansion)
RE_CdTe_steel_replacement = pd.DataFrame(RE_CdTe_inflow_steel - RE_CdTe_steel_expansion)
RE_CdTe_aluminium_replacement = pd.DataFrame(RE_CdTe_inflow_aluminium - RE_CdTe_aluminium_expansion)
RE_CdTe_copper_replacement = pd.DataFrame(RE_CdTe_inflow_copper - RE_CdTe_copper_expansion)
RE_CdTe_cadmium_replacement = pd.DataFrame(RE_CdTe_inflow_cadmium - RE_CdTe_cadmium_expansion)
RE_CdTe_tellurium_replacement = pd.DataFrame(RE_CdTe_inflow_tellurium - RE_CdTe_tellurium_expansion)

RE_aSi_concrete_replacement = pd.DataFrame(RE_aSi_inflow_concrete - RE_aSi_concrete_expansion)
RE_aSi_steel_replacement = pd.DataFrame(RE_aSi_inflow_steel - RE_aSi_steel_expansion)
RE_aSi_aluminium_replacement = pd.DataFrame(RE_aSi_inflow_aluminium - RE_aSi_aluminium_expansion)
RE_aSi_copper_replacement = pd.DataFrame(RE_aSi_inflow_copper - RE_aSi_copper_expansion)
RE_aSi_silicon_replacement = pd.DataFrame(RE_aSi_inflow_silicon - RE_aSi_silicon_expansion)
RE_aSi_germanium_replacement = pd.DataFrame(RE_aSi_inflow_germanium - RE_aSi_germanium_expansion)

RE_CIGS_concrete_replacement = pd.DataFrame(RE_CIGS_inflow_concrete - RE_CIGS_concrete_expansion)
RE_CIGS_steel_replacement = pd.DataFrame(RE_CIGS_inflow_steel - RE_CIGS_steel_expansion)
RE_CIGS_aluminium_replacement = pd.DataFrame(RE_CIGS_inflow_aluminium - RE_CIGS_aluminium_expansion)
RE_CIGS_copper_replacement = pd.DataFrame(RE_CIGS_inflow_copper - RE_CIGS_copper_expansion)
RE_CIGS_indium_replacement = pd.DataFrame(RE_CIGS_inflow_indium - RE_CIGS_indium_expansion)
RE_CIGS_gallium_replacement = pd.DataFrame(RE_CIGS_inflow_gallium - RE_CIGS_gallium_expansion)
RE_CIGS_selenium_replacement = pd.DataFrame(RE_CIGS_inflow_selenium - RE_CIGS_selenium_expansion)

# Concat the results together for plotting #
years = list(range(1990,2051))

# DR scenario flows #
DR_cSi_concrete_flows = pd.concat([DR_cSi_inflow_concrete, DR_cSi_outflow_concrete],ignore_index=True, axis=1)
DR_cSi_concrete_flows.columns = ['inflow','outflow']
DR_cSi_concrete_flows.index = years

DR_CdTe_concrete_flows = pd.concat([DR_CdTe_inflow_concrete, DR_CdTe_outflow_concrete],ignore_index=True, axis=1)
DR_CdTe_concrete_flows.columns = ['inflow','outflow']
DR_CdTe_concrete_flows.index = years

DR_aSi_concrete_flows = pd.concat([DR_aSi_inflow_concrete, DR_aSi_outflow_concrete],ignore_index=True, axis=1)
DR_aSi_concrete_flows.columns = ['inflow','outflow']
DR_aSi_concrete_flows.index = years

DR_CIGS_concrete_flows = pd.concat([DR_CIGS_inflow_concrete, DR_CIGS_outflow_concrete],ignore_index=True, axis=1)
DR_CIGS_concrete_flows.columns = ['inflow','outflow']
DR_CIGS_concrete_flows.index = years

DR_cSi_steel_flows = pd.concat([DR_cSi_inflow_steel, DR_cSi_outflow_steel],ignore_index=True, axis=1)
DR_cSi_steel_flows.columns = ['inflow','outflow']
DR_cSi_steel_flows.index = years

DR_CdTe_steel_flows = pd.concat([DR_CdTe_inflow_steel, DR_CdTe_outflow_steel],ignore_index=True, axis=1)
DR_CdTe_steel_flows.columns = ['inflow','outflow']
DR_CdTe_steel_flows.index = years

DR_aSi_steel_flows = pd.concat([DR_aSi_inflow_steel, DR_aSi_outflow_steel],ignore_index=True, axis=1)
DR_aSi_steel_flows.columns = ['inflow','outflow']
DR_aSi_steel_flows.index = years

DR_CIGS_steel_flows = pd.concat([DR_CIGS_inflow_steel, DR_CIGS_outflow_steel],ignore_index=True, axis=1)
DR_CIGS_steel_flows.columns = ['inflow','outflow']
DR_CIGS_steel_flows.index = years

DR_cSi_aluminium_flows = pd.concat([DR_cSi_inflow_aluminium, DR_cSi_outflow_aluminium],ignore_index=True, axis=1)
DR_cSi_aluminium_flows.columns = ['inflow','outflow']
DR_cSi_aluminium_flows.index = years

DR_CdTe_aluminium_flows = pd.concat([DR_CdTe_inflow_aluminium, DR_CdTe_outflow_aluminium],ignore_index=True, axis=1)
DR_CdTe_aluminium_flows.columns = ['inflow','outflow']
DR_CdTe_aluminium_flows.index = years

DR_aSi_aluminium_flows = pd.concat([DR_aSi_inflow_aluminium, DR_aSi_outflow_aluminium],ignore_index=True, axis=1)
DR_aSi_aluminium_flows.columns = ['inflow','outflow']
DR_aSi_aluminium_flows.index = years

DR_CIGS_aluminium_flows = pd.concat([DR_CIGS_inflow_aluminium, DR_CIGS_outflow_aluminium],ignore_index=True, axis=1)
DR_CIGS_aluminium_flows.columns = ['inflow','outflow']
DR_CIGS_aluminium_flows.index = years

DR_cSi_copper_flows = pd.concat([DR_cSi_inflow_copper, DR_cSi_outflow_copper],ignore_index=True, axis=1)
DR_cSi_copper_flows.columns = ['inflow','outflow']
DR_cSi_copper_flows.index = years

DR_CdTe_copper_flows = pd.concat([DR_CdTe_inflow_copper, DR_CdTe_outflow_copper],ignore_index=True, axis=1)
DR_CdTe_copper_flows.columns = ['inflow','outflow']
DR_CdTe_copper_flows.index = years

DR_aSi_copper_flows = pd.concat([DR_aSi_inflow_copper, DR_aSi_outflow_copper],ignore_index=True, axis=1)
DR_aSi_copper_flows.columns = ['inflow','outflow']
DR_aSi_copper_flows.index = years

DR_CIGS_copper_flows = pd.concat([DR_CIGS_inflow_copper, DR_CIGS_outflow_copper],ignore_index=True, axis=1)
DR_CIGS_copper_flows.columns = ['inflow','outflow']
DR_CIGS_copper_flows.index = years

DR_cSi_silicon_flows = pd.concat([DR_cSi_inflow_silicon, DR_cSi_outflow_silicon],ignore_index=True, axis=1)
DR_cSi_silicon_flows.columns = ['inflow','outflow']
DR_cSi_silicon_flows.index = years

DR_CdTe_cadmium_flows = pd.concat([DR_CdTe_inflow_cadmium, DR_CdTe_outflow_cadmium],ignore_index=True, axis=1)
DR_CdTe_cadmium_flows.columns = ['inflow','outflow']
DR_CdTe_cadmium_flows.index = years

DR_aSi_silicon_flows = pd.concat([DR_aSi_inflow_silicon, DR_aSi_outflow_silicon],ignore_index=True, axis=1)
DR_aSi_silicon_flows.columns = ['inflow','outflow']
DR_aSi_silicon_flows.index = years

DR_CIGS_indium_flows = pd.concat([DR_CIGS_inflow_indium, DR_CIGS_outflow_indium],ignore_index=True, axis=1)
DR_CIGS_indium_flows.columns = ['inflow','outflow']
DR_CIGS_indium_flows.index = years

DR_cSi_silver_flows = pd.concat([DR_cSi_inflow_silver, DR_cSi_outflow_silver],ignore_index=True, axis=1)
DR_cSi_silver_flows.columns = ['inflow','outflow']
DR_cSi_silver_flows.index = years

DR_CdTe_tellurium_flows = pd.concat([DR_CdTe_inflow_tellurium, DR_CdTe_outflow_tellurium],ignore_index=True, axis=1)
DR_CdTe_tellurium_flows.columns = ['inflow','outflow']
DR_CdTe_tellurium_flows.index = years

DR_aSi_germanium_flows = pd.concat([DR_aSi_inflow_germanium, DR_aSi_outflow_germanium],ignore_index=True, axis=1)
DR_aSi_germanium_flows.columns = ['inflow','outflow']
DR_aSi_germanium_flows.index = years

DR_CIGS_gallium_flows = pd.concat([DR_CIGS_inflow_gallium, DR_CIGS_outflow_gallium],ignore_index=True, axis=1)
DR_CIGS_gallium_flows.columns = ['inflow','outflow']
DR_CIGS_gallium_flows.index = years

DR_CIGS_selenium_flows = pd.concat([DR_CIGS_inflow_selenium, DR_CIGS_outflow_selenium],ignore_index=True, axis=1)
DR_CIGS_selenium_flows.columns = ['inflow','outflow']
DR_CIGS_selenium_flows.index = years

# DR scenario expansion and replacement #

DR_cSi_concrete_exp = pd.concat([DR_cSi_concrete_expansion, DR_cSi_concrete_replacement],ignore_index=True, axis=1)
DR_cSi_concrete_exp.columns = ['expansion','replacement']
DR_cSi_concrete_exp.index = years

DR_CdTe_concrete_exp = pd.concat([DR_CdTe_concrete_expansion, DR_CdTe_concrete_replacement],ignore_index=True, axis=1)
DR_CdTe_concrete_exp.columns = ['expansion','replacement']
DR_CdTe_concrete_exp.index = years

DR_aSi_concrete_exp = pd.concat([DR_aSi_concrete_expansion, DR_aSi_concrete_replacement],ignore_index=True, axis=1)
DR_aSi_concrete_exp.columns = ['expansion','replacement']
DR_aSi_concrete_exp.index = years

DR_CIGS_concrete_exp = pd.concat([DR_CIGS_concrete_expansion, DR_CIGS_concrete_replacement],ignore_index=True, axis=1)
DR_CIGS_concrete_exp.columns = ['expansion','replacement']
DR_CIGS_concrete_exp.index = years

DR_cSi_steel_exp = pd.concat([DR_cSi_steel_expansion, DR_cSi_steel_replacement],ignore_index=True, axis=1)
DR_cSi_steel_exp.columns = ['expansion','replacement']
DR_cSi_steel_exp.index = years

DR_CdTe_steel_exp = pd.concat([DR_CdTe_steel_expansion, DR_CdTe_steel_replacement],ignore_index=True, axis=1)
DR_CdTe_steel_exp.columns = ['expansion','replacement']
DR_CdTe_steel_exp.index = years

DR_aSi_steel_exp = pd.concat([DR_aSi_steel_expansion, DR_aSi_steel_replacement],ignore_index=True, axis=1)
DR_aSi_steel_exp.columns = ['expansion','replacement']
DR_aSi_steel_exp.index = years

DR_CIGS_steel_exp = pd.concat([DR_CIGS_steel_expansion, DR_CIGS_steel_replacement],ignore_index=True, axis=1)
DR_CIGS_steel_exp.columns = ['expansion','replacement']
DR_CIGS_steel_exp.index = years

DR_cSi_aluminium_exp = pd.concat([DR_cSi_aluminium_expansion, DR_cSi_aluminium_replacement],ignore_index=True, axis=1)
DR_cSi_aluminium_exp.columns = ['expansion','replacement']
DR_cSi_aluminium_exp.index = years

DR_CdTe_aluminium_exp = pd.concat([DR_CdTe_aluminium_expansion, DR_CdTe_aluminium_replacement],ignore_index=True, axis=1)
DR_CdTe_aluminium_exp.columns = ['expansion','replacement']
DR_CdTe_aluminium_exp.index = years

DR_aSi_aluminium_exp = pd.concat([DR_aSi_aluminium_expansion, DR_aSi_aluminium_replacement],ignore_index=True, axis=1)
DR_aSi_aluminium_exp.columns = ['expansion','replacement']
DR_aSi_aluminium_exp.index = years

DR_CIGS_aluminium_exp = pd.concat([DR_CIGS_aluminium_expansion, DR_CIGS_aluminium_replacement],ignore_index=True, axis=1)
DR_CIGS_aluminium_exp.columns = ['expansion','replacement']
DR_CIGS_aluminium_exp.index = years

DR_cSi_copper_exp = pd.concat([DR_cSi_copper_expansion, DR_cSi_copper_replacement],ignore_index=True, axis=1)
DR_cSi_copper_exp.columns = ['expansion','replacement']
DR_cSi_copper_exp.index = years

DR_CdTe_copper_exp = pd.concat([DR_CdTe_copper_expansion, DR_CdTe_copper_replacement],ignore_index=True, axis=1)
DR_CdTe_copper_exp.columns = ['expansion','replacement']
DR_CdTe_copper_exp.index = years

DR_aSi_copper_exp = pd.concat([DR_aSi_copper_expansion, DR_aSi_copper_replacement],ignore_index=True, axis=1)
DR_aSi_copper_exp.columns = ['expansion','replacement']
DR_aSi_copper_exp.index = years

DR_CIGS_copper_exp = pd.concat([DR_CIGS_copper_expansion, DR_CIGS_copper_replacement],ignore_index=True, axis=1)
DR_CIGS_copper_exp.columns = ['expansion','replacement']
DR_CIGS_copper_exp.index = years

DR_cSi_silicon_exp = pd.concat([DR_cSi_silicon_expansion, DR_cSi_silicon_replacement],ignore_index=True, axis=1)
DR_cSi_silicon_exp.columns = ['expansion','replacement']
DR_cSi_silicon_exp.index = years

DR_CdTe_cadmium_exp = pd.concat([DR_CdTe_cadmium_expansion, DR_CdTe_cadmium_replacement],ignore_index=True, axis=1)
DR_CdTe_cadmium_exp.columns = ['expansion','replacement']
DR_CdTe_cadmium_exp.index = years

DR_aSi_silicon_exp = pd.concat([DR_aSi_silicon_expansion, DR_aSi_silicon_replacement],ignore_index=True, axis=1)
DR_aSi_silicon_exp.columns = ['expansion','replacement']
DR_aSi_silicon_exp.index = years

DR_CIGS_indium_exp = pd.concat([DR_CIGS_indium_expansion, DR_CIGS_indium_replacement],ignore_index=True, axis=1)
DR_CIGS_indium_exp.columns = ['expansion','replacement']
DR_CIGS_indium_exp.index = years

DR_cSi_silver_exp = pd.concat([DR_cSi_silver_expansion, DR_cSi_silver_replacement],ignore_index=True, axis=1)
DR_cSi_silver_exp.columns = ['expansion','replacement']
DR_cSi_silver_exp.index = years

DR_CdTe_tellurium_exp = pd.concat([DR_CdTe_tellurium_expansion, DR_CdTe_tellurium_replacement],ignore_index=True, axis=1)
DR_CdTe_tellurium_exp.columns = ['expansion','replacement']
DR_CdTe_tellurium_exp.index = years

DR_aSi_germanium_exp = pd.concat([DR_aSi_germanium_expansion, DR_aSi_germanium_replacement],ignore_index=True, axis=1)
DR_aSi_germanium_exp.columns = ['expansion','replacement']
DR_aSi_germanium_exp.index = years

DR_CIGS_gallium_exp = pd.concat([DR_CIGS_gallium_expansion, DR_CIGS_gallium_replacement],ignore_index=True, axis=1)
DR_CIGS_gallium_exp.columns = ['expansion','replacement']
DR_CIGS_gallium_exp.index = years

DR_CIGS_selenium_exp = pd.concat([DR_CIGS_selenium_expansion, DR_CIGS_selenium_replacement],ignore_index=True, axis=1)
DR_CIGS_selenium_exp.columns = ['expansion','replacement']
DR_CIGS_selenium_exp.index = years


# DE scenario flows #
DE_cSi_concrete_flows = pd.concat([DE_cSi_inflow_concrete, DE_cSi_outflow_concrete],ignore_index=True, axis=1)
DE_cSi_concrete_flows.columns = ['inflow','outflow']
DE_cSi_concrete_flows.index = years

DE_CdTe_concrete_flows = pd.concat([DE_CdTe_inflow_concrete, DE_CdTe_outflow_concrete],ignore_index=True, axis=1)
DE_CdTe_concrete_flows.columns = ['inflow','outflow']
DE_CdTe_concrete_flows.index = years

DE_aSi_concrete_flows = pd.concat([DE_aSi_inflow_concrete, DE_aSi_outflow_concrete],ignore_index=True, axis=1)
DE_aSi_concrete_flows.columns = ['inflow','outflow']
DE_aSi_concrete_flows.index = years

DE_CIGS_concrete_flows = pd.concat([DE_CIGS_inflow_concrete, DE_CIGS_outflow_concrete],ignore_index=True, axis=1)
DE_CIGS_concrete_flows.columns = ['inflow','outflow']
DE_CIGS_concrete_flows.index = years

DE_cSi_steel_flows = pd.concat([DE_cSi_inflow_steel, DE_cSi_outflow_steel],ignore_index=True, axis=1)
DE_cSi_steel_flows.columns = ['inflow','outflow']
DE_cSi_steel_flows.index = years

DE_CdTe_steel_flows = pd.concat([DE_CdTe_inflow_steel, DE_CdTe_outflow_steel],ignore_index=True, axis=1)
DE_CdTe_steel_flows.columns = ['inflow','outflow']
DE_CdTe_steel_flows.index = years

DE_aSi_steel_flows = pd.concat([DE_aSi_inflow_steel, DE_aSi_outflow_steel],ignore_index=True, axis=1)
DE_aSi_steel_flows.columns = ['inflow','outflow']
DE_aSi_steel_flows.index = years

DE_CIGS_steel_flows = pd.concat([DE_CIGS_inflow_steel, DE_CIGS_outflow_steel],ignore_index=True, axis=1)
DE_CIGS_steel_flows.columns = ['inflow','outflow']
DE_CIGS_steel_flows.index = years

DE_cSi_aluminium_flows = pd.concat([DE_cSi_inflow_aluminium, DE_cSi_outflow_aluminium],ignore_index=True, axis=1)
DE_cSi_aluminium_flows.columns = ['inflow','outflow']
DE_cSi_aluminium_flows.index = years

DE_CdTe_aluminium_flows = pd.concat([DE_CdTe_inflow_aluminium, DE_CdTe_outflow_aluminium],ignore_index=True, axis=1)
DE_CdTe_aluminium_flows.columns = ['inflow','outflow']
DE_CdTe_aluminium_flows.index = years

DE_aSi_aluminium_flows = pd.concat([DE_aSi_inflow_aluminium, DE_aSi_outflow_aluminium],ignore_index=True, axis=1)
DE_aSi_aluminium_flows.columns = ['inflow','outflow']
DE_aSi_aluminium_flows.index = years

DE_CIGS_aluminium_flows = pd.concat([DE_CIGS_inflow_aluminium, DE_CIGS_outflow_aluminium],ignore_index=True, axis=1)
DE_CIGS_aluminium_flows.columns = ['inflow','outflow']
DE_CIGS_aluminium_flows.index = years

DE_cSi_copper_flows = pd.concat([DE_cSi_inflow_copper, DE_cSi_outflow_copper],ignore_index=True, axis=1)
DE_cSi_copper_flows.columns = ['inflow','outflow']
DE_cSi_copper_flows.index = years

DE_CdTe_copper_flows = pd.concat([DE_CdTe_inflow_copper, DE_CdTe_outflow_copper],ignore_index=True, axis=1)
DE_CdTe_copper_flows.columns = ['inflow','outflow']
DE_CdTe_copper_flows.index = years

DE_aSi_copper_flows = pd.concat([DE_aSi_inflow_copper, DE_aSi_outflow_copper],ignore_index=True, axis=1)
DE_aSi_copper_flows.columns = ['inflow','outflow']
DE_aSi_copper_flows.index = years

DE_CIGS_copper_flows = pd.concat([DE_CIGS_inflow_copper, DE_CIGS_outflow_copper],ignore_index=True, axis=1)
DE_CIGS_copper_flows.columns = ['inflow','outflow']
DE_CIGS_copper_flows.index = years

DE_cSi_silicon_flows = pd.concat([DE_cSi_inflow_silicon, DE_cSi_outflow_silicon],ignore_index=True, axis=1)
DE_cSi_silicon_flows.columns = ['inflow','outflow']
DE_cSi_silicon_flows.index = years

DE_CdTe_cadmium_flows = pd.concat([DE_CdTe_inflow_cadmium, DE_CdTe_outflow_cadmium],ignore_index=True, axis=1)
DE_CdTe_cadmium_flows.columns = ['inflow','outflow']
DE_CdTe_cadmium_flows.index = years

DE_aSi_silicon_flows = pd.concat([DE_aSi_inflow_silicon, DE_aSi_outflow_silicon],ignore_index=True, axis=1)
DE_aSi_silicon_flows.columns = ['inflow','outflow']
DE_aSi_silicon_flows.index = years

DE_CIGS_indium_flows = pd.concat([DE_CIGS_inflow_indium, DE_CIGS_outflow_indium],ignore_index=True, axis=1)
DE_CIGS_indium_flows.columns = ['inflow','outflow']
DE_CIGS_indium_flows.index = years

DE_cSi_silver_flows = pd.concat([DE_cSi_inflow_silver, DE_cSi_outflow_silver],ignore_index=True, axis=1)
DE_cSi_silver_flows.columns = ['inflow','outflow']
DE_cSi_silver_flows.index = years

DE_CdTe_tellurium_flows = pd.concat([DE_CdTe_inflow_tellurium, DE_CdTe_outflow_tellurium],ignore_index=True, axis=1)
DE_CdTe_tellurium_flows.columns = ['inflow','outflow']
DE_CdTe_tellurium_flows.index = years

DE_aSi_germanium_flows = pd.concat([DE_aSi_inflow_germanium, DE_aSi_outflow_germanium],ignore_index=True, axis=1)
DE_aSi_germanium_flows.columns = ['inflow','outflow']
DE_aSi_germanium_flows.index = years

DE_CIGS_gallium_flows = pd.concat([DE_CIGS_inflow_gallium, DE_CIGS_outflow_gallium],ignore_index=True, axis=1)
DE_CIGS_gallium_flows.columns = ['inflow','outflow']
DE_CIGS_gallium_flows.index = years

DE_CIGS_selenium_flows = pd.concat([DE_CIGS_inflow_selenium, DE_CIGS_outflow_selenium],ignore_index=True, axis=1)
DE_CIGS_selenium_flows.columns = ['inflow','outflow']
DE_CIGS_selenium_flows.index = years

# DE scenario expansion and replacement #

DE_cSi_concrete_exp = pd.concat([DE_cSi_concrete_expansion, DE_cSi_concrete_replacement],ignore_index=True, axis=1)
DE_cSi_concrete_exp.columns = ['expansion','replacement']
DE_cSi_concrete_exp.index = years

DE_CdTe_concrete_exp = pd.concat([DE_CdTe_concrete_expansion, DE_CdTe_concrete_replacement],ignore_index=True, axis=1)
DE_CdTe_concrete_exp.columns = ['expansion','replacement']
DE_CdTe_concrete_exp.index = years

DE_aSi_concrete_exp = pd.concat([DE_aSi_concrete_expansion, DE_aSi_concrete_replacement],ignore_index=True, axis=1)
DE_aSi_concrete_exp.columns = ['expansion','replacement']
DE_aSi_concrete_exp.index = years

DE_CIGS_concrete_exp = pd.concat([DE_CIGS_concrete_expansion, DE_CIGS_concrete_replacement],ignore_index=True, axis=1)
DE_CIGS_concrete_exp.columns = ['expansion','replacement']
DE_CIGS_concrete_exp.index = years

DE_cSi_steel_exp = pd.concat([DE_cSi_steel_expansion, DE_cSi_steel_replacement],ignore_index=True, axis=1)
DE_cSi_steel_exp.columns = ['expansion','replacement']
DE_cSi_steel_exp.index = years

DE_CdTe_steel_exp = pd.concat([DE_CdTe_steel_expansion, DE_CdTe_steel_replacement],ignore_index=True, axis=1)
DE_CdTe_steel_exp.columns = ['expansion','replacement']
DE_CdTe_steel_exp.index = years

DE_aSi_steel_exp = pd.concat([DE_aSi_steel_expansion, DE_aSi_steel_replacement],ignore_index=True, axis=1)
DE_aSi_steel_exp.columns = ['expansion','replacement']
DE_aSi_steel_exp.index = years

DE_CIGS_steel_exp = pd.concat([DE_CIGS_steel_expansion, DE_CIGS_steel_replacement],ignore_index=True, axis=1)
DE_CIGS_steel_exp.columns = ['expansion','replacement']
DE_CIGS_steel_exp.index = years

DE_cSi_aluminium_exp = pd.concat([DE_cSi_aluminium_expansion, DE_cSi_aluminium_replacement],ignore_index=True, axis=1)
DE_cSi_aluminium_exp.columns = ['expansion','replacement']
DE_cSi_aluminium_exp.index = years

DE_CdTe_aluminium_exp = pd.concat([DE_CdTe_aluminium_expansion, DE_CdTe_aluminium_replacement],ignore_index=True, axis=1)
DE_CdTe_aluminium_exp.columns = ['expansion','replacement']
DE_CdTe_aluminium_exp.index = years

DE_aSi_aluminium_exp = pd.concat([DE_aSi_aluminium_expansion, DE_aSi_aluminium_replacement],ignore_index=True, axis=1)
DE_aSi_aluminium_exp.columns = ['expansion','replacement']
DE_aSi_aluminium_exp.index = years

DE_CIGS_aluminium_exp = pd.concat([DE_CIGS_aluminium_expansion, DE_CIGS_aluminium_replacement],ignore_index=True, axis=1)
DE_CIGS_aluminium_exp.columns = ['expansion','replacement']
DE_CIGS_aluminium_exp.index = years

DE_cSi_copper_exp = pd.concat([DE_cSi_copper_expansion, DE_cSi_copper_replacement],ignore_index=True, axis=1)
DE_cSi_copper_exp.columns = ['expansion','replacement']
DE_cSi_copper_exp.index = years

DE_CdTe_copper_exp = pd.concat([DE_CdTe_copper_expansion, DE_CdTe_copper_replacement],ignore_index=True, axis=1)
DE_CdTe_copper_exp.columns = ['expansion','replacement']
DE_CdTe_copper_exp.index = years

DE_aSi_copper_exp = pd.concat([DE_aSi_copper_expansion, DE_aSi_copper_replacement],ignore_index=True, axis=1)
DE_aSi_copper_exp.columns = ['expansion','replacement']
DE_aSi_copper_exp.index = years

DE_CIGS_copper_exp = pd.concat([DE_CIGS_copper_expansion, DE_CIGS_copper_replacement],ignore_index=True, axis=1)
DE_CIGS_copper_exp.columns = ['expansion','replacement']
DE_CIGS_copper_exp.index = years

DE_cSi_silicon_exp = pd.concat([DE_cSi_silicon_expansion, DE_cSi_silicon_replacement],ignore_index=True, axis=1)
DE_cSi_silicon_exp.columns = ['expansion','replacement']
DE_cSi_silicon_exp.index = years

DE_CdTe_cadmium_exp = pd.concat([DE_CdTe_cadmium_expansion, DE_CdTe_cadmium_replacement],ignore_index=True, axis=1)
DE_CdTe_cadmium_exp.columns = ['expansion','replacement']
DE_CdTe_cadmium_exp.index = years

DE_aSi_silicon_exp = pd.concat([DE_aSi_silicon_expansion, DE_aSi_silicon_replacement],ignore_index=True, axis=1)
DE_aSi_silicon_exp.columns = ['expansion','replacement']
DE_aSi_silicon_exp.index = years

DE_CIGS_indium_exp = pd.concat([DE_CIGS_indium_expansion, DE_CIGS_indium_replacement],ignore_index=True, axis=1)
DE_CIGS_indium_exp.columns = ['expansion','replacement']
DE_CIGS_indium_exp.index = years

DE_cSi_silver_exp = pd.concat([DE_cSi_silver_expansion, DE_cSi_silver_replacement],ignore_index=True, axis=1)
DE_cSi_silver_exp.columns = ['expansion','replacement']
DE_cSi_silver_exp.index = years

DE_CdTe_tellurium_exp = pd.concat([DE_CdTe_tellurium_expansion, DE_CdTe_tellurium_replacement],ignore_index=True, axis=1)
DE_CdTe_tellurium_exp.columns = ['expansion','replacement']
DE_CdTe_tellurium_exp.index = years

DE_aSi_germanium_exp = pd.concat([DE_aSi_germanium_expansion, DE_aSi_germanium_replacement],ignore_index=True, axis=1)
DE_aSi_germanium_exp.columns = ['expansion','replacement']
DE_aSi_germanium_exp.index = years

DE_CIGS_gallium_exp = pd.concat([DE_CIGS_gallium_expansion, DE_CIGS_gallium_replacement],ignore_index=True, axis=1)
DE_CIGS_gallium_exp.columns = ['expansion','replacement']
DE_CIGS_gallium_exp.index = years

DE_CIGS_selenium_exp = pd.concat([DE_CIGS_selenium_expansion, DE_CIGS_selenium_replacement],ignore_index=True, axis=1)
DE_CIGS_selenium_exp.columns = ['expansion','replacement']
DE_CIGS_selenium_exp.index = years

# RE scenario flows #
RE_cSi_concrete_flows = pd.concat([RE_cSi_inflow_concrete, RE_cSi_outflow_concrete],ignore_index=True, axis=1)
RE_cSi_concrete_flows.columns = ['inflow','outflow']
RE_cSi_concrete_flows.index = years

RE_CdTe_concrete_flows = pd.concat([RE_CdTe_inflow_concrete, RE_CdTe_outflow_concrete],ignore_index=True, axis=1)
RE_CdTe_concrete_flows.columns = ['inflow','outflow']
RE_CdTe_concrete_flows.index = years

RE_aSi_concrete_flows = pd.concat([RE_aSi_inflow_concrete, RE_aSi_outflow_concrete],ignore_index=True, axis=1)
RE_aSi_concrete_flows.columns = ['inflow','outflow']
RE_aSi_concrete_flows.index = years

RE_CIGS_concrete_flows = pd.concat([RE_CIGS_inflow_concrete, RE_CIGS_outflow_concrete],ignore_index=True, axis=1)
RE_CIGS_concrete_flows.columns = ['inflow','outflow']
RE_CIGS_concrete_flows.index = years

RE_cSi_steel_flows = pd.concat([RE_cSi_inflow_steel, RE_cSi_outflow_steel],ignore_index=True, axis=1)
RE_cSi_steel_flows.columns = ['inflow','outflow']
RE_cSi_steel_flows.index = years

RE_CdTe_steel_flows = pd.concat([RE_CdTe_inflow_steel, RE_CdTe_outflow_steel],ignore_index=True, axis=1)
RE_CdTe_steel_flows.columns = ['inflow','outflow']
RE_CdTe_steel_flows.index = years

RE_aSi_steel_flows = pd.concat([RE_aSi_inflow_steel, RE_aSi_outflow_steel],ignore_index=True, axis=1)
RE_aSi_steel_flows.columns = ['inflow','outflow']
RE_aSi_steel_flows.index = years

RE_CIGS_steel_flows = pd.concat([RE_CIGS_inflow_steel, RE_CIGS_outflow_steel],ignore_index=True, axis=1)
RE_CIGS_steel_flows.columns = ['inflow','outflow']
RE_CIGS_steel_flows.index = years

RE_cSi_aluminium_flows = pd.concat([RE_cSi_inflow_aluminium, RE_cSi_outflow_aluminium],ignore_index=True, axis=1)
RE_cSi_aluminium_flows.columns = ['inflow','outflow']
RE_cSi_aluminium_flows.index = years

RE_CdTe_aluminium_flows = pd.concat([RE_CdTe_inflow_aluminium, RE_CdTe_outflow_aluminium],ignore_index=True, axis=1)
RE_CdTe_aluminium_flows.columns = ['inflow','outflow']
RE_CdTe_aluminium_flows.index = years

RE_aSi_aluminium_flows = pd.concat([RE_aSi_inflow_aluminium, RE_aSi_outflow_aluminium],ignore_index=True, axis=1)
RE_aSi_aluminium_flows.columns = ['inflow','outflow']
RE_aSi_aluminium_flows.index = years

RE_CIGS_aluminium_flows = pd.concat([RE_CIGS_inflow_aluminium, RE_CIGS_outflow_aluminium],ignore_index=True, axis=1)
RE_CIGS_aluminium_flows.columns = ['inflow','outflow']
RE_CIGS_aluminium_flows.index = years

RE_cSi_copper_flows = pd.concat([RE_cSi_inflow_copper, RE_cSi_outflow_copper],ignore_index=True, axis=1)
RE_cSi_copper_flows.columns = ['inflow','outflow']
RE_cSi_copper_flows.index = years

RE_CdTe_copper_flows = pd.concat([RE_CdTe_inflow_copper, RE_CdTe_outflow_copper],ignore_index=True, axis=1)
RE_CdTe_copper_flows.columns = ['inflow','outflow']
RE_CdTe_copper_flows.index = years

RE_aSi_copper_flows = pd.concat([RE_aSi_inflow_copper, RE_aSi_outflow_copper],ignore_index=True, axis=1)
RE_aSi_copper_flows.columns = ['inflow','outflow']
RE_aSi_copper_flows.index = years

RE_CIGS_copper_flows = pd.concat([RE_CIGS_inflow_copper, RE_CIGS_outflow_copper],ignore_index=True, axis=1)
RE_CIGS_copper_flows.columns = ['inflow','outflow']
RE_CIGS_copper_flows.index = years

RE_cSi_silicon_flows = pd.concat([RE_cSi_inflow_silicon, RE_cSi_outflow_silicon],ignore_index=True, axis=1)
RE_cSi_silicon_flows.columns = ['inflow','outflow']
RE_cSi_silicon_flows.index = years

RE_CdTe_cadmium_flows = pd.concat([RE_CdTe_inflow_cadmium, RE_CdTe_outflow_cadmium],ignore_index=True, axis=1)
RE_CdTe_cadmium_flows.columns = ['inflow','outflow']
RE_CdTe_cadmium_flows.index = years

RE_aSi_silicon_flows = pd.concat([RE_aSi_inflow_silicon, RE_aSi_outflow_silicon],ignore_index=True, axis=1)
RE_aSi_silicon_flows.columns = ['inflow','outflow']
RE_aSi_silicon_flows.index = years

RE_CIGS_indium_flows = pd.concat([RE_CIGS_inflow_indium, RE_CIGS_outflow_indium],ignore_index=True, axis=1)
RE_CIGS_indium_flows.columns = ['inflow','outflow']
RE_CIGS_indium_flows.index = years

RE_cSi_silver_flows = pd.concat([RE_cSi_inflow_silver, RE_cSi_outflow_silver],ignore_index=True, axis=1)
RE_cSi_silver_flows.columns = ['inflow','outflow']
RE_cSi_silver_flows.index = years

RE_CdTe_tellurium_flows = pd.concat([RE_CdTe_inflow_tellurium, RE_CdTe_outflow_tellurium],ignore_index=True, axis=1)
RE_CdTe_tellurium_flows.columns = ['inflow','outflow']
RE_CdTe_tellurium_flows.index = years

RE_aSi_germanium_flows = pd.concat([RE_aSi_inflow_germanium, RE_aSi_outflow_germanium],ignore_index=True, axis=1)
RE_aSi_germanium_flows.columns = ['inflow','outflow']
RE_aSi_germanium_flows.index = years

RE_CIGS_gallium_flows = pd.concat([RE_CIGS_inflow_gallium, RE_CIGS_outflow_gallium],ignore_index=True, axis=1)
RE_CIGS_gallium_flows.columns = ['inflow','outflow']
RE_CIGS_gallium_flows.index = years

RE_CIGS_selenium_flows = pd.concat([RE_CIGS_inflow_selenium, RE_CIGS_outflow_selenium],ignore_index=True, axis=1)
RE_CIGS_selenium_flows.columns = ['inflow','outflow']
RE_CIGS_selenium_flows.index = years

# RE scenario expansion and replacement #

RE_cSi_concrete_exp = pd.concat([RE_cSi_concrete_expansion, RE_cSi_concrete_replacement],ignore_index=True, axis=1)
RE_cSi_concrete_exp.columns = ['expansion','replacement']
RE_cSi_concrete_exp.index = years

RE_CdTe_concrete_exp = pd.concat([RE_CdTe_concrete_expansion, RE_CdTe_concrete_replacement],ignore_index=True, axis=1)
RE_CdTe_concrete_exp.columns = ['expansion','replacement']
RE_CdTe_concrete_exp.index = years

RE_aSi_concrete_exp = pd.concat([RE_aSi_concrete_expansion, RE_aSi_concrete_replacement],ignore_index=True, axis=1)
RE_aSi_concrete_exp.columns = ['expansion','replacement']
RE_aSi_concrete_exp.index = years

RE_CIGS_concrete_exp = pd.concat([RE_CIGS_concrete_expansion, RE_CIGS_concrete_replacement],ignore_index=True, axis=1)
RE_CIGS_concrete_exp.columns = ['expansion','replacement']
RE_CIGS_concrete_exp.index = years

RE_cSi_steel_exp = pd.concat([RE_cSi_steel_expansion, RE_cSi_steel_replacement],ignore_index=True, axis=1)
RE_cSi_steel_exp.columns = ['expansion','replacement']
RE_cSi_steel_exp.index = years

RE_CdTe_steel_exp = pd.concat([RE_CdTe_steel_expansion, RE_CdTe_steel_replacement],ignore_index=True, axis=1)
RE_CdTe_steel_exp.columns = ['expansion','replacement']
RE_CdTe_steel_exp.index = years

RE_aSi_steel_exp = pd.concat([RE_aSi_steel_expansion, RE_aSi_steel_replacement],ignore_index=True, axis=1)
RE_aSi_steel_exp.columns = ['expansion','replacement']
RE_aSi_steel_exp.index = years

RE_CIGS_steel_exp = pd.concat([RE_CIGS_steel_expansion, RE_CIGS_steel_replacement],ignore_index=True, axis=1)
RE_CIGS_steel_exp.columns = ['expansion','replacement']
RE_CIGS_steel_exp.index = years

RE_cSi_aluminium_exp = pd.concat([RE_cSi_aluminium_expansion, RE_cSi_aluminium_replacement],ignore_index=True, axis=1)
RE_cSi_aluminium_exp.columns = ['expansion','replacement']
RE_cSi_aluminium_exp.index = years

RE_CdTe_aluminium_exp = pd.concat([RE_CdTe_aluminium_expansion, RE_CdTe_aluminium_replacement],ignore_index=True, axis=1)
RE_CdTe_aluminium_exp.columns = ['expansion','replacement']
RE_CdTe_aluminium_exp.index = years

RE_aSi_aluminium_exp = pd.concat([RE_aSi_aluminium_expansion, RE_aSi_aluminium_replacement],ignore_index=True, axis=1)
RE_aSi_aluminium_exp.columns = ['expansion','replacement']
RE_aSi_aluminium_exp.index = years

RE_CIGS_aluminium_exp = pd.concat([RE_CIGS_aluminium_expansion, RE_CIGS_aluminium_replacement],ignore_index=True, axis=1)
RE_CIGS_aluminium_exp.columns = ['expansion','replacement']
RE_CIGS_aluminium_exp.index = years

RE_cSi_copper_exp = pd.concat([RE_cSi_copper_expansion, RE_cSi_copper_replacement],ignore_index=True, axis=1)
RE_cSi_copper_exp.columns = ['expansion','replacement']
RE_cSi_copper_exp.index = years

RE_CdTe_copper_exp = pd.concat([RE_CdTe_copper_expansion, RE_CdTe_copper_replacement],ignore_index=True, axis=1)
RE_CdTe_copper_exp.columns = ['expansion','replacement']
RE_CdTe_copper_exp.index = years

RE_aSi_copper_exp = pd.concat([RE_aSi_copper_expansion, RE_aSi_copper_replacement],ignore_index=True, axis=1)
RE_aSi_copper_exp.columns = ['expansion','replacement']
RE_aSi_copper_exp.index = years

RE_CIGS_copper_exp = pd.concat([RE_CIGS_copper_expansion, RE_CIGS_copper_replacement],ignore_index=True, axis=1)
RE_CIGS_copper_exp.columns = ['expansion','replacement']
RE_CIGS_copper_exp.index = years

RE_cSi_silicon_exp = pd.concat([RE_cSi_silicon_expansion, RE_cSi_silicon_replacement],ignore_index=True, axis=1)
RE_cSi_silicon_exp.columns = ['expansion','replacement']
RE_cSi_silicon_exp.index = years

RE_CdTe_cadmium_exp = pd.concat([RE_CdTe_cadmium_expansion, RE_CdTe_cadmium_replacement],ignore_index=True, axis=1)
RE_CdTe_cadmium_exp.columns = ['expansion','replacement']
RE_CdTe_cadmium_exp.index = years

RE_aSi_silicon_exp = pd.concat([RE_aSi_silicon_expansion, RE_aSi_silicon_replacement],ignore_index=True, axis=1)
RE_aSi_silicon_exp.columns = ['expansion','replacement']
RE_aSi_silicon_exp.index = years

RE_CIGS_indium_exp = pd.concat([RE_CIGS_indium_expansion, RE_CIGS_indium_replacement],ignore_index=True, axis=1)
RE_CIGS_indium_exp.columns = ['expansion','replacement']
RE_CIGS_indium_exp.index = years

RE_cSi_silver_exp = pd.concat([RE_cSi_silver_expansion, RE_cSi_silver_replacement],ignore_index=True, axis=1)
RE_cSi_silver_exp.columns = ['expansion','replacement']
RE_cSi_silver_exp.index = years

RE_CdTe_tellurium_exp = pd.concat([RE_CdTe_tellurium_expansion, RE_CdTe_tellurium_replacement],ignore_index=True, axis=1)
RE_CdTe_tellurium_exp.columns = ['expansion','replacement']
RE_CdTe_tellurium_exp.index = years

RE_aSi_germanium_exp = pd.concat([RE_aSi_germanium_expansion, RE_aSi_germanium_replacement],ignore_index=True, axis=1)
RE_aSi_germanium_exp.columns = ['expansion','replacement']
RE_aSi_germanium_exp.index = years

RE_CIGS_gallium_exp = pd.concat([RE_CIGS_gallium_expansion, RE_CIGS_gallium_replacement],ignore_index=True, axis=1)
RE_CIGS_gallium_exp.columns = ['expansion','replacement']
RE_CIGS_gallium_exp.index = years

RE_CIGS_selenium_exp = pd.concat([RE_CIGS_selenium_expansion, RE_CIGS_selenium_replacement],ignore_index=True, axis=1)
RE_CIGS_selenium_exp.columns = ['expansion','replacement']
RE_CIGS_selenium_exp.index = years

# Calculate stock with a inflow driven approach #
from pv_helper import inflow_driven_stock

# DR scenario stock #
DR_cSi_stock = inflow_driven_stock(DR_cSi_inflow.values.flatten(), lifetime)
DR_CdTe_stock = inflow_driven_stock(DR_CdTe_inflow.values.flatten(), lifetime)
DR_aSi_stock = inflow_driven_stock(DR_aSi_inflow.values.flatten(), lifetime)
DR_CIGS_stock = inflow_driven_stock(DR_CIGS_inflow.values.flatten(), lifetime)

# DE scenario stock #
DE_cSi_stock = inflow_driven_stock(DE_cSi_inflow.values.flatten(), lifetime)
DE_CdTe_stock = inflow_driven_stock(DE_CdTe_inflow.values.flatten(), lifetime)
DE_aSi_stock = inflow_driven_stock(DE_aSi_inflow.values.flatten(), lifetime)
DE_CIGS_stock = inflow_driven_stock(DE_CIGS_inflow.values.flatten(), lifetime)

# RE scenario stock #
RE_cSi_stock = inflow_driven_stock(RE_cSi_inflow.values.flatten(), lifetime)
RE_CdTe_stock = inflow_driven_stock(RE_CdTe_inflow.values.flatten(), lifetime)
RE_aSi_stock = inflow_driven_stock(RE_aSi_inflow.values.flatten(), lifetime)
RE_CIGS_stock = inflow_driven_stock(RE_CIGS_inflow.values.flatten(), lifetime)

# Stock materials #
DR_cSi_stock_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DR_cSi_stock.values.flatten())
DR_cSi_stock_steel = pd.DataFrame(cSi_MI.iloc[1].values * DR_cSi_stock.values.flatten())
DR_cSi_stock_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DR_cSi_stock.values.flatten())
DR_cSi_stock_copper = pd.DataFrame(cSi_MI.iloc[3].values * DR_cSi_stock.values.flatten())
DR_cSi_stock_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DR_cSi_stock.values.flatten())
DR_cSi_stock_silver = pd.DataFrame(cSi_MI.iloc[5].values * DR_cSi_stock.values.flatten())

DR_CdTe_stock_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DR_CdTe_stock.values.flatten())
DR_CdTe_stock_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DR_CdTe_stock.values.flatten())
DR_CdTe_stock_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DR_CdTe_stock.values.flatten())
DR_CdTe_stock_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DR_CdTe_stock.values.flatten())
DR_CdTe_stock_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DR_CdTe_stock.values.flatten())
DR_CdTe_stock_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * DR_CdTe_stock.values.flatten())

DR_aSi_stock_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DR_aSi_stock.values.flatten())
DR_aSi_stock_steel = pd.DataFrame(aSi_MI.iloc[1].values * DR_aSi_stock.values.flatten())
DR_aSi_stock_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DR_aSi_stock.values.flatten())
DR_aSi_stock_copper = pd.DataFrame(aSi_MI.iloc[3].values * DR_aSi_stock.values.flatten())
DR_aSi_stock_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DR_aSi_stock.values.flatten())
DR_aSi_stock_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DR_aSi_stock.values.flatten())

DR_CIGS_stock_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DR_CIGS_stock.values.flatten())
DR_CIGS_stock_selenium = pd.DataFrame(CIGS_MI.iloc[6].values * DR_CIGS_stock.values.flatten())

DE_cSi_stock_concrete = pd.DataFrame(cSi_MI.iloc[0].values * DE_cSi_stock.values.flatten())
DE_cSi_stock_steel = pd.DataFrame(cSi_MI.iloc[1].values * DE_cSi_stock.values.flatten())
DE_cSi_stock_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * DE_cSi_stock.values.flatten())
DE_cSi_stock_copper = pd.DataFrame(cSi_MI.iloc[3].values * DE_cSi_stock.values.flatten())
DE_cSi_stock_silicon = pd.DataFrame(cSi_MI.iloc[4].values * DE_cSi_stock.values.flatten())
DE_cSi_stock_silver = pd.DataFrame(cSi_MI.iloc[5].values * DE_cSi_stock.values.flatten())

DE_CdTe_stock_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * DE_CdTe_stock.values.flatten())
DE_CdTe_stock_steel = pd.DataFrame(CdTe_MI.iloc[1].values * DE_CdTe_stock.values.flatten())
DE_CdTe_stock_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * DE_CdTe_stock.values.flatten())
DE_CdTe_stock_copper = pd.DataFrame(CdTe_MI.iloc[3].values * DE_CdTe_stock.values.flatten())
DE_CdTe_stock_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * DE_CdTe_stock.values.flatten())
DE_CdTe_stock_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * DE_CdTe_stock.values.flatten())

DE_aSi_stock_concrete = pd.DataFrame(aSi_MI.iloc[0].values * DE_aSi_stock.values.flatten())
DE_aSi_stock_steel = pd.DataFrame(aSi_MI.iloc[1].values * DE_aSi_stock.values.flatten())
DE_aSi_stock_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * DE_aSi_stock.values.flatten())
DE_aSi_stock_copper = pd.DataFrame(aSi_MI.iloc[3].values * DE_aSi_stock.values.flatten())
DE_aSi_stock_silicon = pd.DataFrame(aSi_MI.iloc[4].values * DE_aSi_stock.values.flatten())
DE_aSi_stock_germanium = pd.DataFrame(aSi_MI.iloc[5].values * DE_aSi_stock.values.flatten())

DE_CIGS_stock_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_steel = pd.DataFrame(CIGS_MI.iloc[1].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_copper = pd.DataFrame(CIGS_MI.iloc[3].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_indium = pd.DataFrame(CIGS_MI.iloc[4].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_stock.values.flatten())
DE_CIGS_stock_selenium = pd.DataFrame(CIGS_MI.iloc[5].values * DE_CIGS_stock.values.flatten())

RE_cSi_stock_concrete = pd.DataFrame(cSi_MI.iloc[0].values * RE_cSi_stock.values.flatten())
RE_cSi_stock_steel = pd.DataFrame(cSi_MI.iloc[1].values * RE_cSi_stock.values.flatten())
RE_cSi_stock_aluminium = pd.DataFrame(cSi_MI.iloc[2].values * RE_cSi_stock.values.flatten())
RE_cSi_stock_copper = pd.DataFrame(cSi_MI.iloc[3].values * RE_cSi_stock.values.flatten())
RE_cSi_stock_silicon = pd.DataFrame(cSi_MI.iloc[4].values * RE_cSi_stock.values.flatten())
RE_cSi_stock_silver = pd.DataFrame(cSi_MI.iloc[5].values * RE_cSi_stock.values.flatten())

RE_CdTe_stock_concrete = pd.DataFrame(CdTe_MI.iloc[0].values * RE_CdTe_stock.values.flatten())
RE_CdTe_stock_steel = pd.DataFrame(CdTe_MI.iloc[1].values * RE_CdTe_stock.values.flatten())
RE_CdTe_stock_aluminium = pd.DataFrame(CdTe_MI.iloc[2].values * RE_CdTe_stock.values.flatten())
RE_CdTe_stock_copper = pd.DataFrame(CdTe_MI.iloc[3].values * RE_CdTe_stock.values.flatten())
RE_CdTe_stock_cadmium = pd.DataFrame(CdTe_MI.iloc[4].values * RE_CdTe_stock.values.flatten())
RE_CdTe_stock_tellurium = pd.DataFrame(CdTe_MI.iloc[5].values * RE_CdTe_stock.values.flatten())

RE_aSi_stock_concrete = pd.DataFrame(aSi_MI.iloc[0].values * RE_aSi_stock.values.flatten())
RE_aSi_stock_steel = pd.DataFrame(aSi_MI.iloc[1].values * RE_aSi_stock.values.flatten())
RE_aSi_stock_aluminium = pd.DataFrame(aSi_MI.iloc[2].values * RE_aSi_stock.values.flatten())
RE_aSi_stock_copper = pd.DataFrame(aSi_MI.iloc[3].values * RE_aSi_stock.values.flatten())
RE_aSi_stock_silicon = pd.DataFrame(aSi_MI.iloc[4].values * RE_aSi_stock.values.flatten())
RE_aSi_stock_germanium = pd.DataFrame(aSi_MI.iloc[5].values * RE_aSi_stock.values.flatten())

RE_CIGS_stock_concrete = pd.DataFrame(CIGS_MI.iloc[0].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_steel = pd.DataFrame(CIGS_MI.iloc[1].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_aluminium = pd.DataFrame(CIGS_MI.iloc[2].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_copper = pd.DataFrame(CIGS_MI.iloc[3].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_indium = pd.DataFrame(CIGS_MI.iloc[4].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_gallium = pd.DataFrame(CIGS_MI.iloc[5].values * RE_CIGS_stock.values.flatten())
RE_CIGS_stock_selenium = pd.DataFrame(CIGS_MI.iloc[5].values * RE_CIGS_stock.values.flatten())

# Concat flows for plotting #
DR_cSi_inflow_silicon['years'] = years
DR_cSi_outflow_silicon['years'] = years
DR_cSi_inflow_silicon['Flows'] = 'inflows'
DR_cSi_outflow_silicon['Flows'] = 'outflows'

DR_cSi_inflow_silicon = DR_cSi_inflow_silicon.iloc[20:61]
DR_cSi_outflow_silicon = DR_cSi_outflow_silicon.iloc[20:61]

DR_cSi_silicon_all_flows = pd.concat([DR_cSi_inflow_silicon, DR_cSi_outflow_silicon],ignore_index=True, axis=0)
DR_cSi_silicon_all_flows.columns = ['Flows [ton/year]','years','Flows']

DR_cSi_inflow_silver['years'] = years
DR_cSi_outflow_silver['years'] = years
DR_cSi_inflow_silver['Flows'] = 'inflows'
DR_cSi_outflow_silver['Flows'] = 'outflows'

DR_cSi_inflow_silver = DR_cSi_inflow_silver.iloc[20:61]
DR_cSi_outflow_silver = DR_cSi_outflow_silver.iloc[20:61]

DR_cSi_silver_all_flows = pd.concat([DR_cSi_inflow_silver, DR_cSi_outflow_silver],ignore_index=True, axis=0)
DR_cSi_silver_all_flows.columns = ['Flows [ton/year]','years','Flows']

DE_cSi_inflow_silicon['years'] = years
DE_cSi_outflow_silicon['years'] = years
DE_cSi_inflow_silicon['Flows'] = 'inflows'
DE_cSi_outflow_silicon['Flows'] = 'outflows'

DE_cSi_inflow_silicon = DE_cSi_inflow_silicon.iloc[20:61]
DE_cSi_outflow_silicon = DE_cSi_outflow_silicon.iloc[20:61]

DE_cSi_silicon_all_flows = pd.concat([DE_cSi_inflow_silicon, DE_cSi_outflow_silicon],ignore_index=True, axis=0)
DE_cSi_silicon_all_flows.columns = ['Flows [ton/year]','years','Flows']

DE_cSi_inflow_silver['years'] = years
DE_cSi_outflow_silver['years'] = years
DE_cSi_inflow_silver['Flows'] = 'inflows'
DE_cSi_outflow_silver['Flows'] = 'outflows'

DE_cSi_inflow_silver = DE_cSi_inflow_silver.iloc[20:61]
DE_cSi_outflow_silver = DE_cSi_outflow_silver.iloc[20:61]

DE_cSi_silver_all_flows = pd.concat([DE_cSi_inflow_silver, DE_cSi_outflow_silver],ignore_index=True, axis=0)
DE_cSi_silver_all_flows.columns = ['Flows [ton/year]','years','Flows']

RE_cSi_inflow_silicon['years'] = years
RE_cSi_outflow_silicon['years'] = years
RE_cSi_inflow_silicon['Flows'] = 'inflows'
RE_cSi_outflow_silicon['Flows'] = 'outflows'

RE_cSi_inflow_silicon = RE_cSi_inflow_silicon.iloc[20:61]
RE_cSi_outflow_silicon = RE_cSi_outflow_silicon.iloc[20:61]

RE_cSi_silicon_all_flows = pd.concat([RE_cSi_inflow_silicon, RE_cSi_outflow_silicon],ignore_index=True, axis=0)
RE_cSi_silicon_all_flows.columns = ['Flows [ton/year]','years','Flows']

RE_cSi_inflow_silver['years'] = years
RE_cSi_outflow_silver['years'] = years
RE_cSi_inflow_silver['Flows'] = 'inflows'
RE_cSi_outflow_silver['Flows'] = 'outflows'

RE_cSi_inflow_silver = RE_cSi_inflow_silver.iloc[20:61]
RE_cSi_outflow_silver = RE_cSi_outflow_silver.iloc[20:61]

RE_cSi_silver_all_flows = pd.concat([RE_cSi_inflow_silver, RE_cSi_outflow_silver],ignore_index=True, axis=0)
RE_cSi_silver_all_flows.columns = ['Flows [ton/year]','years','Flows']

# Plotting #
years = pd.DataFrame(years)

# Plotting #
cm = 1/2.54  # centimeters in inches
cols = ['#8ECAE6','#219EBC']

fig, axs  = plt.subplots(4,3, sharey='row', figsize=(19*cm, 19*cm))
fig.tight_layout()

sns.barplot(ax=axs[0,0], data=DR_cSi_silicon_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)
sns.barplot(ax=axs[0,1], data=DE_cSi_silicon_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)
sns.barplot(ax=axs[0,2], data=RE_cSi_silicon_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)

axs[0,0].tick_params(axis='x', rotation=90)
axs[0,1].tick_params(axis='x', rotation=90)
axs[0,2].tick_params(axis='x', rotation=90)

axs[1,0].stackplot(years.values.flatten(), DR_cSi_stock_silicon.T, labels=['cSi'], color=['#FB8500'])
axs[1,1].stackplot(years.values.flatten(), DE_cSi_stock_silicon.T, labels=['cSi'], color=['#FB8500'])
axs[1,2].stackplot(years.values.flatten(), RE_cSi_stock_silicon.T, labels=['cSi'], color=['#FB8500'])

sns.barplot(ax=axs[2,0], data=DR_cSi_silver_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)
sns.barplot(ax=axs[2,1], data=DE_cSi_silver_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)
sns.barplot(ax=axs[2,2], data=RE_cSi_silver_all_flows, x="years", y="Flows [ton/year]", hue="Flows", errorbar=None, palette=cols)

axs[3,0].stackplot(years.values.flatten(), DR_cSi_stock_silver.T, labels=['cSi'], color=['#FB8500'])
axs[3,1].stackplot(years.values.flatten(), DE_cSi_stock_silver.T, labels=['cSi'], color=['#FB8500'])
axs[3,2].stackplot(years.values.flatten(), RE_cSi_stock_silver.T, labels=['cSi'], color=['#FB8500'])

axs[2,0].tick_params(axis='x', rotation=90)
axs[2,1].tick_params(axis='x', rotation=90)
axs[2,2].tick_params(axis='x', rotation=90)

axs[1,0].set_xlim(xmin=2010, xmax=2050)
axs[1,1].set_xlim(xmin=2010, xmax=2050)
axs[1,2].set_xlim(xmin=2010, xmax=2050)

axs[1,0].set(xlabel='years', ylabel='Stock [ton]')
axs[1,1].set(xlabel='years', ylabel='Stock [ton]')
axs[1,2].set(xlabel='years', ylabel='Stock [ton]')

axs[3,0].set_xlim(xmin=2010, xmax=2050)
axs[3,1].set_xlim(xmin=2010, xmax=2050)
axs[3,2].set_xlim(xmin=2010, xmax=2050)

axs[3,0].set(xlabel='years', ylabel='Stock [ton]')
axs[3,1].set(xlabel='years', ylabel='Stock [ton]')
axs[3,2].set(xlabel='years', ylabel='Stock [ton]')


# Stacked area plot #
#plt.stackplot(years.values.flatten(), DR_cSi_stock.T, DR_CdTe_stock.T, DR_CIGS_stock.T, labels=['cSi','CdTe','CIGS'])
#plt.legend(loc='upper left')
plt.savefig("pv_plot.png", dpi=500)
plt.show()


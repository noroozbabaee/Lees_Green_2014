# Author: Leyla Noroozbaee
# Date: 12/09/2021
# Read the data (model simulations) from the selected files (csv) and plot the results for the selected variation
# The data is produced through the 'ICC_Lees_Green.py'

import matplotlib.pyplot as plt
import pandas as pd
prefilename = 'Fig4_1'
filename1 = '%sa.csv' % (prefilename)
data = pd.read_csv(filename1)
time = data ['time']
Ca_i_Ano1 = data ['Ca_i']
Vm_Ano1 = data ['Vm']
filename2 = '%sb.csv' % (prefilename)
data = pd.read_csv(filename2)
time = data ['time']
Ca_i_no_Ano1 = data ['Ca_i']
Vm_no_Ano1 = data ['Vm']

fig, ax = plt.subplots(2,1, figsize=(8, 4))
# ax[0,0] = fig.add_subplot(111)
ax [ 0 ].plot(time[8500:10000]  , Vm_Ano1[8500:10000]  , 'b', time[8500:10000]  , Vm_no_Ano1[8500:10000]  , 'r')
ax [ 0 ].set_ylabel('Vm [mV]')
ax [ 1 ].plot(time[8500:10000] , Ca_i_Ano1[8500:10000] , 'b', time[8500:10000]  , Ca_i_no_Ano1[8500:10000]  , 'r')
ax [ 1].set_xlabel('Time (ms)')
ax [ 1 ].set_ylabel('Ca [10^-6 M]')
plt.show()
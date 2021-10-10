# Author: Leyla Noroozbabaee
# Date: 12/09/2021
# To reproduce Figure 3 from original paper, the python file 'IAo1.py' should be run.

import matplotlib.pyplot as plt
import pandas as pd

# Figure name
figfile = 'Fig3'

# Read data from the files
x_name = 'Time'
y_name = [ 'IAon1']
current = r'$I_{Aon1}(pA)$'
print(current)
y_labels = [ '%s' % current ]
Vm = range(-100, 140, 40)
suffix = [ 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a' ]
c = ['a','b','c','d']
# Set figure dimension (width, height) in inches.
fw, fh = 15, 6
# Set subplots
subpRow, subpCol = 1, 4
ax, lns = {}, {}
# Set Title
tit = ['A $Ca_{Aon1}$ =$10^{-7}$ M','B $Ca_{Aon1}$ = $10^{-6}$ M','C $Ca_{Aon1}$ = $10^{-5}$ M','D']
# This gives list with the colors from the cycle, which you can use to iterate over.
cycle = plt.rcParams [ 'axes.prop_cycle' ].by_key() [ 'color' ]
# Set subplots
lfontsize, labelfontsize = 10, 15  # legend, label fontsize
fig, axs = plt.subplots(subpRow, subpCol, figsize=(fw, fh), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .1, wspace=.1)
for j in range(4):
    for i, V in enumerate(Vm):
        filename = '%s_%d_%s.csv' % (figfile, i, c [ j ])
        print('filename', filename)
        data = pd.read_csv(filename)
        x_data = data [ x_name ]
        y_data = data [ y_name ]
        axs [ j ].plot(x_data, y_data, color=cycle [ i % 7 ], label='%d mV ' % (V))
        plt.tick_params(direction='in', axis='both')
        axs [ j ].legend(loc='best', fontsize=lfontsize, frameon=False)
        axs [ j ].set_xlabel('Time (ms)', fontsize=labelfontsize)
        axs [ j ].set_title('%s' % (tit[j]))
    axs [ 0 ].set_ylabel(y_labels [ 0 ], fontsize=labelfontsize)
    figfiles = '%s.png' % figfile
    plt.savefig(figfiles)
plt.show()

# Author : Leyla Noroozbabaee
# Date: 12/09/2021
import matplotlib.pyplot as plt
import pandas as pd
# Use csv files Fig5_1a and Fig5_1b to reproduce Figure 5A and 5C
# Use csv files Fig5_2a and Fig5_2b to reproduce Figure 5B and 5D
prefig = 'Fig5'
figfile = 'sim%s' % prefig
fig, axs = plt.subplots(2,2, figsize=(8,8), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace = .5, wspace=.5)

axs = axs.ravel()
title = ['A Low-Cl(NaV)','B Low-Cl(NSCa)','C Low-Cl(NaV)','D Low-Cl(NSCa)']
for i in range(2):
    filename = 'Fig5_%da.csv' % (i + 1)
    data = pd.read_csv(filename)
    Ca_i_Ano1 = data [ 'Ca_i' ]
    Vm_Ano1 = data [ 'Vm' ]
    filename2 = 'Fig5_%db.csv' % (i + 1)
    data = pd.read_csv(filename2)
    time = data [ 'time' ]
    Ca_i_no_Ano1 = data [ 'Ca_i' ]
    Vm_no_Ano1 = data [ 'Vm' ]
    axs [ i ].plot(time [ 300:1800 ], Vm_Ano1 [ 300:1800 ], 'b', time [ 300:1800 ], Vm_no_Ano1 [ 300:1800 ], 'r')
    axs[i+ 2].plot(time[ 300:1800 ], Ca_i_Ano1[ 300:1800 ], 'b', time[ 300:1800 ], Ca_i_no_Ano1[ 300:1800 ], 'r')
    axs[i].set_title(str(title[i]))
    axs [ i ].set_ylabel('Vm (mV)')
    axs [i + 2].set_title(str(title[i+2]))
    axs [ i + 2 ].set_ylabel('Ca_i (10^-6 M)')
    figfiles = '%s.png' % prefig
    plt.savefig(figfiles)
plt.show()

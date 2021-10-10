# Author : Leyla Noroozbabaee
# Date: 12/09/2021
import matplotlib.pyplot as plt
import pandas as pd

# Figure name
prefig = 'Fig_4'
fig, axs = plt.subplots(2, 4, figsize=(14, 7), facecolor='w', edgecolor='k')
fig.subplots_adjust(hspace =.5, wspace=.5)
axs = axs.ravel()
title = ['A  High-Cl(NaV)','B  High-Cl(NSV)','C  High-Cl(NSCa)','D  High-Cl(CaV)','E  High-Cl(NaV)','F  High-Cl(NSV)',
       'G  High-Cl(NSCa)', 'H High-Cl(CaV)']
for i in range(4):
    filename1 = 'Fig4_%da.csv' % (i + 1)
    data = pd.read_csv(filename1)
    Ca_i_Ano1 = data [ 'Ca_i' ]
    Vm_Ano1 = data [ 'Vm' ]
    filename2 = 'Fig4_%db.csv' % (i + 1)
    data = pd.read_csv(filename2)
    time = data ['time']
    Ca_i_no_Ano1 = data ['Ca_i']
    Vm_no_Ano1 = data [ 'Vm' ]
    axs[i].plot(time [ 300:1800 ], Vm_Ano1 [ 300:1800 ], 'b', time [ 300:1800 ], Vm_no_Ano1 [ 300:1800 ], 'r')
    axs[i + 4].plot(time[0:1500], Ca_i_Ano1[0:1500], 'b', time[0:1500], Ca_i_no_Ano1[0:1500], 'r')
    axs[i].set_title(str(title[i]))
    axs[i].set_ylabel('Vm (mV)')
    axs[i+4].set_title(str(title[i+4]))
    axs [i+4].set_ylabel('Ca_i (10^-6 M)')
    figfiles = '%s.png' % (prefig)
    plt.savefig(figfiles)
plt.show()


# Author : Leyla Noroozbabaee
# Date: 12/09/2021

# To reproduce the data needed for Figure 3 in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: run IAno1.py

import opencor as oc
import numpy as np
# The prefix of the saved output file name
prefilename = 'Fig3'
# Load the simulation file
simfile = 'Ano1_Lees_2021.sedml'
simulation = oc.open_simulation(simfile)
# The data object houses all the relevant information
# and pointers to the OpenCOR internal data representations
data = simulation.data()
# Set the experiments
Vm = range(-100, +140, 40)
print(type(Vm))
duration = 15
# Define the interval of interest for this simulation experiment
start, end, pointInterval = 0, duration, 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)
# Data to save
varName = np.array([ "Time", "IAon1" ])
vars = np.reshape(varName, (1, len(varName)))
rows = duration * 100 + 1
r = np.zeros((rows, len(varName)))
Ca = [0.10, 1, 10, 20]
Ca_local = np.linspace(0.1, 20, num=6)

c = ['a','b','c','d']
for j, Calocal in enumerate(Ca):
    for i, V in enumerate(Vm):
        # Reset states and parameters
        simulation.reset(True)
        # Set constant parameter values
        if j == 3:
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_clamp'] = Ca_local[i]
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_bl'] = 0.0
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_init'] = 0.0
            data.constants()['ICC_Membrane/V_clamp'] = V
            data.constants()['ICC_Membrane/V_bl'] = V
            data.constants()['ICC_Membrane/V_init'] = V

        else:
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_clamp'] = Calocal
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_bl'] = Calocal
            data.constants()['ICC_Membrane/I_Ano1/d_Ano1/localCa_init'] = Calocal
            data.constants()['ICC_Membrane/V_clamp'] = V
            data.constants()['ICC_Membrane/V_bl'] = -100
            data.constants()['ICC_Membrane/V_init'] = 0
        data.constants() ['ICC_Membrane/I_Ano1/d_Ano1/Ano1_s'] = 0.156
        simulation.run()
        # Access simulation results
        results = simulation.results()
        # Grab a specific algebraic variable results
        r [:, 0] = results.voi().values()
        r [ :, 1 ] = results.algebraic()['ICC_Membrane/I_Ano1/I_Ano1'].values()
        simulation.clear_results()
        # Save the simulation result of the last run
        filename = '%s_%d_%s.csv' % (prefilename, i, c[j])
        np.savetxt(filename, vars, fmt='%s', delimiter=",")
        with open(filename, "ab") as f:
            np.savetxt(f, r, delimiter=",")
        f.close

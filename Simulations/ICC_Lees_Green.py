import opencor as oc
import numpy as np
import json
# Author: Leyla Noroozbabaee
# Date: 12/ 09/2021

# To reproduce the data needed for Figure 3 in associated original paper,
# execute this script in the Python console in OpenCOR. This can be done
# with the following commands at the prompt in the OpenCOR Python console:
#
#     In [1]: cd path/to/folder_this_file_is_in
#     In [2]: run ICC_Lees_Green.py

# To reproduce 4A-4E; the json file 'HCl_NaV.json' is loaded to update the model's parameters and initial conditions
# for model simulations accordingly. Data is saved in the cvs files:  Fig4_1a and Fig4_1b.
# To reproduce 4B-4F; 'HCl_NSV.json' is loaded. Data is saved in the cvs files:  Fig4_2a and Fig4_2b
# To reproduce 4C-4G; 'HCl_NSCC.json' is loaded. Data is saved in the cvs files:  Fig4_3a and Fig4_3b
# To reproduce 4D-4H; 'HCl_CaV.json' is loaded. Data is saved in the cvs files:  Fig4_4a and Fig4_4b

# To reproduce 5A-5C; 'LCl_NaV.json' is loaded. Data is saved in the cvs files:  Fig5_1a and Fig5_1b
# To reproduce 5B-5D; 'LCl_NSCC.json' is loaded. Data is saved in the cvs files:  Fig5_2a and Fig5_2b

prefilename = 'Fig4_1'
simfile = 'ICC_Lees_2021.sedml'
simulation = oc.open_simulation(simfile)
data = simulation.data()
# Reset states and parameters
simulation.reset(True)
# Set constant parameter values
start = 0
end = 150
pointInterval = 0.01
data.set_starting_point(start)
data.set_ending_point(end)
data.set_point_interval(pointInterval)
rows = 150 * 100 + 1
# Setting the new parameters and initial conditions
with open('HCl_NaV.json','r') as fp:
    variables = json.load(fp)
for k, v in variables['constants'].items():
    data.constants()[k] = v
for k, v in variables['states'].items():
    data.states()[k] = v
# Run the simulation for WT scenarios
simulation.run()
# Access simulation results
results = simulation.results()
# Grab a selected algebraic variable results
varName = np.array([ "time", "Vm", "Ca_i"])
vars = np.reshape(varName, (1, 3))
r = np.zeros((rows, len(varName)))
r[:,0] = results.voi().values()
r[:,1] = results.states()['ICC_Membrane/Vm'].values()
r[:,2] = results.states()['ICC_Membrane/Ca_i'].values()

# Save the simulation results
filename = '%sa.csv' % prefilename
np.savetxt(filename, vars, fmt='%s',delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close

# Run the simulation for KO scenarios
data.constants()['ICC_Membrane/I_Ano1/g_Ano1'] = 0
simulation.run()
# Access simulation results
results = simulation.results()
# Grab a selected algebraic variable results
varName = np.array([ "time", "Vm", "Ca_i"])
vars = np.reshape(varName, (1, 3))
r = np.zeros((rows, len(varName)))
r[:,0] = results.voi().values()
r[:,1] = results.states()['ICC_Membrane/Vm'].values()
r[:,2] = results.states()['ICC_Membrane/Ca_i'].values()

# Save the simulation result of the last run
filename = '%sb.csv' % prefilename
np.savetxt(filename, vars, fmt='%s',delimiter=",")
with open(filename, "ab") as f:
    np.savetxt(f, r, delimiter=",")
f.close


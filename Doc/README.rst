Original Paper
==============

:Original publication:  "Computational modeling of anoctamin 1 calcium-activated chloride channels
as pacemaker channels in interstitial cells of Cajal" Am J Physiol Gastrointest Liver Physiol 306: G711–G727, 2014.

:DOI: https://doi.org/10.1152/ajpgi.00449.2013


Model status
=============

The current CellML model implementation runs in OpenCOR_.
The CellML model parameters and equations must be updated regarding each specific model variation to reproduce the related simulations; see the section :ref:`Model Experiments` for more detailed information.
The results have been validated against the data extracted from the figures in the published `Lees-Green, Rachel,  et al (2014)`_; see the section :ref:`Model Validation`.
Using the default parameters provided in the paper except for the modification listed in the following sections, Figure 4, 5 can be reproduced with no difference; see the section :ref:`Model Modifications`.


Model Summary
==============
Interstitial cells of Cajal (ICC) pacemaker activity begins when IP3-mediated Ca2 release from the ER leads
to depletion of the ER Ca2 stores, activating SOCE via SOC channels. Ano1 channels colocalized with SOC channels
are activated by the local rise in Ca2 in microdomains surrounding the open SOC channels, causing depolarization
of the ICC. The depolarization initiates a slow wave by activating voltage-dependent ion channels.
The morphology of the slow wave, including the plateau phase and repolarization, is determined by the balance of
voltage- and Ca2-dependent ion currents. The pacemaker cycle concludes when Ca2 influx via SOC channels and uptake via SERCA pumps
is sufficient to refill the ER stores, resulting in deactivation of the SOC channels and Ano1 channels.

.. image:: Doc/Schematic_diagram_ICC.png
   :width: 70%
   :alt: Schematic diagram of ICC.


Model Equations
===============
The model is implemented using a Hodgkin-Huxley type formulation. The cell membrane lipid bilayer is represented as a capacitance (Cm),
and the ion channels in the membrane are represented as conductance. The change in the transmembrane potential (Vm) over time depends on
is the sum of the individual ion currents through each class of ion channel in the cell current:


:math:` \frac{dVm}{dt} = - \frac{I_{tot}}{C_{m}}`.


Where there are 12 different ion channels, the total current, total fluxes equations,
and even the definition of ion channels can vary according to the model variations.

Model Variations
================
High chloride enviroment ( :math:`E_{Cl} = - 20.2` mV,  :math:`C_{Cl} = 78` mM) is categorized into four different variations, as the following:|br|

High-Cl(NaV): Ion current specific to Voltage-gated Na channel,

High-Cl(NSCa): Ion currents specific to Ca2-activated nonselective channel,

High-Cl(CaV): Ion current specific to Voltage-gated  `Ca` channel,

and then low chloride environment (:math:`E_{Cl} = - 49.7` mV, :math:`C_{Cl} = 25.85` mM) where the low chloride simulations categorized into two different variations:

Low-Cl(NaV) : Ion currents specific to Voltage-gated Na channel,

Low-Cl(NSCa): Ion currents specific to Ca2-activated nonselective channel.


Model Experiments
=================
This workspace contains two sets of experiments and corresponding simulation results:
The first sets reproduce the four variations for the high chloride concentration and therefore :math:`E_{Cl}=-20 mV`, and the results are demonstrated in Figure. 4.
The second sets of variations represent the low chloride environment with the :math:`E_{Cl}=-50 mV`, see Figure. 5 in the original paper. In each run, the required variables are saved: time, Ca concentration, and membrane voltage.
Here is the list of variations for both high chloride (HIGH-CL) and low chloride (LOW-CL) concentration and experiment information to reproduce the related simulations:

- Figure 4A-4E  (HIGH-CL(NaV): Sodium  Voltage Activated Channel): the json file 'HCl-NaV.json', contains the HIGH-CL(NAV) model's parameters and initial conditions. The wild-type (WT) simulation's result (full model simulation) is saved in 'Fig4_1a.csv'. For the Ano1 knockout (KO) scenarios, data are saved in 'Fig4_1b.csv'.

- Figure 4B-4F (HIGH-CL(NSV): Non-Selective Voltage  Activated Channel): the json file 'HCl-NSV.json' contains the HIGH-CL(NSV) model's parameters and initial conditions. The data relating to HIGH-CL(NSV) wild-type simulation is saved in 'Fig4_2a.csv'. For the Ano1 knockout (KO) scenarios, data are saved in 'Fig4_2b.csv'.

- Figure 4C-4G (HIGH-CL(NSCC): Non-Selective Ca Activated Channel): the json file 'HCl-NSCC.json' contains the HIGH-CL(NSCC) model's parameters and initial conditions. The  WT and KO results are saved in 'Fig4_3a.csv' and 'Fig4_3b.csv', respectively.

- Figure 4D-4H (HIGH-CL(CaV): Ca Voltage Activated Channel): the json file 'HCl-CaV.json' contains the HIGH-CL(CaV) model's parameters and initial conditions. The data for WT and KO scenarios are saved in 'Fig4_4a.csv' and 'Fig4_4b.csv', respectively.

- Figure 5A-5C  (LOW-CL(NaV): Sodium  Voltage Activated Channel) : the json file 'LCl-NaV.json' contains the LOW-CL(NAV) model's parameters and initial conditions. The data for WT and KO scenarios are saved in 'Fig5_1a.csv' and 'Fig5_1b.csv', respectively.

- Figure 5B-5D (LOW-CL(NSCC): Non-Selective Ca Activated Channel): the json file 'LCl-NSCC.json' contains the LOW-CL(NSCC) model's parameters and initial conditions. The data for WT and KO scenarios are saved in 'Fig5_2a.csv' and 'Fig5_2b.csv', respectively.

Model Modifications
===================
In the case of reproducibility and reusability, there are a couple of issues with the model equations and model default parameters. We point them as below:

- There are no definitions of the fluxes for some ion channels; definitions are defined from the references and compared to the similar descriptions of the other fluxes with similar behaviour in the original work and confirmed through the MATLAB updated model of ICC.
  :math:` J = - I/ZFV` where V indicates the cell Volume.

- To reproduce Figure 5A-5C; the K parameter for voltage-dependent gating equation for the NaV channel inactivation F_{NaV} is changed from -4.5 mV to 4.5 mV as the K parameter for voltage-dependent gating equation in the case of inactivation is always positive.

.. image:: Doc/Issue_LCl_NaV.png
   :width: 60%
   :alt: Schematic diagram of ICC.
- To reproduce Figure 5B-5D; the conductance value for the CaV channel is needed to reduce to g = 3.72 nS from the original value g = 4 nS. As shown in the below diagram at g = 4 nS, there are damped oscillations that indicate the dominant eigenvalue with a negative real part and stable system. These damped oscillations switch to the slow-wave oscillations for g = 3.72 nS.

.. image:: Doc/Issue_LCL_NSCC.png
   :width: 60%
   :alt: Schematic diagram of ICC.


Model Validations
=================
The results have been validated against the data extracted from the figures in the published `Lees-Green, Rachel,  et al (2014)`_.
To reproduce Figure 4, the default parameters are provided in the paper is used. Figure 4 can be reproduced with no difference as the original Figure 4 in `Lees-Green, Rachel,  et al (2014)`_.

.. image:: Doc/Figure4.png
      :width: 100%
      :alt: Schematic diagram of ICC.


To reproduce Figure 5, the default parameters are provided in the paper  is used, except for the modifications listed in the section ::ref: `Model Modifications`, Figure 5 can be reproduced with no difference as the original Figure 4 in `Lees-Green, Rachel,  et al (2014)`_.


.. image:: Doc/Figure5.png
     :width: 60%
     :alt: Schematic diagram of ICC.

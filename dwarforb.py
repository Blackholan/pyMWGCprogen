#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import sys
import matplotlib.pyplot as plt
import numpy as np
import time
from math import *
import random


# Debut du decompte du temps  ############################
start_time = time.time()

###############################################################


##### Loading initial conditions for GCs and dwarfs##########################

fname2 = 'dataBattaglia21.txt'
dtype2 = np.dtype([('name', '|S20'),('alpha', 'f8'), ('delta', 'f8'), ('distance', 'f8'), ('mualpha', 'f8'),('emualpha', 'f8'), ('mudelta', 'f8'),('emudelta', 'f8'),('covmu', 'f8') ,('Vlos', 'f8'), ('eVlos', 'f8')])
dataDGs = np.loadtxt(fname2, dtype=dtype2, usecols=(0,1,2,3,4,5,6,7,8,9,10))

AA2 = ['LMC', 'SMC', 'Sgr', 'Fornax', 'Carina', 'Leo II', 'Sextans', 'Sculptor', 'Draco', 'Umi', 'Leo I']

################### Sampling ###################

KR=50

for jj,name in enumerate(AA2):

	print(name)
	Rai2=dataDGs['alpha'][jj]
	Deci2=dataDGs['delta'][jj]

	pmrai2=dataDGs['mualpha'][jj]
	pmdeci2=dataDGs['mudelta'][jj]
	
	epmrai2=dataDGs['emualpha'][jj]
	epmdeci2=dataDGs['emudelta'][jj]
	ecovmu2=dataDGs['covmu'][jj]
	
	mean2 = [pmrai2, pmdeci2]
	cov2 = [[epmrai2*epmrai2,ecovmu2*epmrai2*epmdeci2], [ecovmu2*epmrai2*epmdeci2,epmdeci2*epmdeci2]]
	g2pra2, g2pde2 = np.random.multivariate_normal(mean2, cov2, KR).T
	g2pra2=list(g2pra2)
	g2pde2=list(g2pde2)

	mud2=dataDGs['distance'][jj]
	sigmad2=0.046*mud2
	g1dd2 = np.random.normal(mud2, sigmad2,KR)
	g1dd2=list(g1dd2)

	muv2=dataDGs['Vlos'][jj]
	sigmav2=dataDGs['eVlos'][jj]
	g1dv2= np.random.normal(muv2, sigmav2,KR)
	g1dv2=list(g1dv2)
	
	BBB2=[]
	BBB3=[]
	
	for gg2 in range(0,KR,1):

		di2=random.choice(g1dd2)
		vlosi2=random.choice(g1dv2)
		
		pmrai12=random.choice(g2pra2)
		pmdeci12=random.choice(g2pde2)
		
		g1dv2.remove(vlosi2)
		g1dd2.remove(di2)
		g2pra2.remove(pmrai12)
		g2pde2.remove(pmdeci12)


		BBB3.append([Rai2,Deci2,di2,pmrai12,pmdeci12,vlosi2])
	
	GO=np.array(BBB3)
	np.savetxt('OrbDW/{}ORB.txt'.format(jj),GO, fmt='%s')

	print('done')

	
		
# Affichage du temps d execution
print("Temps d execution : %s secondes ---" % (time.time() - start_time))





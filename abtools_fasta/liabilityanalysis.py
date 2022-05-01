# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 22:34:11 2022
Created by @Kung-Fuzi

Description:
	Analyzes antibody sequence liabilities using the several metrics.
    Len = Total CDR length
    Cys = Unpaired cysteines
    Gly = N-linked glycosylation (NXS/T)
    Met = Methionine oxidation
    Trp = Tryptophan oxidation
    Asn = Asparagine deamidation (NG NS NT)
    Asp = Aspartate isomerization (DG DS DT DD DH)
    Lys = Lysine glycation (KE KD EK ED)
    Glu = N-terminal glutamates
    Int = Integrin binding (RGD, RYD, LDV)
    GPR = CD11c/CD18 binding
    Frg = Fragmentation (DP)
    Hyd = Hydrophobicity
    

Usage:
	python script.py
	
Example:
	python script.py
"""


import re


def Len_liability():
    """Calculates total CDR length"""


def Cys_liability():
    """Predicts unpaired cysteines"""


def Gly_liability(sequence):
    """Predicts N-linked glycosylation"""
    
    glycansites = [site.start() for site in re.finditer(r'N(?=.[ST])',sequence)]








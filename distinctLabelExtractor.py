# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 23:02:38 2019

@author: Sowmya 
updated: Dijiang Huang 4/19/2020
"""

import pandas as pd

# Data file Path
DatasetPath='NSL-KDD/'
# Data file name
dataset_filename='KDDTrain+.txt'

#All attacks in NSL-KDD classed based on their attack classes: DoS, Prob, U2R, and R2L
attacks_subClass = [['apache2', 'back', 'land', 'neptune', 'mailbomb', 'pod', 'processtable', 'smurf', 'teardrop', 'udpstorm', 'worm'], 
     ['ipsweep', 'mscan', 'portsweep', 'saint', 'satan'],
     ['buffer.overflow', 'loadmodule', 'perl', 'ps', 'rootkit', 'sqlattack', 'xterm'],
     ['ftp.write', 'guess.passwd', 'httptunnel', 'imap', 'multihop', 'named', 'phf', 'sendmail', 'snmpgetattack', 'spy', 'snmmpguess', 'warezclient', 'warezserver', 'xlock', 'xsnoop']
     ]

# Four attack classes
expectedAttackClasses = ['DoS (A1)', 'Probe (A2)', 'U2R (A3)', 'R2L (A4)']

# Load data
dataset = pd.read_csv(DatasetPath + dataset_filename, header=None, encoding="ISO-8859-1")

# Read values
evaluator = dataset.iloc[:, :].values

# Initialize empty subClass and currentAttackClasses in the loaded file
subClasses = []
currentAttackClasses = []
attack_class_dict = {}
attack_subclass_dict = {}

# The for loop check if the attack identified, then it update subClasses and currentAttackClasses
for i in range(len(evaluator)):
    subClass = str.lower(evaluator[i, -2])
    if subClass not in subClasses:
        subClasses.append(subClass)
        if subClass not in attack_subclass_dict:
            attack_subclass_dict[subClass] = 0
        for i in range(len(attacks_subClass)):
            if subClass in attacks_subClass[i] and expectedAttackClasses[i] not in currentAttackClasses:
                currentAttackClasses.append(expectedAttackClasses[i])
    current_attack = ''
    for i in range(len(attacks_subClass)):
            if subClass in attacks_subClass[i]:
                 current_attack = expectedAttackClasses[i]
    attack_subclass_dict[subClass] += 1
    if current_attack not in attack_class_dict:
         attack_class_dict[current_attack] = 0
    attack_class_dict[current_attack] += 1

# Print finding results:
print("\nSub classes of Attacks")
print(subClasses)
# print(attack_subclass_dict)
print("\n\nAttack Classes")
print(currentAttackClasses)
print(attack_class_dict)

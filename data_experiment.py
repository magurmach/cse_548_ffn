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

class_to_type_dict = {}
class_to_type_dict['normal'] = 'normal'

for i in range(4):
    for j in attacks_subClass[i]:
        class_to_type_dict[j] = expectedAttackClasses[i]

# Load data
dataset = pd.read_csv(DatasetPath + dataset_filename, header=None, encoding="ISO-8859-1")

dataset[42] = dataset[41]
dataset[42] = dataset[42].replace(class_to_type_dict)

dataset_dos = dataset[dataset[42] == 'DoS (A1)']
dataset_probe = dataset[dataset[42] == 'Probe (A2)']
dataset_u2r = dataset[dataset[42] == 'U2R (A3)']
dataset_r2l = dataset[dataset[42] == 'R2L (A4)']

print(len(dataset_dos), len(dataset_probe), len(dataset_u2r), len(dataset_r2l))


# dataset_dos.groupby(0).plot(kind='hist', edgecolor='black')

print(dataset_dos[1].value_counts(normalize=True))
print(dataset_u2r[1].value_counts(normalize=True))

# print(dataset_dos[2].value_counts(normalize=True))
# print(dataset_probe[2].value_counts(normalize=True))

print(dataset_dos[3].value_counts(normalize=True))
print(dataset_u2r[3].value_counts(normalize=True))

# print(dataset_dos[2].unique(), dataset_probe[2].unique())
# print(dataset_dos[3].unique(), dataset_probe[3].unique())

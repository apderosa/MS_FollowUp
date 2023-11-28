import numpy as np
import pandas as pd

clinical = pd.read_excel('clin_feat.xlsx')
anatomical = pd.read_excel('anat_feat.xlsx')

clinical_features = clinical[['age', 'sex_coded', 'disease_duration', 'education', 'EDSS']]
anatomical_features = anatomical.filter(regex='.N*V').drop(['NGMV', 'NBV'], axis=1)

sdmt_BS = clinical[['SDMT_Z']]
sdmt_FU = clinical[['SDMT_Z_FU']]

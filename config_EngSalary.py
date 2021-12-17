#Variables categóricas
CATEGORICAL_VARS = ['10board', '12board', 'Specialization', 'CollegeState', 'CollegeID', 'Gender', 'Degree']

#Variables numéricas
NUMERICAL_VARS = ['10percentage',
 '12percentage',
 'CollegeTier',
 'collegeGPA',
 'CollegeCityTier',
 'English',
 'Logical',
 'Quant',
 'Domain',
 'ComputerProgramming',
 'ElectronicsAndSemicon',
 'ComputerScience',
 'MechanicalEngg',
 'ElectricalEngg',
 'TelecomEngg',
 'CivilEngg',
 'conscientiousness',
 'agreeableness',
 'extraversion',
 'nueroticism',
 'openess_to_experience']

#Variables con etiquetas raras
RARE_LABEL_VARS = ['10board', '12board', 'Specialization', 'CollegeState', 'CollegeID']

#Variables para binarizar por sesgo fuerte
BINARIZE_VARS = ['ElectronicsAndSemicon', 'MechanicalEngg', 'ElectricalEngg', 'TelecomEngg']

#Variables para aplicar transformación Yeo Johnson
YEOJOHNSON_VARS = ['10percentage', '12percentage', 'collegeGPA', 'English', 'Logical', 'Quant', 'Domain', 'conscientiousness', 'agreeableness', 'extraversion', 'nueroticism', 'openess_to_experience']

#Variables de temporalidad
TEMPORAL_VARS = ['12graduation', 'GraduationYear']

REF_VAR = 'DOB'

#Variable a eliminar
DROP_FEATURES = ['DOB']

#Variables a utilizar en el modelo
FEATURES = ['Gender',
 'DOB',
 '10percentage',
 '10board',
 '12graduation',
 '12percentage',
 '12board',
 'CollegeID',
 'CollegeTier',
 'Degree',
 'Specialization',
 'collegeGPA',
 'CollegeCityTier',
 'CollegeState',
 'GraduationYear',
 'English',
 'Logical',
 'Quant',
 'Domain',
 'ComputerProgramming',
 'ElectronicsAndSemicon',
 'ComputerScience',
 'MechanicalEngg',
 'ElectricalEngg',
 'TelecomEngg',
 'CivilEngg',
 'conscientiousness',
 'agreeableness',
 'extraversion',
 'nueroticism',
 'openess_to_experience']
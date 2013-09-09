from vec import Vec
from matutil import rowdict2mat

def read_training_data(fname, features=None):
    """Given a file in appropriate format,
    returns the triple (feature_vectors, patient_diagnoses, D)
    feature_vectors is a dictionary that maps integer patient identification numbers to
    D-vectors where D is the set of feature labels,
    and patient_diagnoses is a dictionary mapping patient identification numbers to
    {+1, -1}, where +1 indicates malignant and -1 indicates benign.
    """
    file = open(fname)
    params = ["radius", "texture", "perimeter","area","smoothness","compactness","concavity","concave points","symmetry","fractal dimension"];
    stats = ["(mean)", "(stderr)", "(worst)"]
    feature_labels = set([y+x for x in stats for y in params])
    feature_map = {params[i]+stats[j]:j*len(params)+i for i in range(len(params)) for j in range(len(stats))}
    if features is None: features = feature_labels
    feature_vectors = {}
    patient_diagnoses = {}
    for line in file:
        row = line.split(",")
        patient_ID = int(row[0])
        patient_diagnoses[patient_ID] = -1 if row[1]=='B' else +1
        feature_vectors[patient_ID] = Vec(features, {f:float(row[feature_map[f]+2]) for f in features})
    return rowdict2mat(feature_vectors), Vec(set(patient_diagnoses.keys()), patient_diagnoses)

def read_unclassified_data(fname):
    return read_training_data(fname)[0]


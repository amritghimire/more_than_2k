#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 147


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.rf.dense',
                  'featurize.preset.max_features',
                  'featurize.preset.split',
                  'featurize.prod.max_depth',
                  'featurize.long.seed',
                  'featurize.classifier.seed',
                  'featurize.diff.folds',
                  'featurize.long.split',
                  'featurize.diff.columns',
                  'featurize.classifier.folds',
                  'featurize.classifier.min_features',
                  'featurize.long.threads',
                  'featurize.prod.layers',
                  'featurize.prod.threads',
                  'featurize.classifier.threads',
                  'featurize.long.min_features',
                  'featurize.preset.tags',
                  'featurize.preset.weight_factor',
                  'featurize.diff.num_est',
                  'featurize.rf.columns',
                  'featurize.diff.seed',
                  'featurize.classifier.epochs',
                  'featurize.prod.split',
                  'featurize.rf.max_features',
                  'featurize.rf.drop',
                  'featurize.preset.learning_rate',
                  'featurize.other.drop',
                  'featurize.other.learning_rate',
                  'featurize.rf.num_est',
                  'featurize.prod.epochs',
                  'featurize.preset.max_depth',
                  'featurize.prod.min_split',
                  'featurize.rf.batch_size',
                  'featurize.prod.features',
                  'featurize.prod.min_features',
                  'featurize.rf.trees']}]

params_values = {}
for rec in used_params:
    for fname, pnames in rec.items():
        with open(fname, 'r') as fd:
            params = yaml.safe_load(fd)

        for name in pnames:
            params_values[f"{fname}:{name}"] = get_in(params, name.split("."))


def get_param_value(name, default=None):
    return next((v for k, v in params_values.items() if k.endswith("." + name)), default)

def set_random_seed():
    random.seed(get_param_value("seed", 1234))

# A generic fake featurize script. Saves params amd "work" as json.
# Params might affect result in any way, work will improve metrics.
assert len(sys.argv) == 3, "Expected argv: featurize.py in out"

with open(sys.argv[2], "w") as feat:
    data_size = os.stat(sys.argv[1]).st_size
    json.dump({"params": params_values, "work": [math.log(data_size + 1), VERSION]}, feat)

# Comment to update:0061942493366
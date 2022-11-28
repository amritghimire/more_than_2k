#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 96


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.classifier.threads',
                  'featurize.dev.epochs',
                  'featurize.batch.batch_size',
                  'featurize.dev.ngrams',
                  'featurize.dev.tags',
                  'featurize.dev.features',
                  'featurize.requests.sample',
                  'featurize.selection.columns',
                  'featurize.rf.passes',
                  'featurize.classifier.folds',
                  'featurize.rf.weight_factor',
                  'featurize.rf.max_features',
                  'featurize.rf.tags',
                  'featurize.rf.random_state',
                  'featurize.rf.min_features',
                  'featurize.classifier.num_est',
                  'featurize.batch.threads',
                  'featurize.requests.num_est',
                  'featurize.classifier.max_depth',
                  'featurize.rf.learning_rate',
                  'featurize.selection.passes',
                  'featurize.selection.threads',
                  'featurize.batch.weight_factor',
                  'featurize.dev.passes',
                  'featurize.classifier.batch_size',
                  'featurize.requests.threads',
                  'featurize.other.dense',
                  'featurize.rf.layers',
                  'featurize.classifier.max_features',
                  'featurize.batch.max_features',
                  'featurize.dev.seed']}]

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

# Comment to update:1278411730562
#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 77


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.preprocessing.estimators',
                  'featurize.test.trees',
                  'featurize.model.random_state',
                  'featurize.combine.weight_factor',
                  'featurize.other.trees',
                  'featurize.combine.features',
                  'featurize.preprocessing.epochs',
                  'featurize.combine.min_split',
                  'featurize.other.random_state',
                  'featurize.dev.num_est',
                  'featurize.preprocessing.trees',
                  'featurize.test.min_split',
                  'featurize.dev.sample',
                  'featurize.other.passes',
                  'featurize.other.estimators',
                  'featurize.model.batch_size',
                  'featurize.model.tags',
                  'featurize.combine.trees',
                  'featurize.concurrent.seed',
                  'featurize.model.passes',
                  'featurize.combine.estimators',
                  'featurize.combine.columns',
                  'featurize.model.folds',
                  'featurize.concurrent.num_est',
                  'featurize.other.batch_size',
                  'featurize.model.split',
                  'featurize.preprocessing.columns',
                  'featurize.model.columns',
                  'featurize.other.drop',
                  'featurize.combine.tags',
                  'featurize.preprocessing.min_features',
                  'featurize.preprocessing.max_features',
                  'featurize.combine.threads',
                  'featurize.concurrent.max_features']}]

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

# Comment to update:30576366
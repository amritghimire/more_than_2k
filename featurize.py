#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 45


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.binary.features',
                  'featurize.long.ngrams',
                  'featurize.preset.estimators',
                  'featurize.dev.min_split',
                  'featurize.dev.trees',
                  'featurize.rf.folds',
                  'featurize.long.tags',
                  'featurize.binary.passes',
                  'featurize.preset.max_features',
                  'featurize.preset.passes',
                  'featurize.short.trees',
                  'featurize.binary.drop',
                  'featurize.long.folds',
                  'featurize.long.seed',
                  'featurize.binary.estimators',
                  'featurize.batch.ngrams',
                  'featurize.dev.sample',
                  'featurize.binary.ngrams',
                  'featurize.long.sample',
                  'featurize.long.epochs',
                  'featurize.binary.tags',
                  'featurize.dev.seed',
                  'featurize.dev.min_features',
                  'featurize.dev.batch_size',
                  'featurize.long.max_features',
                  'featurize.short.threads']}]

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

# Comment to update:4810046
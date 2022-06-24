#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 162


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.other.layers',
                  'featurize.short.min_features',
                  'featurize.diff.estimators',
                  'featurize.long.tags',
                  'featurize.long.min_features',
                  'featurize.short.layers',
                  'featurize.other.passes',
                  'featurize.short.max_depth',
                  'featurize.long.learning_rate',
                  'featurize.other.weight_factor',
                  'featurize.diff.layers',
                  'featurize.long.folds',
                  'featurize.long.random_state',
                  'featurize.short.num_est',
                  'featurize.other.drop',
                  'featurize.diff.max_depth',
                  'featurize.auto.max_features',
                  'featurize.combine.batch_size',
                  'featurize.short.estimators',
                  'featurize.other.max_features',
                  'featurize.auto.ngrams',
                  'featurize.combine.sample',
                  'featurize.diff.max_features',
                  'featurize.combine.max_depth',
                  'featurize.short.dense',
                  'featurize.other.tags',
                  'featurize.combine.max_features',
                  'featurize.short.epochs',
                  'featurize.short.columns']}]

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

# Comment to update:054724576983566881
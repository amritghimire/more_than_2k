#!/usr/bin/env python3
import os, sys, json, math
import random

VERSION = 57


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['featurize.combine.dense',
                  'featurize.prod.seed',
                  'featurize.prod.trees',
                  'featurize.classifier.num_est',
                  'featurize.preset.folds',
                  'featurize.prod.dense',
                  'featurize.requests.weight_factor',
                  'featurize.auto.drop',
                  'featurize.preset.min_features',
                  'featurize.requests.split',
                  'featurize.requests.passes',
                  'featurize.preset.layers',
                  'featurize.combine.num_est',
                  'featurize.prod.random_state',
                  'featurize.batch.seed',
                  'featurize.classifier.columns',
                  'featurize.prod.max_depth',
                  'featurize.prod.split',
                  'featurize.batch.tags',
                  'featurize.auto.min_features',
                  'featurize.classifier.trees',
                  'featurize.prod.threads',
                  'featurize.auto.trees',
                  'featurize.batch.split',
                  'featurize.auto.passes',
                  'featurize.auto.dense',
                  'featurize.requests.layers',
                  'featurize.classifier.folds',
                  'featurize.classifier.threads']}]

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

# Comment to update:191627709331872878
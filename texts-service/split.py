#!/usr/bin/env python3
# A train test split generic script
import sys, random
import random

VERSION = 1


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['prepare.test.num_est',
                  'prepare.test.sample',
                  'prepare.preset.max_depth',
                  'prepare.preset.seed',
                  'prepare.requests.passes',
                  'prepare.preset.folds',
                  'prepare.long.trees',
                  'prepare.test.trees',
                  'prepare.combine.dense',
                  'prepare.test.features',
                  'prepare.combine.weight_factor',
                  'prepare.combine.folds',
                  'prepare.long.features',
                  'prepare.other.random_state',
                  'prepare.diff.epochs',
                  'prepare.long.dense',
                  'prepare.test.columns',
                  'prepare.preset.estimators',
                  'prepare.preset.dense',
                  'prepare.other.trees',
                  'prepare.preset.learning_rate',
                  'prepare.long.sample',
                  'prepare.other.split',
                  'prepare.combine.features',
                  'prepare.combine.split',
                  'prepare.combine.learning_rate',
                  'prepare.requests.epochs',
                  'prepare.long.max_depth',
                  'prepare.long.epochs',
                  'prepare.preset.min_features',
                  'prepare.requests.weight_factor',
                  'prepare.requests.random_state',
                  'prepare.long.weight_factor',
                  'prepare.diff.estimators']}]

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

assert len(sys.argv) == 4, "Expected argv: split.py in out.train out.test"

set_random_seed()
split = get_param_value("split") or 0.2

with open(sys.argv[1]) as raw, open(sys.argv[2], "w") as train, open(sys.argv[3], "w") as test:
    for line in raw:
        if random.random() < split:
            test.write(line)
        else:
            train.write(line)

# Comment to update:52018388100
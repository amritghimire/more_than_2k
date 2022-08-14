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

used_params = [{'params.yaml': ['prepare.concurrent.threads',
                  'prepare.concurrent.split',
                  'prepare.preprocessing.min_features',
                  'prepare.model.estimators',
                  'prepare.combine.weight_factor',
                  'prepare.preprocessing.drop',
                  'prepare.test.weight_factor',
                  'prepare.preprocessing.batch_size',
                  'prepare.concurrent.max_depth',
                  'prepare.other.max_depth',
                  'prepare.other.split',
                  'prepare.model.num_est',
                  'prepare.test.passes',
                  'prepare.concurrent.drop',
                  'prepare.dev.ngrams',
                  'prepare.preprocessing.weight_factor',
                  'prepare.dev.batch_size',
                  'prepare.preprocessing.split',
                  'prepare.combine.passes',
                  'prepare.dev.min_features',
                  'prepare.combine.ngrams',
                  'prepare.other.max_features',
                  'prepare.other.ngrams',
                  'prepare.model.split',
                  'prepare.dev.epochs',
                  'prepare.preprocessing.seed',
                  'prepare.concurrent.dense',
                  'prepare.model.features',
                  'prepare.dev.split',
                  'prepare.dev.columns',
                  'prepare.preprocessing.max_depth',
                  'prepare.combine.layers',
                  'prepare.combine.num_est',
                  'prepare.concurrent.weight_factor',
                  'prepare.combine.max_depth',
                  'prepare.other.num_est',
                  'prepare.test.min_split',
                  'prepare.other.columns',
                  'prepare.dev.seed',
                  'prepare.test.threads',
                  'prepare.other.dense',
                  'prepare.model.min_split']}]

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

# Comment to update:447164
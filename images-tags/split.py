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

used_params = [{'params.yaml': ['prepare.preset.min_split',
                  'prepare.prod.estimators',
                  'prepare.rf.ngrams',
                  'prepare.long.min_split',
                  'prepare.long.columns',
                  'prepare.other.sample',
                  'prepare.rf.epochs',
                  'prepare.other.drop',
                  'prepare.preset.trees',
                  'prepare.other.columns',
                  'prepare.prod.seed',
                  'prepare.other.split',
                  'prepare.long.sample',
                  'prepare.classifier.weight_factor',
                  'prepare.prod.split',
                  'prepare.long.random_state',
                  'prepare.diff.learning_rate',
                  'prepare.long.layers',
                  'prepare.diff.max_depth',
                  'prepare.prod.batch_size',
                  'prepare.prod.threads',
                  'prepare.long.features',
                  'prepare.preset.seed',
                  'prepare.classifier.dense',
                  'prepare.diff.split',
                  'prepare.other.batch_size',
                  'prepare.diff.min_features',
                  'prepare.other.random_state',
                  'prepare.classifier.tags',
                  'prepare.prod.min_split']}]

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

# Comment to update:8331586
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

used_params = [{'params.yaml': ['prepare.batch.learning_rate',
                  'prepare.rf.num_est',
                  'prepare.batch.ngrams',
                  'prepare.requests.split',
                  'prepare.rf.passes',
                  'prepare.dev.columns',
                  'prepare.batch.min_split',
                  'prepare.classifier.columns',
                  'prepare.other.num_est',
                  'prepare.batch.features',
                  'prepare.dev.seed',
                  'prepare.dev.weight_factor',
                  'prepare.dev.sample',
                  'prepare.rf.layers',
                  'prepare.requests.folds',
                  'prepare.other.features',
                  'prepare.rf.epochs',
                  'prepare.dev.epochs',
                  'prepare.other.drop',
                  'prepare.dev.trees',
                  'prepare.other.epochs',
                  'prepare.selection.split',
                  'prepare.selection.layers',
                  'prepare.selection.ngrams',
                  'prepare.dev.batch_size',
                  'prepare.classifier.split',
                  'prepare.rf.columns',
                  'prepare.selection.seed',
                  'prepare.rf.random_state',
                  'prepare.dev.features',
                  'prepare.classifier.features',
                  'prepare.batch.split',
                  'prepare.selection.features',
                  'prepare.dev.max_features',
                  'prepare.other.folds',
                  'prepare.requests.features',
                  'prepare.other.ngrams',
                  'prepare.selection.passes',
                  'prepare.dev.tags']}]

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

# Comment to update:49912433657
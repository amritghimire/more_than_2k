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

used_params = [{'params.yaml': ['prepare.short.num_est',
                  'prepare.preset.trees',
                  'prepare.combine.passes',
                  'prepare.combine.min_features',
                  'prepare.diff.tags',
                  'prepare.long.columns',
                  'prepare.diff.trees',
                  'prepare.auto.num_est',
                  'prepare.short.weight_factor',
                  'prepare.preset.split',
                  'prepare.combine.sample',
                  'prepare.short.sample',
                  'prepare.long.trees',
                  'prepare.short.learning_rate',
                  'prepare.other.tags',
                  'prepare.preset.columns',
                  'prepare.short.split',
                  'prepare.combine.trees',
                  'prepare.diff.layers',
                  'prepare.other.split',
                  'prepare.preset.passes',
                  'prepare.other.dense',
                  'prepare.other.random_state',
                  'prepare.diff.passes',
                  'prepare.combine.num_est',
                  'prepare.auto.min_split',
                  'prepare.diff.dense',
                  'prepare.preset.batch_size',
                  'prepare.other.learning_rate',
                  'prepare.preset.tags',
                  'prepare.auto.passes',
                  'prepare.diff.max_features',
                  'prepare.combine.tags',
                  'prepare.short.layers',
                  'prepare.short.trees',
                  'prepare.other.layers']}]

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

# Comment to update:01832389084348416201301
#!/usr/bin/env python3
import sys, json
import random

VERSION = 68


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['settings.max_depth',
                  'concurrent.weight_factor',
                  'settings.epochs',
                  'concurrent.sample',
                  'variables.min_features',
                  'concurrent.ngrams',
                  'settings.tags',
                  'tagging.drop',
                  'concurrent.min_split',
                  'concurrent.num_est',
                  'concurrent.drop',
                  'tagging.ngrams',
                  'tagging.threads',
                  'settings.min_features',
                  'tagging.num_est',
                  'variables.learning_rate',
                  'tagging.batch_size',
                  'variables.columns',
                  'settings.threads',
                  'variables.estimators',
                  'concurrent.random_state',
                  'tagging.layers',
                  'concurrent.threads',
                  'tagging.estimators',
                  'concurrent.passes',
                  'variables.max_depth',
                  'tagging.folds',
                  'tagging.weight_factor',
                  'concurrent.tags',
                  'concurrent.features',
                  'variables.seed',
                  'tagging.columns',
                  'concurrent.folds',
                  'variables.passes',
                  'settings.estimators',
                  'tagging.trees',
                  'concurrent.dense',
                  'tagging.learning_rate',
                  'settings.num_est',
                  'variables.random_state',
                  'settings.ngrams',
                  'tagging.seed',
                  'concurrent.trees',
                  'variables.sample',
                  'variables.tags',
                  'variables.min_split',
                  'tagging.dense',
                  'concurrent.columns',
                  'settings.max_features',
                  'variables.num_est',
                  'variables.folds',
                  'settings.seed',
                  'settings.batch_size',
                  'concurrent.epochs',
                  'settings.dense',
                  'variables.dense',
                  'tagging.max_depth',
                  'settings.passes',
                  'tagging.min_features',
                  'variables.split',
                  'variables.batch_size',
                  'settings.columns',
                  'settings.random_state',
                  'concurrent.learning_rate',
                  'tagging.sample',
                  'settings.trees',
                  'variables.features',
                  'settings.min_split',
                  'variables.max_features',
                  'concurrent.max_features',
                  'variables.ngrams',
                  'variables.layers',
                  'concurrent.min_features',
                  'concurrent.seed',
                  'variables.drop',
                  'settings.split',
                  'tagging.tags',
                  'tagging.epochs',
                  'concurrent.batch_size',
                  'settings.drop',
                  'concurrent.estimators',
                  'tagging.features',
                  'settings.layers']}]

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

# A train generic fake script, simply add train params and "work" to the data
assert len(sys.argv) == 3, "Expected argv: train.py in model"

with open(sys.argv[1]) as fd, open(sys.argv[2], "w") as model:
    data = json.load(fd)
    data["params"].update(params_values)
    data["work"].append(VERSION)
    json.dump(data, model)

# Comment to update:272995487460531067
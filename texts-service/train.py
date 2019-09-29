#!/usr/bin/env python3
import sys, json
import random

VERSION = 48


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['settings.preset.epochs',
                  'concurrent.long.num_est',
                  'model.combine.min_features',
                  'concurrent.test.ngrams',
                  'settings.requests.batch_size',
                  'model.preset.columns',
                  'model.diff.split',
                  'variables.preset.weight_factor',
                  'model.combine.max_depth',
                  'variables.long.estimators',
                  'preprocessing.requests.num_est',
                  'preprocessing.preset.features',
                  'settings.test.random_state',
                  'variables.test.threads',
                  'variables.diff.split',
                  'settings.combine.max_features',
                  'preprocessing.combine.sample',
                  'preprocessing.combine.learning_rate',
                  'preprocessing.requests.weight_factor',
                  'concurrent.requests.learning_rate',
                  'model.long.learning_rate',
                  'variables.requests.num_est',
                  'concurrent.diff.trees',
                  'model.combine.sample',
                  'model.diff.seed',
                  'preprocessing.combine.weight_factor',
                  'model.other.sample',
                  'concurrent.long.batch_size',
                  'settings.preset.min_features',
                  'concurrent.long.sample',
                  'variables.preset.epochs',
                  'concurrent.preset.sample',
                  'preprocessing.other.min_split',
                  'variables.combine.sample',
                  'model.test.min_split',
                  'variables.requests.random_state',
                  'tagging.other.batch_size',
                  'concurrent.requests.max_features',
                  'preprocessing.combine.max_features',
                  'variables.diff.min_split',
                  'preprocessing.other.epochs',
                  'tagging.requests.max_depth',
                  'tagging.diff.epochs',
                  'settings.other.learning_rate',
                  'settings.requests.min_split',
                  'model.other.max_depth',
                  'tagging.other.features',
                  'concurrent.diff.tags',
                  'preprocessing.diff.weight_factor',
                  'model.test.min_features',
                  'model.requests.estimators',
                  'tagging.diff.layers',
                  'concurrent.diff.max_depth',
                  'settings.other.seed',
                  'settings.combine.min_split',
                  'settings.diff.max_depth',
                  'concurrent.long.random_state',
                  'variables.diff.max_features',
                  'tagging.long.columns',
                  'preprocessing.test.layers',
                  'model.requests.min_features',
                  'concurrent.long.split',
                  'model.test.threads',
                  'model.other.weight_factor',
                  'preprocessing.other.features',
                  'concurrent.test.weight_factor',
                  'tagging.diff.ngrams',
                  'variables.preset.seed',
                  'tagging.preset.split',
                  'settings.test.learning_rate',
                  'concurrent.diff.columns',
                  'tagging.long.estimators',
                  'variables.preset.trees',
                  'preprocessing.combine.features',
                  'preprocessing.requests.folds',
                  'settings.requests.layers',
                  'tagging.test.folds',
                  'model.long.sample',
                  'tagging.test.epochs',
                  'preprocessing.test.drop',
                  'variables.other.passes',
                  'variables.preset.ngrams',
                  'concurrent.diff.seed',
                  'concurrent.test.estimators',
                  'settings.test.layers',
                  'variables.test.layers',
                  'concurrent.requests.features',
                  'concurrent.long.min_split',
                  'model.other.min_split',
                  'concurrent.other.tags',
                  'settings.other.min_split',
                  'preprocessing.long.drop',
                  'tagging.diff.threads',
                  'model.other.batch_size',
                  'concurrent.test.dense',
                  'model.diff.num_est',
                  'preprocessing.test.seed',
                  'variables.combine.features',
                  'settings.preset.folds',
                  'tagging.long.max_depth',
                  'preprocessing.other.weight_factor',
                  'tagging.preset.min_features',
                  'tagging.preset.min_split',
                  'settings.combine.estimators',
                  'tagging.diff.max_features',
                  'tagging.requests.num_est',
                  'settings.combine.batch_size',
                  'variables.other.columns',
                  'preprocessing.combine.min_features',
                  'settings.combine.learning_rate',
                  'preprocessing.test.features',
                  'settings.other.trees',
                  'model.combine.estimators',
                  'tagging.requests.max_features',
                  'settings.preset.num_est',
                  'settings.test.drop',
                  'concurrent.requests.num_est',
                  'variables.long.tags',
                  'model.long.columns',
                  'settings.diff.random_state',
                  'model.combine.features',
                  'concurrent.long.dense',
                  'preprocessing.requests.min_split',
                  'tagging.test.max_depth',
                  'settings.other.max_features',
                  'concurrent.test.random_state',
                  'model.combine.split',
                  'settings.preset.drop',
                  'tagging.other.layers',
                  'model.test.max_features',
                  'settings.requests.threads',
                  'model.requests.trees',
                  'preprocessing.preset.sample',
                  'preprocessing.diff.sample',
                  'settings.long.sample',
                  'tagging.test.sample',
                  'preprocessing.preset.max_features',
                  'model.test.folds',
                  'variables.combine.dense',
                  'settings.diff.columns',
                  'settings.preset.features',
                  'preprocessing.other.tags',
                  'settings.diff.weight_factor',
                  'model.test.seed',
                  'concurrent.test.passes',
                  'model.other.threads',
                  'variables.combine.min_features',
                  'model.requests.sample',
                  'model.other.split',
                  'model.long.split',
                  'variables.other.learning_rate',
                  'preprocessing.preset.seed',
                  'preprocessing.other.columns',
                  'tagging.combine.min_split',
                  'preprocessing.diff.min_split',
                  'preprocessing.long.passes',
                  'variables.other.split',
                  'variables.other.random_state',
                  'tagging.requests.epochs',
                  'tagging.combine.estimators',
                  'model.requests.drop',
                  'concurrent.test.min_split',
                  'model.other.ngrams',
                  'model.combine.layers',
                  'preprocessing.requests.sample',
                  'concurrent.diff.sample',
                  'settings.long.folds',
                  'preprocessing.combine.folds',
                  'concurrent.test.features',
                  'tagging.requests.columns',
                  'model.diff.learning_rate',
                  'settings.requests.num_est',
                  'preprocessing.preset.folds',
                  'settings.preset.random_state',
                  'concurrent.test.trees',
                  'variables.test.passes',
                  'settings.test.max_features',
                  'model.diff.estimators',
                  'model.test.split',
                  'preprocessing.test.passes',
                  'tagging.requests.trees',
                  'variables.long.weight_factor',
                  'concurrent.long.ngrams',
                  'settings.preset.tags',
                  'variables.test.sample',
                  'concurrent.requests.columns',
                  'preprocessing.test.tags',
                  'settings.preset.dense',
                  'preprocessing.long.tags',
                  'settings.requests.random_state',
                  'variables.diff.tags',
                  'preprocessing.preset.threads',
                  'settings.requests.max_features',
                  'model.test.sample',
                  'preprocessing.diff.max_features',
                  'model.preset.folds',
                  'concurrent.preset.features',
                  'concurrent.preset.weight_factor',
                  'model.preset.passes',
                  'concurrent.test.folds',
                  'concurrent.requests.split',
                  'settings.preset.weight_factor',
                  'concurrent.other.max_depth',
                  'concurrent.test.num_est',
                  'model.other.passes',
                  'tagging.other.seed',
                  'settings.combine.epochs',
                  'tagging.test.drop',
                  'tagging.combine.batch_size',
                  'variables.test.dense',
                  'preprocessing.combine.split',
                  'model.diff.features',
                  'model.long.max_features',
                  'tagging.long.seed',
                  'concurrent.preset.seed',
                  'tagging.other.max_features',
                  'concurrent.preset.learning_rate',
                  'tagging.test.estimators',
                  'tagging.combine.passes',
                  'settings.requests.estimators',
                  'concurrent.long.folds',
                  'preprocessing.combine.max_depth',
                  'variables.long.max_features',
                  'tagging.test.seed',
                  'tagging.long.drop',
                  'concurrent.preset.passes',
                  'tagging.combine.folds',
                  'model.other.learning_rate',
                  'preprocessing.combine.min_split',
                  'preprocessing.long.features',
                  'concurrent.long.max_depth',
                  'model.combine.drop',
                  'variables.other.drop',
                  'concurrent.requests.estimators',
                  'preprocessing.diff.random_state',
                  'variables.diff.max_depth',
                  'preprocessing.other.estimators',
                  'tagging.diff.random_state',
                  'concurrent.combine.epochs',
                  'model.preset.max_depth',
                  'model.long.random_state',
                  'concurrent.preset.layers']}]

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

# Comment to update:8137
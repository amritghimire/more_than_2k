#!/usr/bin/env python3
import sys, json
import random

VERSION = 138


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['model.preset.batch_size',
                  'settings.long.min_split',
                  'settings.short.max_depth',
                  'concurrent.long.seed',
                  'settings.combine.epochs',
                  'concurrent.auto.batch_size',
                  'train.auto.epochs',
                  'concurrent.other.min_features',
                  'concurrent.preset.max_depth',
                  'settings.long.num_est',
                  'variables.other.drop',
                  'concurrent.auto.random_state',
                  'settings.preset.learning_rate',
                  'model.other.estimators',
                  'train.other.columns',
                  'train.diff.dense',
                  'concurrent.preset.num_est',
                  'variables.other.dense',
                  'concurrent.combine.trees',
                  'model.combine.tags',
                  'concurrent.other.max_features',
                  'train.combine.threads',
                  'variables.short.min_features',
                  'train.diff.learning_rate',
                  'model.long.passes',
                  'concurrent.other.min_split',
                  'variables.combine.num_est',
                  'model.diff.estimators',
                  'settings.other.max_depth',
                  'model.long.trees',
                  'train.preset.learning_rate',
                  'settings.other.max_features',
                  'concurrent.combine.dense',
                  'variables.short.weight_factor',
                  'train.other.trees',
                  'model.other.sample',
                  'concurrent.other.batch_size',
                  'model.short.num_est',
                  'variables.long.estimators',
                  'settings.short.ngrams',
                  'variables.auto.tags',
                  'concurrent.other.seed',
                  'concurrent.short.sample',
                  'train.diff.ngrams',
                  'model.other.min_features',
                  'settings.diff.folds',
                  'model.auto.epochs',
                  'variables.short.tags',
                  'variables.short.trees',
                  'model.other.columns',
                  'model.combine.min_features',
                  'model.long.learning_rate',
                  'settings.preset.epochs',
                  'concurrent.combine.drop',
                  'train.combine.ngrams',
                  'settings.long.drop',
                  'concurrent.other.learning_rate',
                  'variables.auto.layers',
                  'concurrent.short.columns',
                  'settings.short.random_state',
                  'model.long.ngrams',
                  'variables.combine.tags',
                  'variables.preset.estimators',
                  'train.combine.min_split',
                  'train.combine.seed',
                  'model.short.seed',
                  'model.diff.threads',
                  'settings.other.tags',
                  'concurrent.preset.estimators',
                  'concurrent.combine.split',
                  'settings.combine.weight_factor',
                  'model.long.estimators',
                  'variables.combine.random_state',
                  'model.long.folds',
                  'settings.other.random_state',
                  'settings.short.passes',
                  'variables.other.weight_factor',
                  'settings.long.epochs',
                  'concurrent.diff.weight_factor',
                  'variables.diff.sample',
                  'model.short.dense',
                  'variables.diff.epochs',
                  'model.diff.num_est',
                  'concurrent.combine.weight_factor',
                  'train.other.epochs',
                  'model.short.batch_size',
                  'model.auto.layers',
                  'train.diff.tags',
                  'model.other.layers',
                  'model.diff.epochs',
                  'settings.combine.folds',
                  'settings.long.passes',
                  'settings.auto.weight_factor',
                  'train.short.columns',
                  'model.long.columns',
                  'concurrent.other.layers',
                  'model.combine.threads',
                  'settings.other.trees',
                  'concurrent.diff.random_state',
                  'train.diff.batch_size',
                  'variables.auto.dense',
                  'variables.other.seed',
                  'concurrent.preset.columns',
                  'concurrent.combine.min_features',
                  'settings.short.columns',
                  'model.long.min_split',
                  'settings.combine.min_split',
                  'settings.other.estimators',
                  'train.combine.split',
                  'train.combine.sample',
                  'variables.other.layers',
                  'train.auto.columns',
                  'train.combine.estimators',
                  'concurrent.preset.ngrams',
                  'variables.combine.learning_rate',
                  'settings.diff.sample',
                  'model.combine.estimators',
                  'concurrent.other.tags',
                  'train.other.sample',
                  'train.long.random_state',
                  'concurrent.other.threads',
                  'model.diff.max_depth',
                  'model.short.tags',
                  'variables.long.weight_factor',
                  'variables.preset.min_features',
                  'concurrent.long.weight_factor',
                  'variables.long.tags',
                  'concurrent.other.passes',
                  'train.short.num_est',
                  'settings.other.passes',
                  'settings.diff.columns',
                  'train.preset.features',
                  'settings.long.folds',
                  'train.diff.estimators',
                  'model.short.random_state',
                  'concurrent.combine.min_split',
                  'concurrent.auto.features',
                  'concurrent.preset.folds',
                  'train.other.drop',
                  'model.long.threads',
                  'concurrent.short.seed',
                  'variables.short.num_est',
                  'train.diff.random_state',
                  'settings.auto.tags',
                  'variables.short.learning_rate',
                  'train.diff.max_features',
                  'settings.diff.epochs',
                  'train.other.tags',
                  'concurrent.diff.folds',
                  'variables.short.folds',
                  'variables.short.seed',
                  'train.short.folds',
                  'train.other.estimators',
                  'train.diff.epochs',
                  'variables.combine.epochs',
                  'concurrent.auto.tags',
                  'variables.long.min_features',
                  'train.auto.sample',
                  'train.preset.drop',
                  'train.diff.features',
                  'variables.auto.max_depth',
                  'concurrent.diff.layers',
                  'variables.diff.ngrams',
                  'train.long.seed',
                  'settings.diff.min_split',
                  'model.combine.drop',
                  'model.short.split',
                  'model.combine.columns',
                  'settings.combine.split',
                  'model.auto.max_features']}]

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

# Comment to update:46378393592024392747832870
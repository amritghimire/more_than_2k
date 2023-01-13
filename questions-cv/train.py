#!/usr/bin/env python3
import sys, json
import random

VERSION = 144


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['concurrent.batch.tags',
                  'model.collection.tags',
                  'concurrent.short.max_features',
                  'validation.prod.layers',
                  'preprocessing.collection.sample',
                  'model.rf.ngrams',
                  'model.other.random_state',
                  'validation.collection.passes',
                  'variables.short.min_features',
                  'concurrent.selection.random_state',
                  'variables.batch.epochs',
                  'concurrent.rf.weight_factor',
                  'validation.rf.ngrams',
                  'validation.short.max_depth',
                  'validation.other.learning_rate',
                  'settings.selection.dense',
                  'preprocessing.rf.tags',
                  'concurrent.rf.columns',
                  'validation.prod.max_depth',
                  'variables.short.ngrams',
                  'validation.batch.max_features',
                  'model.prod.num_est',
                  'variables.other.ngrams',
                  'concurrent.batch.epochs',
                  'validation.batch.learning_rate',
                  'preprocessing.selection.columns',
                  'validation.other.max_features',
                  'concurrent.collection.ngrams',
                  'variables.batch.threads',
                  'model.selection.layers',
                  'preprocessing.selection.max_features',
                  'model.prod.epochs',
                  'model.prod.ngrams',
                  'model.prod.split',
                  'concurrent.rf.passes',
                  'concurrent.other.num_est',
                  'preprocessing.other.learning_rate',
                  'validation.short.tags',
                  'preprocessing.short.columns',
                  'preprocessing.rf.weight_factor',
                  'concurrent.other.dense',
                  'variables.collection.seed',
                  'model.other.max_features',
                  'settings.prod.min_features',
                  'validation.rf.dense',
                  'variables.prod.epochs',
                  'concurrent.collection.max_depth',
                  'concurrent.rf.estimators',
                  'variables.selection.threads',
                  'validation.rf.trees',
                  'concurrent.collection.threads',
                  'preprocessing.collection.layers',
                  'settings.selection.trees',
                  'model.rf.drop',
                  'model.selection.batch_size',
                  'validation.batch.split',
                  'concurrent.selection.epochs',
                  'concurrent.selection.max_depth',
                  'concurrent.selection.num_est',
                  'settings.rf.max_depth',
                  'preprocessing.selection.dense',
                  'validation.short.folds',
                  'validation.collection.layers',
                  'settings.collection.weight_factor',
                  'preprocessing.prod.max_features',
                  'model.rf.estimators',
                  'concurrent.short.folds',
                  'concurrent.selection.folds',
                  'validation.collection.weight_factor',
                  'concurrent.selection.split',
                  'variables.rf.threads',
                  'settings.selection.seed',
                  'concurrent.collection.min_split',
                  'variables.other.dense',
                  'variables.prod.learning_rate',
                  'validation.other.tags',
                  'variables.selection.features',
                  'preprocessing.selection.sample',
                  'preprocessing.selection.batch_size',
                  'variables.prod.tags',
                  'validation.prod.folds',
                  'validation.batch.passes',
                  'settings.selection.passes',
                  'validation.rf.split',
                  'concurrent.batch.features',
                  'settings.batch.num_est',
                  'model.batch.ngrams',
                  'validation.rf.features',
                  'preprocessing.short.trees',
                  'model.rf.min_split',
                  'model.selection.learning_rate',
                  'variables.short.folds',
                  'variables.rf.weight_factor',
                  'settings.batch.estimators',
                  'concurrent.batch.batch_size',
                  'validation.selection.sample',
                  'concurrent.collection.weight_factor',
                  'validation.rf.min_split',
                  'concurrent.other.batch_size',
                  'concurrent.prod.folds',
                  'settings.prod.columns',
                  'preprocessing.other.min_features',
                  'validation.other.min_features',
                  'model.rf.batch_size',
                  'variables.selection.split',
                  'preprocessing.short.estimators',
                  'settings.selection.max_depth',
                  'validation.short.split',
                  'model.batch.max_depth',
                  'model.selection.max_features',
                  'concurrent.prod.sample',
                  'preprocessing.rf.split',
                  'model.other.seed',
                  'settings.other.folds',
                  'model.collection.num_est',
                  'settings.short.ngrams',
                  'preprocessing.prod.weight_factor',
                  'preprocessing.rf.passes',
                  'preprocessing.prod.passes']}]

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

# Comment to update:465062710
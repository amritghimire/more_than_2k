#!/usr/bin/env python3
import sys, json
import random

VERSION = 90


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['model.preset.random_state',
                  'concurrent.rf.random_state',
                  'settings.rf.min_split',
                  'preprocessing.prod.dense',
                  'variables.other.min_split',
                  'preprocessing.prod.max_features',
                  'settings.rf.max_depth',
                  'variables.diff.max_depth',
                  'settings.other.min_split',
                  'settings.preset.layers',
                  'preprocessing.prod.split',
                  'model.prod.columns',
                  'model.prod.num_est',
                  'settings.prod.epochs',
                  'settings.rf.dense',
                  'model.preset.tags',
                  'concurrent.preset.columns',
                  'model.rf.folds',
                  'settings.long.folds',
                  'model.other.tags',
                  'settings.prod.ngrams',
                  'variables.other.trees',
                  'preprocessing.rf.min_features',
                  'preprocessing.diff.threads',
                  'variables.long.seed',
                  'concurrent.other.passes',
                  'settings.diff.min_features',
                  'concurrent.diff.tags',
                  'concurrent.prod.columns',
                  'concurrent.classifier.learning_rate',
                  'model.rf.random_state',
                  'preprocessing.prod.trees',
                  'variables.classifier.random_state',
                  'variables.other.threads',
                  'concurrent.preset.max_depth',
                  'preprocessing.prod.max_depth',
                  'concurrent.rf.min_features',
                  'variables.long.num_est',
                  'preprocessing.prod.folds',
                  'model.rf.ngrams',
                  'model.preset.min_features',
                  'variables.diff.trees',
                  'concurrent.preset.sample',
                  'settings.long.layers',
                  'variables.classifier.ngrams',
                  'model.classifier.min_features',
                  'preprocessing.diff.min_features',
                  'settings.prod.max_depth',
                  'settings.diff.min_split',
                  'preprocessing.other.columns',
                  'preprocessing.prod.batch_size',
                  'preprocessing.rf.columns',
                  'preprocessing.other.threads',
                  'model.prod.dense',
                  'model.diff.estimators',
                  'model.long.layers',
                  'preprocessing.prod.ngrams',
                  'settings.other.learning_rate',
                  'concurrent.classifier.num_est',
                  'model.long.seed',
                  'variables.preset.dense',
                  'model.prod.sample',
                  'variables.rf.min_features',
                  'model.classifier.min_split',
                  'model.prod.random_state',
                  'settings.preset.learning_rate',
                  'variables.other.random_state',
                  'model.rf.dense',
                  'preprocessing.other.random_state',
                  'settings.classifier.folds',
                  'variables.classifier.columns',
                  'variables.diff.estimators',
                  'concurrent.classifier.max_depth',
                  'concurrent.long.layers',
                  'preprocessing.preset.epochs',
                  'concurrent.other.features',
                  'settings.long.min_split',
                  'settings.rf.drop',
                  'variables.other.features',
                  'variables.diff.min_features',
                  'settings.prod.features',
                  'settings.diff.drop',
                  'variables.diff.split',
                  'model.rf.weight_factor',
                  'settings.long.epochs',
                  'settings.diff.estimators',
                  'preprocessing.diff.random_state',
                  'preprocessing.long.estimators',
                  'concurrent.other.columns',
                  'concurrent.prod.threads',
                  'model.preset.estimators',
                  'preprocessing.preset.split',
                  'concurrent.other.sample',
                  'variables.rf.sample',
                  'concurrent.long.max_features',
                  'model.prod.max_features',
                  'concurrent.preset.min_split',
                  'model.classifier.ngrams',
                  'model.preset.folds',
                  'concurrent.prod.random_state',
                  'settings.preset.passes',
                  'preprocessing.long.seed',
                  'model.preset.seed',
                  'model.diff.drop',
                  'settings.prod.tags',
                  'model.prod.drop',
                  'preprocessing.other.passes',
                  'concurrent.classifier.passes',
                  'preprocessing.preset.seed',
                  'concurrent.classifier.threads',
                  'settings.rf.num_est',
                  'preprocessing.prod.passes',
                  'variables.classifier.layers',
                  'preprocessing.prod.estimators',
                  'preprocessing.rf.tags',
                  'model.prod.features',
                  'concurrent.prod.dense',
                  'preprocessing.other.features',
                  'variables.preset.passes',
                  'variables.classifier.folds',
                  'model.diff.columns',
                  'variables.preset.layers',
                  'preprocessing.long.min_features',
                  'concurrent.other.random_state',
                  'model.classifier.max_depth',
                  'concurrent.preset.features',
                  'preprocessing.preset.estimators',
                  'preprocessing.diff.trees',
                  'variables.prod.seed',
                  'variables.long.min_split',
                  'model.other.layers',
                  'preprocessing.long.layers',
                  'concurrent.long.weight_factor']}]

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

# Comment to update:269799912212506
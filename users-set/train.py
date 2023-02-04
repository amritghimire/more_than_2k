#!/usr/bin/env python3
import sys, json
import random

VERSION = 113


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['variables.other.epochs',
                  'preprocessing.batch.weight_factor',
                  'validation.dev.sample',
                  'settings.rf.tags',
                  'model.batch.layers',
                  'preprocessing.batch.dense',
                  'settings.requests.min_features',
                  'variables.selection.max_depth',
                  'variables.selection.num_est',
                  'validation.requests.ngrams',
                  'model.selection.passes',
                  'preprocessing.selection.learning_rate',
                  'preprocessing.selection.random_state',
                  'validation.selection.folds',
                  'preprocessing.other.epochs',
                  'settings.classifier.min_features',
                  'variables.rf.trees',
                  'settings.selection.layers',
                  'variables.batch.threads',
                  'preprocessing.rf.threads',
                  'validation.other.layers',
                  'model.batch.trees',
                  'preprocessing.other.folds',
                  'variables.requests.dense',
                  'model.requests.seed',
                  'settings.other.epochs',
                  'model.selection.layers',
                  'model.batch.num_est',
                  'validation.rf.max_depth',
                  'preprocessing.rf.num_est',
                  'model.rf.num_est',
                  'validation.other.split',
                  'variables.selection.learning_rate',
                  'settings.batch.estimators',
                  'validation.selection.tags',
                  'preprocessing.rf.folds',
                  'settings.batch.ngrams',
                  'model.requests.epochs',
                  'variables.classifier.estimators',
                  'validation.other.tags',
                  'settings.selection.estimators',
                  'preprocessing.rf.sample',
                  'model.rf.max_depth',
                  'model.batch.seed',
                  'settings.selection.seed',
                  'model.selection.folds',
                  'variables.batch.split',
                  'variables.dev.batch_size',
                  'variables.classifier.seed',
                  'variables.classifier.threads',
                  'validation.selection.min_split',
                  'settings.classifier.ngrams',
                  'validation.requests.num_est',
                  'model.classifier.columns',
                  'variables.batch.weight_factor',
                  'validation.dev.batch_size',
                  'validation.selection.weight_factor',
                  'validation.dev.tags',
                  'validation.selection.estimators',
                  'settings.selection.folds',
                  'model.other.seed',
                  'preprocessing.rf.ngrams',
                  'validation.rf.estimators',
                  'settings.classifier.dense',
                  'preprocessing.other.learning_rate',
                  'model.batch.epochs',
                  'validation.requests.layers',
                  'model.dev.sample',
                  'preprocessing.dev.columns',
                  'preprocessing.other.passes',
                  'settings.batch.columns',
                  'validation.dev.trees',
                  'model.batch.threads',
                  'preprocessing.dev.tags',
                  'settings.other.weight_factor',
                  'preprocessing.batch.folds',
                  'model.batch.weight_factor',
                  'model.rf.sample',
                  'settings.rf.batch_size',
                  'variables.dev.passes',
                  'preprocessing.dev.random_state',
                  'variables.other.layers',
                  'preprocessing.classifier.weight_factor',
                  'preprocessing.rf.trees',
                  'settings.requests.trees',
                  'variables.classifier.columns',
                  'settings.requests.threads',
                  'model.classifier.sample',
                  'model.classifier.weight_factor',
                  'validation.rf.min_split',
                  'validation.selection.num_est',
                  'settings.classifier.columns',
                  'validation.other.estimators',
                  'settings.other.estimators',
                  'validation.selection.passes',
                  'validation.classifier.split',
                  'model.dev.max_depth',
                  'model.rf.learning_rate',
                  'variables.rf.threads',
                  'model.rf.folds',
                  'model.selection.sample',
                  'variables.requests.learning_rate',
                  'preprocessing.batch.random_state',
                  'model.classifier.split',
                  'variables.dev.tags',
                  'settings.batch.dense',
                  'preprocessing.dev.dense',
                  'variables.dev.min_split',
                  'preprocessing.rf.passes',
                  'preprocessing.classifier.learning_rate',
                  'model.batch.random_state',
                  'settings.classifier.epochs',
                  'preprocessing.dev.threads',
                  'variables.batch.batch_size',
                  'settings.rf.trees',
                  'model.requests.dense',
                  'settings.dev.max_depth',
                  'model.dev.trees',
                  'variables.classifier.layers',
                  'variables.selection.columns',
                  'variables.requests.passes',
                  'model.classifier.threads',
                  'variables.classifier.split',
                  'preprocessing.other.ngrams',
                  'variables.batch.tags',
                  'validation.classifier.max_features',
                  'variables.dev.max_features',
                  'model.classifier.max_depth',
                  'variables.selection.seed',
                  'model.selection.num_est',
                  'model.classifier.min_features',
                  'variables.classifier.min_split',
                  'variables.requests.min_split',
                  'model.classifier.batch_size',
                  'preprocessing.classifier.min_features',
                  'variables.rf.min_features',
                  'variables.dev.epochs',
                  'settings.other.columns',
                  'variables.other.features',
                  'validation.other.features',
                  'settings.dev.batch_size',
                  'settings.classifier.estimators',
                  'validation.dev.split',
                  'preprocessing.dev.folds',
                  'model.requests.trees',
                  'settings.other.max_features',
                  'validation.requests.weight_factor',
                  'preprocessing.rf.drop',
                  'preprocessing.other.max_depth',
                  'preprocessing.dev.trees',
                  'settings.dev.seed',
                  'variables.requests.folds',
                  'model.rf.estimators',
                  'variables.rf.seed',
                  'validation.dev.passes',
                  'validation.requests.estimators',
                  'model.classifier.seed',
                  'preprocessing.requests.epochs',
                  'model.dev.passes',
                  'validation.requests.trees',
                  'preprocessing.selection.drop',
                  'variables.classifier.features',
                  'variables.classifier.random_state',
                  'variables.batch.learning_rate',
                  'settings.selection.threads',
                  'variables.classifier.sample',
                  'model.dev.columns',
                  'preprocessing.other.max_features',
                  'model.rf.weight_factor',
                  'validation.batch.drop',
                  'preprocessing.classifier.trees',
                  'preprocessing.rf.random_state',
                  'preprocessing.selection.epochs',
                  'settings.rf.epochs',
                  'validation.classifier.tags',
                  'model.rf.features',
                  'variables.selection.threads',
                  'variables.batch.epochs',
                  'validation.batch.threads',
                  'validation.dev.folds']}]

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

# Comment to update:896231633857630170
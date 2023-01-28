#!/usr/bin/env python3
import sys, json
import random

VERSION = 60


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['validation.concurrent.layers',
                  'settings.dev.ngrams',
                  'settings.dev.tags',
                  'settings.dev.threads',
                  'settings.other.folds',
                  'tagging.model.weight_factor',
                  'variables.concurrent.min_features',
                  'variables.combine.features',
                  'validation.dev.features',
                  'variables.preprocessing.estimators',
                  'train.preprocessing.drop',
                  'tagging.combine.max_depth',
                  'variables.other.batch_size',
                  'variables.concurrent.split',
                  'variables.dev.max_features',
                  'settings.test.random_state',
                  'tagging.other.max_features',
                  'variables.concurrent.threads',
                  'tagging.other.columns',
                  'variables.dev.weight_factor',
                  'settings.concurrent.min_features',
                  'variables.dev.min_features',
                  'validation.dev.trees',
                  'variables.test.min_split',
                  'settings.concurrent.random_state',
                  'validation.combine.min_features',
                  'tagging.test.trees',
                  'validation.test.tags',
                  'tagging.dev.columns',
                  'tagging.model.seed',
                  'tagging.concurrent.trees',
                  'settings.preprocessing.sample',
                  'tagging.combine.split',
                  'validation.concurrent.weight_factor',
                  'validation.preprocessing.split',
                  'train.model.random_state',
                  'settings.preprocessing.drop',
                  'validation.concurrent.drop',
                  'variables.dev.split',
                  'validation.other.tags',
                  'train.test.trees',
                  'settings.concurrent.sample',
                  'train.model.features',
                  'validation.combine.passes',
                  'settings.other.columns',
                  'settings.dev.batch_size',
                  'validation.model.max_depth',
                  'settings.preprocessing.threads',
                  'train.dev.min_split',
                  'tagging.dev.features',
                  'train.dev.learning_rate',
                  'variables.model.folds',
                  'variables.combine.batch_size',
                  'settings.test.columns',
                  'train.concurrent.layers',
                  'validation.dev.min_split',
                  'tagging.test.max_depth',
                  'validation.test.weight_factor',
                  'validation.other.num_est',
                  'variables.preprocessing.dense',
                  'validation.preprocessing.columns',
                  'variables.combine.sample',
                  'train.model.threads',
                  'settings.test.num_est',
                  'validation.concurrent.epochs',
                  'tagging.dev.max_depth',
                  'variables.combine.estimators',
                  'tagging.other.epochs',
                  'train.dev.seed',
                  'settings.preprocessing.split',
                  'tagging.dev.random_state',
                  'tagging.test.min_split',
                  'settings.test.ngrams',
                  'train.preprocessing.learning_rate',
                  'tagging.model.split',
                  'variables.test.weight_factor',
                  'tagging.other.threads',
                  'tagging.model.min_features',
                  'tagging.dev.tags',
                  'validation.combine.features',
                  'tagging.preprocessing.ngrams',
                  'validation.preprocessing.passes',
                  'settings.concurrent.ngrams',
                  'tagging.model.batch_size',
                  'variables.dev.threads',
                  'variables.test.features',
                  'train.dev.features',
                  'settings.dev.num_est',
                  'settings.other.min_features',
                  'settings.other.weight_factor',
                  'validation.preprocessing.weight_factor',
                  'train.concurrent.estimators',
                  'train.concurrent.batch_size',
                  'settings.dev.folds',
                  'settings.combine.sample',
                  'settings.model.dense',
                  'variables.model.max_features',
                  'variables.other.weight_factor',
                  'train.test.split',
                  'tagging.model.min_split',
                  'validation.model.ngrams',
                  'tagging.concurrent.num_est',
                  'variables.dev.columns',
                  'tagging.test.drop',
                  'train.model.weight_factor',
                  'tagging.dev.epochs',
                  'tagging.test.folds',
                  'tagging.dev.learning_rate',
                  'train.model.split',
                  'validation.combine.learning_rate',
                  'variables.other.max_features',
                  'validation.preprocessing.layers',
                  'train.other.passes',
                  'variables.test.random_state',
                  'tagging.other.features',
                  'variables.preprocessing.ngrams',
                  'variables.concurrent.columns',
                  'tagging.concurrent.passes',
                  'settings.dev.random_state',
                  'tagging.concurrent.max_depth',
                  'validation.other.epochs',
                  'settings.preprocessing.estimators',
                  'tagging.concurrent.dense',
                  'tagging.other.random_state',
                  'settings.test.min_features',
                  'tagging.concurrent.threads',
                  'settings.other.features',
                  'tagging.preprocessing.dense',
                  'train.concurrent.sample',
                  'variables.concurrent.folds',
                  'tagging.model.layers',
                  'settings.test.dense',
                  'settings.preprocessing.min_split',
                  'train.combine.ngrams',
                  'tagging.dev.folds',
                  'variables.test.epochs',
                  'train.combine.folds',
                  'validation.preprocessing.trees',
                  'train.model.columns',
                  'tagging.combine.columns',
                  'validation.model.min_split',
                  'validation.test.threads',
                  'train.other.seed',
                  'tagging.test.split',
                  'tagging.preprocessing.sample',
                  'settings.preprocessing.max_features',
                  'train.concurrent.split',
                  'settings.other.random_state',
                  'tagging.other.dense',
                  'settings.other.estimators',
                  'variables.other.sample',
                  'variables.other.threads',
                  'settings.model.estimators',
                  'tagging.test.max_features',
                  'validation.other.learning_rate',
                  'train.model.learning_rate',
                  'validation.concurrent.random_state',
                  'settings.dev.learning_rate',
                  'train.concurrent.trees',
                  'settings.concurrent.drop',
                  'settings.concurrent.seed',
                  'validation.dev.split',
                  'variables.other.features',
                  'validation.test.dense',
                  'tagging.preprocessing.features',
                  'train.combine.layers',
                  'tagging.model.features',
                  'variables.model.columns',
                  'validation.dev.folds',
                  'validation.test.passes',
                  'settings.other.tags']}]

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

# Comment to update:54717591
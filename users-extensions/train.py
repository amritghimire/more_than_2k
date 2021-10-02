#!/usr/bin/env python3
import sys, json
import random

VERSION = 88


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['concurrent.settings.columns',
                  'concurrent.other.split',
                  'model.settings.batch_size',
                  'variables.preset.epochs',
                  'train.short.threads',
                  'validation.preset.trees',
                  'train.settings.learning_rate',
                  'variables.batch.threads',
                  'tagging.settings.learning_rate',
                  'concurrent.settings.min_features',
                  'preprocessing.dev.trees',
                  'concurrent.settings.max_features',
                  'variables.test.epochs',
                  'preprocessing.batch.layers',
                  'validation.preset.layers',
                  'variables.batch.sample',
                  'model.settings.epochs',
                  'tagging.settings.epochs',
                  'tagging.batch.batch_size',
                  'concurrent.test.sample',
                  'validation.preset.batch_size',
                  'train.settings.drop',
                  'variables.preset.layers',
                  'validation.settings.learning_rate',
                  'concurrent.other.drop',
                  'validation.batch.epochs',
                  'validation.test.epochs',
                  'concurrent.other.folds',
                  'train.settings.weight_factor',
                  'variables.batch.passes',
                  'tagging.test.sample',
                  'variables.batch.weight_factor',
                  'train.other.trees',
                  'tagging.preset.seed',
                  'variables.test.sample',
                  'tagging.dev.dense',
                  'train.batch.epochs',
                  'tagging.dev.folds',
                  'preprocessing.test.min_features',
                  'validation.batch.min_features',
                  'validation.preset.min_split',
                  'train.dev.min_features',
                  'train.test.layers',
                  'variables.short.learning_rate',
                  'tagging.settings.trees',
                  'tagging.preset.num_est',
                  'train.dev.threads',
                  'preprocessing.dev.folds',
                  'variables.test.tags',
                  'model.other.ngrams',
                  'variables.preset.batch_size',
                  'concurrent.preset.max_depth',
                  'tagging.batch.seed',
                  'train.short.dense',
                  'concurrent.test.max_features',
                  'model.short.sample',
                  'validation.dev.min_features',
                  'preprocessing.settings.layers',
                  'concurrent.settings.features',
                  'concurrent.batch.trees',
                  'concurrent.test.batch_size',
                  'concurrent.other.min_features',
                  'variables.other.drop',
                  'tagging.batch.max_features',
                  'train.short.tags',
                  'variables.preset.learning_rate',
                  'variables.test.columns',
                  'concurrent.batch.threads',
                  'concurrent.dev.threads',
                  'tagging.dev.tags',
                  'concurrent.settings.drop',
                  'preprocessing.test.ngrams',
                  'validation.dev.columns',
                  'validation.preset.weight_factor',
                  'preprocessing.other.drop',
                  'variables.settings.tags',
                  'validation.other.min_features',
                  'preprocessing.batch.features',
                  'concurrent.test.drop',
                  'train.batch.features',
                  'preprocessing.settings.weight_factor',
                  'train.settings.max_features',
                  'train.other.drop',
                  'tagging.preset.ngrams',
                  'model.dev.max_depth',
                  'preprocessing.short.split',
                  'train.batch.columns',
                  'train.preset.passes',
                  'train.test.features',
                  'validation.preset.max_depth',
                  'validation.batch.estimators',
                  'preprocessing.settings.seed',
                  'model.dev.learning_rate',
                  'preprocessing.batch.batch_size',
                  'train.preset.random_state',
                  'preprocessing.batch.learning_rate',
                  'concurrent.preset.split',
                  'train.preset.weight_factor',
                  'concurrent.short.min_split',
                  'tagging.batch.drop',
                  'validation.batch.batch_size',
                  'concurrent.short.num_est',
                  'preprocessing.batch.trees',
                  'train.batch.dense',
                  'concurrent.short.features',
                  'model.test.layers',
                  'validation.dev.dense',
                  'preprocessing.short.folds',
                  'tagging.other.ngrams',
                  'validation.test.layers',
                  'variables.preset.passes',
                  'validation.batch.split',
                  'variables.short.passes',
                  'concurrent.test.trees',
                  'tagging.short.features',
                  'model.settings.columns',
                  'model.other.columns',
                  'tagging.test.random_state',
                  'variables.settings.min_split',
                  'preprocessing.test.columns',
                  'validation.batch.learning_rate',
                  'tagging.dev.num_est',
                  'model.dev.tags',
                  'tagging.batch.min_split',
                  'model.dev.estimators',
                  'train.dev.random_state',
                  'tagging.dev.seed',
                  'preprocessing.dev.batch_size',
                  'model.test.estimators',
                  'variables.dev.max_depth',
                  'validation.preset.tags',
                  'variables.dev.trees',
                  'model.short.dense',
                  'concurrent.other.estimators',
                  'preprocessing.other.trees',
                  'validation.dev.layers',
                  'preprocessing.preset.columns',
                  'variables.settings.num_est',
                  'validation.short.max_depth',
                  'preprocessing.settings.sample',
                  'concurrent.preset.tags',
                  'train.test.random_state',
                  'validation.dev.trees',
                  'preprocessing.settings.num_est',
                  'validation.short.drop',
                  'model.short.folds',
                  'concurrent.dev.estimators',
                  'variables.preset.dense',
                  'validation.short.sample',
                  'preprocessing.settings.min_features',
                  'tagging.short.threads',
                  'concurrent.dev.trees',
                  'model.dev.seed',
                  'preprocessing.batch.min_features',
                  'concurrent.test.learning_rate',
                  'tagging.test.max_depth',
                  'model.dev.dense',
                  'train.preset.epochs',
                  'train.test.sample',
                  'train.preset.layers',
                  'train.other.min_features',
                  'train.dev.dense',
                  'tagging.dev.ngrams',
                  'concurrent.short.estimators',
                  'preprocessing.settings.threads',
                  'train.test.split',
                  'variables.other.features',
                  'variables.short.random_state',
                  'train.settings.layers',
                  'variables.preset.drop',
                  'concurrent.preset.columns',
                  'train.other.max_features',
                  'concurrent.preset.num_est',
                  'model.other.batch_size',
                  'concurrent.dev.split',
                  'preprocessing.settings.columns',
                  'train.dev.num_est',
                  'train.batch.random_state',
                  'concurrent.short.epochs',
                  'concurrent.preset.dense',
                  'preprocessing.batch.ngrams',
                  'preprocessing.batch.split',
                  'concurrent.test.tags',
                  'preprocessing.other.sample',
                  'preprocessing.other.epochs',
                  'concurrent.test.min_features',
                  'model.test.random_state',
                  'tagging.short.columns',
                  'variables.short.estimators',
                  'train.test.threads',
                  'train.preset.num_est',
                  'preprocessing.test.tags',
                  'model.preset.drop',
                  'preprocessing.test.dense',
                  'tagging.short.split',
                  'model.settings.sample',
                  'variables.preset.num_est',
                  'validation.dev.drop',
                  'model.test.weight_factor',
                  'variables.dev.num_est',
                  'validation.test.max_depth',
                  'preprocessing.preset.learning_rate',
                  'train.short.columns']}]

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

# Comment to update:53848045460
#!/usr/bin/env python3
import sys, json
import random

VERSION = 162


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['model.rf.max_depth',
                  'tagging.rf.max_depth',
                  'model.batch.layers',
                  'train.dev.sample',
                  'model.short.min_split',
                  'model.rf.min_features',
                  'preprocessing.preset.split',
                  'settings.preset.epochs',
                  'settings.long.min_features',
                  'model.preset.ngrams',
                  'tagging.dev.threads',
                  'model.short.trees',
                  'preprocessing.binary.dense',
                  'preprocessing.binary.ngrams',
                  'preprocessing.rf.threads',
                  'settings.short.estimators',
                  'model.binary.ngrams',
                  'model.long.min_features',
                  'settings.dev.sample',
                  'tagging.binary.weight_factor',
                  'model.preset.split',
                  'validation.long.ngrams',
                  'model.rf.weight_factor',
                  'model.long.learning_rate',
                  'model.short.epochs',
                  'validation.batch.sample',
                  'tagging.dev.features',
                  'train.rf.passes',
                  'validation.long.random_state',
                  'train.rf.num_est',
                  'settings.rf.learning_rate',
                  'validation.binary.max_depth',
                  'train.binary.learning_rate',
                  'settings.batch.learning_rate',
                  'validation.binary.num_est',
                  'preprocessing.dev.weight_factor',
                  'preprocessing.dev.learning_rate',
                  'settings.binary.min_split',
                  'model.preset.folds',
                  'validation.short.layers',
                  'validation.long.passes',
                  'train.batch.drop',
                  'tagging.preset.seed',
                  'tagging.dev.sample',
                  'settings.binary.batch_size',
                  'model.preset.epochs',
                  'settings.preset.tags',
                  'settings.batch.columns',
                  'model.short.learning_rate',
                  'validation.batch.layers',
                  'tagging.rf.epochs',
                  'validation.rf.threads',
                  'tagging.rf.threads',
                  'tagging.long.features',
                  'preprocessing.preset.dense',
                  'settings.rf.num_est',
                  'validation.dev.trees',
                  'model.binary.epochs',
                  'validation.dev.dense',
                  'model.batch.min_split',
                  'settings.dev.min_split',
                  'model.batch.split',
                  'settings.rf.min_features',
                  'preprocessing.long.layers',
                  'preprocessing.binary.split',
                  'settings.binary.max_features',
                  'settings.preset.columns',
                  'tagging.rf.random_state',
                  'train.preset.num_est',
                  'tagging.dev.columns',
                  'validation.dev.features',
                  'validation.short.min_split',
                  'validation.binary.learning_rate',
                  'tagging.binary.ngrams',
                  'tagging.short.dense',
                  'settings.batch.trees',
                  'settings.preset.drop',
                  'settings.short.max_depth',
                  'validation.rf.passes',
                  'settings.long.features',
                  'preprocessing.preset.tags',
                  'model.binary.sample',
                  'preprocessing.short.max_features',
                  'preprocessing.long.weight_factor',
                  'preprocessing.long.learning_rate',
                  'tagging.short.threads',
                  'settings.batch.batch_size',
                  'validation.dev.threads',
                  'train.short.min_split',
                  'model.batch.max_depth',
                  'validation.short.columns',
                  'validation.preset.learning_rate',
                  'tagging.batch.sample',
                  'tagging.batch.dense',
                  'validation.dev.min_features',
                  'tagging.dev.dense',
                  'settings.binary.features',
                  'train.batch.tags',
                  'tagging.preset.batch_size',
                  'settings.long.min_split',
                  'tagging.dev.min_split',
                  'settings.binary.passes',
                  'settings.binary.split',
                  'tagging.long.layers',
                  'model.long.split',
                  'validation.binary.split',
                  'validation.rf.max_features',
                  'validation.short.folds',
                  'model.binary.min_features',
                  'preprocessing.preset.epochs',
                  'train.preset.features',
                  'validation.dev.num_est',
                  'model.dev.folds',
                  'validation.binary.weight_factor',
                  'train.dev.batch_size',
                  'model.rf.batch_size',
                  'train.binary.max_features',
                  'model.rf.trees',
                  'validation.long.batch_size',
                  'validation.rf.max_depth',
                  'preprocessing.binary.weight_factor',
                  'model.binary.dense',
                  'settings.binary.ngrams',
                  'model.binary.tags',
                  'validation.long.weight_factor',
                  'validation.preset.ngrams',
                  'tagging.long.min_features',
                  'preprocessing.batch.estimators',
                  'preprocessing.batch.ngrams',
                  'settings.rf.seed',
                  'preprocessing.short.epochs',
                  'tagging.binary.min_split',
                  'preprocessing.binary.max_depth',
                  'tagging.preset.estimators',
                  'train.dev.learning_rate',
                  'validation.preset.weight_factor',
                  'validation.dev.learning_rate',
                  'preprocessing.batch.min_split',
                  'settings.preset.ngrams',
                  'preprocessing.rf.weight_factor',
                  'preprocessing.long.ngrams',
                  'tagging.batch.num_est',
                  'train.preset.drop']}]

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

# Comment to update:5198383649990487825739927923
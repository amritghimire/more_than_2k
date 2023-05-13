#!/usr/bin/env python3
import sys, json
import random

VERSION = 102


import yaml

def get_in(value, path):
    for k in path:
        try:
            value = value[k]
        except:
            return None
    return value

used_params = [{'params.yaml': ['tagging.requests.ngrams',
                  'variables.preset.tags',
                  'concurrent.classifier.dense',
                  'train.auto.sample',
                  'settings.combine.min_features',
                  'tagging.prod.weight_factor',
                  'concurrent.prod.columns',
                  'train.requests.min_split',
                  'settings.requests.max_features',
                  'settings.batch.sample',
                  'model.preset.learning_rate',
                  'concurrent.classifier.split',
                  'settings.preset.min_split',
                  'tagging.combine.tags',
                  'tagging.prod.sample',
                  'train.combine.passes',
                  'model.combine.threads',
                  'settings.prod.estimators',
                  'model.classifier.tags',
                  'variables.auto.split',
                  'tagging.auto.num_est',
                  'tagging.prod.columns',
                  'settings.prod.max_depth',
                  'tagging.classifier.ngrams',
                  'concurrent.batch.split',
                  'settings.auto.estimators',
                  'model.prod.seed',
                  'model.batch.trees',
                  'concurrent.auto.split',
                  'concurrent.requests.max_features',
                  'train.requests.threads',
                  'variables.requests.estimators',
                  'train.classifier.num_est',
                  'train.combine.dense',
                  'concurrent.batch.ngrams',
                  'concurrent.preset.random_state',
                  'settings.prod.tags',
                  'train.requests.batch_size',
                  'concurrent.classifier.max_features',
                  'variables.combine.random_state',
                  'settings.batch.random_state',
                  'model.batch.columns',
                  'train.requests.split',
                  'model.combine.sample',
                  'settings.auto.layers',
                  'tagging.requests.random_state',
                  'concurrent.requests.trees',
                  'concurrent.preset.folds',
                  'model.preset.ngrams',
                  'settings.auto.passes',
                  'concurrent.auto.folds',
                  'concurrent.preset.columns',
                  'train.preset.batch_size',
                  'tagging.classifier.threads',
                  'model.requests.random_state',
                  'tagging.batch.seed',
                  'model.combine.max_depth',
                  'settings.classifier.dense',
                  'settings.combine.passes',
                  'tagging.prod.max_depth',
                  'model.classifier.max_features',
                  'concurrent.preset.tags',
                  'variables.requests.tags',
                  'concurrent.classifier.seed',
                  'concurrent.auto.tags',
                  'settings.requests.min_features',
                  'model.batch.num_est',
                  'model.classifier.split',
                  'model.auto.min_split',
                  'variables.combine.passes',
                  'model.auto.batch_size',
                  'settings.preset.ngrams',
                  'concurrent.auto.num_est',
                  'settings.prod.learning_rate',
                  'settings.classifier.ngrams',
                  'model.auto.min_features',
                  'train.classifier.threads',
                  'train.combine.columns',
                  'concurrent.preset.trees',
                  'model.preset.sample',
                  'concurrent.requests.min_split',
                  'train.preset.passes',
                  'variables.prod.threads',
                  'settings.requests.layers',
                  'tagging.prod.tags',
                  'tagging.batch.num_est',
                  'variables.classifier.max_features',
                  'variables.classifier.seed',
                  'tagging.auto.dense',
                  'variables.auto.max_features',
                  'settings.batch.epochs',
                  'tagging.combine.num_est',
                  'concurrent.combine.max_depth',
                  'variables.requests.sample',
                  'train.combine.drop',
                  'settings.preset.learning_rate',
                  'concurrent.combine.trees',
                  'train.requests.folds',
                  'concurrent.requests.num_est',
                  'model.auto.layers',
                  'settings.preset.drop',
                  'model.requests.layers',
                  'settings.combine.max_features',
                  'train.preset.epochs',
                  'settings.combine.ngrams',
                  'train.classifier.min_split',
                  'settings.auto.batch_size',
                  'settings.auto.drop',
                  'train.classifier.features',
                  'settings.prod.weight_factor',
                  'train.combine.max_features',
                  'tagging.requests.estimators',
                  'train.preset.learning_rate',
                  'variables.batch.tags',
                  'variables.auto.estimators',
                  'settings.auto.ngrams',
                  'train.requests.random_state',
                  'concurrent.classifier.passes',
                  'model.combine.passes',
                  'variables.prod.trees',
                  'settings.auto.epochs',
                  'settings.auto.tags',
                  'tagging.requests.weight_factor',
                  'concurrent.batch.folds',
                  'train.prod.threads',
                  'model.classifier.trees',
                  'tagging.batch.random_state',
                  'model.preset.epochs',
                  'variables.combine.max_features',
                  'variables.preset.layers',
                  'variables.auto.dense',
                  'concurrent.batch.dense',
                  'model.prod.dense',
                  'variables.preset.estimators',
                  'concurrent.preset.sample',
                  'variables.combine.estimators',
                  'settings.auto.sample',
                  'train.requests.features',
                  'train.batch.ngrams',
                  'variables.preset.trees',
                  'settings.classifier.columns',
                  'model.auto.max_depth']}]

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

# Comment to update:78137275857
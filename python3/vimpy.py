#!/usr/bin/env python3
import shelve
import types
import pandas as pd
from datetime import date

"""  TOOLS """

def store(d,name=False):
    """ saves data as .csv and .shelf (excl. modules, functions) """
    if not name:
        name = date.today().strftime("%Y_%m_%d")
    if isinstance(d, pd.DataFrame):
        d.to_csv(f'{name}.csv')
        print(f'{name}.csv written')
    if isinstance(d, dict):
        d = {key:d[key] for key in d if not isinstance(d[key], types.ModuleType)}
        d = {key:d[key] for key in d if not callable(d[key])}
    with shelve.open(f'.shelf') as data:
        data[name] = d
    print(f'{name} added to .shelf')

def restore(key=False):
    """ returns dict of variables saved in .shelf """
    results = {}
    with shelve.open('.shelf') as d:
        if key:
            if key in d:
                return d[key]
        for key in d:
            results[key] = d[key]
    return results


def printState(d):
    """ prints local variables """
    d = {key:d[key] for key in d if not isinstance(d[key], types.ModuleType)}
    d = {key:d[key] for key in d if not callable(d[key])}
    d = {key:d[key] for key in d if not key.startswith("__")}
    d = {key:d[key] for key in d if not key.endswith(".py")}
    print('\033[93m Variables\n', end='')
    for key in d:
        print(f"    {key:15}{d[key]}")
    print('\033[0m', end='')



# -*- coding: utf-8 -*-
import sys
import pandas as pd
from argparse import ArgumentParser

# print(sys.argv)

# un script qui affiche la moyenne des ages dans le fichier passé en argument
# if len(sys.argv) > 1:
#     df = pd.read_csv(sys.argv[1])
#     print(df["Age"].mean())


parser = ArgumentParser(
    description="Outils pour trouver la moyenne des ages dans un fichier"
)

parser.add_argument("file", type=str, help="CSV file that contains data")
parser.add_argument("--column", default="Age", type=str, help="column to extract data")
parser.add_argument("--stats", default="mean", type=str, choices=["min", "max", "mean", "median"], help="Stat to extract")

args = parser.parse_args()

df = pd.read_csv(args.file)
print(getattr(pd.Series, args.stats)(df[args.column]))


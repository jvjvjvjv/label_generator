#!/usr/bin/python
# -*- coding: utf-8 -*-

## Format:
# 0     1       2       3       4       5   6       7           8   9  10      11
# Order,Family,Species,Country,State,County,City,Description,long.,lat.,Date,Collector

import sys

orders = []
families = []
species = []
with open(sys.argv[1], "r") as f:
    for line in f.readlines()[1:]:
        l = line.split(",")
        orders.append(l[0])
        families.append(l[1])
        species.append(l[2])
        # Country: State: County Co.
        print(l[3], ": ", l[4], ": ", l[5], " Co.", sep="")
        # Town, Description
        print(l[6], ", ", l[7], sep="")
        # Coordinataes
        print(l[8], "°, ", l[9], "°", sep="")
        # Date
        print(l[10])
        # Collector coll.
        print(l[11].strip("\n"), " coll.", "\n",  sep="")

    print("ORDERS:", *set(orders), "", sep="\n")
    print("FAMILIES:", *filter(None,families), "", sep="\n")
    print("SPECIES:", *filter(None,species), "", sep="\n")

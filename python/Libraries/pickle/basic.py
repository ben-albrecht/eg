#!/usr/bin/env python3
import pickle

colors = { "lion": "yellow", "turtle" : "green" }

pickle.dump(colors, open("save.p", "wb"))

newcolors = pickle.load(open("save.p", "rb"))

print(newcolors)

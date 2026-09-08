#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge week-sectioned album table into one single table."""
SRC = "/workspace/.uploads/_album_table_weeks1_18.md"
OUT = "/workspace/.uploads/_album_table_weeks1_18_merged.md"

header = sep = None
rows = []
with open(SRC, encoding="utf-8") as f:
    for line in f.read().splitlines():
        if not line.startswith("|"):
            continue
        if line.startswith("| :"):
            if sep is None:
                sep = line
            continue
        if line.startswith("| Type |"):
            if header is None:
                header = line
            continue
        rows.append(line)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(header + "\n" + sep + "\n" + "\n".join(rows) + "\n")

print("data rows:", len(rows))
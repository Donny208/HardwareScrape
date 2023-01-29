#!/bin/bash

git reset --hard
git pull
source activate HardwareScrape
python -m src.main
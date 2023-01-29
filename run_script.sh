#!/bin/bash

git reset --hard
git pull
chmod +x ./run_script
source activate HardwareScrape
python -m src.main
#!/bin/bash

git reset --hard
git pull
chmod +x ./run_script.sh
source activate HardwareScrape
python -m src.main
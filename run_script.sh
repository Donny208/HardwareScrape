#!/bin/bash

cd "${0%/*}"
git reset --hard
git pull
chmod +x ./run_script.sh
export PATH=/home/pi/berryconda3/bin:$PATH
source activate HardwareScrape
python -m src.main
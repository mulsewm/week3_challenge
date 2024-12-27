# Data Version Control Setup
# Run this script to initialize DVC and track datasets

import os
import subprocess

def setup_dvc():
    subprocess.run(['dvc', 'init'])
    os.makedirs('data', exist_ok=True)
    subprocess.run(['dvc', 'add', 'data'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'DVC initialized and data tracked'])

if __name__ == "__main__":
    setup_dvc()

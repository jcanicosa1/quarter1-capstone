- `pip install -r requirements.txt`
- `python3 run_luigi.py salary.yml`
  - for verbose debugging: `python3 run_luigi.py --verbose salary.yml`
  - to replace existing output file (specified in yml), otherwise will resume: `python3 run_luigi.py --replace salary.yml`
# ASVK Course

## Deploy

python -m pip install --upgrade pip
or located in .venv: pip install --upgrade pip

pip install -r requirements.txt


## [for readline]
The package libreadline is for running applications using readline command

and the package libreadline-dev is for compiling and building readline application.
(source: https://askubuntu.com/questions/194523/how-do-i-install-gnu-readline)

sudo apt get update && sudo apt get install -y libreadline-dev

## [run test]
python -m pytest -s -v <some folder with task or folder tests or . to run all>
always use:
-v or --verbose (show name test)
-s (show prints)

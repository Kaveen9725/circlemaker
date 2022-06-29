mkdir output_files
mkdir reports\images
%cd%\venv\scripts\python -m pip install -r %cd%\requirements.txt
%cd%\venv\scripts\python -m pytest -k image -v --html=%cd%\reports\holopot.html
copy output_files reports\images
del /F /Q output_files

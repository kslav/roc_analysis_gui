
## ROC Analysis through a simple, graphical user interface

### Assumptions
1. The input (for "Select Excel File", Figure 1) is a path to an Excel file (.xlsx) that contains columns named "Confidence" and "Actual", where the former contains probabilities outputted by the classification model and the latter contains actual outcomes (1s and 0s). 
2. You have a sufficient sample size to do ROC analysis. The ROC plot and corresponding AUC value will not exist if your data has no positive findings. 

<img src="assets/Figure1.png" width="500">

### Installation
1. This codebase assumes you're running `Python 3.10.0`. For managing Python version with ease, you might consider installing and managing Python with `pyenv` as described in this [Medium article](https://medium.com/marvelous-mlops/the-rightway-to-install-python-on-a-mac-f3146d9d9a32). These instructions are from the perspective of using `pyenv`.
2. The GUI relies on the `Tkinter` library, which is typically installed as a separate package from Python. Homebrew can be used to install this package on mac OS. The top answer in this [Stackoverflow post](https://stackoverflow.com/questions/59987762/python-tkinter-modulenotfounderror-no-module-named-tkinter) worked for the macbook on which this GUI was developed. If `python -m tkinter -c "tkinter._test()"` does not return the image in Figure 2, please follow the instructions in the linked post.

<img src="assets/Figure2.png" width="300">

3. Using pyenv, create a virtual environment with Python 3.10.0 by running `pyenv virtual 3.10.0 [name_of_env]`. Activate the environment with `pyenv local [name_of_env]`. You will know the environment is activated when you see ([name_of_env]) at the very start of the current line in the command line. 
4. Run `pip install -r requirements.txt `.
5. Finally, you can launch the GUI with `python compute_AUC_GUI.py`. It may take 10s of seconds for the window to launch. Now you're ready to generate plots!

### Using the GUI
1. 



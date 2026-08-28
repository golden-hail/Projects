import os

# get files list from os directory
files = os.listdir('.')

# create the list of 'plot_' scripts/files to run 
plot_scripts = [file for file in files if 'plot_' in file]

'''
Note, currently using runpy to run plot_ scripts due to them not being def()
'''

import runpy

# Create a dictionary or list of function handles using lambda
plot_handles = {
    script: (lambda s=script: runpy.run_path(s)) for script in plot_scripts
}

# Loop through all plot functions
for script_name, run_script in plot_handles.items():
    print(f"Running {script_name}...")
    try:
        run_script()
    except:
        print(f'Error Running {script_name}')

######################################
# If my plot scripts become functions...
######################################

# import importlib.util
# from pathlib import Path


# def get_plot_function(script_path, function_name="run"):
#     """Dynamically loads a .py file and returns a handle to a specific function."""
#     path = Path(script_path)
#     module_name = path.stem  # Gets filename without .py extension

#     spec = importlib.util.spec_from_file_location(module_name, path)
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)

#     # Return the function handle from the loaded module
#     return getattr(module, function_name)


# plot_scripts = [
#     "plot_shmons_per_game.py",
#     "plot_shmons_types.py",
#     "plot_shmon_dates.py",
#     "plot_shmon_genders.py",
# ]

# # 1. Create a list of function handles
# plot_funcs = [get_plot_function(script, "run") for script in plot_scripts]

# # 2. Execute them one by one
# for plot_func in plot_funcs:
#     plot_func()

################
# Consider
################
# user names feed in
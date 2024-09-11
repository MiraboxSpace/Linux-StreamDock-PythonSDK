import os
import sys

# Define and update LD_LIBRARY_PATH
os.environ['LD_LIBRARY_PATH'] = module_path = os.path.dirname(os.path.abspath(__file__))
# Add module_path to sys.path
if module_path not in sys.path:
    sys.path.insert(0, module_path)

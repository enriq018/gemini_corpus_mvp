import os
import sys

def add_project_root_to_sys_path(levels_up=3):
    """
    Adds the project root directory to sys.path for local imports.
    
    Args:
        levels_up (int): The number of directory levels to go up to find the project root.
    """
    current_dir = os.path.abspath(__file__)
    project_root = current_dir
    for _ in range(levels_up):
        project_root = os.path.dirname(project_root)
    
    if project_root not in sys.path:
        sys.path.append(project_root)

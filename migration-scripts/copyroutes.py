import os
import shutil

# Variables for paths and folder names
base_path = os.path.expanduser("~/projects")
ci3_folder = "ci3-news"
ci4_folder = "ci4-news"

# Paths to the config files
ci3_config_path = os.path.join(base_path, ci3_folder, "application", "config", "routes.php")
ci4_config_path = os.path.join(base_path, ci4_folder, "app", "Config", "Routes.php")

try:
  # Check if the CI3 config file exists
  if not os.path.exists(ci3_config_path):
    raise FileNotFoundError(f"The source file '{ci3_config_path}' does not exist.")

  # Ensure the target directory exists
  os.makedirs(os.path.dirname(ci4_config_path), exist_ok=True)

  # Copy CI3 config file to CI4 config directory (updated paths)
  shutil.copyfile(ci3_config_path, ci4_config_path)
  print(f"Copied '{ci3_config_path}' to '{ci4_config_path}'")

except Exception as e:
  print(f"An error occurred while copying the config file: {e}")


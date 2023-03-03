import os
import sys
import winreg as reg


# Get path of current working directory and python.exe
cwd = os.getcwd()
python_exe = sys.executable


# optional hide python terminal in windows
hidden_terminal = '\\'.join(python_exe.split('\\')[:-1])+"\\pythonw.exe"


format_list = [".png", ".jpg"]  # List of image format
for format in format_list:
	# Set the path of the context menu (right-click menu)
	key_path = f'SystemFileAssociations\\\\{format}\\\\Shell\\\\Cropper\\\\' # Change 'Organiser' to the name of your project


	# Create outer key
	key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
	command_name = "Crop the image"                         # Change the command_name to your script
	reg.SetValue(key, '', reg.REG_SZ, f'&{command_name}')


	# create inner key
	key1 = reg.CreateKey(key, r"command")
	script_name = "cropper.py"
	# reg.SetValue(key1, '', reg.REG_SZ, python_exe + f' "{cwd}\\{script_name}" "%1"') # change 'cropper.py' to the name of your script
	reg.SetValue(key1, '', reg.REG_SZ, hidden_terminal + f' "{cwd}\\{script_name}" "%1"')  # use to to hide terminal
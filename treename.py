import uproot

# Path to the ROOT file
root_file_path = r"C:\root_scripts\ddsim.root"

# Open the ROOT file
file = uproot.open(root_file_path)

# List all keys in the ROOT file
keys = file.keys()
print(keys)

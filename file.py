# File Location
fileLocation = "D:\Documents\GitRepos\pyhandling\/file1.txt"

# Read
with open(fileLocation, 'r') as fileR:
    content = fileR.read()
    print(content)

# Write (Strict)
with open(fileLocation, 'w') as fileW:
    fileW.write("New Data")

# Append (Non-Strict)
with open(fileLocation, 'a') as fileA:
    fileA.write("New Data & New File")

# Read/Write (Strict)
with open(fileLocation, 'r+') as fileRW:
    fileRW.write("File needs to be present before overwriting data")

# Write/Read (Non-Strict)
with open(fileLocation, 'w+') as fileWR:
    fileWR.write("File will be created with new data else overwrite existing data")

# Append/Read (Non-Strict)
with open(fileLocation, 'a+') as fileAR:
    fileAR.write("File will be created and data will be appended to existing data")
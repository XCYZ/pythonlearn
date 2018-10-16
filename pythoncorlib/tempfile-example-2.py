import tempfile

file = tempfile.TemporaryFile()

for i in range(100):
    file.write("*"*1000)
print file
file.close()

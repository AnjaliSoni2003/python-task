try:
    file1=open('sample.txt','r')
    reading_file=file1.read()
    print(reading_file)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

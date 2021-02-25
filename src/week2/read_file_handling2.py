PATH = '/home/srujan/Documents/github/pcap/src/data/emp_data.txt'

read_file = open(PATH,'r')

# read whole file
#whole_file = read_file.read()
#print(whole_file)

# single line
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
read_file.close()



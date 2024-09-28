def reverse_file(input_fileName,output_fileName) :
    try :
        with open(input_fileName,'r') as input_file, open (output_fileName,'w') as output_file :
            lines = input_file.readlines()
            lines.reverse()
            print(lines)
            output_file.writelines(lines)
    except FileNotFoundError :
        print(f"file :{input_fileName} not found")

input_file = "FIleIO/xyz.txt"
output_file = "outputfile.txt"
reverse_file(input_file,output_file)
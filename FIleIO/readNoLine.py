def count_line(filename) :
    try :
        with open(filename,"r") as file :
            line_count = sum(1 for _ in file)
            return line_count               
    except FileNotFoundError as FNFE :
        print(FNFE)
        
count = count_line("FIleIO/xyz.txt")
print(f"count :{count}")
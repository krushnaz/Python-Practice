def check_occurance(content,occur_string) :
    count = 0
    for i in content :
        if i in occur_string :
            count +=1;
    return count

def main() :
    occur_string = "adgefkfe"
    try :
        with open("QP_Practice/outputfile.txt",'r') as file :
            content = file.read()
            count = check_occurance(content,occur_string)
            print(f"count :{count}")
    except FileNotFoundError :
        print("file not found")
        
main()

email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]\.[a-zA-Z]{2,}$'
password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&?*])[A-Za-z0-9!@#$&?*]{8.20}$'
url = r'^(https|ftp)://[^\s/$.?#][^\s]*$'
date = r'^(\d{2})-(\d{2}|[A-Za-z]+)-(\d{4})'

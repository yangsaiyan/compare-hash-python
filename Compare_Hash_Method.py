import os
import hashlib

def calculate_hash(file_path):
    #Calculate the hash of a file using SHA-256 algorithm.
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as f:
        
        for byte_block in iter(lambda: f.read(4096), b""):
            
            sha256_hash.update(byte_block)
    
    return sha256_hash.hexdigest()

def saveHash(directory_to_scan):
    #Save hashes into variable to use in other functions
    openHash = directory_to_scan.replace("/", "-") + ".txt"

    known_good_hashes = dict()

    with open(openHash, 'r') as file:
        
        for line in file:
            
            temp = line.split(': ')
            
            known_good_hashes[temp[0]] = temp[1]

    return known_good_hashes

def scan_files(directory_path):
    #Scan and compare current hash and hash stored before
    known_good_hashes = saveHash(directory_path)
        
    for file_name in os.listdir(directory_path):
        
        file_path = os.path.join(directory_path, file_name)
        
        if os.path.isfile(file_path):
            
            file_hash = calculate_hash(file_path)

        else: 
            
            return False

        for key, value in known_good_hashes.items():
            
            if file_name == key and file_hash == value.strip():

                print(f"{file_name}: Trusted")

            elif file_name == key and file_hash != value.strip():

                print(f"{file_name}: Potentially malicious!")

    return True

def storeHash(output_file, directory_path):
    #Save hashes into txt file
    with open(output_file, "w") as f:
        f.write

    f.close()

    for file_name in os.listdir(directory_path):
        
        file_path = os.path.join(directory_path, file_name)
        
        if os.path.isfile(file_path):

            file_hash = calculate_hash(file_path)

        with open(output_file, "a") as f:

            f.write(f"{file_name}: {file_hash}\n")

    f.close

    return True

if __name__ == "__main__":

    while True:
            
            print("\nExample: C:\\Users\\UTAR\\Documents\n")

            print("Please enter the directory: ")

            directory_path = input()

            directory_path = directory_path.replace("\\", "/")

            output_file = os.path.join(os.path.dirname(__file__) , directory_path.replace("/", "-") + ".txt")

            if os.path.exists(directory_path):

                print(f"The directory '{directory_path}' exists.")

                break
            
            else:

                print(f"The directory '{directory_path}' does not exist.\n Please enter again!")


    while True:

            selection = input("\nEnter your selection (1: Store Hash, 2: Scan Files, 0: Exit): ")

            if selection == "1":
                if storeHash(output_file, directory_path):

                    print("Hashes Stored!")

                else : 

                    print("Failed to store hash!")

            elif selection == "2":

                if not scan_files(directory_path):

                    print("Failed to scan file!")

            elif selection == "0":

                print("Exiting...")

                break

            else:

                print("Invalid selection. Please enter 1, 2, or 0.")
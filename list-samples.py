import os
import sys
import csv
import glob

def get_next_file_number():
    """
    Determines the next available file number for the tracklist CSV files.
    Returns the next number formatted as a 4-digit string (e.g., '0000', '0001').
    """
    # Create datasets directory if it doesn't exist
    datasets_dir = os.path.join(os.getcwd(), "datasets")
    if not os.path.exists(datasets_dir):
        os.makedirs(datasets_dir)
    
    # Find all existing tracklist files
    existing_files = glob.glob(os.path.join(datasets_dir, "????-tracklist.csv"))
    
    if not existing_files:
        return "0000"
    
    # Extract numbers from filenames
    numbers = []
    for file_path in existing_files:
        filename = os.path.basename(file_path)
        try:
            number = int(filename[:4])
            numbers.append(number)
        except ValueError:
            continue
    
    # Return next number formatted as 4 digits
    if numbers:
        next_num = max(numbers) + 1
    else:
        next_num = 0
    
    return f"{next_num:04d}"

def write_files_to_csv(directory_path):
    """
    Takes a directory path and writes all file paths to a CSV file in the datasets subdirectory.
    The file is named using an incremental numbering scheme: ####-tracklist.csv
    Files are sorted alphabetically.
    
    Args:
        directory_path (str): Path to the directory to process
    """
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory")
        sys.exit(1)
    
    # Get all files from the directory (non-recursive)
    files = [os.path.join(directory_path, f) for f in os.listdir(directory_path) 
             if os.path.isfile(os.path.join(directory_path, f))]
    
    # Sort files alphabetically
    files.sort()
    
    # Create datasets directory if it doesn't exist
    datasets_dir = os.path.join(os.getcwd(), "datasets")
    if not os.path.exists(datasets_dir):
        os.makedirs(datasets_dir)
    
    # Get the next available file number
    file_number = get_next_file_number()
    
    # Create output filename
    output_file = os.path.join(datasets_dir, f"{file_number}-tracklist.csv")
    
    # Write to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['audio'])
        
        # Write file paths
        for file_path in files:
            writer.writerow([file_path])
    
    print(f"Successfully wrote {len(files)} file paths to {output_file}")

if __name__ == "__main__":
    # Check if directory path is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    write_files_to_csv(directory_path)

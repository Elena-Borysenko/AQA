import os

root_folder = os.getcwd()

def scan_directory(folder):
    largest_file = ('', 0)

    with open('iles_size.txt', 'w') as f:
        for root, dirs, files in os.walk(folder):
            for filename in files:
                file_path = os.path.join(root, filename)
                file_size = os.path.getsize(file_path)
                f.write(f'{filename}: {file_size} bytes\n')

                if file_size > largest_file[1]:
                    largest_file = (filename, file_size)

    return largest_file

largest_file_info = scan_directory(root_folder)

if largest_file_info[0]:
    print(f'Largest file: {largest_file_info[0]}, Size: {largest_file_info[1]} byte')
else:
    print('There are no files in folder.')


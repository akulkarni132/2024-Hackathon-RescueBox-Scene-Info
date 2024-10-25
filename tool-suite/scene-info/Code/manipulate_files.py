import os
import shutil
import xml.etree.ElementTree as ET
import pandas as pd


def move_all_files(folder, dest_folder):
    subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]
    for sub in subfolders:
        folder_name = os.path.basename(sub)  # Get the name of the subfolder
        for f in os.listdir(sub):
            src = os.path.join(sub, f)
            # Create a new filename by appending the folder name to the original filename
            new_filename = f"{folder_name}---{f}"
            dst = os.path.join(dest_folder, new_filename)

            # Move the file to the main folder with the new name
            #shutil.move(src, dst)
            shutil.copy(src, dst)

def extract_xml_names():
    directory = r"Hackathon\Data\MITAnnotationsUnnested"

    # Initialize a list to hold the data
    data = []
    count = 0
    # Iterate over all XML files in the specified directory
    for filename in os.listdir(directory):
        count += 1
        if count % 100 == 0:
            print(f"{count}/15000")
        if filename.endswith('.xml'):
            try:
                # Construct the full file path
                file_path = os.path.join(directory, filename)

                # Parse the XML file
                tree = ET.parse(file_path)
                root = tree.getroot()

                # Extract all "name" tags and their text
                names = root.findall('.//name')  # Adjust the XPath if needed

                # Create a list to hold the names
                name_list = [name.text.replace('\n', '').strip() for name in names if
                             name.text]  # Remove newlines and whitespace

                name_list = list(set(name_list))
                # Join the names into a single string
                name_string = ', '.join(name_list)

                # Append the filename and the combined names to the data list
                data.append({'file': filename, 'unique_names': name_string})
            except:
                data.append({'file': filename, 'unique_names': None})
                print(f"Error in {count}")

    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(data)
    df.to_csv("xml_stuff.csv")
    # Display the DataFrame
    print(df)


move_all_files(folder = r"C:\Users\aholleran\Downloads\Hackathon\Data\MITImages_2\indoorCVPR_09annotations\Annotations",
                dest_folder = r"C:\Users\aholleran\Downloads\Hackathon\Data\MITAnnotationsUnnested")
move_all_files(folder = r"C:\Users\aholleran\Downloads\Hackathon\Data\MITImages\indoorCVPR_09\Images",
                dest_folder = r"C:\Users\aholleran\Downloads\Hackathon\Data\Unnested")
extract_xml_names()

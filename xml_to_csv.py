import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     member[0].text,
                     )
            xml_list.append(value)
    # column_name = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class']
    xml_df = pd.DataFrame(xml_list)
    return xml_df


def main():  # this is the part we change to work with our setup
    for directory in ['dataset\\annotations\\deer', 'dataset\\annotations\\geese']:
        image_path = os.path.join(os.getcwd(), '{}'.format(directory))
        xml_df = xml_to_csv(image_path)
        filepath = '{}_labels.csv'.format(directory)
        with open(filepath, 'w+') as output_file:
            xml_df.to_csv(output_file, index=False, header=False, line_terminator='\n')
    print('Successfully converted xml to csv.')


if __name__ == '__main__':
    main()

import os
import xml.etree.ElementTree as ET

classes = ["With Helmet", "Without Helmet"] # <-- exact class from your XML file

def convert(xml_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith('.xml'):
            continue

        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()

        size = root.find('size')
        if size is None:
            print(f"[WARNING] No <size> tag in {xml_file}")
            continue
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        objects_found = 0
        with open(os.path.join(out_folder, xml_file.replace('.xml', '.txt')), 'w') as txt_file:
            for obj in root.iter('object'):
                cls = obj.find('name').text
                if cls not in classes:
                    print(f"[WARNING] Class '{cls}' not in classes list for file: {xml_file}")
                    continue
                cls_id = classes.index(cls)
                xmlbox = obj.find('bndbox')
                if xmlbox is None:
                    print(f"[WARNING] No <bndbox> for object in {xml_file}")
                    continue

                b = (
                    float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                    float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text)
                )

                x_center = ((b[0] + b[2]) / 2) / w
                y_center = ((b[1] + b[3]) / 2) / h
                bbox_width = (b[2] - b[0]) / w
                bbox_height = (b[3] - b[1]) / h

                txt_file.write(f"{cls_id} {x_center} {y_center} {bbox_width} {bbox_height}\n")
                objects_found += 1

        if objects_found == 0:
            print(f"[INFO] No objects found in {xml_file}, empty file created.")

convert('Dataset/annotations', 'Dataset/labels')

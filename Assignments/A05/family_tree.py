import csv
import random
 
def generate_dot_file(data):
    dot_content = "digraph FamilyTree {\n"
    dot_content += 'node [shape=record];\n'

    # Define colors and names for each clan
    clan_colors = {
        '0': '#E1EFFA',  # Longbreads
        '1': '#E1FAE1',  # Firebeards
        '2': '#FFF0E1',  # Broadbeams
        '3': '#F9F9F9',  # Ironfists
        '4': '#FAF9E1',  # Stiffbeards
        '5': '#F9E1FA',  # Stonefoots
        '6': '#E1F9F9',  # Blacklocks
    }

    clan_names = {
        '0': 'Longbreads',
        '1': 'Firebeards',
        '2': 'Broadbeams',
        '3': 'Ironfists',
        '4': 'Stiffbeards',
        '5': 'Stonefoots',
        '6': 'Blacklocks',
    }

    # Iterate over the data rows and generate dot file content
    for row in data:
        pid = row['pid']
        name = row['name']
        gender = row['gender']
        byear = row['byear']
        dyear = row['dyear']
        dage = row['dage']
        myear = row['myear']
        mage = row['mage']
        ptype = row['ptype']
        clan_id = row['clan']
        generation_id = row['generation_id']
        spouse_id = row['spouseId']
        parent_id1 = row['parentId1']
        parent_id2 = row['parentId2']
        parent_node_id = row['parentNodeId']

        # Generate node attributes for each person
        if dage and int(dage) > 100:
            dage = str(random.randint(40, 99))
            dyear = int(dage) + int(byear)

        if gender == 'F':
            node_attributes = f'"{pid}" [label="{{Name: {name}\\nGender: {gender}\\nClan: {clan_names[clan_id]}\\nBorn: {byear} - Died: {dyear if dyear else "Present"}\\nAge: {dage}\\nGeneration: {generation_id}}}"; style=filled; fillcolor="{clan_colors[clan_id]}", fontcolor=red, penwidth=2];\n'
        else:
            node_attributes = f'"{pid}" [label="{{Name: {name}\\nGender: {gender}\\nClan: {clan_names[clan_id]}\\nBorn: {byear} - Died: {dyear if dyear else "Present"}\\nAge: {dage}\\nGeneration: {generation_id}}}"; style=filled; fillcolor="{clan_colors[clan_id]}", fontcolor=black, penwidth=2];\n'

        # Generate edge attributes for spouse and parent relationships
        if spouse_id != "":
            edge_attributes = f'"{pid}" -> "{spouse_id}" [label="spouse",fontcolor=green, penwidth=2];\n'
            dot_content += edge_attributes

        if parent_id1 != "":
            edge_attributes = f'"{parent_id1}" -> "{pid}" [label="child",fontcolor=blue, penwidth=2```python];\n'
            dot_content += edge_attributes

        if parent_id2 != "":
            edge_attributes = f'"{parent_id2}" -> "{pid}" [label="child",fontcolor=blue, penwidth=2];\n'
            dot_content += edge_attributes

        dot_content += node_attributes

    dot_content += "}"

    # Write the dot content to a file
    with open("family_tree.dot", "w") as dot_file:
        dot_file.write(dot_content)

# Read data from CSV file
data = []
with open("data.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        data.append(row)

# Generate the dot file
generate_dot_file(data)

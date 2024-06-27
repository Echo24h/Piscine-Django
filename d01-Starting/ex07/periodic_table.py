# periodic_table.py

def read_periodic_table_data(file_path):
    elements = []
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():  # check if line is not empty
                parts = line.strip().split(', ')
                if len(parts) == 5:
                    element_data = {
                        'name': parts[0].split('=')[0].strip(),
                        'position': int(parts[0].split(':')[1].strip()),
                        'number': int(parts[1].split(':')[1].strip()),
                        'symbol': parts[2].split(':')[1].strip(),
                        'molar': float(parts[3].split(':')[1].strip()),
                        'electron': parts[4].split(':')[1].strip()
                    }
                    elements.append(element_data)
    return elements

def generate_html(elements, output_file):
    with open(output_file, 'w') as f:
        f.write('<!DOCTYPE html>\n')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<title>Periodic Table of Elements</title>\n')
        f.write('<style>\n')
        f.write('table {\n')
        f.write('    border-collapse: collapse;\n')
        f.write('    width: 100%;\n')
        f.write('}\n')
        f.write('td, th {\n')
        f.write('    border: 1px solid black;\n')
        f.write('    padding: 8px;\n')
        f.write('    text-align: center;\n')
        f.write('}\n')
        f.write('td {\n')
        f.write('    width: 200px;\n')
        f.write('    height: 200px;\n')
        f.write('}\n')
        f.write('td.empty {\n')
        f.write('    border: none\n')
        f.write('}\n')
        f.write('ul {\n')
        f.write('    list-style-type: none;\n')
        f.write('    margin: 0;\n')
        f.write('}\n')
        f.write('h4 {\n')
        f.write('    margin: 0;\n')
        f.write('}\n')
        f.write('h3 {\n')
        f.write('    font-size: 40px;\n')
        f.write('    margin: 0;\n')
        f.write('}\n')
        f.write('</style>\n')
        f.write('</head>\n')
        f.write('<body>\n')
        f.write('<table>\n')
        
        number = 1
        for row in range(7):  # 7 rows in the periodic table
            f.write('<tr>\n')
            for col in range(18):  # 18 columns in the periodic table
                element_data = next((elem for elem in elements if elem['position'] == col and elem['number'] == number), None)
                if element_data:
                    
                    if number == 56 or number == 88:
                        number += 16
                    else:
                        number += 1

                    f.write('<td>\n')
                    f.write(f'<h4>N° {element_data["number"]}</h4>\n')
                    f.write(f'<h3>{element_data["symbol"]}</h3>\n')
                    f.write(f'<h4>{element_data["name"]}</h4>\n')
                    f.write(f'<p>{element_data["molar"]}</p>\n')
                    f.write(f'<p>{element_data["electron"]}</p>\n')
                    f.write('</td>\n')
                else:
                    f.write('<td class="empty"></td>\n')
            f.write('</tr>\n')

        f.write('</table>\n')
        f.write('</body>\n')
        f.write('</html>\n')

if __name__ == "__main__":
    
    input_file = "periodic_table.txt"
    output_file = "periodic_table.html"
    
    elements = read_periodic_table_data(input_file)
    generate_html(elements, output_file)
    print(f"HTML file generated: {output_file}")
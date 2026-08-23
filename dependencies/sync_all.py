with open('solutions/Electrical_Circuits_and_Machines_Solutions_Master.tex', 'r') as f:
    text = f.read()

# Clean up mesh current arrows from Diagram 1.3 problem statement box
old_mesh_lines = """  % Mesh current labels
  \\draw (1.75, 2.0) node{\\Large $\\circlearrowright$} node[above=0.15cm]{$I_1$};
  \\draw (5.25, 3.0) node{\\Large $\\circlearrowright$} node[above=0.15cm]{$I_2$};
  \\draw (5.25, 1.0) node{\\Large $\\circlearrowright$} node[above=0.15cm]{$I_3$};"""

if old_mesh_lines in text:
    text = text.replace(old_mesh_lines, '')
    print('Removed overlapping mesh current labels from Diagram 1.3')

with open('solutions/Electrical_Circuits_and_Machines_Solutions_Master.tex', 'w') as f:
    f.write(text)

with open('Electrical_Circuits_and_Machines_Solutions_Master.tex', 'w') as f:
    f.write(text)

with open('solutions/make_latex_book.py', 'w') as f:
    f.write("import subprocess\nimport os\n\nlatex_source = " + repr(text) + "\n\n")
    f.write("""def compile_pdf():
    tex_path = 'Electrical_Circuits_and_Machines_Solutions_Master.tex'
    with open(tex_path, 'w') as f:
        f.write(latex_source)
    print('Wrote LaTeX master source.')
    
    for i in range(2):
        print(f'Running pdflatex pass {i+1}...')
        res = subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_path], capture_output=True, text=True)
        if res.returncode != 0:
            print(f'Error during pdflatex pass {i+1}:')
            print(res.stdout[-1500:])
            return False
    print('Compilation successful!')
    return True

if __name__ == '__main__':
    compile_pdf()
""")
print('Successfully synced master tex and make_latex_book.py')

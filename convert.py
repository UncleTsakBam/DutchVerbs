import json
import pandas as pd

# Το μονοπάτι του Excel σου στο τοπικό δίκτυο
excel_path = r'C:\Users\atsakonas\Documents\project\Python_coding\DutchVerbs\woordenlijst.xlsx'

# Φόρτωση Excel
df = pd.read_excel(excel_path)

verbs_list = []
for idx, row in df.iterrows():
  verb_obj = {
      'id': str(idx + 1),
      'infinitive': str(row.iloc[0]).strip(),  # Στήλη απαρεμφάτου (A = 0)
      'translation': (
          str(row.iloc[1]).strip() if pd.notna(row.iloc[1]) else ''
      ),  # Στήλη B (1)
      'ovt1': str(row.iloc[6]).strip() if pd.notna(row.iloc[7]) else '',  # Στήλη G (6)
      'ovt2': str(row.iloc[7]).strip() if pd.notna(row.iloc[7]) else '',  # Στήλη H (7)      
      'vtt': str(row.iloc[8]).strip() if pd.notna(row.iloc[8]) else '',  # Στήλη I (8)
      'weight': 1,
  }
  verbs_list.append(verb_obj)

# Αποθήκευση ως JavaScript αρχείο (verbs.js)
with open('verbs.js', 'w', encoding='utf-8') as f:
  f.write('const verbsData = ')
  json.dump(verbs_list, f, ensure_ascii=False, indent=2)
  f.write(';')

print(f'Επιτυχής εξαγωγή {len(verbs_list)} ρημάτων στο verbs.js!')
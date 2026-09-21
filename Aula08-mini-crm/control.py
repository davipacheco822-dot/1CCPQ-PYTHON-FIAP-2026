from pathlib import Path
import json, csv

DATA_DIR = Path(__file__).resolve().parent / "data"
DB_PATH = DATA_DIR / "leads.json"

def read_leads():
    if not DB_PATH.exists():
        return []

    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

def create_lead(lead_dict):
    leads = read_leads()
    leads.append(lead_dict)
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent = 2), encoding="utf-8")

def read_leads_search(query):
    "Busca leads de acordo com a query e retorna uma lista de resultados"
    leads = read_leads()
    results = []

    for i, lead in enumerate(leads):
        txt_lead = f"{lead["name"]} - {lead['email']}".lower()

        if query.lower() in txt_lead:
            results.append((i, lead))
    return results

def export_csv():
    """Exporta TODOS os leads para CSV e RETORNA o caminho do CSV"""
    path_csv = DATA_DIR / "leads.csv"
    leads = read_leads()

    try:
        with path_csv.open("w", newline="", encoding="utf-8") as file_csv:
            writer = csv.DictWriter(file_csv, leads[0].keys())
            writer.writeheader()
            for row_dict in leads:
                writer.writerow(row_dict)
        return path_csv
    except PermissionError:
        return None
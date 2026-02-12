import pandas as pd
from bs4 import BeautifulSoup
import argparse
import re
import os
import sys

def normalize_column_name(columns, keyword):
    """
    Helper function to find a column name containing a specific keyword 
    (handling potential newlines or bilingual text in headers).
    """
    for col in columns:
        if keyword in str(col):
            return col
    return None

def extract_log_content(full_text):
    """
    Extracts text between 'test begin >>>' and '>>> test end'.
    """
    pattern = r"test begin >>>(.*?)>>> test end"
    match = re.search(pattern, full_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def main():
    parser = argparse.ArgumentParser(description="Generate Test Report from HTML Source to Excel Target.")
    parser.add_argument("--source", required=True, help="Path to the source HTML file")
    parser.add_argument("--target", required=True, help="Path to the target Excel file (xlsx)")
    
    args = parser.parse_args()
    
    source_path = args.source
    target_path = args.target

    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' not found.")
        sys.exit(1)
    if not os.path.exists(target_path):
        print(f"Error: Target file '{target_path}' not found.")
        sys.exit(1)

    print(f"Loading source HTML: {source_path}...")
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'lxml') # Using lxml for speed, fallback to html.parser if needed
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        sys.exit(1)

    print("Parsing HTML content map...")
    # Build a map of { full_test_case_name_in_html : log_content }
    # Structure: <tr><td><div class='testcase'>NAME</div></td> ... <td><div class='popup_window'><pre>LOG</pre></div></td></tr>
    html_test_data = {}
    
    # Find all rows that might contain test cases
    rows = soup.find_all('tr')
    for row in rows:
        testcase_div = row.find('div', class_='testcase')
        if testcase_div:
            test_name_html = testcase_div.get_text(strip=True)
            
            # Find the popup window inside the same row (usually contains the pre tag)
            popup_div = row.find('div', class_='popup_window')
            if popup_div:
                pre_tag = popup_div.find('pre')
                if pre_tag:
                    html_test_data[test_name_html] = pre_tag.get_text()

    print(f"Found {len(html_test_data)} test execution records in source HTML.")

    print(f"Loading target Excel: {target_path}...")
    try:
        # Load the specific sheet
        sheet_name = "Test Case Report"
        df = pd.read_excel(target_path, sheet_name=sheet_name)
    except ValueError:
        print(f"Error: Sheet '{sheet_name}' not found in target Excel.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        sys.exit(1)

    # Identify key columns (handling potential bilingual headers with newlines)
    col_id_name = normalize_column_name(df.columns, "Test Case No")
    col_log_name = normalize_column_name(df.columns, "Test Log")

    if not col_id_name:
        print("Error: Column 'Test Case No' (or similar) not found in Excel.")
        sys.exit(1)
    if not col_log_name:
        print("Error: Column 'Test Log' (or similar) not found in Excel.")
        sys.exit(1)

    print(f"Processing using columns: ID='{col_id_name}', Log='{col_log_name}'")

    updated_count = 0
    
    # Iterate through Excel rows and update content
    for index, row in df.iterrows():
        excel_case_id = str(row[col_id_name]).strip()
        
        if not excel_case_id or excel_case_id.lower() == 'nan':
            continue

        # Logic: Find if source HTML contains a test case name that includes the Excel ID substring
        # Requirement: "source中检索到tcfTcs_...包含该子串" (HTML ID contains Excel ID)
        matched_html_key = None
        for html_key in html_test_data.keys():
            if excel_case_id in html_key:
                matched_html_key = html_key
                break
        
        if matched_html_key:
            full_log = html_test_data[matched_html_key]
            extracted_log = extract_log_content(full_log)
            
            if extracted_log:
                # Update the DataFrame
                df.at[index, col_log_name] = extracted_log
                updated_count += 1
                # print(f"  Matched: {excel_case_id} -> {matched_html_key}")
            else:
                print(f"  Warning: Markers 'test begin >>>' / '>>> test end' not found for {matched_html_key}")
        else:
            # Optional: Print if no match found (can be noisy)
            # print(f"  No match found in source for: {excel_case_id}")
            pass

    print(f"Updated {updated_count} rows.")

    # Save the file
    output_path = target_path # Overwrite existing or change to 'report_output.xlsx'
    print(f"Saving updated report to {output_path}...")
    try:
        # Use OpenPyXL engine to try and preserve other sheets if possible, 
        # but standard to_excel overwrites. To preserve other sheets, we need a different approach.
        # For this script, we assume rewriting the specific sheet or file is acceptable as per standard automation.
        # To strictly preserve other sheets, we use ExcelWriter with mode='a' and replace=True if supported,
        # or load the whole book with openpyxl. Here we use a safe pandas write-back.
        
        with pd.ExcelWriter(output_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
             df.to_excel(writer, sheet_name=sheet_name, index=False)
             
    except Exception as e:
        # Fallback if mode='a' fails (e.g. if file is open or corrupt)
        print(f"Warning: Could not update existing file in place ({e}). Creating new file.")
        df.to_excel("generated_report_output.xlsx", sheet_name=sheet_name, index=False)
        print("Saved to generated_report_output.xlsx")

    print("Done.")

if __name__ == "__main__":
    main()
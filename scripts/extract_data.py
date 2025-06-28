from notion_client import Client
import json

# Initialize Notion client
notion = Client(auth="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")

# Define your database ID
database_id = "b3b2549a0ee649baa782733b68ba3824"

try:
    # Query the database
    response = notion.databases.query(database_id=database_id)

    # Check if data was retrieved successfully
    if response.get('results'):
        print("✅ API query successful! Here are the first few entries:\n")
        print(json.dumps(response['results'][:1], indent=4))  # Print the first few results
    else:
        print("⚠️ No data found in the database.")
except Exception as e:
    print("❌ API request failed. Error details:")
    print(str(e))


# Function to extract Case ID from the Case ID property
def get_case_id(properties):
    if 'Case ID' in properties and properties['Case ID']['formula']['string']:
        return properties['Case ID']['formula']['string']
    return "N/A"

# Function to extract CPT Code from the Case property
def get_cpt_code(properties):
    if 'Case' in properties and properties['Case']['title']:
        return properties['Case']['title'][0]['text']['content']
    return "N/A"

# Function to extract Case Date from the DOS property
def get_case_date(properties):
    if 'DOS' in properties and properties['DOS']['date']:
        return properties['DOS']['date']['start']
    return "N/A"

# Function to extract Trauma status from the Trauma property
def get_trauma_status(properties):
    if 'Trauma' in properties and properties['Trauma']['checkbox'] is not None:
        return properties['Trauma']['checkbox']
    return False

# Function to extract Case Year from the Training Year property
def get_case_year(properties):
    if 'Training Year' in properties and properties['Training Year']['formula']['string']:
        return properties['Training Year']['formula']['string']
    return "N/A"

# Extract data from the response
cases = []
for result in response['results']:
    properties = result['properties']
    case = {
        'case_id': get_case_id(properties),
        'cpt_code': get_cpt_code(properties),
        'case_date': get_case_date(properties),
        'trauma': get_trauma_status(properties),
        'case_year': get_case_year(properties)
    }
    cases.append(case)

# Print the extracted data
print("\nExtracted Case Data (CPT Codes, Case IDs, Case Dates, Trauma Status, Case Year):")
print(json.dumps(cases, indent=4))
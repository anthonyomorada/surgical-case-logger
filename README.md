# **Surgical Case Logger**
_Automate the process of extracting surgical case data from Notion, cleaning it, and logging it on the ACGME website._

---

## **Overview**
**Surgical Case Logger** automates the end-to-end workflow of logging surgical cases. It extracts data from a Notion database, cleans and standardizes the data, and then enters the information on the ACGME website using Selenium.

This project is designed to improve productivity for surgical residents by minimizing repetitive manual data entry.

---

## **Features**

1. **Data Extraction**
   - Accesses a Notion database through the Notion API.

2. **Data Cleaning**
   - Cleans and formats case data (e.g., procedures, dates, diagnoses).
   - Handles missing or inconsistent fields.

3. **Automated Case Entry**
   - Logs into the ACGME website.
   - Automates form filling and case submission using Selenium.

4. **Error Handling & Logging**
   - Logs errors for failed submissions.
   - Provides feedback on successfully submitted cases.

5. **Optional Notifications**
   - Notifications via email or messaging apps upon completion.

---

## **Requirements**

### **1. Python Environment**
- Python 3.8+
- Install dependencies:
```bash
pip install selenium notion-client pandas
```

### **2. Notion Integration**
- Set up an API integration on the [Notion Developer Portal](https://developers.notion.com).
- Share your case log database with the integration.

### **3. Selenium Setup**
- Install a browser driver (e.g., ChromeDriver) compatible with your browser version.

---

## **Project Structure**
```plaintext
📁 surgical-case-logger/
│
├── 📂 data/                  # Raw and cleaned data files
│   ├── raw_cases.json        # Raw data fetched from Notion
│   └── cleaned_cases.csv     # Cleaned data ready for submission
│
├── 📂 scripts/               # Automation scripts
│   ├── extract_data.py       # Script to fetch data from Notion
│   ├── clean_data.py         # Script to clean and format data
│   └── submit_cases.py       # Script to automate ACGME case entry
│
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/surgical-case-logger.git
cd surgical-case-logger
```

### **2. Set Up Notion Integration**
- Add your Notion API key to the environment:
```bash
export NOTION_API_KEY="your_notion_api_key"
```
- Replace the `database_id` in `extract_data.py` with your Notion database ID.

### **3. Run the Scripts**

1. **Extract Data:**
   ```bash
   python scripts/extract_data.py
   ```

2. **Clean Data:**
   ```bash
   python scripts/clean_data.py
   ```

3. **Submit Cases:**
   ```bash
   python scripts/submit_cases.py
   ```

---

## **Future Plans**
- Add real-time validation for case entries.
- Implement support for bulk uploads via CSV.
- Enhance error handling and add retry logic for failed submissions.
- Integrate notifications for case logging updates.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

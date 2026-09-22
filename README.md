# Security Assessment Toolkit

A Python-based cybersecurity toolkit prototype with a graphical interface for performing basic Nmap-based security assessments and saving scan results as reports.

## Overview

This project was built as a hands-on cybersecurity project to make common Nmap scanning tasks easier to run through a simple graphical interface.

The toolkit allows users to enter a target, select a scan level, run the corresponding Nmap scan, view the results, and save the assessment as a TXT or JSON report.

## Features

* Target input for IP addresses or domains
* Three Nmap scan levels:

  * **Basic** - Standard Nmap scan
  * **Normal** - Service and version detection
  * **Aggressive** - Nmap aggressive scan
* Displays scan results directly in the application
* Save reports in:

  * TXT
  * JSON
* Reports section for viewing previously saved assessments
* Simple dark-themed graphical interface

## Scan Levels

| Level      | Nmap Command        | Purpose                      |
| ---------- | ------------------- | ---------------------------- |
| Basic      | `nmap <target>`     | Basic port scanning          |
| Normal     | `nmap -sV <target>` | Detect services and versions |
| Aggressive | `nmap -A <target>`  | More detailed enumeration    |

## Technologies Used

* **Python**
* **CustomTkinter** - Graphical user interface
* **Nmap** - Network scanning
* **JSON** - Report formatting

## How It Works

The general workflow is:

```text
Enter Target
     ↓
Select Scan Level
     ↓
Run Nmap Scan
     ↓
Display Results
     ↓
Save Assessment Report
```

The application uses Python's `subprocess` module to execute the selected Nmap command and capture its output.

## Reports

The toolkit can save scan results in two formats.

### TXT

A readable text report containing:

* Target
* Scan level
* Report format
* Nmap results

### JSON

A structured report containing the same assessment information in JSON format.

Example structure:

```json
{
    "target": "TARGET",
    "scan_level": "Normal",
    "report_format": "JSON",
    "nmap_results": "Nmap scan output"
}
```

## Screenshots

### Security Dashboard
<img width="671" height="351" alt="Screenshot 2026-09-21 130539" src="https://github.com/user-attachments/assets/2c0e2b02-845e-4c88-b49b-070e076a68fb" />



### Saved Reports
<img width="672" height="357" alt="Screenshot 2026-09-21 130620" src="https://github.com/user-attachments/assets/b3d4c8b4-e3f3-4600-81ec-6aa3679dfa7f" />



### Open Security Report
<img width="668" height="350" alt="Screenshot 2026-09-21 130643" src="https://github.com/user-attachments/assets/6217d2e9-583e-4a05-b7ea-b4cc80dcdc53" />



## Scan Configuration and Results
<img width="671" height="351" alt="Screenshot 2026-09-21 130716" src="https://github.com/user-attachments/assets/fcfca8b2-75c4-434f-9d79-2c117eab7d8f" />

### Requirements

* Python 3.x
* Nmap
* Required Python

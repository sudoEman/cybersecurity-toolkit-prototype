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

![Security Dashboard](screenshots/dashboard.png)

### Scan Results

![Scan Results](screenshots/scan-results.png)

### Saved Reports

![Reports](screenshots/reports.png)

## Installation

### Requirements

* Python 3.x
* Nmap
* Required Python

import customtkinter as ctk
from tkinter import filedialog
import json
import os
from nmap import target_scan

# ============================================================
# APPEARANCE
# ============================================================

ctk.set_appearance_mode("dark")


# ============================================================
# COLOR PALETTE
# ============================================================

BACKGROUND = "#000000"

# Rose Quartz
BOX_PINK = "#F7CAC9"

# Cotton Candy
TEXT_PINK = "#FFB6D9"

# Dusty Pink
HOVER_PINK = "#D99AAE"

# Baby Pink
BORDER_PINK = "#FFC1CC"

# Dark text for inside pink boxes
DARK_TEXT = "#111111"


last_scan_output = ""
last_scan_target = ""
last_scan_level = ""

reports_page = None

last_report_file = ""
# ============================================================
# MAIN WINDOW
# ============================================================

app = ctk.CTk()

app.title("Security Assessment Toolkit")
app.geometry("1100x700")
app.minsize(900, 600)

app.configure(fg_color=BACKGROUND)

# ============================================================
# LEFT SIDEBAR
# ============================================================

sidebar = ctk.CTkFrame(app,width=220,corner_radius=0,fg_color=BACKGROUND,
                       border_width=1,border_color=BORDER_PINK)
sidebar.pack(side="left",fill="y")
sidebar.pack_propagate(False)


# ------------------------------------------------------------
# TOOLKIT TITLE
# ------------------------------------------------------------

logo = ctk.CTkLabel(sidebar,text="SECURITY\nASSESSMENT\nTOOLKIT",font=("Arial", 20, "bold"),
                    text_color=TEXT_PINK,justify="left")
logo.pack(padx=25,pady=(40, 55),anchor="w")

def reset_sidebar_buttons():
    dashboard_button.configure(fg_color=BACKGROUND,text_color=TEXT_PINK)
    reports_button.configure(fg_color=BACKGROUND,text_color=TEXT_PINK)
    settings_button.configure(fg_color=BACKGROUND,text_color=TEXT_PINK)
# ------------------------------------------------------------
# DASHBOARD BUTTON
# ------------------------------------------------------------

def show_dashboard():
    global reports_page
    reset_sidebar_buttons()
    dashboard_button.configure(fg_color=BOX_PINK,text_color=DARK_TEXT)
    if reports_page is not None:
        reports_page.place_forget()
    main_area.lift()    

        
dashboard_button = ctk.CTkButton(sidebar,text="Dashboard",width=170,height=42,
                                 fg_color=BOX_PINK,hover_color=HOVER_PINK,
                                 text_color=DARK_TEXT,font=("Arial", 13, "bold"),
                                 corner_radius=8,command=show_dashboard)
dashboard_button.pack(padx=25,pady=6)

def open_report(filename):

    report_window = ctk.CTkToplevel()
    report_window.title("Security Report")
    report_window.geometry("800x600")
    report_window.configure(fg_color=BACKGROUND)

    title = ctk.CTkLabel(report_window,text=filename,
                         font=("Arial", 18, "bold"),text_color=TEXT_PINK)

    title.pack(pady=(20, 10))

    report_text = ctk.CTkTextbox(report_window,fg_color=BOX_PINK,text_color=DARK_TEXT,
                                 border_width=1,border_color=BORDER_PINK,corner_radius=10,
                                 font=("Consolas", 12))
    report_text.pack(fill="both",expand=True,padx=25,pady=(0, 25))
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        report_text.insert("1.0", content)

    except Exception as e:
        report_text.insert(
            "1.0",
            f"Unable to open report.\n\nError: {e}"
        )

    report_text.configure(state="disabled")


def show_reports():
    global reports_page
    global last_report_file
    reset_sidebar_buttons()
    reports_button.configure(fg_color=BOX_PINK,text_color=DARK_TEXT)


    if reports_page is not None:
        reports_page.destroy()
    reports_page = ctk.CTkFrame(main_area,fg_color=BACKGROUND)
    reports_page.place(relx=0,rely=0,relwidth=1,relheight=1)
    # Reports title
    reports_title = ctk.CTkLabel(reports_page,text="REPORTS",font=("Arial", 22, "bold"),
                                 text_color=TEXT_PINK)
                                 
    reports_title.pack(anchor="w",padx=35,pady=(25, 5))
    reports_description = ctk.CTkLabel(reports_page,text="Saved security assessment reports",
                                       font=("Arial", 13),text_color=TEXT_PINK)
   
    reports_description.pack(
        anchor="w",
        padx=35,
        pady=(0, 20)
    )

    # Reports box
    reports_frame = ctk.CTkFrame(reports_page,fg_color=BACKGROUND,border_width=1,
                                 border_color=BORDER_PINK,corner_radius=10)
        
    reports_frame.pack(fill="both",expand=True,padx=35,pady=(0, 25))
   
    # Find saved reports
    report_files = []

    if last_report_file and os.path.exists(last_report_file):
        report_files.append(last_report_file)

    for file in os.listdir():

        if file.endswith(".txt") or file.endswith(".json"):
            full_path = os.path.abspath(file)

            if full_path not in report_files:
                report_files.append(full_path)
            

    if report_files:

        for file in report_files:

            report_row = ctk.CTkFrame(reports_frame,fg_color=BOX_PINK,corner_radius=7)
                
            report_row.pack(fill="x",padx=20,pady=8)
                

            report_name = ctk.CTkLabel(report_row,text=os.path.basename(file),
                                       text_color=DARK_TEXT,font=("Arial", 13, "bold"))
                                  
            report_name.pack(side="left", padx=15,pady=12)
            
            open_button = ctk.CTkButton(report_row, text="OPEN", width=90, height=32,
                                        fg_color=BOX_PINK,hover_color=HOVER_PINK,text_color=DARK_TEXT,
                                        border_width=1,border_color=BORDER_PINK,command=lambda f=file: open_report(f))


            open_button.pack(side="right",padx=15)

    else:

        no_reports = ctk.CTkLabel(reports_frame,text="No reports have been saved yet.",text_color=TEXT_PINK,
                                  font=("Arial", 14))

        no_reports.pack(pady=40)

# ------------------------------------------------------------
# REPORTS BUTTON
# ------------------------------------------------------------

reports_button = ctk.CTkButton(sidebar,text="Reports",width=170,height=42,fg_color=BACKGROUND,
                               hover_color=HOVER_PINK,border_width=1,border_color=BORDER_PINK,
                               text_color=TEXT_PINK,font=("Arial", 13, "bold"),corner_radius=8,
                               command=show_reports)

reports_button.pack(padx=25,pady=6)


# ------------------------------------------------------------
# SETTINGS BUTTON
# ------------------------------------------------------------

settings_button = ctk.CTkButton(sidebar,text="Settings",width=170,height=42,fg_color=BACKGROUND,
                                hover_color=HOVER_PINK,border_width=1,border_color=BORDER_PINK,
                                text_color=TEXT_PINK,font=("Arial", 13, "bold"),corner_radius=8)


settings_button.pack(padx=25,pady=6)


# ============================================================
# MAIN AREA
# ============================================================

main_area = ctk.CTkFrame(app,fg_color=BACKGROUND,corner_radius=0)

main_area.pack(side="left",fill="both",expand=True)
show_dashboard()

# ============================================================
# HEADER
# ============================================================

header = ctk.CTkFrame(
    main_area,
    fg_color=BACKGROUND,
    height=70
)

header.pack(fill="x",padx=35,pady=(25, 5))
 
header.pack_propagate(False)


# ------------------------------------------------------------
# DASHBOARD TITLE
# ------------------------------------------------------------

title = ctk.CTkLabel(
    header,text="SECURITY DASHBOARD",font=("Arial", 27, "bold"),text_color=TEXT_PINK)

title.pack(side="left",pady=10)
# ------------------------------------------------------------
# SYSTEM STATUS
# ------------------------------------------------------------

status = ctk.CTkLabel(
    header,font=("Arial", 13, "bold"),
    text="SYSTEM READY",text_color=TEXT_PINK)
status.pack( side="right",pady=10)

# ============================================================
# SCANNER SECTION
# ============================================================

scanner_frame = ctk.CTkFrame(
    main_area,fg_color=BACKGROUND,border_width=1,border_color=BORDER_PINK,corner_radius=10)
 
scanner_frame.pack( fill="x",padx=35,pady=15)


# ------------------------------------------------------------
# SCANNER TITLE
# ------------------------------------------------------------

scanner_title = ctk.CTkLabel(scanner_frame,text="TARGET SCANNER",font=("Arial", 19, "bold"),
                             text_color=TEXT_PINK)
    
scanner_title.pack(anchor="w",padx=25,pady=(20, 5))
    
scanner_description = ctk.CTkLabel(scanner_frame,
                                   text="Configure the security assessment before starting the scan.",
                                   font=("Arial", 12),text_color=TEXT_PINK)

scanner_description.pack(anchor="w",padx=25,pady=(0, 20))

# ============================================================
# TARGET + REPORT FORMAT
# ============================================================

top_controls = ctk.CTkFrame(scanner_frame,fg_color=BACKGROUND)
top_controls.pack(fill="x",padx=25)
# ------------------------------------------------------------
# TARGET SECTION
# ------------------------------------------------------------

target_section = ctk.CTkFrame(top_controls,fg_color=BACKGROUND)
target_section.pack(side="left",fill="x",expand=True,padx=(0, 10))
        
target_label = ctk.CTkLabel(target_section,text="TARGET IP / DOMAIN",
                            font=("Arial", 12, "bold"),text_color=TEXT_PINK)
    
target_label.pack(anchor="w",pady=(0, 7))

target_entry = ctk.CTkEntry( target_section,height=42,fg_color=BOX_PINK,
                            text_color=DARK_TEXT,border_color=BORDER_PINK,
                            border_width=2,placeholder_text="Enter IP address or Domain",
                            placeholder_text_color="#6F5555",corner_radius=7)
target_entry.pack( fill="x")
# ============================================================
# REPORT FORMAT
# ============================================================

report_section = ctk.CTkFrame(top_controls,fg_color=BACKGROUND)

report_section.pack( side="left",fill="x",expand=True,padx=(10, 0))
report_label = ctk.CTkLabel(report_section,text="REPORT FORMAT",
                            font=("Arial", 12, "bold"),text_color=TEXT_PINK)
    
    
report_label.pack( anchor="w", pady=(0, 7))
report_format = ctk.CTkOptionMenu(report_section,values=["TXT", "JSON"],height=42,
                                  fg_color=BOX_PINK,button_color=BOX_PINK,
                                  button_hover_color=HOVER_PINK,text_color=DARK_TEXT,
                                  dropdown_fg_color=BOX_PINK,dropdown_hover_color=HOVER_PINK,
                                  dropdown_text_color=DARK_TEXT,corner_radius=7)
   
report_format.pack(fill="x")
# ============================================================
# SCAN LEVEL
# ============================================================

scan_level_section = ctk.CTkFrame(scanner_frame,fg_color=BACKGROUND)
    
scan_level_section.pack(fill="x",padx=25,pady=(20, 0))
    
scan_level_label = ctk.CTkLabel(scan_level_section,
                                text="SCAN LEVEL",font=("Arial", 12, "bold"),text_color=TEXT_PINK)
scan_level_label.pack(anchor="w",pady=(0, 7))
    
scan_level = ctk.CTkOptionMenu(
    scan_level_section,

    values=[ "Basic","Normal", "Aggressive"],height=42,fg_color=BOX_PINK,
    button_color=BOX_PINK,button_hover_color=HOVER_PINK,text_color=DARK_TEXT,
    dropdown_fg_color=BOX_PINK,dropdown_hover_color=HOVER_PINK,
    dropdown_text_color=DARK_TEXT, corner_radius=7)

scan_level.pack(fill="x")
def start_scan():

    global last_scan_output
    global last_scan_target
    global last_scan_level

    target = target_entry.get()
    level = scan_level.get()

    if not target:
        results_box.configure(state="normal")
        results_box.delete("1.0", "end")
        results_box.insert("1.0","Please enter a target.")
            
          
        results_box.configure(state="disabled")
        return

    results_box.configure(state="normal")
    results_box.delete("1.0", "end")
    results_box.insert( "1.0","Scanning... Please wait.\n\n")
       
     
    app.update()

    output = target_scan(target, level)

    # Store the scan information
    last_scan_output = output
    last_scan_target = target
    last_scan_level = level

    # Display results
    results_box.delete("1.0", "end")
    results_box.insert("1.0", output)

    results_box.configure(state="disabled")

def save_report():
    global last_report_file

    if not last_scan_output:
        results_box.configure(state="normal")

        results_box.insert("end","\n\nPlease run a scan before saving a report.")
         
        results_box.configure(state="disabled")

        return

    report_type = report_format.get()

    if report_type == "TXT":

        filename = filedialog.asksaveasfilename(
            title="Save Security Assessment Report",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"),("All files", "*.*")])
          
        if not filename:
            return

        with open(filename,"w", encoding="utf-8"
        ) as file:

            file.write(
                "SECURITY ASSESSMENT REPORT\n")
            file.write(
                "==========================\n\n")
            file.write(
                f"Target: {last_scan_target}\n")
            file.write(
                f"Scan Level: {last_scan_level}\n")
            file.write(
                "Report Format: TXT\n\n")
            file.write(
                "NMAP RESULTS\n")

            file.write(
                "============\n\n")

            file.write(last_scan_output)

        last_report_file = filename
            
    else:
            filename = filedialog.asksaveasfilename(title="Save Security Assessment Report",
                                                    defaultextension=".json",
                                                    filetypes=[("JSON files", "*.json"),("All files", "*.*")])
            if not filename:
                return
            report_data = { "target": last_scan_target,"scan_level": last_scan_level,
                           "report_format": "JSON","nmap_results": last_scan_output}
            
            with open(filename,"w",encoding="utf-8"
           
        )as file:
                json.dump(report_data,file,indent=4)
            last_report_file = filename
             
    results_box.configure(state="normal")

    results_box.insert(
        "end","\n\n========================================\n"
        "REPORT SAVED SUCCESSFULLY\n"
        "========================================")
    results_box.configure(state="disabled")
            
# ============================================================
# BUTTON AREA
# ============================================================

button_frame = ctk.CTkFrame( scanner_frame,fg_color=BACKGROUND)
   
button_frame.pack(pady=(20, 20))

# ------------------------------------------------------------
# START SCAN
# ------------------------------------------------------------

scan_button = ctk.CTkButton(button_frame,

    text="START SCAN",width=180,height=45,fg_color=BOX_PINK,hover_color=HOVER_PINK,

    text_color=DARK_TEXT,font=("Arial", 14, "bold"),

    border_width=1,border_color=BORDER_PINK,corner_radius=8,command=start_scan)

scan_button.grid(row=0,column=0,padx=8)

# ------------------------------------------------------------
# SAVE REPORT
# ------------------------------------------------------------

save_report_button = ctk.CTkButton(button_frame,

    text="SAVE REPORT",width=180,height=45,fg_color=BOX_PINK,hover_color=HOVER_PINK,text_color=DARK_TEXT,

    font=("Arial", 14, "bold"),border_width=1,border_color=BORDER_PINK,corner_radius=8,command=save_report)

save_report_button.grid(  row=0, column=1, padx=8)


# ============================================================
# RESULTS SECTION
# ============================================================

results_frame = ctk.CTkFrame(main_area,fg_color=BACKGROUND,border_width=1,border_color=BORDER_PINK,corner_radius=10)

results_frame.pack(fill="both",expand=True, padx=35,pady=(0, 25))


# ------------------------------------------------------------
# RESULTS TITLE
# ------------------------------------------------------------

results_title = ctk.CTkLabel( results_frame, text="SCAN RESULTS", font=("Arial", 19, "bold"), text_color=TEXT_PINK)

results_title.pack(anchor="w", padx=25, pady=(15, 8))


# ------------------------------------------------------------
# RESULTS BOX
# ------------------------------------------------------------

results_box = ctk.CTkTextbox(results_frame,fg_color=BOX_PINK,text_color=DARK_TEXT,
                             border_width=2,border_color=BORDER_PINK,corner_radius=7,
                             font=("Consolas", 12), padx=10, pady=10)
                             
results_box.pack(fill="both", expand=True,padx=25,pady=(0, 20))


# Initial message
results_box.insert( "1.0","No scan has been performed yet.\n\n"
                   "Enter a target above and click START SCAN.")

# Keep results read-only
results_box.configure(state="disabled")

# ============================================================
# RUN APPLICATION
# ============================================================

app.mainloop()        

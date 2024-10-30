UDR_2023 = "https://www.responsibilityreports.com/HostedData/ResponsibilityReports/PDF/NYSE_UDR_2023.pdf"
UDR_2022 = "https://www.responsibilityreports.com/HostedData/ResponsibilityReportArchive/u/NYSE_UDR_2022.pdf"
UDR_2021 = "https://www.responsibilityreports.com/HostedData/ResponsibilityReportArchive/u/NYSE_UDR_2021.pdf"
UDR_reports = [UDR_2023, UDR_2022, UDR_2021]
# Create separate variables for each path in all_reports named by file name without .pdf extension
var_names = []
for file in files:
    var_name = os.path.splitext(file)[0]
    globals()[var_name] = os.path.join(directory_path, file)
    var_names.append(var_name)

# Create a list similar to UDR_reports
all_reports = [os.path.join(directory_path, file) for file in files]
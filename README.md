# 🌍 Earthquake Data Analysis using Azure Databricks & Power BI

## 📌 Project Overview
This project focuses on **analyzing global earthquake data** using **Azure Databricks** for data processing and **Power BI** for visualization. The goal is to gain insights into earthquake trends, magnitudes, affected locations, and fatalities.

## 🚀 Data Source
https://www.ngdc.noaa.gov/hazel/view/hazards/earthquake/search

## 🚀 Tech Stack
- **Azure Databricks** (Data Processing & Transformation)
- **PySpark** (Data Cleaning & ETL)
- **Power BI** (Interactive Dashboard)
- **Azure Storage** (Data Source)
- **GitHub** (Version Control)

---

## 📊 Features & Analysis
### ✅ **Data Cleaning & Transformation**
- Removed unnecessary columns (`Search Parameters`).
- Filtered out missing earthquake records (`NULL` values).
- Extracted **Country** from `Location Name` using **PySpark**.
- Converted `Year`, `Month`, and `Date` to **integers**.
- Stored **cleaned data** in Databricks Hive Metastore (`earthquake_data_updated`).

### ✅ **Power BI Dashboard**
- **🌍 World Map Visualization**:
  - Plotted **earthquake occurrences** based on Country.
  - Used **bubble size & red color intensity** to represent `Magnitude`.
- **📈 Trend Analysis**:
  - **Line Chart**: Year-wise earthquake frequency.
  - **Bar Chart**: Top affected **countries**.
- **📊 Filters & Slicers**:
  - **Year Selector** (Slider).
  - **Magnitude Drop-down** (To filter high-magnitude earthquakes).

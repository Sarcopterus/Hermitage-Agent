from Hermitage.utils.analyzer import analizar_logs, exportar_a_csv

if __name__ == "__main__":
    resumen = analizar_logs()  # por defecto hoy
    exportar_a_csv(resumen)
    print("✅ Resumen exportado a logs/summary_export.csv") 

import flet as ft
from logica import predecir_credito  # Importamos tu modelo convertido

def main(page: ft.Page):
    page.title = "Evaluador Crédito Offline"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = "adaptive"

    # --- Entradas de usuario ---
    # Nota: Ponemos valores por defecto para probar rápido
    dep = ft.TextField(label="Dependientes", value="0")
    edu = ft.Dropdown(label="Educación", options=[ft.dropdown.Option("Graduate"), ft.dropdown.Option("Not Graduate")], value="Graduate")
    self_emp = ft.Dropdown(label="Autoempleado", options=[ft.dropdown.Option("Yes"), ft.dropdown.Option("No")], value="No")
    
    # Entradas numéricas
    income = ft.TextField(label="Ingreso Anual", value="5000000")
    loan_amt = ft.TextField(label="Monto Préstamo", value="2000000")
    loan_term = ft.TextField(label="Plazo (Meses)", value="12")
    cibil = ft.TextField(label="CIBIL Score", value="700")
    
    res_asset = ft.TextField(label="Activos Residenciales", value="0")
    comm_asset = ft.TextField(label="Activos Comerciales", value="0")
    lux_asset = ft.TextField(label="Activos Lujo", value="0")
    bank_asset = ft.TextField(label="Activos Bancarios", value="0")

    lbl_result = ft.Text(size=30, weight="bold")

    def calcular(e):
        try:
            # Convertimos textos a números
            # Mapeo manual simple (sin pandas)
            edu_val = 1 if edu.value == "Graduate" else 0
            emp_val = 1 if self_emp.value == "Yes" else 0
            
            # Llamamos a la lógica extraída
            resultado = predecir_credito(
                no_of_dependents=int(dep.value),
                education=edu_val,
                self_employed=emp_val,
                income_annum=float(income.value),
                loan_amount=float(loan_amt.value),
                loan_term=float(loan_term.value),
                cibil_score=float(cibil.value),
                residential_assets_value=float(res_asset.value),
                commercial_assets_value=float(comm_asset.value),
                luxury_assets_value=float(lux_asset.value),
                bank_asset_value=float(bank_asset.value)
            )
            
            lbl_result.value = f"Resultado: {resultado}"
            lbl_result.color = "green" if resultado == "Aprobado" else "red"
            page.update()
            
        except Exception as ex:
            lbl_result.value = "Error: Revisa los números"
            page.update()

    btn = ft.ElevatedButton("Calcular Ahora", on_click=calcular)

    page.add(
        ft.Text("Datos Personales", size=20, weight="bold"),
        dep, edu, self_emp,
        ft.Text("Datos Financieros", size=20, weight="bold"),
        income, loan_amt, loan_term, cibil,
        ft.Text("Activos", size=20, weight="bold"),
        res_asset, comm_asset, lux_asset, bank_asset,
        ft.Divider(),
        btn, lbl_result
    )

ft.app(target=main)
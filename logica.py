def predecir_credito(no_of_dependents, education, self_employed, income_annum, loan_amount, loan_term, cibil_score, residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value):
    # NOTA: Tu modelo parece haber sido entrenado con datos escalados o en unidades diferentes
    # (ej. Millones en lugar de unidades completas), ya que usa cortes como "5.0" para montos.
    # Si tus datos están en millones (ej. 29000000), tal vez debas dividirlos antes de usar esta función.
    
    if loan_term <= 549.5:
        if loan_amount <= 5.0:  # ¿Ojo aquí con la escala!
            if income_annum <= 28450000.0:
                if commercial_assets_value <= 11300000.0:
                    if income_annum <= 20200000.0:
                        if residential_assets_value <= 7300000.0:
                            if loan_term <= 332.5:
                                return 'Aprobado'
                            else:
                                if commercial_assets_value <= 3150000.0:
                                    if income_annum <= 8300000.0:
                                        if cibil_score <= 4850000.0:
                                            return 'Aprobado'
                                        else:
                                            return 'Rechazado'
                                    else:
                                        return 'Aprobado'
                                else:
                                    if income_annum <= 13650000.0:
                                        return 'Rechazado'
                                    else:
                                        if commercial_assets_value <= 6650000.0:
                                            return 'Aprobado'
                                        else:
                                            return 'Rechazado'
                        else:
                            if income_annum <= 17050000.0:
                                return 'Rechazado'
                            else:
                                return 'Rechazado'
                    else:
                        if commercial_assets_value <= 7000000.0:
                            return 'Aprobado'
                        else:
                            if loan_term <= 357.5:
                                return 'Aprobado'
                            else:
                                return 'Rechazado'
                else:
                    return 'Rechazado'
            else:
                return 'Aprobado'
        else:
            return 'Rechazado'
    else:
        # Lógica para plazos largos (> 549 meses)
        if cibil_score <= 1050000.0:
            if residential_assets_value <= 1850000.0:
                if income_annum <= 3400000.0:
                    if cibil_score <= 150000.0:
                        if income_annum <= 1250000.0:
                            return 'Aprobado'
                        else:
                            return 'Aprobado'
                    else:
                        return 'Aprobado'
                else:
                    if loan_term <= 664.0:
                        return 'Aprobado'
                    else:
                        if residential_assets_value <= 450000.0:
                            return 'Aprobado'
                        else:
                            return 'Aprobado'
            else:
                return 'Aprobado'
        else:
            return 'Aprobado'
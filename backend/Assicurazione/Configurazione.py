class Configurazione:
    def config(i):
        switcher = {
            'Database': 'D:/assicurazione.db'

        }
        return switcher.get(i, "Chiave non trovata")

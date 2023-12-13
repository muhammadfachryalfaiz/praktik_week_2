class Gempa:
    lokasi = ""
    skala = ""

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            return "Dampak gempa tidak berasa."
        elif 2 <= self.skala < 4:
            return "Dampak gempa: Bangunan retak-retak."
        elif 4 <= self.skala < 6:
            return "Dampak gempa: Bangunan roboh."
        elif self.skala >= 6:
            return "Dampak gempa: Bangunan roboh dan berpotensi tsunami."


gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)


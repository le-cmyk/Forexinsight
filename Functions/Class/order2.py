class Order2:
    def __init__(self, prix_debut, prix_fin, position, duration=None, volume=None):
        self.Duration = duration
        self.Prix_debut = prix_debut
        self.Prix_fin = prix_fin
        self.Position = position
        self.Volume = volume

        if volume is None:
            self.Duration = prix_fin - prix_debut

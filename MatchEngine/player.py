class Player:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        position: str,
        price: float = 0.0,
        total_points: int = 0,
        minutes: int = 0
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.price = price
        self.total_points = total_points
        self.minutes = minutes

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name} ({self.position})"
class Settings:
    def __init__(self):
        self.runTime = 100 # cycle runtime in seconds
        self.operatorInitials = ""

    def setOperatorInitials(self, initials: str) -> None:
        self.operatorInitials = initials

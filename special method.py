class course:
    def __init__(self,qualification type,fees):
        self.qualification=qualification
        self.fees=fees
    def qualification(self):
        print("qualification" & "fees:",self.qualification,self.fees)
c1=course("DA","10K")
c2=course("DS","12K")
c1.qualification()
c2.qualification()
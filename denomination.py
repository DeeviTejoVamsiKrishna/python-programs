#Denomination
amount=1260
Five_hundred_notes=amount//500
print(f"Five hundred notes:{Five_hundred_notes}")
remaining_notes=amount%500
Hundred_notes=remaining_notes//100
print(f"Hundred notes:{Hundred_notes}")
remaining_notes1=remaining_notes%100
Fifty_notes=remaining_notes1//50
print("Fifty notes:{Fifty_notes}")
remaining_notes2=remaining_notes1%50
Ten_notes=remaining_notes2//10
print("Ten notes:{Ten_notes}")

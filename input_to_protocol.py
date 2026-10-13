#python3 input_to_protocol.py

#final solution volume
final_volume = input('Please enter the final volume of the solution:')
final_volume = int(final_volume)

#NaCl
NaCl_stock = input('Please enter the NaCl stock (mM):')
NaCl_stock = int(NaCl_stock)
NaCl_final = input('Please enter the NaCl final (mM):')
NaCl_final = int(NaCl_final)

#MgCl2
MgCl2_stock = input('Please enter the MgCl2 stock (mM):')
MgCl2_stock = int(MgCl2_stock)
MgCl2_final = input('Please enter the MgCl2 final (mM):')
MgCl2_final = float(MgCl2_final)

#NaCl
Step1 = f"Add {str(final_volume * (NaCl_final / NaCl_stock))} ml NaCl\n"

#MgCl2
Step2 = f"Add {str(final_volume * (MgCl2_final / MgCl2_stock))} ml MgCl2\n"

#Water
Step3 = f"Add water to a final volume of {str(final_volume)} ml and mix"

print(Step1 + Step2 + Step3)
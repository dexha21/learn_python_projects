has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit and not has_criminal_record:
  print("Eligible for loan")
elif has_high_income or has_good_credit and not has_criminal_record:
  print("Eligible for loan")

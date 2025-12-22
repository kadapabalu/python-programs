headache=(input("headache:"))
cold=(input("cold:"))
cough=(input("cough:"))
if headache=="yes" and cold=="yes" and cough=="yes":
    print("covid-19 positive")
elif headache=="no" and cold=="yes" and cough=="yes":
    print("fever")
else:
    print("healthy body")

# I am going to go to Japan next May and wanted to create a currency converter in Javascript to help me calculate my exchange rate from GPB to Japanese yen

gbp2yen = 186.14 # exchange rate

gbp = input("How much GBP do you wish to convert?\n")

yen = float(gbp) * gbp2yen

print(yen)
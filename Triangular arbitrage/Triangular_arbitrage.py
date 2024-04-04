#The dollar-Euro exchange (E$/Euro) is equal to 1.1, the
#dollar-pound exchange rate (E$/£) is equal to 1.2 and the poundeuro exchange rate (E£/Euro)is equal to .95.

E_dollar_euro = 1.1
E_euro_dollar = 1/E_dollar_euro

E_dollar_pound = 1.2
E_pound_dollar = 1/E_dollar_pound

E_pound_euro = 0.95
E_euro_pound = 1/E_pound_euro

#Try dollar -> euro -> pound -> dollar
def euro_first(sum):
  buy_euro = sum * E_dollar_euro
  buy_pound = buy_euro * E_euro_pound
  buy_dollar = buy_pound * E_pound_dollar
  return buy_dollar


#Try dollar -> pound -> euro -> dollar
def pound_first(sum):
  buy_pound = sum * E_dollar_pound
  buy_euro = buy_pound * E_pound_euro
  buy_dollar = buy_euro * E_euro_dollar 
  return buy_dollar

print(euro_first(100), pound_first(100))
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np


x = float(input('Enter the amount you have on "1st December 2001" in rupees : '))
df = pd.read_csv('currency_output.csv')


Country_List = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY', 'NZD', 'THB', 'HUF', 'AED', 'HKD', 'MXN', 'ZAR', 'PHP', 'SEK', 'IDR', 'SAR', 'BRL', 'TRY', 'KES', 'KRW', 'EGP', 'IQD', 'NOK', 'KWD', 'RUB', 'DKK', 'PKR', 'ILS', 'PLN', 'QAR', 'XAU', 'OMR', 'COP', 'CLP', 'TWD', 'ARS', 'CZK', 'VND', 'MAD', 'JOD', 'BHD', 'XOF', 'LKR', 'UAH', 'NGN', 'TND', 'UGX', 'RON', 'BDT', 'PEN', 'GEL', 'XAF', 'FJD', 'VEF', 'BYN', 'HRK', 'UZS', 'BGN', 'DZD', 'IRR', 'DOP', 'ISK', 'XAG', 'CRC', 'SYP', 'LYD', 'JMD', 'MUR', 'GHS', 'AOA', 'UYU', 'AFN', 'LBP', 'XPF', 'TTD', 'TZS', 'ALL', 'XCD', 'GTQ', 'NPR', 'BOB', 'ZWD', 'BBD', 'CUC', 'LAK', 'BND', 'BWP', 'HNL', 'PYG', 'ETB', 'NAD', 'PGK', 'SDG', 'MOP', 'NIO', 'BMD', 'KZT', 'PAB', 'BAM', 'GYD', 'YER', 'MGA', 'KYD', 'MZN', 'RSD', 'SCR', 'AMD', 'SBD', 'AZN', 'SLL', 'TOP', 'BZD', 'MWK', 'GMD', 'BIF', 'SOS', 'HTG', 'GNF', 'MVR', 'MNT', 'CDF', 'STD', 'TJS', 'KPW', 'MMK', 'LSL', 'LRD', 'KGS', 'GIP', 'XPT', 'MDL', 'CUP', 'KHR', 'MKD', 'VUV', 'MRO', 'ANG', 'SZL', 'CVE', 'SRD', 'XPD', 'SVC', 'BSD', 'XDR', 'RWF', 'AWG', 'DJF', 'BTN', 'KMF', 'WST', 'SPL', 'ERN', 'FKP', 'SHP', 'JEP', 'TMT', 'TVD', 'IMP', 'GGP', 'ZMW']
Final_net_worth_profit = []

p= 0
while p<len(Country_List):
    if df[Country_List[p]][5550]==0:
        Final_net_worth_profit.append(0)
        p+=1
    else:
        No_Of_Notes = x/(df[Country_List[p]][5550])
        Final_net_worth = (No_Of_Notes)*(df[Country_List[p]][0])-(x)
        Final_net_worth_profit.append(Final_net_worth)
        #print ((Country_List[p],Final_net_worth))
        p+=1


Index_Max = Final_net_worth_profit.index(max(Final_net_worth_profit))
Value_Max = max(Final_net_worth_profit)

Country_Max = Country_List[Index_Max]

print ('You gain maximum profit of "%(Value_Max)d rupees" when you invest in "%(Country_Max)s"' %{'Value_Max':Value_Max,'Country_Max':Country_Max})


objects = Country_List
y_pos = np.arange(len(objects))
performance = Final_net_worth_profit
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Profit in Rupees')
plt.title('Profit margin in a span of 15 years')
 
plt.show()

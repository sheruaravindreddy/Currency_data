import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
from matplotlib import style
style.use('fivethirtyeight')


main_df = pd.DataFrame()

z = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY', 'NZD', 'THB', 'HUF', 'AED', 'HKD', 'MXN', 'ZAR', 'PHP', 'SEK', 'IDR', 'SAR', 'BRL', 'TRY', 'KES', 'KRW', 'EGP', 'IQD', 'NOK', 'KWD', 'RUB', 'DKK', 'PKR', 'ILS', 'PLN', 'QAR', 'XAU', 'OMR', 'COP', 'CLP', 'TWD', 'ARS', 'CZK', 'VND', 'MAD', 'JOD', 'BHD', 'XOF', 'LKR', 'UAH', 'NGN', 'TND', 'UGX', 'RON', 'BDT', 'PEN', 'GEL', 'XAF', 'FJD', 'VEF', 'BYN', 'HRK', 'UZS', 'BGN', 'DZD', 'IRR', 'DOP', 'ISK', 'XAG', 'CRC', 'SYP', 'LYD', 'JMD', 'MUR', 'GHS', 'AOA', 'UYU', 'AFN', 'LBP', 'XPF', 'TTD', 'TZS', 'ALL', 'XCD', 'GTQ', 'NPR', 'BOB', 'ZWD', 'BBD', 'CUC', 'LAK', 'BND', 'BWP', 'HNL', 'PYG', 'ETB', 'NAD', 'PGK', 'SDG', 'MOP', 'NIO', 'BMD', 'KZT', 'PAB', 'BAM', 'GYD', 'YER', 'MGA', 'KYD', 'MZN', 'RSD', 'SCR', 'AMD', 'SBD', 'AZN', 'SLL', 'TOP', 'BZD', 'MWK', 'GMD', 'BIF', 'SOS', 'HTG', 'GNF', 'MVR', 'MNT', 'CDF', 'STD', 'TJS', 'KPW', 'MMK', 'LSL', 'LRD', 'KGS', 'GIP', 'XPT', 'MDL', 'CUP', 'KHR', 'MKD', 'VUV', 'MRO', 'ANG', 'SZL', 'CVE', 'SRD', 'XPD', 'SVC', 'BSD', 'XDR', 'RWF', 'AWG', 'DJF', 'BTN', 'KMF', 'WST', 'SPL', 'ERN', 'FKP', 'SHP', 'JEP', 'TMT', 'TVD', 'IMP', 'GGP', 'ZMW']
x=0
while x< len(z):
    output_df = pd.read_csv('currency_output.csv',index_col  = 'DATE')
##    output_df = output_df.pct_change()
##    output_df[z[x]] = (output_df[z[x]] - output_df[z[x]][0])/output_df[z[x]][0] * 100.0

    print ([z[x]])
    if main_df.empty:
        main_df = pd.DataFrame(output_df[z[x]])
    else:
        main_df = main_df.join(pd.DataFrame(output_df[z[x]]))
    x+=1

##pickle_out = open('countries_currency.pickle','wb')
####pickle_out = open('countries_currency_pct.pickle','wb')
####pickle_out = open('countries_currency_from_begin.pickle','wb')
##pickle.dump(main_df, pickle_out)
##pickle_out.close()


##Output_data = pd.read_pickle('countries_currency.pickle')
##Output_data = pd.read_pickle('countries_currency_pct.pickle')
##Output_data = pd.read_pickle('countries_currency_from_begin.pickle')


main_df.plot()
plt.legend().remove()
plt.show()


#######use countries_currency_from_begin.pickle for correlation

##currency_correlation = main_df.corr()
##print(currency_correlation.describe())


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:31:30 2022

@author: Scott Tudo
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 17:31:30 2022
@author: Scott Tudo
"""
import pandas as pd
import numpy as np

# budget_data_df = pd.read_csv("/Users/hannahtudo/UofT/python-homework/Pybank/budget_data.csv")
budget_data_df = pd.read_csv("/UofT/python-homework/Pybank/budget_data.csv")
profit_losses_diff_df = pd.DataFrame(budget_data_df['Profit/Losses']).diff()
profit_losses_diff_df = profit_losses_diff_df.rename(columns={"Profit/Losses": "Chg"})
concat_df = pd.concat([budget_data_df,profit_losses_diff_df],axis=1,join="outer")
# Calculation and convert to string
ln_str = str(len(concat_df))
total_str = str((concat_df["Profit/Losses"]).sum())
avg_str = str(np.round_((concat_df["Chg"]).mean(), decimals=2))
max_str = str(np.round_((concat_df["Chg"]).max(), decimals=0))
max_date = concat_df["Date"][(concat_df["Chg"]).idxmax()]
min_str = str(np.round_((concat_df["Chg"]).min(), decimals=0))
min_date = concat_df["Date"][(concat_df["Chg"]).idxmin()]
lines = ['Financial Analysis',
         '----------------------------',
         'Total Months: ' + ln_str,
         'Total: $' + total_str,
         'Average Change: $' + avg_str,
         'Greatest Increase in Profits: ' + max_date + '($' + max_str.rstrip(".0") + ')',
         'Greatest Decrease in Profits: ' + min_date + '($' + min_str.rstrip(".0") + ')']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')



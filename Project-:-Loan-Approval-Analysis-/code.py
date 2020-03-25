# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# --------------
# code starts here
import pandas as pd
banks = bank.drop(['Loan_ID'],axis = 1)
banks_isnull = banks.isnull().sum()
bank_mode = banks.mode()
print(banks_isnull)
print(bank_mode)
for column in banks.columns:
    banks[column].fillna(banks[column].mode()[0], inplace=True)

print(banks)
banks_isnull = banks.isnull().sum()
print(banks_isnull)


# --------------
# Code starts here
import pandas as pd
import numpy as np



avg_loan_amount=banks.pivot_table(index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc = np.mean)
print(avg_loan_amount)

# code ends here



# --------------
# code starts here
a = banks['Loan_Status'].count()



loan_approved_se=len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')])
loan_approved_nse=len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')])
percentage_se = 100*loan_approved_se/a
percentage_nse = 100*loan_approved_nse/a
print(percentage_se)
print(percentage_nse)
# code ends here                


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x/12 )
big_loan_term = len(banks[banks['Loan_Amount_Term']>=300])
print('big_loan_term is',big_loan_term)
# code ends here


# --------------
# code starts here
import pandas as pd
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome','Credit_History']]
mean_values = loan_groupby.mean()

# code ends here



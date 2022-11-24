from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from Locators import *
import pandas as pd
import time
from openpyxl import Workbook

class picking_data():
    def picking_process(self):

        name_data = []
        dob_data = []
        Ref_Acct = []
        cliam_no = []
        proc_no = []
        paid_amonttt = []
        paymnt_date = []
        check_no = []
        status_no = []
        paymnt_code = []


        try:

            for i in range(1,9):

                j=str(i)
                Name = driver.find_element(By.XPATH, '//p[@style="display: block;word-break: break-all"]').text
                name=Name.split('\n')[-1]
                name_data.append(name)

                DOB = driver.find_elements(By.XPATH, '//div[@id="multicolumn-details"]//p[3]')[0]
                dob=DOB.split('\n')[-1]
                dob_data.append(dob)
                RefNO= driver.find_elements(By.XPATH,'//div[@id="multicolumn-details"]/div[2]/p')[0]

                refno= RefNO.split('\n')[-1]
                Ref_Acct.append(refno)

                Claim_no= driver.find_element(by=By.XPATH,value=claim_enter)
                cliam_no.append(Claim_no.text)

                proc= driver.find_element(by=By.XPATH,value='//tr['+j+']//td[3]')
                proc_no.append(proc.text)
                paid_amt= driver.find_element(by=By.XPATH,value='//tr['+j+']//td[8]')
                paid_amonttt.append(paid_amt.text)
                try:

                    payment_date= driver.find_element(by=By.XPATH,value='//tr['+j+']//td[9]')
                    paymnt_date.append(payment_date.text)
                    chequeNo= driver.find_element(by=By.XPATH,value='//tr['+j+']//td[10]')
                    check_no.append(chequeNo.text)
                    status= driver.find_element(by=By.XPATH,value='//tr['+j+']//td[11]')
                    status_no.append(status.text)

                    Payment_code = driver.find_element(by=By.XPATH,value='//tr['+j+']//td[12]')
                    paymnt_code.append(Payment_code.text)
                except:
                    pass
                print(len(name_data),print(len(cliam_no)))
                columns=['Name','DOB','REF/Visit ID','claim_no','proc','paid amount','payment date','cheque no','status no','paymentcode']
                df = pd.DataFrame(columns=columns)
                for f in range(0,len(name_data)):
                    df.at[f, 'Name'] = name_data[f]
                    df.at[f, 'DOB'] = dob_data[f]
                    df.at[f,'REF/Visit ID'] = Ref_Acct[f]
                    df.at[f,'claim_no']=cliam_no[f]
                    df.at[f, 'proc'] = proc_no[f]
                    df.at[f,'paid amount']=paid_amonttt[f]


                for j in range(0,len(paymnt_date)):
                    df.at[j,'payment date']=paymnt_date[j]


                    df.at[j, 'cheque no'] =check_no[j]
                    df.at[j, 'status no'] = status_no[j]
                    df.at[j, 'paymentcode'] =paymnt_code[j]
                    #dataset.append([name_data[f],dob_data[j],cliam_no[j],paid_amonttt[j],paymnt_date[j],check_no[j],status_no[j],paymnt_code[j],proc_no[j]])
                print(df)
                df.to_csv('df.csv', index=False)


        except:
             pass




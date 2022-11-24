# from Utilities.CommonPage import *
#
# import time
# from conftest import *
# from Config.configdata import *
# from Utilities.CommonPage import *
# from Utilities.CyberArk import *
# from Locators.AvailityLocators import *
# from Utilities.submit_patient_info import *
# from Locators.PatientLocators import *
# import pandas as pd
#
# class TestEVBV():
#
#
#     @pytest.mark.usefixtures("initiate_driver")
#     def test_evbv(self, initiate_driver):
#         path = "C:\\Users\\adity\\PycharmProjects\\EVBV2\\EVBV Test Patient.xlsx"
#         df = pd.read_excel(path)
#         find = CommonFunctions()
#         dataset = []
#         subscriber_list = []
#         cb_date_list = []
#         total_deductible_list = []
#         met_deductible_list = []
#         total_out_of_pocket_list = []
#         met_out_of_pocket_list = []
#         co_insurance_list = []
#         cyberark().cyberark_setup(email_cyberark, password_cyberark)
#         df['Relation'] = " "
#
#         for i in range(1, 2):
#             driver.switch_to.default_content()
#             find.click(patient_reg_dropdown)
#             find.click(eb_inquiry)
#             driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, iframe_for_avail))
#             time.sleep(5)
#             patient_info().input_and_submit(i)
#             time.sleep(3)
#
#             print(i)
#             if (find.check_for_element(subscriber) == True):
#                 df.at[i,'Relation'] = find.get_element_text(subscriber)
#                 subscriber_list.append(find.get_element_text(subscriber))
#             else:
#                 subscriber_list.append("null")
#             time.sleep(3)
#             if (find.check_for_element(coverage_date) == True):
#                 cb_date_list.append(find.get_element_text(coverage_date)[21:])
#             else:
#                 cb_date_list.append("null")
#             find.click(coverage_and_benefits_button)
#             time.sleep(5)
#             if (find.check_for_element(deductible_total_amount) == True):
#                 total_deductible_list.append(str(find.get_element_text(deductible_total_amount)))
#             else:
#                 total_deductible_list.append("null")
#             if (find.check_for_element(deductible_met_amount) == True):
#                 met_deductible_list.append(find.get_element_text(deductible_met_amount))
#             else:
#                 met_deductible_list.append("null")
#             if (find.check_for_element(out_of_pocket_total_amount) == True):
#                 total_out_of_pocket_list.append(find.get_element_text(out_of_pocket_total_amount))
#             else:
#                  total_out_of_pocket_list.append("null")
#             if (find.check_for_element(out_of_pocket_met_amount) == True):
#                 met_out_of_pocket_list.append(find.get_element_text(out_of_pocket_met_amount))
#             else:
#                 met_out_of_pocket_list.append("null")
#             if (find.check_for_element(co_insurance_percentage) == True):
#                 co_insurance_list.append(find.get_element_text(co_insurance_percentage))
#             else:
#                 co_insurance_list.append("null")
#             time.sleep(5)
#
#         for i in range(0, 1):
#             dataset.append([subscriber_list[i], cb_date_list[i], total_deductible_list[i], met_deductible_list[i],
#                             total_out_of_pocket_list[i], met_out_of_pocket_list[i], co_insurance_list[i]])
#
#         print(dataset)
#
#         dp = pd.DataFrame(dataset,
#                           columns=['Relation', 'Plan/Coverage Date', 'Total Deductible Amount', 'Met Deductible Amount',
#                                    'Total Out of Pocket Amount', 'Met Out of Pocket Amount', 'Co-Insurance Percentage'])
#
#         df.to_csv('C:\\Users\\adity\\PycharmProjects\\EVBV2\\result\\EVBV_DATA.xlsx')
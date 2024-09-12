import pandas as pd

# Load the unmatched postcodes file
unmatched_df_2010 = pd.read_csv(
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\unmatched_postcodes_from_10_nov_2010.csv'
)

# Defining a list of file paths for all ONSPD CSV files
onspd_files = [
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_AB.csv',  
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_AL.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_B.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BA.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BB.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BD.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BH.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BL.csv',  
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BN.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BR.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BS.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_BT.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CA.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CB.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CF.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CH.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CM.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CO.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CR.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CT.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CV.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_CW.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DA.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DD.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DE.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DG.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DH.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DL.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DN.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DT.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_DY.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_E.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_EC.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_EH.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_EN.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_EX.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_FK.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_FY.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_G.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_GL.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_GU.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_GY.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HA.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HD.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HG.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HP.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HR.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HS.csv', 
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HU.csv', 
      r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_HX.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_IG.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_IM.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_IP.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_IV.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_JE.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_KA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_KT.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_KW.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_KY.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_L.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LD.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LE.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LL.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LN.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LS.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_LU.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_M.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_ME.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_MK.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_ML.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_N.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NE.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NG.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NN.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NP.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NR.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_NW.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_OL.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_OX.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PE.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PH.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PL.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PO.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_PR.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_RG.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_RH.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_RM.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_S.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SE.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SG.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SK.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SL.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SM.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SN.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SO.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SP.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SR.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SS.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_ST.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SW.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_SY.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TD.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TF.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TN.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TQ.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TR.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TS.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_TW.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_UB.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_W.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WA.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WC.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WD.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WF.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WN.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WR.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WS.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_WV.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_YO.csv',
    r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\ONSPD_AUG_2024_UK_ZE.csv'
]

# Specifing the columns to extract from the ONSPD data
columns_of_interest = [
    'pcd', 'lat', 'long', 'oseast1m', 'osnrth1m', 'dointr', 'doterm', 'oa11', 'oa21'
]

# Extract the PCD10nov column from the unmatched dataframe
unmatched_postcodes = unmatched_df_2010['PCD10nov'].str.strip().str.upper().unique()

# Initialize an empty DataFrame to store the results
matched_results = pd.DataFrame()

# Initialize a set to track all matched postcodes
matched_postcodes_set = set()

# Iterate over each ONSPD file
for file in onspd_files:
    # Load the current ONSPD file into a DataFrame
    onspd_df = pd.read_csv(file, usecols=columns_of_interest)
    
    # Strip and uppercase the postcode column to match formats
    onspd_df['pcd'] = onspd_df['pcd'].str.strip().str.upper()
    
    # Filter the ONSPD data where the postcodes match with the unmatched postcodes
    matched_df = onspd_df[onspd_df['pcd'].isin(unmatched_postcodes)]
    
    # Append the matched postcodes to the matched_results DataFrame
    matched_results = pd.concat([matched_results, matched_df], ignore_index=True)
    
    # Add the matched postcodes to the set
    matched_postcodes_set.update(matched_df['pcd'].unique())

# Identifing the unmatched postcodes that were not found in any ONSPD file
unmatched_still = set(unmatched_postcodes) - matched_postcodes_set

# Save the matched results to a CSV file
output_file = r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\matched_postcodes.csv'
matched_results.to_csv(output_file, index=False)

# Save the still unmatched postcodes to a CSV file 
unmatched_file = r'C:\Users\rakesh.yarragangu\OneDrive - Jisc\Desktop\multi_csv\multi_csv\unmatched_still.csv'
pd.DataFrame(list(unmatched_still), columns=['Unmatched_PCD']).to_csv(unmatched_file, index=False)

print(f"Matched results saved to {output_file}")
print(f"Still unmatched postcodes saved to {unmatched_file}")

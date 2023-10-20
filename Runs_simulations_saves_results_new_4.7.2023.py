import os
import openpyxl
import pandas as pd
import time
import numpy as np
start =time.time()
################### INSERT PATH TO THE DIRECTORY ###########################################
# cwd = os.getcwd() # get the current working directory path
cwd = r'D:\Locomotion_Combinations-Copy' # get the current working directory path

############################################################################################
folder_EnergyPLAN =cwd+ r'\Simulations\Process'
df_outputtable_folder=cwd+ r'\Simulations'
results_folder = cwd+ r'\Simulations\results'
# nspools_final_data=pd.read_csv(cwd+r"\nspools_final.txt",header=None,delimiter='\t',skip_blank_lines=True)
# nspools_final_data1=nspools_final_data.iat[0,0]
# excess_data=pd.read_csv(cwd+r"\excess.txt",header=None,delimiter='\t',skip_blank_lines=True)
# excess_data1=excess_data.iat[0,0]

cases_in_1_spool_function_data=pd.read_csv(cwd+r"\cases_in_1_spool_function.csv",header=None,delimiter='\t',skip_blank_lines=True)
cases_in_1_spool_function=cases_in_1_spool_function_data.iat[0,0]

cases_total=pd.read_csv(cwd+r"\total_combinations.csv",header=None,delimiter='\t',skip_blank_lines=True)
cases_total1=cases_total.iat[0,0]

nmultiptoc=pd.read_csv(cwd+r"\n_multiprocess.csv",header=None,delimiter='\t',skip_blank_lines=True)
nmultiptoc1=nmultiptoc.iat[0,0]

cases_in_1_multiprocess=cases_total1/nmultiptoc1

# lines_per_file_data=pd.read_csv(cwd+r"\lines_per_file.txt",header=None,delimiter='\t',skip_blank_lines=True)
# lines_per_file_data1=lines_per_file_data.iat[0,0]

# cases_in_1_multiprocess = lines_per_file_data1
# cases_in_1_spool_function = cases_in_1_spool_function_data1
# cases_in_final_spool = nspools_final_data1 * cases_in_1_spool_function + excess_data1




############ DATA 1 ###################
df_outputtable = r'{0}\input_names_1.0.csv'.format(df_outputtable_folder)
df_names = pd.read_csv(df_outputtable, header=None)
m_rowp1=df_names.shape[0]
folder_csv_xlsxp1 = r'{0}-1\spool\results'.format(folder_EnergyPLAN)
spool_folder = r'{0}-1\spool'.format(folder_EnergyPLAN)

############# DATA 2 #####################
df_outputtable2 = r'{0}\input_names_2.0.csv'.format(df_outputtable_folder)
df_names2 = pd.read_csv(df_outputtable2, header=None)
m_rowp12=df_names2.shape[0]
folder_csv_xlsxp2 = r'{0}-2\spool\results'.format(folder_EnergyPLAN)
spool_folder2 = r'{0}-2\spool'.format(folder_EnergyPLAN)


################ DATA 3 ###########################
df_outputtable3 = r'{0}\input_names_3.0.csv'.format(df_outputtable_folder)
df_names3 = pd.read_csv(df_outputtable3, header=None)
m_rowp13=df_names3.shape[0]
folder_csv_xlsxp3 = r'{0}-3\spool\results'.format(folder_EnergyPLAN)
spool_folder3 = r'{0}-3\spool'.format(folder_EnergyPLAN)


################### DATA 4 #########################
df_outputtable4 = r'{0}\input_names_4.0.csv'.format(df_outputtable_folder)
df_names4 = pd.read_csv(df_outputtable4, header=None)
m_rowp14=df_names4.shape[0]
folder_csv_xlsxp4 = r'{0}-4\spool\results'.format(folder_EnergyPLAN)
spool_folder4 = r'{0}-4\spool'.format(folder_EnergyPLAN)

################### DATA 5 #########################
df_outputtable5 = r'{0}\input_names_5.0.csv'.format(df_outputtable_folder)
df_names5 = pd.read_csv(df_outputtable5, header=None)
m_rowp15=df_names5.shape[0]
folder_csv_xlsxp5 = r'{0}-5\spool\results'.format(folder_EnergyPLAN)
spool_folder5 = r'{0}-5\spool'.format(folder_EnergyPLAN)


################### DATA 6 #########################
df_outputtable6 = r'{0}\input_names_6.0.csv'.format(df_outputtable_folder)
df_names6 = pd.read_csv(df_outputtable6, header=None)
m_rowp16=df_names6.shape[0]
folder_csv_xlsxp6 = r'{0}-6\spool\results'.format(folder_EnergyPLAN)
spool_folder6 = r'{0}-6\spool'.format(folder_EnergyPLAN)

################### DATA 7 #########################
df_outputtable7 = r'{0}\input_names_7.0.csv'.format(df_outputtable_folder)
df_names7 = pd.read_csv(df_outputtable7, header=None)
m_rowp17=df_names7.shape[0]
folder_csv_xlsxp7 = r'{0}-7\spool\results'.format(folder_EnergyPLAN)
spool_folder7 = r'{0}-7\spool'.format(folder_EnergyPLAN)

################### DATA 8 #########################
df_outputtable8 = r'{0}\input_names_8.0.csv'.format(df_outputtable_folder)
df_names8 = pd.read_csv(df_outputtable8, header=None)
m_rowp18=df_names8.shape[0]
folder_csv_xlsxp8 = r'{0}-8\spool\results'.format(folder_EnergyPLAN)
spool_folder8 = r'{0}-8\spool'.format(folder_EnergyPLAN)


################### DATA 9 #########################
df_outputtable9 = r'{0}\input_names_9.0.csv'.format(df_outputtable_folder)
df_names9 = pd.read_csv(df_outputtable9, header=None)
m_rowp19=df_names9.shape[0]
folder_csv_xlsxp9 = r'{0}-9\spool\results'.format(folder_EnergyPLAN)
spool_folder9 = r'{0}-9\spool'.format(folder_EnergyPLAN)


################### DATA 10 #########################
df_outputtable10 = r'{0}\input_names_10.0.csv'.format(df_outputtable_folder)
df_names10 = pd.read_csv(df_outputtable10, header=None)
m_rowp110=df_names10.shape[0]
folder_csv_xlsxp10 = r'{0}-10\spool\results'.format(folder_EnergyPLAN)
spool_folder10 = r'{0}-10\spool'.format(folder_EnergyPLAN)


################### DATA 11 #########################
df_outputtable11 = r'{0}\input_names_11.0.csv'.format(df_outputtable_folder)
df_names11 = pd.read_csv(df_outputtable11, header=None)
m_rowp111=df_names11.shape[0]
folder_csv_xlsxp11 = r'{0}-11\spool\results'.format(folder_EnergyPLAN)
spool_folder11 = r'{0}-11\spool'.format(folder_EnergyPLAN)


################### DATA 12 #########################
df_outputtable12 = r'{0}\input_names_12.0.csv'.format(df_outputtable_folder)
df_names12 = pd.read_csv(df_outputtable12, header=None)
m_rowp112=df_names12.shape[0]
folder_csv_xlsxp12 = r'{0}-12\spool\results'.format(folder_EnergyPLAN)
spool_folder12 = r'{0}-12\spool'.format(folder_EnergyPLAN)


################### DATA 13 #########################
df_outputtable13 = r'{0}\input_names_13.0.csv'.format(df_outputtable_folder)
df_names13 = pd.read_csv(df_outputtable13, header=None)
m_rowp113=df_names13.shape[0]
folder_csv_xlsxp13 = r'{0}-13\spool\results'.format(folder_EnergyPLAN)
spool_folder13 = r'{0}-13\spool'.format(folder_EnergyPLAN)


################### DATA 14 #########################
df_outputtable14 = r'{0}\input_names_14.0.csv'.format(df_outputtable_folder)
df_names14 = pd.read_csv(df_outputtable14, header=None)
m_rowp114=df_names14.shape[0]
folder_csv_xlsxp14 = r'{0}-14\spool\results'.format(folder_EnergyPLAN)
spool_folder14 = r'{0}-14\spool'.format(folder_EnergyPLAN)


################### DATA 15 #########################
df_outputtable15 = r'{0}\input_names_15.0.csv'.format(df_outputtable_folder)
df_names15 = pd.read_csv(df_outputtable15, header=None)
m_rowp115=df_names15.shape[0]
folder_csv_xlsxp15 = r'{0}-15\spool\results'.format(folder_EnergyPLAN)
spool_folder15 = r'{0}-15\spool'.format(folder_EnergyPLAN)


################## DATA 16 #########################
df_outputtable16 = r'{0}\input_names_16.0.csv'.format(df_outputtable_folder)
df_names16 = pd.read_csv(df_outputtable16, header=None)
m_rowp116=df_names16.shape[0]
folder_csv_xlsxp16 = r'{0}-16\spool\results'.format(folder_EnergyPLAN)
spool_folder16 = r'{0}-16\spool'.format(folder_EnergyPLAN)

##############################################################################
##################### START PARALEL PROCESSES ################################
##############################################################################

cases_in_1_multiprocess = int(cases_in_1_multiprocess)
cases_in_1_spool_function = int(cases_in_1_spool_function)

    
from multiprocessing import Process
def func1():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]
        # name51=df_novi.iloc[51][0]
        # name52=df_novi.iloc[52][0]
        # name53=df_novi.iloc[53][0]
        # name54=df_novi.iloc[54][0]
        # name55=df_novi.iloc[55][0]
        # name56=df_novi.iloc[56][0]
        # name57=df_novi.iloc[57][0]
        # name58=df_novi.iloc[58][0]
        # name59=df_novi.iloc[59][0]
        # name60=df_novi.iloc[60][0]
        # name61=df_novi.iloc[61][0]
        # name62=df_novi.iloc[62][0]
        # name63=df_novi.iloc[63][0]
        # name64=df_novi.iloc[64][0]
        # name65=df_novi.iloc[65][0]
        # name66=df_novi.iloc[66][0]
        # name67=df_novi.iloc[67][0]
        # name68=df_novi.iloc[68][0]
        # name69=df_novi.iloc[69][0]
        # name70=df_novi.iloc[70][0]
        # name71=df_novi.iloc[71][0]
        # name72=df_novi.iloc[72][0]
        # name73=df_novi.iloc[73][0]
        # name74=df_novi.iloc[74][0]
        # name75=df_novi.iloc[75][0]
        # name76=df_novi.iloc[76][0]
        # name77=df_novi.iloc[77][0]
        # name78=df_novi.iloc[78][0]
        # name79=df_novi.iloc[79][0]
        # name80=df_novi.iloc[80][0]
        # name81=df_novi.iloc[81][0]
        # name82=df_novi.iloc[82][0]
        # name83=df_novi.iloc[83][0]
        # name84=df_novi.iloc[84][0]
        # name85=df_novi.iloc[85][0]
        # name86=df_novi.iloc[86][0]
        # name87=df_novi.iloc[87][0]
        # name88=df_novi.iloc[88][0]
        # name89=df_novi.iloc[89][0]
        # name90=df_novi.iloc[90][0]
        # name91=df_novi.iloc[91][0]
        # name92=df_novi.iloc[92][0]
        # name93=df_novi.iloc[93][0]
        # name94=df_novi.iloc[94][0]
        # name95=df_novi.iloc[95][0]
        # name96=df_novi.iloc[96][0]
        # name97=df_novi.iloc[97][0]
        # name98=df_novi.iloc[98][0]
        # name99=df_novi.iloc[99][0]

    
        # os.system(r'{0}-1\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-1\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # # os.system(r'{0}-1\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))
        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            # dataframmp1=pd.read_csv("{1}\{0}.txt".format(name0x,folder_csv_xlsxp1))

            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp1),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp1),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp1),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp1)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
                
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        ### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
        

def func2():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names2[prvi:drugi]
        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-2\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-2\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-2\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp2),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder2),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp2),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp2),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp2)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
         


def func3():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names3[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-3\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-3\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-3\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp3),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder3),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp3),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp3),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp3)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        
def func4():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names4[prvi:drugi]


        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-4\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-4\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-4\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp4),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder4),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp4),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp4),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp4)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
      

def func5():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names5[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-5\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-5\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-5\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp5),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder5),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp5),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp5),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp5)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
            
def func6():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names6[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-6\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-6\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-6\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))
        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp6),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder6),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp6),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp6),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp6)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                    
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
            
def func7():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names7[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-7\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-7\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-7\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp7),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder7),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp7),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp7),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp7)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                   
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        
            
def func8():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names8[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-8\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-8\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-8\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp8),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder8),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp8),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp8),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp8)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                   
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 

def func9():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names9[prvi:drugi]


        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

    
        # os.system(r'{0}-9\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-9\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-9\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp9),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder9),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp9),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp9),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp9)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                   
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        

def func10():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names10[prvi:drugi]


        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-10\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-10\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-10\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp10),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder10),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp10),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp10),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp10)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                   
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        

def func11():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names11[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-11\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-11\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-11\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp11),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder11),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp11),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp11),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp11)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                   
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
         
            
def func12():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names12[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-12\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-12\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-12\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp12),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder12),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp12),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp12),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp12)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                 
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
         
            
def func13():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names13[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-13\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-13\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-13\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp13),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder13),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp13),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp13),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp13)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                 
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        
            
def func14():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names14[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-14\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-14\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-14\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp14),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder14),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp14),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp14),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp14)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                 
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
 
        
            
def func15():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names15[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-15\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-15\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-15\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp15),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder15),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp15),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp15),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp15)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                 
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
   
        
def func16():
    for i in range (0, cases_in_1_multiprocess,cases_in_1_spool_function):
        prvi = i
        drugi = i + cases_in_1_spool_function
        df_novi =df_names16[prvi:drugi]

        name0=df_novi.iloc[0][0]+".txt"
        name1=df_novi.iloc[1][0]+".txt"
        name2=df_novi.iloc[2][0]+".txt"
        name3=df_novi.iloc[3][0]+".txt"
        name4=df_novi.iloc[4][0]+".txt"
        name5=df_novi.iloc[5][0]+".txt"
        name6=df_novi.iloc[6][0]+".txt"
        name7=df_novi.iloc[7][0]+".txt"
        name8=df_novi.iloc[8][0]+".txt"
        name9=df_novi.iloc[9][0]+".txt"
        name10=df_novi.iloc[10][0]+".txt"
        name11=df_novi.iloc[11][0]+".txt"
        name12=df_novi.iloc[12][0]+".txt"
        name13=df_novi.iloc[13][0]+".txt"
        name14=df_novi.iloc[14][0]+".txt"
        name15=df_novi.iloc[15][0]+".txt"
        name16=df_novi.iloc[16][0]+".txt"
        name17=df_novi.iloc[17][0]+".txt"
        name18=df_novi.iloc[18][0]+".txt"
        name19=df_novi.iloc[19][0]+".txt"
        name20=df_novi.iloc[20][0]+".txt"
        name21=df_novi.iloc[21][0]+".txt"
        name22=df_novi.iloc[22][0]+".txt"
        name23=df_novi.iloc[23][0]+".txt"
        name24=df_novi.iloc[24][0]+".txt"
        name25=df_novi.iloc[25][0]+".txt"
        name26=df_novi.iloc[26][0]+".txt"
        name27=df_novi.iloc[27][0]+".txt"
        name28=df_novi.iloc[28][0]+".txt"
        name29=df_novi.iloc[29][0]+".txt"
        name30=df_novi.iloc[30][0]+".txt"
        name31=df_novi.iloc[31][0]+".txt"
        name32=df_novi.iloc[32][0]+".txt"
        name33=df_novi.iloc[33][0]+".txt"
        name34=df_novi.iloc[34][0]+".txt"
        name35=df_novi.iloc[35][0]+".txt"
        name36=df_novi.iloc[36][0]+".txt"
        name37=df_novi.iloc[37][0]+".txt"
        name38=df_novi.iloc[38][0]+".txt"
        name39=df_novi.iloc[39][0]+".txt"
        name40=df_novi.iloc[40][0]+".txt"
        name41=df_novi.iloc[41][0]+".txt"
        name42=df_novi.iloc[42][0]+".txt"
        name43=df_novi.iloc[43][0]+".txt"
        name44=df_novi.iloc[44][0]+".txt"
        name45=df_novi.iloc[45][0]+".txt"
        name46=df_novi.iloc[46][0]+".txt"
        name47=df_novi.iloc[47][0]+".txt"
        name48=df_novi.iloc[48][0]+".txt"
        name49=df_novi.iloc[49][0]+".txt"
        # name50=df_novi.iloc[50][0]+".txt"
        # name51=df_novi.iloc[51][0]+".txt"
        # name52=df_novi.iloc[52][0]+".txt"
        # name53=df_novi.iloc[53][0]+".txt"
        # name54=df_novi.iloc[54][0]+".txt"
        # name55=df_novi.iloc[55][0]+".txt"
        # name56=df_novi.iloc[56][0]+".txt"
        # name57=df_novi.iloc[57][0]+".txt"
        # name58=df_novi.iloc[58][0]+".txt"
        # name59=df_novi.iloc[59][0]+".txt"
        # name60=df_novi.iloc[60][0]+".txt"
        # name61=df_novi.iloc[61][0]+".txt"
        # name62=df_novi.iloc[62][0]+".txt"
        # name63=df_novi.iloc[63][0]+".txt"
        # name64=df_novi.iloc[64][0]+".txt"
        # name65=df_novi.iloc[65][0]+".txt"
        # name66=df_novi.iloc[66][0]+".txt"
        # name67=df_novi.iloc[67][0]+".txt"
        # name68=df_novi.iloc[68][0]+".txt"
        # name69=df_novi.iloc[69][0]+".txt"
        # name70=df_novi.iloc[70][0]+".txt"
        # name71=df_novi.iloc[71][0]+".txt"
        # name72=df_novi.iloc[72][0]+".txt"
        # name73=df_novi.iloc[73][0]+".txt"
        # name74=df_novi.iloc[74][0]+".txt"
        # name75=df_novi.iloc[75][0]+".txt"
        # name76=df_novi.iloc[76][0]+".txt"
        # name77=df_novi.iloc[77][0]+".txt"
        # name78=df_novi.iloc[78][0]+".txt"
        # name79=df_novi.iloc[79][0]+".txt"
        # name80=df_novi.iloc[80][0]+".txt"
        # name81=df_novi.iloc[81][0]+".txt"
        # name82=df_novi.iloc[82][0]+".txt"
        # name83=df_novi.iloc[83][0]+".txt"
        # name84=df_novi.iloc[84][0]+".txt"
        # name85=df_novi.iloc[85][0]+".txt"
        # name86=df_novi.iloc[86][0]+".txt"
        # name87=df_novi.iloc[87][0]+".txt"
        # name88=df_novi.iloc[88][0]+".txt"
        # name89=df_novi.iloc[89][0]+".txt"
        # name90=df_novi.iloc[90][0]+".txt"
        # name91=df_novi.iloc[91][0]+".txt"
        # name92=df_novi.iloc[92][0]+".txt"
        # name93=df_novi.iloc[93][0]+".txt"
        # name94=df_novi.iloc[94][0]+".txt"
        # name95=df_novi.iloc[95][0]+".txt"
        # name96=df_novi.iloc[96][0]+".txt"
        # name97=df_novi.iloc[97][0]+".txt"
        # name98=df_novi.iloc[98][0]+".txt"
        # name99=df_novi.iloc[99][0]+".txt"

        # os.system(r'{0}-16\energyPLAN.exe -spool 10 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9))
        os.system(r'{0}-16\energyPLAN.exe -spool 50 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49))
        # os.system(r'{0}-16\energyPLAN.exe -spool 100 {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26} {27} {28} {29} {30} {31} {32} {33} {34} {35} {36} {37} {38} {39} {40} {41} {42} {43} {44} {45} {46} {47} {48} {49} {50} {51} {52} {53} {54} {55} {56} {57} {58} {59} {60} {61} {62} {63} {64} {65} {66} {67} {68} {69} {70} {71} {72} {73} {74} {75} {76} {77} {78} {79} {80} {81} {82} {83} {84} {85} {86} {87} {88} {89} {90} {91} {92} {93} {94} {95} {96} {97} {98} {99} {100} -ascii run'.format(folder_EnergyPLAN,name0,name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15,name16,name17,name18,name19,name20,name21,name22,name23,name24,name25,name26,name27,name28,name29,name30,name31,name32,name33,name34,name35,name36,name37,name38,name39,name40,name41,name42,name43,name44,name45,name46,name47,name48,name49,name50,name51,name52,name53,name54,name55,name56,name57,name58,name59,name60,name61,name62,name63,name64,name65,name66,name67,name68,name69,name70,name71,name72,name73,name74,name75,name76,name77,name78,name79,name80,name81,name82,name83,name84,name85,name86,name87,name88,name89,name90,name91,name92,name93,name94,name95,name96,name97,name98,name99))

        for j in range(0,cases_in_1_spool_function):
            name0x=df_novi.iloc[j][0]
            dataframmp1=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp16),header=None,delimiter='\t',skip_blank_lines=False,skiprows=102,encoding= 'unicode_escape')
            
            dataframmp1['From_grid']=dataframmp1.iloc[0:,[1,16,54,55,62,65,68,73,74,76,79,81,82,86,87,88,89,100]].sum(axis=1)
            dataframmp1['RES_gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,61]].sum(axis=1)
            dispgen=pd.read_csv("{1}\{0}.txt".format(name0x,spool_folder16),header=None,delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PP1cap = dispgen.iloc[178,0]
            PP2cap = dispgen.iloc[998,0]
            CHPcap = dispgen.iloc[164,0]
            NUCLcap = dispgen.iloc[192,0]
    
            Windcap = float(dispgen.iloc[18,0])
            PVcap = float(dispgen.iloc[20,0])
                
            BATTcap = dispgen.iloc[2010,0]
            ROCKcap = dispgen.iloc[1844,0]
            PHScap = dispgen.iloc[538,0]
            V2Gcap = dispgen.iloc[148,0]
            
            HEAT_DEMAND= float(dispgen.iloc[46,0])
            
            wind_csv =  pd.read_csv("{0}\EU27_wind_on7_off3.txt".format(cwd),header=None,names= ["Wind_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')
            PV_csv   =  pd.read_csv("{0}\EU27_PV.txt".format(cwd),header=None,names= ["PV_CF"],delimiter='\t',skip_blank_lines=False,encoding= 'unicode_escape')

            dataframmp1['Disp_cap']= int(float(PP1cap)) + int(float(PP2cap)) + int(float(CHPcap)) + int(float(NUCLcap))
            disp_cap=dataframmp1['Disp_cap']
            dataframmp1['Flex_cap']= int(float(BATTcap)) + int(float(ROCKcap)) + int(float(PHScap)) + int(float(V2Gcap))
            dataframmp1=dataframmp1.drop(dataframmp1.index[0:3])        
            dataframmp1=dataframmp1.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            dataframmp1= pd.concat([dataframmp1, wind_csv,PV_csv], axis=1)
            dataframmp1['Wind'] = dataframmp1['Wind_CF']*Windcap
            dataframmp1['PV'] = dataframmp1['PV_CF']*PVcap
            
            dataframmp1['To_grid']=dataframmp1.iloc[0:,[5,6,7,8,9,10,11,12,15,56,57,58,59,60,61,63,66,69,77,99]].sum(axis=1)            
            dataframmp1['GAP']=  dataframmp1['Disp_cap'] + 0.5* dataframmp1['Flex_cap'] + dataframmp1['RES_gen'] - dataframmp1['To_grid']+dataframmp1['Wind']+dataframmp1['PV']
    
            dataframmp1['gen']=dataframmp1.iloc[0:,[7,8,9,10,11,12,15,57,58,59,60,61,63,66,69,77]].sum(axis=1)+dataframmp1['Wind']+dataframmp1['PV']            
            dataframmp1['dem']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,76,79,81,82,86,87,88,89]].sum(axis=1)
            Gap_datap1genMax = dataframmp1['gen'].max()
            Gap_datap1demMax = dataframmp1['dem'].max()
            Gap_datap1gendem = Gap_datap1genMax-Gap_datap1demMax
            dataframmp1['GAP_MW'] = dataframmp1['gen']-dataframmp1['dem']
    
            Def_PP2=dataframmp1[99].max()
            GAP_PP2_TWh=dataframmp1[99].sum()
            
            Gap_PP2_MW=str(min(Gap_datap1gendem,Def_PP2))
            Gap_PP2_MWdf = pd.DataFrame({Gap_PP2_MW})
            Gap_PP2_TWhdf = pd.DataFrame({GAP_PP2_TWh})
            Gap_PP2_MWdf.set_axis(['Gap_PP2_MW'], axis='columns', inplace=True)
            Gap_PP2_TWhdf.set_axis(['Gap_PP2_TWh'], axis='columns', inplace=True)
    
            df1p0=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp16),header=None,skip_blank_lines=False,skipfooter=8810,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35'),delimiter='\t',encoding= 'unicode_escape')
            cell_value = str(df1p0['A1'].loc[df1p0.index[1]])
            Gap_datap1 = dataframmp1[dataframmp1['GAP'] > 0].min()
            if "PP too small" in cell_value:
                Gap_datap1['GAP'] = 0
                 
            df1p0.to_csv(r"{1}\{0}_annual_data.csv".format(name0x,results_folder),header=None,index=None)
                    
                    
                # with open(r"{1}\{0}Gap_PP2_MW.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % Gap_PP2_MW)
                # with open(r"{1}\{0}Gap_PP2_TWh.csv".format(name0x,results_folder), 'w') as f:
                #     f.write('%d' % GAP_PP2_TWh)
            Gap_datap1df = Gap_datap1.to_frame()
            Gap_datap1df = Gap_datap1df.drop(Gap_datap1df.index[0:150])
            
            Gap_datap1df=Gap_datap1df.T
            Gap_datap1df= pd.concat([Gap_datap1df, Gap_PP2_MWdf,Gap_PP2_TWhdf], axis=1)
            
            Gap_datap1df.to_csv(r"{1}\{0}Gap_datap1df.csv".format(name0x,results_folder))
            
            
        
                                
            df1p00=pd.read_csv("{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp16),header=None,skip_blank_lines=False,skiprows=80,names=('A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16','A17','A18','A19','A20','A21','A22','A23','A24','A25','A26','A27','A28','A29','A30','A31','A32','A33','A34','A35','A36','A37','A38','A39','A40','A41','A42','A43','A44','A45','A46','A47','A48','A49','A50','A51','A52','A53','A54','A55','A56','A57','A58','A59','A60','A61','A62','A63','A64','A65','A66','A67','A68','A69','A70','A71','A72','A73','A74','A75','A76','A77','A78','A79','A80','A81','A82','A83','A84','A85','A86','A87','A88','A89','A90','A91','A92','A93','A94','A95','A96','A97','A98','A99','A100','A101','A102','A103','A104','A105','A106','A107','A108','A109','A110','A111','A112','A113','A114','A115','A116','A117','A118','A119','A120','A121','A122','A123','A124','A125','A126','A127','A128','A129','A130','A131','A132','A133','A134','A135','A136','A137','A138','A139','A140','A141','A142','A143','A144','A145','A146','A147','A148','A149'),delimiter='\t',encoding= 'unicode_escape')            
            df1p00y = df1p00.drop(df1p00.index[25:])
            df1p00y.to_csv(r"{1}\{0}_annual_month_data.csv".format(name0x,results_folder),header=None,index=None)
            
            os.remove(r"{1}\{0}.txt.txt".format(name0x,folder_csv_xlsxp16)) 
                
                
            df1p00yy=df1p00y.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
                 
        
        #### RESULTS OF CLUSTER 1
        
            SOLAR_TWh=df1p00yy.at[4,'A6'].replace(" ", "")
            SOLAR_TWh=float(SOLAR_TWh)
            
        #### RESULTS OF CLUSTER 2
        
            WIND_TWh=df1p00yy.at[4,'A5'].replace(" ", "")
            WIND_TWh=float(WIND_TWh)
        
        #### RESULTS OF CLUSTER 3
        
            limit = 0
            column = dataframmp1[60]
            UtilizationZERO_GHG_SEMIFLEX_share = (column[column > limit].count())/8784 
            
            ZERO_GHG_SEMIFLEX_TWh=df1p00yy.at[4,'A60'].replace(" ", "")
            ZERO_GHG_SEMIFLEX_TWh=float(ZERO_GHG_SEMIFLEX_TWh)
            
        #### RESULTS OF CLUSTER 4
        
            STATICElecStorageLosses_sharex=float(df1p00yy.at[4,'A62'].replace(" ", ""))-float(df1p00yy.at[4,'A63'].replace(" ", ""))
            STATICElecStorageLosses_sharepump=float(df1p00yy.at[4,'A62'].replace(" ", ""))
            if STATICElecStorageLosses_sharepump==0:
                STATICElecStorageLosses_share="nul"
            else:
                STATICElecStorageLosses_share=STATICElecStorageLosses_sharex/STATICElecStorageLosses_sharepump
            STATIC_Elec_STORAGE_input_TWh=df1p00yy.at[4,'A62'].replace(" ", "")
            STATIC_Elec_STORAGE_input_TWh=float(STATIC_Elec_STORAGE_input_TWh)
            
        #### RESULTS OF CLUSTER 5
        
            balheat = dataframmp1[53]
            balheat1 = balheat.drop(balheat.index[8783:8784])
            balheat2 = balheat.drop(balheat.index[0:1])
            balheat2=balheat2.reset_index(level=None, drop=False, inplace=False)
            balheat3= pd.concat([balheat1, balheat2], axis=1)
            balheat3.set_axis(['n', 'index', 'n+1'], axis='columns', inplace=True)
            balheat3['heat_storage_flows']=balheat3['n+1']-balheat3['n']
        
            limit = 0
            column = balheat3['heat_storage_flows']
            HeatStorage_input_TWh = (column[column > limit].sum())/1000000 
            HeatStorage_output_TWh = (column[column < limit].sum())/1000000 
            
        
            if HeatStorage_input_TWh==0:
                HeatStorageLosses_share="nul"
            else:
                HeatStorageLosses_share=(HeatStorage_input_TWh+HeatStorage_output_TWh)/HeatStorage_input_TWh
           
        
            limit = 0
            column = balheat3['heat_storage_flows']
            InputHeatStorage_share = (column[column > limit].sum())/1000000/HEAT_DEMAND 
        
            CriticalMinHourlyBoilers_MW=df1p00yy.at[21,'A53'].replace(" ", "")
            CriticalMinHourlyBoilers_MW=float(CriticalMinHourlyBoilers_MW)    
            
            Shortage_HeatDem_share = dataframmp1.loc[dataframmp1[53]<0,53].sum()/1000000/HEAT_DEMAND    
        
            limit = 0
            column = dataframmp1[52]
            UtilizationHeatStorage_share = (column[column > limit].count())/8784     
                
            BALANCE_HEAT_TWh=df1p00yy.at[4,'A53'].replace(" ", "")
            BALANCE_HEAT_TWh=float(BALANCE_HEAT_TWh)
            
        #### RESULTS OF CLUSTER 6
        
            limit = 0
            column = dataframmp1[45]
            UtilizationCHP_share = (column[column > limit].count())/8784 
            
            CHP_el=df1p00yy.at[4,'A57'].replace(" ", "")
            CHP_el_tot=float(CHP_el)
            CHP_elec_share=CHP_el_tot/100
        
            CHP_heat_share=df1p00yy.at[4,'A45'].replace(" ", "")
            CHP_heat_share=float(CHP_heat_share)
            CHP_heat_share=CHP_heat_share/HEAT_DEMAND    
            
        #### RESULTS OF CLUSTER 7
        
            limit = 0
            column = dataframmp1[46]
            UtilizationHeatPumps_share = (column[column > limit].count())/8784    
            
            HP_el=df1p00yy.at[4,'A55'].replace(" ", "")
            HP_el_tot=float(HP_el)
            HEAT_PUMPS_elec_share=HP_el_tot/100
            
            HEAT_PUMPS_heat_share=df1p00yy.at[4,'A46'].replace(" ", "")
            HEAT_PUMPS_heat_share=float(HEAT_PUMPS_heat_share)
            HEAT_PUMPS_heat_share=HEAT_PUMPS_heat_share/HEAT_DEMAND
        
        #### RESULTS OF CLUSTER 8
        
            limit = 0
            column = dataframmp1[46]
            UtilizationElecBoilers_share = (column[column > limit].count())/8784    
            
            ELEC_BOILERS_heat_TWh=df1p00yy.at[4,'A48'].replace(" ", "")
            ELEC_BOILERS_heat_TWh=float(ELEC_BOILERS_heat_TWh)
            
            Requirement_Boilers_MW=CriticalMinHourlyBoilers_MW
            
        ##### RESULTS OF CLUSTER 9 & 10
          
            limit = 0
            column = dataframmp1[77]
            UtilizationV2G_share = (column[column > limit].count())/8784    
            
            limit = float(V2Gcap)
            column = dataframmp1[77]
            CongestionV2G_share = (column[column == limit].count())/8784        
            
            V2G_ElecDischarge_TWh=df1p00yy.at[4,'A77'].replace(" ", "")
            V2G_ElecDischarge_TWh=float(V2G_ElecDischarge_TWh)
            
            V2G_ElecCharge_TWh=df1p00yy.at[4,'A76'].replace(" ", "")
            V2G_ElecCharge_TWh=float(V2G_ElecCharge_TWh)
            
            V2G_ElecDemand_TWh=df1p00yy.at[4,'A75'].replace(" ", "")
            V2G_ElecDemand_TWh=float(V2G_ElecDemand_TWh)
            
        ##### RESULTS OF CLUSTER 11 & 12
        
            df1p0xyz=df1p0.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')
            Hydrogen_CEEP_TWh=df1p0xyz.at[12,'A27'].replace(" ", "")
            Hydrogen_CEEP_TWh=float(Hydrogen_CEEP_TWh)
        
            Hydrogen_potential_economy_TWh=df1p0xyz.at[12,'A34'].replace(" ", "")
            Hydrogen_potential_economy_TWh=float(Hydrogen_potential_economy_TWh)
            
            Peak_ELT = dataframmp1[81].max()
            limit = 0
            column = dataframmp1[79]
            UtilizationELT_share = (column[column > limit].count())/8784
            Max_ELT_MW = dataframmp1[79].max()
        
        #### RESULTS OF CLUSTER 13
        
            FlexibleDemand_TWh=df1p00yy.at[4,'A54'].replace(" ", "")
            FlexibleDemand_TWh=float(FlexibleDemand_TWh)
        
        #### OTHER RESULTS OF INTEREST
        
            dataframmp1['load']=dataframmp1.iloc[0:,[1,2,16,54,55,62,65,68,71,72,73,74,76,79,81,82,86,87,88,89]].sum(axis=1)      
            MaxHourlyElecDem_MW=dataframmp1['load'].max()
        
            tot_imp=df1p00yy.at[4,'A99'].replace(" ", "")
            tot_imp=float(tot_imp)
            ShortageElecDem_Percent=tot_imp/HEAT_DEMAND
            
            limit = 0
            column = dataframmp1[99]
            HoursShortageinYear_share = (column[column > limit].count())/8784
            
            MaxHourlyHeatDem_MWth = dataframmp1[4].max()
            CriticalMinHourlyPP2_MW=df1p00yy.at[21,'A99'].replace(" ", "")
    
    
            el1=df1p00yy.at[4,'A1'].replace(" ", "")
            el2=df1p00yy.at[4,'A2'].replace(" ", "")
            el54=df1p00yy.at[4,'A54'].replace(" ", "")
            el62=df1p00yy.at[4,'A62'].replace(" ", "")
            el73=df1p00yy.at[4,'A73'].replace(" ", "")
            el76=df1p00yy.at[4,'A76'].replace(" ", "")
            el79=df1p00yy.at[4,'A79'].replace(" ", "")
            el81=df1p00yy.at[4,'A81'].replace(" ", "")
            el3=df1p00yy.at[4,'A3'].replace(" ", "")
    
            el1=float(el1)
            el2=float(el2)
            el54=float(el54)
            el62=float(el62)
            el73=float(el73)
            el76=float(el76)
            el79=float(el79)
            el81=float(el81)
            el3=float(el3)
    
            fact1=el1+el2+el54+el62+el73+el76+el79+el81
            fact2=el1+el2+el3
            fact3=el1+el2+el3
            
            if fact3==0:
                facttot="nul"
            else:
                facttot=(fact1-fact2)/fact3
            
    
            cluster1DF= pd.DataFrame([[SOLAR_TWh]], columns = ["SOLAR_TWh"])
            cluster2DF= pd.DataFrame([[WIND_TWh]], columns = ["WIND_TWh"])
            cluster3DF= pd.DataFrame([[UtilizationZERO_GHG_SEMIFLEX_share,ZERO_GHG_SEMIFLEX_TWh]], columns = ["UtilizationZERO_GHG_SEMIFLEX_share","ZERO_GHG_SEMIFLEX_TWh"])
            cluster4DF= pd.DataFrame([[STATICElecStorageLosses_share,STATIC_Elec_STORAGE_input_TWh]], columns = ["STATICElecStorageLosses_share","STATIC_Elec_STORAGE_input_TWh"])
            cluster5DF= pd.DataFrame([[BALANCE_HEAT_TWh,InputHeatStorage_share,HeatStorageLosses_share,CriticalMinHourlyBoilers_MW,Shortage_HeatDem_share,UtilizationHeatStorage_share]], columns = ["BALANCE_HEAT_TWh","InputHeatStorage_share","HeatStorageLosses_share","CriticalMinHourlyBoilers_MW","Shortage_HeatDem_share","UtilizationHeatStorage_share"])
            cluster6DF= pd.DataFrame([[CHP_heat_share,CHP_elec_share,UtilizationCHP_share]], columns = ["CHP_heat_share","CHP_elec_share","UtilizationCHP_share"])
            cluster7DF= pd.DataFrame([[HEAT_PUMPS_heat_share,HEAT_PUMPS_elec_share,UtilizationHeatPumps_share]], columns = ["HEAT_PUMPS_heat_share","HEAT_PUMPS_elec_share","UtilizationHeatPumps_share"])
            cluster8DF= pd.DataFrame([[ELEC_BOILERS_heat_TWh,Requirement_Boilers_MW,UtilizationElecBoilers_share]], columns = ["ELEC_BOILERS_heat_TWh","Requirement_Boilers_MW","UtilizationElecBoilers_share"])
            cluster9_10DF= pd.DataFrame([[V2G_ElecDemand_TWh,V2G_ElecCharge_TWh,V2G_ElecDischarge_TWh,UtilizationV2G_share,CongestionV2G_share]], columns = ["V2G_ElecDemand_TWh","V2G_ElecCharge_TWh","V2G_ElecDischarge_TWh","UtilizationV2G_share","CongestionV2G_share"])
            cluster11_12DF= pd.DataFrame([[Hydrogen_potential_economy_TWh,Hydrogen_CEEP_TWh,Max_ELT_MW,UtilizationELT_share,Peak_ELT]], columns = ["Hydrogen_potential_economy_TWh","Hydrogen_CEEP_TWh","Max_ELT_MW","UtilizationELT_share","Peak_ELT"])
            cluster13DF= pd.DataFrame([[FlexibleDemand_TWh]], columns = ["FlexibleDemand_TWh"])
            clusterOTHER= pd.DataFrame([[MaxHourlyElecDem_MW,CriticalMinHourlyPP2_MW,ShortageElecDem_Percent,HoursShortageinYear_share,MaxHourlyHeatDem_MWth,facttot]], columns = ["MaxHourlyElecDem_MW","CriticalMinHourlyPP2_MW","ShortageElecDem_Percent","HoursShortageinYear_share","MaxHourlyHeatDem_MWth","IncrementElec_Dem_share"])
        
            Cluster_results= pd.concat([cluster1DF, cluster2DF,cluster3DF,cluster4DF,cluster5DF,cluster6DF,cluster7DF,cluster8DF,cluster9_10DF,cluster11_12DF,cluster13DF,clusterOTHER], axis=1)
            Cluster_results.to_csv(r"{1}\{0}Cluster_results.csv".format(name0x,results_folder),index=None)
   
        

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p3 = Process(target=func3)
  p3.start()
  p4 = Process(target=func4)
  p4.start()
  p5 = Process(target=func5)
  p5.start()
  p6 = Process(target=func6)
  p6.start()
  p7 = Process(target=func7)
  p7.start()
  p8 = Process(target=func8)
  p8.start()
  p9 = Process(target=func9)
  p9.start()
  p10 = Process(target=func10)
  p10.start()
  p11 = Process(target=func11)
  p11.start()
  p12 = Process(target=func12)
  p12.start()
  p13 = Process(target=func13)
  p13.start()
  p14 = Process(target=func14)
  p14.start()
  p15 = Process(target=func15)
  p15.start()
  p16 = Process(target=func16)
  p16.start()  
  p1.join()
  p2.join()
  p3.join()
  p4.join()   
  p5.join()
  p6.join()
  p7.join()
  p8.join()
  p9.join()
  p10.join()
  p11.join()
  p12.join()
  p13.join()
  p14.join()
  p15.join()
  p16.join()

##### Delete input files from spool folders #####

# try:
#     dir = spool_folder
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder2
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder3
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder4
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder5
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder6
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder7
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder8
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder9
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder10
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder11
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder12
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder13
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder14
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder15
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

# try:
#     dir = spool_folder16
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
# except Exception:
#     pass

end = time.time()

time.sleep(10)
print("Run time is")
print(end - start)
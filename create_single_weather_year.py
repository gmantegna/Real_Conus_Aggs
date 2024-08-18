import pandas as pd
import numpy as np
from pathlib import Path
import shutil

base_folder = Path(".")
base_case_folder = Path("./results_25z")
years=[2007,2008,2009,2010,2011,2012,2013]

for year in years:
    print("year is {}".format(year))
    new_path = base_folder / (base_case_folder.name + "_{}".format(year))
    shutil.copytree(base_case_folder,new_path)
    new_inputs_path = new_path / "2045" / "t52nr_2045" / "Inputs"
    time_index_range = np.arange(1,8761)+(year-2007)*8760
    single_year_index=pd.Index(np.arange(1,8761),name="Time_Index")

    #modify Generators_variability
    gen_var = pd.read_csv(new_inputs_path / "Generators_variability.csv",index_col=0)
    gen_var_new=gen_var.loc[time_index_range,:].copy(deep=True)
    gen_var_new.index=single_year_index
    gen_var_new.to_csv(new_inputs_path / "Generators_variability.csv",index=True)
    print("created gen_var")

    #modify Fuels_data
    fuels = pd.read_csv(new_inputs_path / "Fuels_data.csv",index_col=0)
    first_row_df = fuels.loc[[0],:]
    fuels_new = fuels.loc[time_index_range,:].copy(deep=True)
    fuels_new.index=single_year_index
    fuels_final = pd.concat([first_row_df,fuels_new],axis=0)
    fuels_final.to_csv(new_inputs_path / "Fuels_data.csv",index=True)
    print("created fuels")

    #modify Load_data
    load = pd.read_csv(new_inputs_path / "Load_data.csv")
    load_cols_bool=load.columns.str.contains("Load") | load.columns.str.contains("Time_Index")
    just_load_data=load.loc[:,load_cols_bool].copy(deep=True)
    not_load_data=load.loc[:,~load_cols_bool].copy(deep=True).loc[:8760,:]
    just_load_data.set_index("Time_Index",inplace=True)
    just_load_data_new=just_load_data.loc[time_index_range,:].copy(deep=True)
    just_load_data_new.index=single_year_index
    just_load_data_new.reset_index(inplace=True)
    load_final=pd.concat([not_load_data,just_load_data_new],axis=1)
    load_final.to_csv(new_inputs_path / "Load_data.csv",index=False)
    print("created load")


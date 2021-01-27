import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DataFrameからチャンネル・分光結晶ごとにデータを取り出す
def select_df(df, ch, crystal):
    ch_crystal = df[ ( df["ch"] == ch ) & ( df["crystal"] == crystal ) ]
    return ch_crystal

def select_element(df, element):
    df_element = df[ df["element"] == element ]
    return df_element

def make_plotdata(df):
    date = df["date (y/m/d)"]
    intensity = df["net (count per sec)"] / df["probe_corrent (nA)"]
    return date, intensity

# データをプロットする
def plot_data(ax, ch_crystal, df):
    ch1_tap = select_df(df, 1, "TAP")
    ch1_lde = select_df(df, 1, "LDE")
    ch2_tap = select_df(df, 2, "TAP")
    ch2_lif = select_df(df, 2, "LIF")
    ch3_peth = select_df(df, 3, "PETH")
    ch3_lifh = select_df(df, 3, "LIFH")
    ch4_petj = select_df(df, 4, "PETJ")
    ch4_lif = select_df(df, 4, "LIF")
    ch5_pet = select_df(df, 5, "PET")
    ch5_lif = select_df(df, 5, "LIF")
    
    elements_tap, df_tap = [ "Na", "Mg", "Al", "Si" ], [ "df_na", "df_mg", "df_al", "df_si" ]
    elements_pet, df_pet = [ "P", "K", "Ca", "Ti", "V" ], [ "df_p", "df_k", "df_ca", "df_ti", "df_v"]
    elements_lif, df_lif = [ "Cr", "Mn", "Fe", "Ni" ], [ "df_cr", "df_mn", "df_fe", "df_ni" ]
    
    if ch_crystal == "CH-1_TAP":
        for i, element in enumerate(elements_tap):
            df_tap[i] = select_element(ch1_tap, element)
            date, intensity = make_plotdata(df_tap[i])
            ax.plot( date, intensity, marker="o", label=element )

    elif ch_crystal == "CH-2_TAP":
        for i, element in enumerate(elements_tap):
            df_tap[i] = select_element(ch2_tap, element)
            date, intensity = make_plotdata(df_tap[i])
            ax.plot( date, intensity, marker="o", label=element )

    elif ch_crystal == "CH-3_PETH":
        for i, element in enumerate(elements_pet):
            df_pet[i] = select_element(ch3_peth, element)
            date, intensity = make_plotdata(df_pet[i])
            ax.plot( date, intensity, marker="o", label=element )
    
    elif ch_crystal == "CH-3_LIFH":
        for i, element in enumerate(elements_lif):
            df_lif[i] = select_element(ch3_lifh, element)
            date, intensity = make_plotdata(df_lif[i])
            ax.plot( date, intensity, marker="o", label=element )
    
    elif ch_crystal == "CH-4_PETJ":
        for i, element in enumerate(elements_pet):
            df_pet[i] = select_element(ch4_petj, element)
            date, intensity = make_plotdata(df_pet[i])
            ax.plot( date, intensity, marker="o", label=element )

    elif ch_crystal == "CH-5_LIF":
        for i, element in enumerate(elements_lif):
            df_lif[i] = select_element(ch5_lif, element)
            date, intensity = make_plotdata(df_lif[i])
            ax.plot( date, intensity, marker="o", label=element )

def main():
    df = pd.read_csv("epma_monitor_15kV.csv")

    fig = plt.figure(figsize=(20, 10))
    list_title = [ "CH-1_TAP", "CH-1", "CH-2_TAP", "CH-2","CH-3_PETH", "CH-3_LIFH", \
                   "CH-4_PETJ", "CH-4", "CH-5_LIF", "CH-5"]
    for num, ch_crystal in enumerate(list_title):
        ax = fig.add_subplot(3,4,num+1)
        ax.set_title(ch_crystal)
        plot_data(ax, ch_crystal, df)
        ax.set_xlabel("Date (y/m/d)")
        ax.set_ylabel("Intensity (cps/nA)")
        ax.legend()
    # グラフタイトルと軸ラベルが重なることを防ぐ
    fig.tight_layout()
    fig.savefig( "monitor_15kV.jpg", bbox_inches="tight", dpi=300 )

if __name__ == '__main__':
    main()
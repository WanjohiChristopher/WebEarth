
import numpy as np
import pandas as pd
#read dataset
shopify=pd.read_csv("https://bit.ly/ShoprityDS")


def make_x_and_y():
    x = shopify['Outlet_Establishment_Year']
    y = shopify['Item_Outlet_Sales']
    return x, y
import csv
from collections import namedtuple
import pandas as pd
import os
from pathlib import Path
import copy
import warnings
warnings.filterwarnings("ignore")

# Global variables

FILE_DIRECTORY = __file__
CSV_DIRECTORY = str(FILE_DIRECTORY).split("\src")[0] + "/resources"

ARTISTS_CSV = os.path.join(CSV_DIRECTORY, "artists.csv")
TRACKS_CSV = os.path.join(CSV_DIRECTORY, "tracks.csv")

def ImportCSV2df(filename):
    df = pd.read_csv(filename)
    return df

def String2List(dataframe, column):
    for idx, row in dataframe.iterrows():
        dataframe[column][idx] = dataframe[column][idx].strip('"').strip(']').strip('[').replace("'","").split(", ")
    return dataframe

def RenameDFColumns(dataframe, orig_col = None, new_col = None):
    new = dataframe.rename(columns = {orig_col: new_col})
    return new

def RemoveElementFromList(List, Word):
    for elem in List:
        if elem == Word:
            List.remove(elem)
    return List

def ExpandDF(dataframe, id_vars = None, rename_column = None):
    new = dataframe[rename_column].apply(pd.Series) \
        .merge(dataframe, left_index = True, right_index = True) \
        .drop(rename_column, axis = 1) \
        .melt(id_vars = id_vars, value_name = rename_column) \
        .dropna() \
        .reset_index() \
        .drop(["variable", "index"], axis = 1) 
    return new

def ShapeDF(CSV_File, drop_column = None, reformat_column = None):
    dataframe = ImportCSV2df(CSV_File)
    if drop_column != None:
        dataframe.pop(drop_column)
    modified_df = String2List(dataframe, reformat_column)
    new_df_columns = RemoveElementFromList(list(modified_df.columns), reformat_column)
    new_df = ExpandDF(modified_df, id_vars = new_df_columns, rename_column = reformat_column)
    return new_df
  
def JoinDFs(df1, df2, left_key, right_key):
    merged_df = pd.merge(df1, df2, left_on = left_key, right_on = right_key, how='inner')
    return merged_df

def MergeCSVs():
    Total_Data = Path(os.path.join(CSV_DIRECTORY, "Merged_Data.csv"))
    if Total_Data.is_file():
        pass
    else:
        Tracks_Df = ShapeDF(TRACKS_CSV, drop_column = 'artists', reformat_column = 'id_artists')
        Tracks_Df.to_csv(os.path.join(CSV_DIRECTORY, "Track_Data.csv"))
        Renamed_Tracks_DF = RenameDFColumns(Tracks_Df, "id", "id_song")
        Renamed_Tracks_DF = RenameDFColumns(Renamed_Tracks_DF, "popularity", "song_popularity")
        Renamed_Tracks_DF = RenameDFColumns(Renamed_Tracks_DF, "name", "song_name")
        Artists_Df = ShapeDF(ARTISTS_CSV, reformat_column = 'genres')
        Renamed_Artists_DF = RenameDFColumns(Artists_Df, "id", "id_artists")
        Renamed_Artists_DF = RenameDFColumns(Renamed_Artists_DF, "popularity", "artist_popularity")
        Renamed_Artists_DF = RenameDFColumns(Renamed_Artists_DF, "name", "artist_name")
        Artists_Df.to_csv(os.path.join(CSV_DIRECTORY, "Artists_Data.csv"))
        Merged_DF = JoinDFs(Renamed_Tracks_DF, Renamed_Artists_DF, left_key = 'id_artists', right_key = 'id_artists')
        Merged_DF.to_csv(os.path.join(CSV_DIRECTORY, "Merged_Data.csv"))    

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    if __name__ == '__main__':
        MergeCSVs()
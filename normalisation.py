
##---------------##
## NORMALISATION ##
##---------------##
## -> This file contain different normalisation function for
## the flow cytometry dataset.
## -> Last version of the flow cytometry dataset is considered to be
##    flow_cytometry_transmart_like_PHASE_I_II.csv
## -> write all produced files in a sub data directory


def get_omic_to_center():
    """
    Use the transmart data file to assign a center to each omic ID
    return a dictionnary:
        { omic : center }
    """

    ## importation
    import pandas as pd

    ## parameters
    omic_to_center = {}
    transmart_data_file = "data/transmart_PHASE_I_and_II_29_01_2019.tsv"
    center_var = "\\Cross Sectional\\Low Dimensional Data\\Clinical\\Sampling\\CENTER\\"
    omic_var = "\\Cross Sectional\\Low Dimensional Data\\Clinical\\Sampling\\OMIC number\\"

    ## load dataset
    df = pd.read_csv(transmart_data_file, sep="\t")
    for index, row in df.iterrows():

        ## extract data
        center = row[center_var]
        omicid = row[omic_var]

        ## process center
        center = center.split("_")
        if(center[0] in ["1007", "1014", "1015", "1016"]):
            center = "DRFZ"
        elif(center[0] == "1004"):
            center = "SAS"
        elif(center[0] == "1005"):
            center = "UBO"
        elif(center[0] == "1012"):
            center = "UCL"
        elif(center[0] in ["1017","1018"]):
            center = "IDIBELL"
        elif(center[0] == "1008"):
            center = "UNIGE"
        elif(center[0] in ["1006", "1013"]):
            center = "IRCCS"
        elif(center[0] == "1011"):
            center = "KUL"
        elif(center[0] in ["1001","1002","1003","1019"]):
            center = "FPS"
        elif(center[0] == "1010"):
            center = "MMH"
        elif(center[0] == "1009"):
            center = "CHP"
        else:
            center = "NA"

        ## assign omic to center
        omic_to_center[omicid] = center

    ## return omic to center
    return omic_to_center



def simple_normalisation():
    """
    Load cytometry dataset
    Perform a classic standardisation on all datatset
    Save dataset in a csv file
    """

    ## parameters
    input_file_name = "data/flow_cytometry_transmart_like_PHASE_I_II.csv"
    output_file_name = "data/flow_cytometry_simple_normalisation.csv"

    ## importation
    import pandas as pd
    from sklearn import preprocessing
    import numpy as np

    ## [LOAD DATASET]
    # load cytmetry dataset
    df_cyto = pd.read_csv(input_file_name, sep="\t", low_memory=False)

    # Set non float values to np.nan
    df_cyto = df_cyto.replace('MISSING', np.nan)
    df_cyto = df_cyto.replace('ERROR_FREQ', np.nan)
    df_cyto = df_cyto.replace('ERROR', np.nan)

    # create a tmp dataset without OMICID
    df_tmp = df_cyto.drop(columns=["\\Cross Sectional\\Low Dimensional Data\\Clinical\Sampling\\OMIC number\\ "])

    ## [PERFORM STANDARDISATION]
    # Get column names first
    names = df_tmp.columns

    # Create the Scaler object
    scaler = preprocessing.StandardScaler()

    # Fit data on the scaler object
    scaled_df = scaler.fit_transform(df_tmp)
    scaled_df = pd.DataFrame(scaled_df, columns=names)

    ## [SAVE RESULTS]
    # re add OMICID
    scaled_df['OMICID'] = df_cyto["\\Cross Sectional\\Low Dimensional Data\\Clinical\Sampling\\OMIC number\\ "]

    # save standardized data
    scaled_df.to_csv(output_file_name, index=False)


def center_normalisation():
    """
    Apply a standardisation for each center and then merge the standardized
    dataset
    Save dataset in a csv file
    """

    ## importation
    import pandas as pd
    import numpy as np
    from sklearn import preprocessing

    ## parameters
    input_file_name = "data/flow_cytometry_transmart_like_PHASE_I_II.csv"
    dataset_file_list = []
    output_file_name = "data/flow_cytometry_center_normalisation.csv"

    ## [LOAD DATASET]
    ## load dataset
    df_cyto = pd.read_csv(input_file_name, sep="\t")

    # Set non float values to np.nan
    df_cyto = df_cyto.replace('MISSING', np.nan)
    df_cyto = df_cyto.replace('ERROR_FREQ', np.nan)
    df_cyto = df_cyto.replace('ERROR', np.nan)

    ## rename stupid variable
    df_cyto = df_cyto.rename(columns={"\\Cross Sectional\\Low Dimensional Data\\Clinical\\Sampling\\OMIC number\\ ":'OMICID'})

    ## get omic to center
    omic_to_center = get_omic_to_center()

    ## add center
    df_cyto['CENTER'] = df_cyto['OMICID']
    for omic in omic_to_center.keys():
        df_cyto["CENTER"] = df_cyto["CENTER"].replace(omic, omic_to_center[omic])


    ## [ SPLIT DATASET TO CENTER]
    ## get list of center
    center_list = []
    for center in omic_to_center.values():
        if(center not in center_list):
            center_list.append(center)

    ## split dataset to center
    for center in center_list:

        ## create df for specific center & rename OMICID col
        df_center = df_cyto[df_cyto['CENTER'] == center]

        ## generate output file name
        output_file_name = "data/center_"+str(center)+"_data.csv"

        omic_list = list(df_center['OMICID'])

        ## drop CENTER and OMICID
        df_tmp = df_center.drop(columns=['CENTER', 'OMICID'])

        # Get column names first
        names = df_tmp.columns

        # Create the Scaler object
        scaler = preprocessing.StandardScaler()

        # Fit your data on the scaler object
        scaled_df = scaler.fit_transform(df_tmp)
        scaled_df = pd.DataFrame(scaled_df, columns=names)

        ## readd center and OMICID
        scaled_df['CENTER'] = center
        scaled_df['OMICID'] = omic_list


        ## save scaled center dataset
        scaled_df.to_csv(output_file_name)
        dataset_file_list.append(output_file_name)


    ## [ASSEMBLE FILES]
    # create a list of dataframe and concat all dataframes in this list
    # to craft a final dataframe
    df_list = []
    for f_df in dataset_file_list:
        center_df = pd.read_csv(f_df)
        df_list.append(center_df)
    final_df = pd.concat(df_list)

    # save dataframe to a csv file
    final_df.to_csv(output_file_name)

#normalisation()
#simple_normalisation()
center_normalisation()

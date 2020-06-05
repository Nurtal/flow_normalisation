

def craft_panel_3_dataset():
    """
    Craft P3 for SERVIER analysis
    """

    ## importation
    import pandas as pd

    ## load datafile
    df = pd.read_csv("data/flow_cytometry_center_normalisation.csv")

    ## select P3 variables
    var_to_keep = ['OMICID']
    for k in df.keys():
        var = k.split("\\ ")
        var = var[-1]
        var = var.split("/")
        var = var[0]
        if(var == 'P3'):
            var_to_keep.append(k)
    df = df[var_to_keep]

    ## assign SERVIER Clusters
    # -> load omicid to cluster
    omicid_to_cluster = {}
    labels = pd.read_csv("data/labels.csv")
    for index, row in labels.iterrows():
        omicid = row['OMIC']
        cluster = row['Cluster']
        omicid_to_cluster["N"+str(omicid)] = cluster

    # -> Keep only patients assigned to a cluster
    df = df[df['OMICID'].isin(list(omicid_to_cluster.keys()))]

    # -> Add a cluster columns
    df['CLUSTER'] = df['OMICID']
    df = df.replace({"CLUSTER":omicid_to_cluster})

    ## save dataset
    df.to_csv("data/panel_3_center_normalisation.csv", index=False)



def craft_panel_5_dataset():
    """
    Craft P5 for SERVIER analysis
    """

    ## importation
    import pandas as pd

    ## load datafile
    df = pd.read_csv("data/flow_cytometry_center_normalisation.csv")

    ## select P3 variables
    var_to_keep = ['OMICID']
    for k in df.keys():
        var = k.split("\\ ")
        var = var[-1]
        var = var.split("/")
        var = var[0]
        if(var == 'P5'):
            var_to_keep.append(k)
    df = df[var_to_keep]

    ## assign SERVIER Clusters
    # -> load omicid to cluster
    omicid_to_cluster = {}
    labels = pd.read_csv("data/labels.csv")
    for index, row in labels.iterrows():
        omicid = row['OMIC']
        cluster = row['Cluster']
        omicid_to_cluster["N"+str(omicid)] = cluster

    # -> Keep only patients assigned to a cluster
    df = df[df['OMICID'].isin(list(omicid_to_cluster.keys()))]

    # -> Add a cluster columns
    df['CLUSTER'] = df['OMICID']
    df = df.replace({"CLUSTER":omicid_to_cluster})

    ## save dataset
    df.to_csv("data/panel_5_center_normalisation.csv", index=False)



def craft_article_dataset():
    """
    Craft dataset for the SERVIER
    """

    ## importation
    import pandas as pd

    ## parameters
    # -> target variables
    target_variables = ["\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/PMN_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD15HIGHCD16NEG_EOSINOPHILS_IN PMN_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\ P1/CD15LOWCD16HIGH_NEUTROPHILS_IN PMN_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/MONOCYTES_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD14HIGHCD16NEG_CLASSICALMONOCYTES_IN CD14POS_MONOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD14LOWCD16POS_NONCLASSICALMONOCYTES_IN CD14POS_MONOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD14POSCD16POS_INTERMEDIATEMONOCYTES_IN CD14POS_MONOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/LYMPHOCYTES_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD19POS_BCELLS_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD3POS_TCELLS_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD3POSCD56POS_NKLIKETCELLS_IN CD3POS_TCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\Flow cytometry\\ P1/CD4POS_TCELLS_IN CD3POS_TCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD8NEG_CD4NEG_TCELLS_IN CD3POS_TCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD8POS_CD4POS_TCELLS_IN CD3POS_TCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD8POS_TCELLS_IN CD3POS_TCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD3NEGCD56POS_NKCELLS_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD56HIGH_CD16LOW_IN CD3NEGCD56POS_NKCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P1/CD56LOW_CD16HIGH_IN CD3NEGCD56POS_NKCELLS_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/BASOPHILS_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/DC_IN LEUKOCYTES_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/MDC_IN DC_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/CD1CNEG_CD141NEG_IN MDC_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/MDC1_IN MDC_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/MDC2_IN MDC_FREQUENCY",
    "\\Cross Sectional\\Low Dimensional Data\\Flow cytometry\\ P2/PDC_IN DC_FREQUENCY"]

    ## load datafile
    df = pd.read_csv("data/flow_cytometry_center_normalisation.csv")

    ## select target variables
    var_to_keep = ['OMICID']
    for k in df.keys():

        print(k)



    ## rename variables

    ## assign cluster

    ## save dataset





#craft_panel_5_dataset()
#craft_panel_3_dataset()
craft_article_dataset()

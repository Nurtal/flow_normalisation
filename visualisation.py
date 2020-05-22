


def run_lda(data_file, target_names, panel):
    """
    Use dataset contain in data_file to perform a LDA on specific center
    (target_names) on a specific panel

        - data_file is the name of the file to process, files are produced with
          the normalisation module
        - target_names is a list of center to target, must be 4 target to have
          a 3d representation space
        - panel is the panel to anayse, a string or an int from 1 to 9
    """

    ## importation
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from mpl_toolkits.mplot3d import Axes3D

    ## parameters
    graphe_title = data_file.replace("data/", "")
    graphe_title = graphe_title.split("_")
    graphe_title = "AFD on "+str(graphe_title[0])+" dataset"

    ## load data
    df = pd.read_csv(data_file)

    ## drop variables outside the specific selected panel
    variable_to_drop = []
    for var in df.keys():
        varname = var.split("\\")
        varname = varname[-1]
        varname = varname.split("/")
        if(varname[0] not in ['CENTER', ' P'+str(panel), 'OMICID']):
            variable_to_drop.append(var)
    df = df.drop(columns=variable_to_drop)

    ## drop na
    df = df.dropna()

    indexNames = df[(df['CENTER'] != target_names[0]) & (df['CENTER'] != target_names[1]) & (df['CENTER'] != target_names[2]) & (df['CENTER'] != target_names[3])].index
    df.drop(indexNames , inplace=True)
    df = df.drop(columns=['OMICID'])


    ## Extract data
    y = np.array(df['CENTER'].replace({target_names[0]:0,target_names[1]:1,target_names[2]:2,target_names[3]:3}))
    df2 = df.drop(columns=['CENTER'])
    X = []
    for index, row in df2.iterrows():
        X.append(row.values)
        var_list = list(row.keys())
    X = np.array(X)

    ## Perform LDA
    lda = LinearDiscriminantAnalysis(n_components=3)
    X_r2 = lda.fit(X, y).transform(X)

    ## Display results
    colors = ['red', 'green', 'blue', "darkorange"]
    lw = 2
    fig = plt.figure()
    ax = Axes3D(fig)
    for color, i, target_name in zip(colors, [0, 1, 2, 3], target_names):
        ax.scatter(X_r2[y == i, 0], X_r2[y == i, 1], X_r2[y == i, 2], alpha=.8, color=color,
                    label=target_name)
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title(graphe_title)
    plt.show()
    plt.close()




## RUN EXEMPLE
#target_names = ['UBO','UNIGE','FPS','UCL']
#run_lda('data/flow_cytometry_center_normalisation.csv', target_names, "3")

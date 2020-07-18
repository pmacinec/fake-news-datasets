import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import gensim
import nltk
from nltk.corpus import stopwords


def missing_values_analysis(df: pd.DataFrame) -> None:
    """
    Analyse missing values in dataframe attributes.

    :param df: input dataframe.
    """
    for column in df.columns:
        missing_count = len(df[column][df[column].isna()])
        missing_percentage = round(missing_count / len(df) * 100, 2)
        if missing_count > 0:
            print(f'{column}: {missing_count} ({missing_percentage}%)')

    print('\nMissing values plot (inverse logic, plot is showing how many values are not NaN):')
    msno.bar(df);


def one_value_attributes_analysis(df: pd.DataFrame) -> None:
    """
    Check which attributes contain only one value.

    :param df: input dataframe.
    """
    for col in df.columns:
        if len(df.loc[:, col].dropna().unique()) == 1:
            print(col)


def analyse_numerical_attributes(df: pd.DataFrame, label_column: str, columns: list = None) -> None:
    """
    Analysis of numerical attributes.

    :param df: input dataframe.
    :param label_column: column representing label.
    :param columns: list of columns to use, if None, all columns are used.    
    """
    columns = columns if columns is not None else list(df.columns)

    if columns:
        for col in columns:
            boxplot_per_classes(df, col, label_column, title=f'Boxplot of attribute {col} per class')
            kdeplot_per_classes(df, col, label_column, title=f'Kdeplot of attribute {col} per class')


def analyse_categorical_attributes(df: pd.DataFrame, label_column: str, columns: list = None) -> None:
    """
    Analysis of categorical attributes.

    :param df: input dataframe.
    :param label_column: column representing label.
    :param columns: list of columns to use, if None, all columns are used.
    """
    columns = columns if columns is not None else list(df.columns)
    
    if columns:
        for col in columns:
            if col == label_column:
                continue
            barplot_per_classes(df, col, label_column, title=f'Barplot of attribute {col} per class', ticks_rotation=90, topn=15)


def check_correlations(df: pd.DataFrame, columns: list = None) -> None:
    """
    Check correlations of numerical attributes.

    :param df: input dataframe.
    :param columns: list of columns to use, if None, all columns are used.
    """
    columns = columns if columns is not None else list(df.columns)

    if columns:
        fig, ax = plt.subplots(figsize=(10,10))
        sns.heatmap(
            df[columns].corr(),
            annot=True,
            fmt=".2f",
            vmin=-1.0,
            vmax=1.0,
            square=True
        );


def barplot_per_classes(
    df: pd.DataFrame,
    attribute: str,
    groupby: str,
    title: str = None,
    ticks_rotation: int = 0,
    topn: int = None
) -> None:
    """
    Draw barplot of attribute per each class.
    
    :param df: dataframe with data to be drawn on barplot.
    :param attribute: name of attribute to be drawn on barplot.
    :param groupby: name of attribute with predicted classes.
    :param title: title of plot.
    :param ticks_rotation: rotation of x-ticks (labels).
    :param topn: top n classes to be drawn on the plot.
    """
    uniq_values = df[attribute].value_counts().head(topn).index
    df = df[df[attribute].isin(uniq_values)]
    data = df.groupby(groupby)[attribute] \
        .value_counts(normalize=True) \
        .rename('percentage') \
        .mul(100) \
        .reset_index()
    sns.barplot(attribute, 'percentage', hue=groupby, data=data)
    plt.xticks(rotation=ticks_rotation)
    plt.title(title)

    
def kdeplot_per_classes(
    df: pd.DataFrame,
    attribute: str,
    groupby: str,
    title: str = None,
    ticks_rotation: int = 0
) -> None:
    """
    Draw kdeplot of attribute per each class.
    
    :param df: dataframe with data to be drawn on kdeplot.
    :param attribute: name of attribute to be drawn on kdeplot.
    :param groupby: name of attribute with predicted classes.
    :param title: title of plot.
    :param ticks_rotation: rotation of x-ticks (labels).
    """
    for x in df[groupby].unique():
        sns.kdeplot(df[df[groupby] == x][attribute], label=x, shade=True, shade_lowest=False)
    plt.title(title)
    plt.xticks(rotation=ticks_rotation)


def boxplot_per_classes(
    df: pd.DataFrame,
    attribute: str,
    groupby: str,
    title: str = None,
    ticks_rotation: int = 0
) -> None:
    """
    Draw boxplot of attribute per each class.
    
    :param df: dataframe with data to be drawn on boxplot.
    :param attribute: name of attribute to be drawn on boxplot.
    :param groupby: name of attribute with predicted classes.
    :param title: title of plot.
    :param ticks_rotation: rotation of x-ticks (labels).
    """
    sns.boxplot(x=groupby, y=attribute, data=df)
    plt.title(title)
    plt.xticks(rotation=ticks_rotation)

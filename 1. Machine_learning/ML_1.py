from statsmodels.api import datasets
iris = datasets.get_rdataset("iris")
iris.data.columns = ['Sepal_length', 'Sepal_width', 'Petal_length', 'Petal_width', 'Species']

#print(iris.data.head())
#print(iris.data.dtypes)


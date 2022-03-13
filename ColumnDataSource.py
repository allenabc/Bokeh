from bokeh.plotting import figure
from bokeh.models import ColumnDataSource

# create dict as basis for ColumnDataSource
data = {'x_values': [1, 2, 3, 4, 5],
        'y_values': [6, 7, 2, 3, 6]}

# create ColumnDataSource based on dict
source = ColumnDataSource(data=data)

# create a plot and renderer with ColumnDataSource data
p = figure()
p.circle(x='x_values', y='y_values', source=source)

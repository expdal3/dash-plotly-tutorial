import dash
import dash_core_components as dcc
import dash_html_components as html

xbar = ['Import', 'Export', 'GDP', 'Inflation']
print(dcc.__version__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash',
    style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Reporting for Canada Area:
    ''',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': xbar, 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': xbar, 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montreal'},
                {'x': xbar, 'y': [3, 10, 5, 2], 'type': 'bar', 'name': u'Canada'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


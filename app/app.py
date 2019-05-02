import sys,os
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import Flask, send_from_directory

sys.path.insert(0, 'C:/Users/user/PycharmProjects/flask+dash')

server = Flask(__name__, static_folder='static')

app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title ='Специалист продаж'


app.layout = html.Div([
        html.Link(rel="shortcut icon", href="static/favicon.ico"),
        html.P('', id='my-p-element1'),
        html.Img(
            src='https://pp.userapi.com/c636317/v636317283/6bdbf/4UBvrBo_vPY.jpg',
            ),
        html.P('', id='my-p-element2'),
        html.H1('Специалист отдела продаж ГК AVA-Group'),
        html.H1(html.Label([html.A('ava-sochi.ru', href='https://avagroup.ru/novostroyki/mo_komfort/')])),
        html.H2(html.A('8 918 043 44 48', href="tel:+79180434448")),


], style={'text-align': 'center', 'padding-top': '50px', "width":'100%', 'height':'100%'})


if __name__ == '__main__':
    app.run_server(debug=False)

# coding: utf-8

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import os
import plotly.figure_factory as ff

app = dash.Dash(__name__)
server = app.server

# read data for tables (one df per table)
df_fund_facts = pd.read_csv('https://plot.ly/~bdun9/2754.csv')
df_price_perf = pd.read_csv('https://plot.ly/~bdun9/2756.csv')
df_current_prices = pd.read_csv('https://plot.ly/~bdun9/2753.csv')
df_hist_prices = pd.read_csv('https://plot.ly/~bdun9/2765.csv')
df_avg_returns = pd.read_csv('https://plot.ly/~bdun9/2793.csv')
df_after_tax = pd.read_csv('https://plot.ly/~bdun9/2794.csv')
df_recent_returns = pd.read_csv('https://plot.ly/~bdun9/2795.csv')
df_equity_char = pd.read_csv('https://plot.ly/~bdun9/2796.csv')
df_equity_diver = pd.read_csv('https://plot.ly/~bdun9/2797.csv')
df_expenses = pd.read_csv('https://plot.ly/~bdun9/2798.csv')
df_minimums = pd.read_csv('https://plot.ly/~bdun9/2799.csv')
df_dividend = pd.read_csv('https://plot.ly/~bdun9/2800.csv')
df_realized = pd.read_csv('https://plot.ly/~bdun9/2801.csv')
df_unrealized = pd.read_csv('https://plot.ly/~bdun9/2802.csv')

df_graph = pd.read_csv("https://plot.ly/~bdun9/2804.csv")

# reusable componenets
def make_dash_table(df):
    ''' Return a dash definitio of an HTML table for a Pandas dataframe '''
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


def print_button():
    printButton = html.A(['Print PDF'],className="button no-print print",style={'position': "absolute", 'top': '-40', 'right': '0'})
    return printButton

# includes page/full view
def get_logo():
    logo = html.Div([
        html.Div([
            html.Img(src='http://www.web.uvic.ca/~lidavid/images/logo.png', width = 25, height = 25)
			# Consider adding link to git repo.
        ], className="ten columns padded"),

        html.Div([
            dcc.Link('Full View   ', href='/full-view')
        ], className="two columns page-view no-print")

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'David Li Personal Databoard')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),
		dcc.Link('Co-op Job Hunt   ', href='/coop', className="tab"),
		dcc.Link('Work Term 1 and 2   ', href='/work-term12', className="tab"),
        #dcc.Link('Price Performance   ', href='/price-performance', className="tab"),

        #dcc.Link('Portfolio & Management   ', href='/portfolio-management', className="tab"),

        #dcc.Link('Fees & Minimums   ', href='/fees', className="tab"),

        #dcc.Link('Distributions   ', href='/distributions', className="tab"),

        dcc.Link('Academic TimeLine   ', href='/academic-timeline', className="tab")

    ], className="row ")
    return menu
	
## Page layouts
overview = html.Div([  # page 1

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Personal Dashboard',
                            className="gs-header gs-text-header padded"),
                    html.P("\
							Simple Dashboard highlighting statistics that are interesting to me."),
					dcc.Graph(
                        id = 'graph-6',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["Spring 2014", "Fall 2014", "Winter 2015",
									"Summer 2015", "Fall 2015","Winter 2016",
									"Summer 2016", "Summer 2017","Fall 2017"],
                                    y = ["0", "6.76", "4.94",
									"8.75","7.80","6.66",
									"7.20","7.67","7.20"],
                                    marker = {"color": "rgb(53, 83, 255)"},
                                    name = "Seasonal GPA"
                                ),
								go.Scatter(
                                    x = ["Spring 2014", "Fall 2014", "Winter 2015",
									"Summer 2015", "Fall 2015","Winter 2016",
									"Summer 2016","Summer 2017", "Fall 2017"],
                                    y = ["0", "6.76", "6.12",
									"6.87","7.10","7.04",
									"7.07","7.12","7.20"],
                                    marker = {"color": "rgb(93, 155, 25)"},
                                    name = "Cumulative GPA"
                                ),
							]
						}),
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")
workTerm1and2 =  html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('ENGR 001',
                            className="gs-header gs-text-header padded"),
                    html.P("\
							For my first work term at the Ministry of Transportation: Information Management Branch (TRAN IMB) which \
							oversees and maintains over 100 applications for TRAN, I learned how to work with JIRA and Confluence, \
							discuss potential workflows and assist to ad-hoc tasks as necessary."),
					
					dcc.Markdown('''
#### JIRA and Confluence
I became familar with Atlassian tools [JIRA](https://www.atlassian.com/software/jira) and [Confluence](https://www.atlassian.com/software/confluence)
> While JIRA offers flexible issue tracking and project management, Confluence is wiki software used for technical documentation to 
> locates information quickly and easily.
* Created JIRA dashboards using JIRA Query Language (JQL), and report templates in Confluence
* Assisted with testing web applications.
* Familiar with Microsoft Office, and organizing emails in Outlook.
```SQL
assignee IN membersOf("Collaboration Squad \
    
	ORDER BY assignee")```				
''')
                ], className=" six columns"),
				
				html.Div([
                    html.H6('ENGR 002',
                            className="gs-header gs-text-header padded"),
					html.P("\
						For my second work term at the Ministry of Transportation: Information Management Branch (TRAN IMB) which \
						oversees and maintains over 100 applications for TRAN, I created scripts to automatic tedious tasks and \
						worked on a Java project (documented environment setup, created login interface and report emailing)"),
					dcc.Markdown('''
#### Second Work Term Summary
I created two scripts, one Change Advisory Board Script to extract RFCs from a spreadsheet containing short-term \
IT Changes for all ministries, and the second script was a server to application list.

* Learned to how write pseudocode and rules for creating good documentation.
* Experience working with Java and in particular Eclipse.
* Exposure to dynamically typed programming languages.
* Programatically created word document using DOM framework used in Microsoft Office Product.
			''')
                ], className=" six columns"),
            ], className="row "),

        ], className="subpage")

    ], className="page")
	
coopJobStats = html.Div([  # page 3

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 3

            html.Div([

                html.Div([
                    html.H6('Personal Dashboard',
                            className="gs-header gs-text-header padded"),
                    html.P("\
							I count the terms when I am looking, not the terms \
							where I would be working. The number interviews I have had through UVIC \
							is 11, 3 in Summer 2B, and 8 in Spring 3A/3B"),
                    html.Br([]),
                    html.H6("Risk Potential",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-risk',
                        figure = {
                            'data': [
                                go.Scatter(
                                    x = ["0", "0.18", "0.18", "0"],
                                    y = ["0.2", "0.2", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.2)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "B",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.2", "0.38", "0.38", "0.2", "0.2"],
                                    y = ["0.2", "0.2", "0.6", "0.4", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.4)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "D",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.4", "0.58", "0.58", "0.4", "0.4"],
                                    y = ["0.2", "0.2", "0.8", "0.6", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.6)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "F",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.6", "0.78", "0.78", "0.6", "0.6"],
                                    y = ["0.2", "0.2", "1", "0.8", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgb(31, 119, 180)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "H",
                                    showlegend = False
                                ),
                                go.Scatter(
                                    x = ["0.8", "0.98", "0.98", "0.8", "0.8"],
                                    y = ["0.2", "0.2", "1.2", "1", "0.2"],
                                    fill = "tozerox",
                                    fillcolor = "rgba(31, 119, 180, 0.8)",
                                    hoverinfo = "none",
                                    line = {"width": 0},
                                    mode = "lines",
                                    name = "J",
                                    showlegend = False
                                ),
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                    {
                                      "x": 0.69,
                                      "y": 0.6,
                                      "font": {
                                        "color": "rgb(31, 119, 180)",
                                        "family": "Raleway",
                                        "size": 30
                                      },
                                      "showarrow": False,
                                      "text": "<b>4</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.0631034482759,
                                      "y": -0.04,
                                      "align": "left",
                                      "font": {
                                        "color": "rgb(44, 160, 44)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>Less risk<br>Less reward</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.92125,
                                      "y": -0.04,
                                      "align": "right",
                                      "font": {
                                        "color": "rgb(214, 39, 40)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "<b>More risk<br>More reward</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 200,
                                  width = 340,
                                  hovermode = "closest",
                                  margin = {
                                    "r": 10,
                                    "t": 20,
                                    "b": 80,
                                    "l": 10
                                  },
                                  shapes = [
                                    {
                                      "fillcolor": "rgb(255, 255, 255)",
                                      "line": {
                                        "color": "rgb(31, 119, 180)",
                                        "width": 4
                                      },
                                      "opacity": 1,
                                      "type": "circle",
                                      "x0": 0.621,
                                      "x1": 0.764,
                                      "xref": "x",
                                      "y0": 0.135238095238,
                                      "y1": 0.98619047619,
                                      "yref": "y"
                                    }
                                  ],
                                  showlegend = True,
                                  xaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.05, 1.05],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "fixedrange": True,
                                    "range": [-0.3, 1.6],
                                    "showgrid": False,
                                    "showticklabels": False,
                                    "title": "<br>",
                                    "type": "linear",
                                    "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                    # html.P("\
                            # As the industry’s first index fund for individual investors, \
                            # the 500 Index Fund is a low-cost way to gain diversified exposure \
                            # to the U.S. equity market. The fund offers exposure to 500 of the \
                            # largest U.S. companies, which span many different industries and \
                            # account for about three-fourths of the U.S. stock market’s value. \
                            # The key risk for the fund is the volatility that comes with its full \
                            # exposure to the stock market. Because the 500 Index Fund is broadly \
                            # diversified within the large-capitalization market, it may be \
                            # considered a core equity holding in a portfolio."),

                ], className="six columns"),

                html.Div([
                    html.H6(["Job Interview Rates and Applications"],
                            className="gs-header gs-table-header padded"),
                    #html.Table(make_dash_table(df_fund_facts))
                ], className="six columns"),
                
                html.Div([
#                    html.P([ "%s%s%s%s%s" % ("Table 477-0058 Financial information of universities and degree-granting colleges", 
#                    "revenues by type of funds",
#                    "annual (dollars x 1,000)(1)", 
#                    "Survey or program details:",
#                    "Financial Information of Universities and Colleges Survey - 3121")],
#                            className="gs-header gs-table-header padded"),
#                    
#                    html.Table(make_dash_table(df_coolgraph)),
#                    
#                    html.P("\
#                            Footnotes: \
#                            1,These data can be subject to interpretation or clarification because of \
#                            inherent differences among institutions in size, academic programs, organizations, \
#                            physical environment, management philosophy, and budgetary and accounting  \
#                            procedures. Therefore comparisons should be made with caution. \
#                            11,Includes government departments and agencies - grants and contracts. \
#                            12,Includes foundations. \
#                            Source: \
#                            Statistics Canada. Table 477-0058 - Financial information \
#                            of universities and degree-granting colleges, revenues by type of funds, annual (dollars) \
#                            (accessed: March 30, 2018)"),
                    html.P("\
							In order to find a co-op work term, I applied to a large \
							number of jobs, but as I am not the best at interviews, \
							I usually appeared as a weak/unprepared candidate, guess I'm \
							no good at answering questions. "),
                    dcc.Graph(
                        id = "graph-bar-interviews",
                        figure={
                            'data': [
                                go.Bar(
                                    x=  ['Victoria', 'Vancouver'],
                                    y = ['3','3'],
                                    marker = {
                                      "color": "rgb(255, 225, 53)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                        }
                                    },
                                    name = "2B term (Summer 2016) Interviews",
                                    type = "bar"
                                ),
                                go.Bar(
                                    x = ['Victoria', 'Vancouver'],
                                    y = ['2','8'],
                                    marker = {
                                      "color": "rgb(53, 83, 255)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    # get list of organization from sub dataframe
                                    name = "3B/3A term (Spring 2018) Interviews",
                                    type = "bar"
                                ),
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                bargap = 0.35,
                                font = {
                                  "family": "Raleway",
                                  "size": 10
                                },
                                height = 200,
                                hovermode = "closest",
                                legend = {
                                  "x": -0.0228945952895,
                                  "y": -0.189563896463,
                                  "orientation": "h",
                                  "yanchor": "top"
                                },
                                margin = {
                                  "r": 0,
                                  "t": 20,
                                  "b": 10,
                                  "l": 10
                                },
                                showlegend = True,
                                title = "",
                                width = 340,
                                xaxis = {
                                  "autorange": True,
                                  "range": [-0.5, 4.5],
                                  "showline": True,
                                  "title": "",
                                  "type": "category"
                                },
                                yaxis = {
                                  "autorange": True,
                                  "range": [0, 22.9789473684],
                                  "showgrid": True,
                                  "showline": True,
                                  "title": "",
                                  "type": "linear",
                                  "zeroline": False
                                }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    ),
				   dcc.Graph(
						id = "graph-appPerTerms",
						figure={
							'data': [
								{
									"labels":  ['Summer 1B', 'Summer 2B','Spring 3A/3B'],
									"values": ['6','79','94'],
									"hoverinfo":'label+percent+name', 
									"textinfo": 'value', 
									"name": "Apps Per Term",
									"type": "pie",
									"hole": .2,
									"domain": {"x": [0, .48]},
								},
								{
									"labels": ['Summer 1B', 'Summer 2B','Spring 3A/3B'],
									"values": ['1','6','12'],
									# get list of organization from sub dataframe
									"name": "Interviews Per Term",
									"hoverinfo":'label+percent+name', 
									"textinfo": 'value', 
									"type": "pie",
									"hole": .2,
									"domain": {"x": [0.65, 1.13]},
								},
							],
							'layout': go.Layout(
								autosize = False,
								font = {
								  "family": "Raleway",
								  "size": 10
								},
								height = 200,
								hovermode = "closest",
								legend = {
								  "x": -0.0228945952895,
								  "y": -0.189563896463,
								  "orientation": "h",
								  "yanchor": "top"
								},
								margin = {
								  "r": 0,
								  "t": 20,
								  "b": 10,
								  "l": 10
								},
								showlegend = True,
								title = "",
								width = 340
							)
						},
						config={
							'displayModeBar': False
						},
                    )
                ], className="six columns"),
            ], className="row "),
        ], className="subpage")
    ], className="page")


pricePerformance = html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row ``

            html.Div([

                html.Div([
                    html.H6(["Current Prices"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_current_prices))

                ], className="six columns"),

                html.Div([
                    html.H6(["Historical Prices"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_hist_prices))
                ], className="six columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.H6("Performance",
                            className="gs-header gs-table-header padded"),
                    dcc.Graph(
                        id='graph-4',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['Vanguard 500 Index Fund'],
                                    line = {"color": "rgb(53, 83, 255)"},
                                    mode = "lines",
                                    name = "Vanguard 500 Index Fund"
                                ),
                                go.Scatter(
                                    x = df_graph['Date'],
                                    y = df_graph['MSCI EAFE Index Fund (ETF)'],
                                    line = {"color": "rgb(255, 225, 53)"},
                                    mode = "lines",
                                    name = "MSCI EAFE Index Fund (ETF)"
                                )
                            ],
                            'layout': go.Layout(
                                autosize = False,
                                width = 700,
                                height = 200,
                                font = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                 margin = {
                                    "r": 40,
                                    "t": 40,
                                    "b": 30,
                                    "l": 40
                                  },
                                  showlegend = True,
                                  titlefont = {
                                    "family": "Raleway",
                                    "size": 10
                                  },
                                  xaxis = {
                                    "autorange": True,
                                    "range": ["2007-12-31", "2018-03-06"],
                                    "rangeselector": {"buttons": [
                                        {
                                          "count": 1,
                                          "label": "1Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 3,
                                          "label": "3Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "count": 5,
                                          "label": "5Y",
                                          "step": "year"
                                        },
                                        {
                                          "count": 10,
                                          "label": "10Y",
                                          "step": "year",
                                          "stepmode": "backward"
                                        },
                                        {
                                          "label": "All",
                                          "step": "all"
                                        }
                                      ]},
                                    "showline": True,
                                    "type": "date",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": True,
                                    "range": [18.6880162434, 278.431996757],
                                    "showline": True,
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="twelve columns")

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Average annual returns--updated monthly as of 02/28/2018"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_avg_returns), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["After-tax returns--updated quarterly as of 12/31/2017"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_after_tax), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 5

            html.Div([

                html.Div([
                    html.H6(["Recent investment returns"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_recent_returns), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")


portfolioManagement = html.Div([ # page 3

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Portfolio"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(["Stock style"]),
                    dcc.Graph(
                        id='graph-5',
                        figure={
                            'data': [
                                go.Scatter(
                                    x = ["1"],
                                    y = ["1"],
                                    hoverinfo = "none",
                                    marker = {
                                        "color": ["transparent"]
                                    },
                                    mode = "markers",
                                    name = "B",
                                )
                            ],
                            'layout': go.Layout(
                                title = "",
                                annotations = [
                                {
                                  "x": 0.990130093458,
                                  "y": 1.00181709504,
                                  "align": "left",
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Market<br>Cap</b>",
                                  "xref": "x",
                                  "yref": "y"
                                },
                                {
                                  "x": 1.00001816013,
                                  "y": 1.35907755794e-16,
                                  "font": {
                                    "family": "Raleway",
                                    "size": 9
                                  },
                                  "showarrow": False,
                                  "text": "<b>Style</b>",
                                  "xref": "x",
                                  "yanchor": "top",
                                  "yref": "y"
                                }
                              ],
                              autosize = False,
                              width = 200,
                              height = 150,
                              hovermode = "closest",
                              margin = {
                                "r": 30,
                                "t": 20,
                                "b": 20,
                                "l": 30
                              },
                              shapes = [
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "dash": "solid",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0,
                                  "y1": 0.33,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.33,
                                  "y1": 0.66,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0,
                                  "x1": 0.33,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(255, 127, 14)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 1
                                  },
                                  "opacity": 0.9,
                                  "type": "rectangle",
                                  "x0": 0.33,
                                  "x1": 0.66,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                },
                                {
                                  "fillcolor": "rgb(127, 127, 127)",
                                  "line": {
                                    "color": "rgb(0, 0, 0)",
                                    "width": 2
                                  },
                                  "opacity": 0.3,
                                  "type": "rectangle",
                                  "x0": 0.66,
                                  "x1": 0.99,
                                  "xref": "paper",
                                  "y0": 0.66,
                                  "y1": 0.99,
                                  "yref": "paper"
                                }
                              ],
                              xaxis = {
                                "autorange": True,
                                "range": [0.989694747864, 1.00064057995],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              },
                              yaxis = {
                                "autorange": True,
                                "range": [-0.0358637178721, 1.06395696354],
                                "showgrid": False,
                                "showline": False,
                                "showticklabels": False,
                                "title": "<br>",
                                "type": "linear",
                                "zeroline": False
                              }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )

                ], className="four columns"),

                html.Div([
                    html.P("Vanguard 500 Index Fund seeks to track the performance of\
                     a benchmark index that meaures the investment return of large-capitalization stocks."),
                    html.P("Learn more about this portfolio's investment strategy and policy.")
                ], className="eight columns middle-aligned"),

            ], className="row "),

            # Row 3

            html.Br([]),

            html.Div([

                html.Div([
                    html.H6(["Equity characteristics as of 01/31/2018"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_char), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.H6(["Equity sector diversification"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_equity_diver), className="tiny-header")
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")

feesMins = html.Div([  # page 4

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Expenses"],
                            className="gs-header gs-table-header padded")
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Strong(),
                    html.Table(make_dash_table(df_expenses)),
                    html.H6(["Minimums"],
                            className="gs-header gs-table-header padded"),
                    html.Table(make_dash_table(df_minimums))
                ], className="six columns"),

                html.Div([
                    html.Br([]),
                    html.Strong("Fees on $10,000 invested over 10 years"),
                    dcc.Graph(
                        id = 'graph-6',
                        figure = {
                            'data': [
                                go.Bar(
                                    x = ["Category Average", "This fund"],
                                    y = ["2242", "329"],
                                    marker = {"color": "rgb(53, 83, 255)"},
                                    name = "A"
                                ),
                                go.Bar(
                                    x = ["This fund"],
                                    y = ["1913"],
                                    marker = {"color": "#ADAAAA"},
                                    name = "B"
                                )
                            ],
                            'layout': go.Layout(
                                annotations = [
                                    {
                                      "x": -0.0111111111111,
                                      "y": 2381.92771084,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$2,242",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995555555556,
                                      "y": 509.638554217,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "$329",
                                      "xref": "x",
                                      "yref": "y"
                                    },
                                    {
                                      "x": 0.995551020408,
                                      "y": 1730.32432432,
                                      "font": {
                                        "color": "rgb(0, 0, 0)",
                                        "family": "Raleway",
                                        "size": 10
                                      },
                                      "showarrow": False,
                                      "text": "You save<br><b>$1,913</b>",
                                      "xref": "x",
                                      "yref": "y"
                                    }
                                  ],
                                  autosize = False,
                                  height = 150,
                                  width = 340,
                                  bargap = 0.4,
                                  barmode = "stack",
                                  hovermode = "closest",
                                  margin = {
                                    "r": 40,
                                    "t": 20,
                                    "b": 20,
                                    "l": 40
                                  },
                                  showlegend = False,
                                  title = "",
                                  xaxis = {
                                    "autorange": True,
                                    "range": [-0.5, 1.5],
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "title": "",
                                    "type": "category",
                                    "zeroline": False
                                  },
                                  yaxis = {
                                    "autorange": False,
                                    "mirror": False,
                                    "nticks": 3,
                                    "range": [0, 3000],
                                    "showgrid": True,
                                    "showline": True,
                                    "tickfont": {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    "tickprefix": "$",
                                    "title": "",
                                    "type": "linear",
                                    "zeroline": False
                                  }
                            )
                        },
                        config={
                            'displayModeBar': False
                        }
                    )
                ], className="six columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Fees"],
                            className="gs-header gs-table-header padded"),

                    html.Br([]),

                    html.Div([

                        html.Div([
                            html.Strong(["Purchase fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")


                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Redemption fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["12b-1 fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.P(["None"])
                        ], className="nine columns")

                    ], className="row "),

                    html.Div([

                        html.Div([
                            html.Strong(["Account service fee"])
                        ], className="three columns right-aligned"),

                        html.Div([
                            html.Strong(["Nonretirement accounts, traditional IRAs, Roth IRAs, UGMAs/UTMAs, SEP-IRAs, and education savings accounts (ESAs)"]),
                            html.P(["We charge a $20 annual account service fee for each Vanguard Brokerage Account, as well as each individual Vanguard mutual fund holding with a balance of less than $10,000 in an account. This fee does not apply if you sign up for account access on vanguard.com and choose electronic delivery of statements, confirmations, and Vanguard fund reports and prospectuses. This fee also does not apply to members of Flagship Select™, Flagship®, Voyager Select®, and Voyager® Services."]),
                            html.Br([]),
                            html.Strong(["SIMPLE IRAs"]),
                            html.P(["We charge participants a $25 annual account service fee for each fund they hold in their Vanguard SIMPLE IRA. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
                            html.Br([]),
                            html.Strong(["403(b)(7) plans"]),
                            html.P(["We charge participants a $15 annual account service fee for each fund they hold in their Vanguard 403(b)(7) account. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."]),
                            html.Br([]),
                            html.Strong(["Individual 401(k) plans"]),
                            html.P(["We charge participants a $20 annual account service fee for each fund they hold in their Vanguard Individual 401(k) account. This fee will be waived for all participants in the plan if at least 1 participant qualifies for Flagship Select, Flagship, Voyager Select, and Voyager Services"]),
                            html.Br([]),
                        ], className="nine columns")

                    ], className="row ")

                ], className="twelve columns")

            ], className="row "),

        ], className="subpage")

    ], className="page")

distributions = html.Div([  # page 5

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6(["Distributions"],
                            className="gs-header gs-table-header padded"),
                    html.Strong(["Distributions for this fund are scheduled quaterly"])
                ], className="twelve columns"),

            ], className="row "),

            # Row 2

            html.Div([

                html.Div([
                    html.Br([]),
                    html.H6(["Dividend and capital gains distributions"], className="gs-header gs-table-header tiny-header"),
                    html.Table(make_dash_table(df_dividend), className="tiny-header")
                ], className="twelve columns"),

            ], className="row "),

            # Row 3

            html.Div([

                html.Div([
                    html.H6(["Realized/unrealized gains as of 01/31/2018"], className="gs-header gs-table-header tiny-header")
                ], className=" twelve columns")

            ], className="row "),

            # Row 4

            html.Div([

                html.Div([
                    html.Table(make_dash_table(df_realized))
                ], className="six columns"),

                html.Div([
                    html.Table(make_dash_table(df_unrealized))
                ], className="six columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")


ganttData = [
    dict(Task='Fall 1A', Start='2014-09-01', Finish='2014-12-28', Resource='firstYear'),
    dict(Task='Spring 1B', Start='2015-01-01', Finish='2015-04-30', Resource='firstYear'),
	dict(Task='Summer 1C', Start='2015-05-01', Finish='2015-08-31', Resource='firstYear'),
	dict(Task='Fall 2A', Start='2015-09-01', Finish='2015-12-31', Resource='secondYear'),
	dict(Task='Courses I', Start='2016-01-01', Finish='2016-04-30', Resource='Other'),
	dict(Task='Summer 2B', Start='2016-05-01', Finish='2016-08-31', Resource='secondYear'),
	dict(Task='ENGR-001', Start='2016-09-14', Finish='2016-12-31', Resource='Coop'),
	dict(Task='ENGR-002', Start='2017-01-01', Finish='2017-04-29', Resource='Coop'),
	dict(Task='Courses II', Start='2017-05-01', Finish='2017-09-30', Resource='Other'),
	dict(Task='Fall 3B', Start='2017-09-01', Finish='2017-12-31', Resource='thirdYear'),
	dict(Task='Spring 3B', Start='2018-01-01', Finish='2018-04-30', Resource='thirdYear'),
	dict(Task='Job Hunt', Start='2015-05-01', Finish='2018-04-30', Resource='thirdYear')
    # dict(Task='Anime', Start='2014-01-01', Finish='2019-01-01', Resource='Anime')
]
ganttData.reverse()
colors = dict(firstYear = 'rgb(46, 17, 255)',
			  secondYear = 'rgb(46, 255, 51)',
			  thirdYear = 'rgb(255, 75, 25)',
              Coop = 'rgb(114, 2, 121)',
              Other = 'rgb(128, 17, 15)',
			  Anime = 'rgb(18, 76, 165)')
fig = ff.create_gantt(ganttData,colors,index_col='Resource', title='Academic Life Thus Far',
                      show_colorbar=True, bar_width=0.2, showgrid_x=True, showgrid_y=True,
					  height=575, width=725)
					  
academicTimeline = html.Div([  # page 6

        print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([

                html.Div([
                    html.H6('Life Timeline',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(figure=fig, id='gantt'),
                ], className="twelve columns")

            ], className="row ")

        ], className="subpage")

    ], className="page")

noPage = html.Div([  # 404

    html.P(["404 Page not found"])

    ], className="no-page")



# Describe the layout, or the UI, of the app
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update page
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/' or pathname == '/overview':
        return overview
    elif pathname == '/work-term12':
        return workTerm1and2
    elif pathname == '/coop':
        return coopJobStats 
    elif pathname == '/price-performance':
        return pricePerformance
    elif pathname == '/portfolio-management':
        return portfolioManagement
    elif pathname == '/fees':
        return feesMins
    elif pathname == '/distributions':
        return distributions
    elif pathname == '/academic-timeline':
        return academicTimeline
    elif pathname == '/full-view':
        return overview,workTerm1and2,coopJobStats,academicTimeline
#    elif pathname == '/full-view':
#        return overview,pricePerformance,portfolioManagement,feesMins,distributions,newsReviews
    else:
        return noPage


external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css",
                "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.server.run(debug=True)

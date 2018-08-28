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
df_examS2018 = pd.read_csv("examSchedule.csv")
df_grades = pd.read_excel("gradesSpread.xlsx")
df_numJobsest = pd.read_csv("numofJobsGuess.txt")
df_numJobs = pd.read_csv("numofJobs.txt")
# reusable components
def make_dash_table(df):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
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
            html.Img(src='https://studentweb.uvic.ca/~lidavid/images/logo.png', width = 25, height = 25)
			# Consider adding link to git repo.
        ], className="ten columns padded"),

        html.Div([
            html.A(['Full View'], href='/full-view', className ="button")
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
        dcc.Link('Co-op Work Terms   ', href='/work-terms', className="tab"),
        dcc.Link('Current Facts   ', href='/current-facts', className="tab"),
        dcc.Link('Random Stuff   ', href='/random-stuff', className="tab"),
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
									"Summer 2016", "Summer 2017","Fall 2017","Spring 2018"],
                                    y = ["0", "6.76", "4.94",
									"8.75","7.80","6.66",
									"7.20","7.67","7.20","4.60"],
                                    marker = {"color": "rgb(53, 83, 255)"},
                                    name = "Seasonal GPA"
                                ),
								go.Scatter(
                                    x = ["Spring 2014", "Fall 2014", "Winter 2015",
									"Summer 2015", "Fall 2015","Winter 2016",
									"Summer 2016","Summer 2017", "Fall 2017","Spring 2018"],
                                    y = ["0", "6.76", "6.12",
									"6.87","7.10","7.04",
									"7.07","7.13","7.15","6.81"],
                                    marker = {"color": "rgb(93, 155, 25)"},
                                    name = "Cumulative GPA"
                                ),
							],
						}),
                ], className=" twelve columns"),

            ], className="row "),

        ], className="subpage")

    ], className="page")
workTerms =  html.Div([  # page 2

        print_button(),

        html.Div([

            # Header
            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),
			
            # ENGR 004 
            html.Div([
                # Row 3
                html.Div([
                    html.H6('ENGR 004',
                        className="gs-header gs-text-header padded"),
                    html.Br([]),
                        html.Div([
                            html.H4([
                                'AI (TBD) Developer',
                            ],
                            className="card-title"),
                                html.P([
                            'As a junior developer I worked to develop system Chat assistance for company.'
                            ], className="card-text")
                        ],className="card .bg-dark")
                    ], className="twelve columns"),
			], className ="row"),
            
            # ENGR 003 
			html.Div([
                # Row 3
                html.Div([
                    html.H6('ENGR 003',
                        className="gs-header gs-text-header padded"),
                    html.Br([]),
                        html.Div([
                            html.H4([
                                'Decentralized Application Developer',
                            ],
                            className="card-title"),
                                html.P([
                            'As a junior developer I worked with blockchain (ethereum and solidity) and web technologies such as react/redux. Also, worked in a start-up environment.'
                            ], className="card-text"),
                            dcc.Markdown('''
 * React, front-end framework made by facebook, its okay, built on top
    of javascript.
 * Solidity, programming language for smart contracts, closely
    resembles javascript, but borrows elements from python and C. Also,
    useful for other blockchains such as Hedera HashGraph.
 * Postgres, advanced open source database, similar syntax to SQL.
    Played around with psql and pg-promise (node wrapper for postgres).
 * Unix/Linux, configured digital ocean droplets, used GNU Screen,
    recommend using OSX to develop as its easier to setup than windows.
                                        ''')
                        ],className="card .bg-dark")
                    ], className="twelve columns"),
			], className ="row"),
			
            # Row 4
            html.Div([
                html.Div([
                    html.H6('ENGR 001',
                            className="gs-header gs-text-header padded"),
                    html.P("\
							I learned how to work with JIRA and Confluence, data visualization \
							discuss potential workflows and assist to ad-hoc tasks as necessary."),
					
					dcc.Markdown('''

I became familar with Atlassian tools [JIRA](https://www.atlassian.com/software/jira) and [Confluence](https://www.atlassian.com/software/confluence)
* Created JIRA dashboards using JIRA Query Language (JQL), and report templates in Confluence
* Assisted with testing web applications.
* Familiar with Microsoft Office, and organizing emails in Outlook.
			
''')
                ], className=" six columns"),
				
				html.Div([
                    html.H6('ENGR 002',
                            className="gs-header gs-text-header padded"),
					html.P("\
						I created scripts to automatic tedious tasks and \
						worked with Java, SQL and VBScript."),
					dcc.Markdown('''
* Learned to how write pseudocode and rules for creating good documentation.
* Experience working with Java and in particular Eclipse.
* Exposure to dynamically typed programming languages.
* Automatic report generation using DOM framework.
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
                            is 11, 3 in Summer 2B, and 8 in Spring 3A/3B."),
                    html.P("\
                            In my final co-op term I got an offer by insane luck, 3 apps, one interview, maybe I'll continue to scrap data from LIM tho."),
                    html.Br([]),
 
                    # My plot to show jobs vs time
                    html.H6("Number of jobs for CENG student in Fall 2018",
                            className="gs-header gs-table-header padded"),
                        dcc.Graph(
                            id='graph-jobsEst',
                            figure = {
                                'data': [
                                go.Scatter(
                                    x=df_numJobsest.Date,
                                    y=df_numJobsest.numOfJobs,
                                    name = "Estimated Jobs",
                                    line = dict(color = '#7F7F7F'),
                                    opacity = 0.8),
                                go.Scatter(
                                    x=df_numJobs.Date,
                                    y=df_numJobs.numOfJobs,
                                    name = "Number of jabs Jobs",
                                    line = dict(color = '#FF1FFF'),
                                    opacity = 0.6)
                                ],
                                'layout': go.Layout(
                                    font = {
                                      "family": "Raleway",
                                      "size": 10
                                    },
                                    height = 400,
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
                                    xaxis = {
                                      "autorange": True,
                                      "showline": True,
                                      "title": "Date (dd-mm-yy)"
                                    },
                                    yaxis = {
                                      "autorange": True,
                                      "showgrid": True,
                                      "showline": True
                                    }
                                )   
                            }
                        )
                            

                ], className="six columns"),
                #html.Table(make_dash_table(df_fund_facts))
                
                html.Div([
                    html.H6(["Job Interview Rates and Applications"], className="gs-header gs-table-header padded"),
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
                            no good at answering questions. \
                            Interestingly, it seems as if there is a increased \
                            percentage of jobs are in Victoria near the end of April."),
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
                                    y = ['7','8'],
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
                                 go.Bar(
                                    x = ['Victoria', 'Vancouver'],
                                    y = ['1','0'],
                                    marker = {
                                      "color": "rgb(2, 255, 15)",
                                      "line": {
                                        "color": "rgb(255, 255, 255)",
                                        "width": 2
                                      }
                                    },
                                    # get list of organization from sub dataframe
                                    name = "4A/4B term (Fall 2019) Interviews",
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
                                    "labels":  ['Fall 2A', 'Summer 2B','Spring 3A/3B','Fall 4A/4B'],
                                    "values": ['6','79','105','3'],
                                    "hoverinfo":'label+percent+name', 
                                    "textinfo": 'value', 
                                    "name": "Apps Per Term",
                                    "type": "pie",
                                    "hole": .2,
                                    "domain": {"x": [0, .48]},
                                },
                                {
                                    "labels": ['Fall 2A', 'Summer 2B','Spring 3A/3B','Fall 4A/4B'],
                                    "values": ['1','6','15','1'],
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
                    ), 
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
                ], className="six columns"),
            ], className="row "),
        ], className="subpage")
    ], className="page")


## BoxPlot Data
xls = pd.ExcelFile('gradesScatterPlot.xlsx')
# First Year
df1 = pd.read_excel(xls, 'term1A')
df2 = pd.read_excel(xls, 'term1B')
df3 = pd.read_excel(xls, 'term1C')

# Second Year
df4 = pd.read_excel(xls, 'term2A')
df5 = pd.read_excel(xls, 'coursesI')
df6 = pd.read_excel(xls, 'term2B')
df7 = pd.read_excel(xls, 'term3A')
df8 = pd.read_excel(xls, 'term3B')

# First Year Courses
year1AMyScores = df1['My Score'].tolist()
year1AAverages = df1['Average'].tolist()
year1BMyScores = df2['My Score'].tolist()
year1BAverages = df2['Average'].tolist()
year1CMyScores = df3['My Score'].tolist()
year1CAverages = df3['Average'].tolist()

firstYearScores = year1AMyScores + year1BMyScores + year1CMyScores
firstYearAvgs   = year1AAverages + year1BAverages + year1CAverages

firstYearLabel = ['Term 1A'] * len(year1AMyScores) +  \
    ['Term 1B'] * len(year1BMyScores) + ['Term 1C'] * len(year1CMyScores)

# Second Year Courses
year2AMyScores = df4['My Score'].tolist()
year2AAverages = df4['Average'].tolist()
year2cIMyScores = df5['My Score'].tolist()
year2cIAverages = df5['Average'].tolist()
year2BMyScores = df6['My Score'].tolist()
year2BAverages = df6['Average'].tolist()

secondYearScores = year2AMyScores + year2cIMyScores + year2BMyScores 
secondYearAvgs   = year2AAverages + year2cIAverages + year2BAverages

secondYearLabel = ['Term 2A'] * len(year2AMyScores) +  \
    ['Term 2.5'] * len(year2cIMyScores) + ['Term 2B'] * len(year2BMyScores)

# Third year courses
year3AMyScores = df7['My Score'].tolist()
year3AAverages = df7['Average'].tolist()
year3BMyScores = df8['My Score'].tolist()
year3BAverages = df8['Average'].tolist()

thirdYearScores = year3AMyScores + year3BMyScores
thirdYearAvgs   = year3AAverages + year3BAverages

thirdYearLabel = ['Term 3A'] * len(year3AMyScores) +  \
    ['Term 3B'] * len(year3BMyScores)

# Plot configurations
myScore = go.Box(
    x=firstYearScores+secondYearScores+thirdYearScores,
    y=firstYearLabel+secondYearLabel+thirdYearLabel,
    name='My Grade',
    marker=dict(
        color='#3D9970'
    ),
    orientation = 'h'
)
Average = go.Box(
    x=firstYearAvgs+secondYearAvgs+thirdYearAvgs,
    y=firstYearLabel+secondYearLabel+thirdYearLabel,
    name='Average',
    marker=dict(
        color='#FF4136'
    ),
     orientation = 'h'
)

# Set up Plot, and include under final exam tables
data3 = [myScore, Average]
layout3 = go.Layout(
    yaxis=dict(
        title='Academic Terms',
        zeroline=False
    ),
    xaxis=dict(
        title='Scores (out of 100)',
        zeroline=False
    ),
    boxmode='group'
)
gradesBP = go.Figure(data=data3, layout=layout3)
currentFacts = html.Div([ # page 4
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
                    html.H6('Spring 2018 Final Exam Schedule',
                            className="gs-header gs-text-header padded"),
                    html.Table(make_dash_table(df_examS2018), className="table table-hover"),
                    #html.Table(make_dash_table(df_grades), className="table table-stripeed")                    
                ], className="twelve columns"),
                
                # Row 2
                html.Div([
                        html.H6('Grades',
                                className="gs-header gs-text-header padded"),
                        dcc.Graph(figure=gradesBP, id='boxplot'),
                    ], className="twelve columns"),
            ], className="row ")

        ], className="subpage")

    ], className="page")    


randomStuff = html.Div([ # page 4
 print_button(),

        html.Div([

            # Header

            get_logo(),
            get_header(),
            html.Br([]),
            get_menu(),

            # Row 1

            html.Div([    # Row 2
                html.Div([
                        html.H6('Some Python',
                            className="gs-header gs-text-header padded"),
                        dcc.SyntaxHighlighter('''
import python
print(3)
import easygui
file = easygui.fileopenbox()
print(file)

from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open(file, "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)
        print("File: "+ "document-page%s.pdf" % i + " is printed")

print("The script is done.")
                ''', language='python'),
                        dcc.SyntaxHighlighter('''
assignee IN membersOf("Collaboration Squad \
    ORDER BY assignee")
                        ''', language='SQL'), 
                ], className="twelve columns"),
            ], className="row ")

        ], className="subpage")

    ], className="page")

# Academic Timeline Data
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
    dict(Task='Job Hunt', Start='2015-05-01', Finish='2018-04-30', Resource='thirdYear'),
    dict(Task='ENGR-003', Start='2018-05-01', Finish='2018-08-31', Resource='Coop')
    # dict(Task='Anime', Start='2014-01-01', Finish='2019-01-01', Resource='Anime')
]
ganttData.reverse()
colors = dict(firstYear = 'rgb(46, 17, 255)',
              secondYear = 'rgb(46, 255, 51)',
              thirdYear = 'rgb(255, 75, 25)',
              Coop = 'rgb(114, 2, 121)',
              Other = 'rgb(128, 17, 15)',
              Anime = 'rgb(18, 76, 165)')
figGantt = ff.create_gantt(ganttData,colors,index_col='Resource', title='Academic Life Thus Far',
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
                    html.H6('Engineering Degree Timeline',
                            className="gs-header gs-text-header padded"),
                    dcc.Graph(figure=figGantt, id='gantt'),
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
    elif pathname == '/work-terms':
        return workTerms
    elif pathname == '/coop':
        return coopJobStats 
    elif pathname == '/current-facts':
        return currentFacts
    elif pathname == '/random-stuff':
        return randomStuff
    elif pathname == '/academic-timeline':
        return academicTimeline
    elif pathname == '/full-view':
        return overview,workTerms,coopJobStats,currentFacts,academicTimeline
    else:
        return noPage

# lastest css file wins so 
external_css = ["https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "//fonts.googleapis.com/css?family=Raleway:400,300,600",
                "https://codepen.io/bcd/pen/KQrXdb.css"]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.slim.min.js",
               "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})


if __name__ == '__main__':
    app.server.run(debug=True)

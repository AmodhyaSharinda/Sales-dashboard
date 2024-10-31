from dash import Dash, dcc, html, Input, Output
import dash_table
import plotly.express as px
from data_preprocessing import load_and_preprocess_data

# Load and preprocess data
data = load_and_preprocess_data('SalesData_Assignment.csv')

# Initialize Dash app
app = Dash(__name__)
app.title = "Sales Data Dashboard"

# App layout with refined styling for dark theme
app.layout = html.Div(style={'backgroundColor': '#2C3E50', 'minHeight': '100vh'}, children=[
    # Header section
    html.Div([
        html.H1(
            "Sales Data Dashboard",
            style={
                'textAlign': 'center',
                'color': '#ECF0F1',
                'marginBottom': '20px',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '3em',
                'fontWeight': 'bold',
                'textShadow': '1px 1px 2px rgba(0, 0, 0, 0.5)'
            }
        ),
    ], style={
        'padding': '40px',
        'backgroundColor': '#34495E',
        'borderBottom': '4px solid #2980B9',
        'borderRadius': '8px',
        'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
        'display': 'flex',
        'justifyContent': 'center',
        'alignItems': 'center',
        'flexDirection': 'column'
    }),

    # Filters/Controls Card Layout
    html.Div([
        html.Div([  # Outer card container for filters
            html.Div([
                dcc.DatePickerRange(
                    id='date-range',
                    display_format='YYYY-MM-DD',
                    start_date=data['Date'].min(),
                    end_date=data['Date'].max(),
                    start_date_placeholder_text="Start Date",
                    end_date_placeholder_text="End Date",
                    style={
                        'border': '1px solid #2980B9',
                        'borderRadius': '5px',
                        'padding': '10px',
                        'backgroundColor': '#34495E',
                        'color': '#ECF0F1',
                        'fontSize': '1em',
                    }
                ),
            ], style={'marginRight': '20px'}),

            html.Div([
                dcc.Dropdown(
                    id='category-filter',
                    options=[{'label': cat, 'value': cat} for cat in data['Category'].unique()],
                    placeholder="Select Category",
                    style={
                        'backgroundColor': '#34495E',
                        'color': 'black',
                        'border': '1px solid #2980B9'
                    }
                ),
            ], style={'width': '220px', 'marginRight': '20px'}),

            html.Div([
                dcc.Dropdown(
                    id='region-filter',
                    options=[{'label': region, 'value': region} for region in data['Region'].unique()],
                    placeholder="Select Region",
                    style={
                        'backgroundColor': '#34495E',
                        'color': 'black',
                        'border': '1px solid #2980B9'
                    }
                ),
            ], style={'width': '220px'}),

            html.Div([
                html.Button('Apply Filters', id='apply-filters-button', style={
                    'backgroundColor': '#2980B9',
                    'color': '#ECF0F1',
                    'border': 'none',
                    'borderRadius': '5px',
                    'padding': '10px 20px',
                    'cursor': 'pointer',
                    'marginLeft': '20px',
                    'fontSize': '1em'
                }),
            ], style={'display': 'inline-block', 'verticalAlign': 'top'}),
        ], style={
            'display': 'flex', 
            'justifyContent': 'center', 
            'alignItems': 'center',
            'padding': '15px',
            'borderBottom': '2px solid #1A5276', 
            'backgroundColor': '#2C3E50',
            'borderRadius': '8px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
            'margin': '20px 0'
        }),
    ], style={'backgroundColor': '#34495E'}),

    # KPIs
    # Statistics Card Layout
    html.Div([
        html.Div([  # Card for Total Sales
            html.H4("Total Sales", style={'textAlign': 'center', 'color': '#ECF0F1', 'fontFamily': 'Arial'}),
            html.P(id='total-sales', style={'textAlign': 'center', 'fontSize': '22px', 'color': '#ECF0F1', 'fontWeight': 'bold'})
        ], style={
            'flex': '1', 
            'padding': '20px', 
            'borderRight': '1px solid #7F8C8D',
            'borderRadius': '8px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
            'backgroundColor': '#2C3E50',
            'margin': '10px'
        }),

        html.Div([  # Card for Average Sales per Order
            html.H4("Average Sales per Order", style={'textAlign': 'center', 'color': '#ECF0F1', 'fontFamily': 'Arial'}),
            html.P(id='avg-sales', style={'textAlign': 'center', 'fontSize': '22px', 'color': '#ECF0F1', 'fontWeight': 'bold'})
        ], style={
            'flex': '1', 
            'padding': '20px', 
            'borderRight': '1px solid #7F8C8D',
            'borderRadius': '8px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
            'backgroundColor': '#2C3E50',
            'margin': '10px'
        }),

        html.Div([  # Card for Total Quantity Sold
            html.H4("Total Quantity Sold", style={'textAlign': 'center', 'color': '#ECF0F1', 'fontFamily': 'Arial'}),
            html.P(id='total-quantity', style={'textAlign': 'center', 'fontSize': '22px', 'color': '#ECF0F1', 'fontWeight': 'bold'})
        ], style={
            'flex': '1', 
            'padding': '20px', 
            'borderRadius': '8px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
            'backgroundColor': '#2C3E50',
            'margin': '10px'
        }),
    ], style={
        'display': 'flex', 
        'justifyContent': 'space-around', 
        'backgroundColor': '#34495E', 
        'margin': '20px 0', 
        'border': '1px solid #7F8C8D', 
        'borderRadius': '5px',
        'padding': '10px'  # Optional padding for the container
    }),

    # Charts
    html.Div([
        html.Div([
            dcc.Graph(id='sales-over-time', config={'displayModeBar': False}),
        ], style={'padding': '20px', 'borderRadius': '8px', 'backgroundColor': '#34495E', 'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)'}),
    ], style={'padding': '20px'}),

    # Charts in One Row
    html.Div([
        html.Div([
            dcc.Graph(id='sales-by-category-or-region', config={'displayModeBar': False}),
        ], style={'flex': '1', 'padding': '10px', 'borderRadius': '8px', 'backgroundColor': '#34495E', 'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)'}),

        html.Div([
            dcc.Graph(id='sales-proportion', config={'displayModeBar': False}),
        ], style={'flex': '1', 'padding': '10px', 'borderRadius': '8px', 'backgroundColor': '#34495E', 'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)'}),
    ], style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between', 'padding': '20px'}),

    # Data Table
    html.Div([
        html.H4("Sales Transactions", style={'textAlign': 'center', 'color': '#ECF0F1', 'marginBottom': '15px', 'fontFamily': 'Arial'}),
        html.Div([  # Wrap the DataTable in a card-like Div
            dash_table.DataTable(
                id='sales-table',
                columns=[{'name': col, 'id': col} for col in data.columns],
                export_format="csv",
                style_table={'height': '400px', 'overflowY': 'auto', 'backgroundColor': '#34495E'},
                style_cell={'textAlign': 'center', 'padding': '10px', 'border': '1px solid #7F8C8D', 'backgroundColor': '#34495E', 'color': '#ECF0F1'},
                style_header={'backgroundColor': '#2C3E50', 'fontWeight': 'bold', 'color': '#ECF0F1'},
                style_data={'borderRadius': '8px', 'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)'},
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Category'},  # Optional: style for specific columns
                        'textAlign': 'left'
                    },
                ],
            )
        ], style={
            'borderRadius': '8px',
            'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.25)',
            'backgroundColor': '#34495E',
            'padding': '20px',
            'marginTop': '15px'  # Margin to separate from other elements
        })
    ], style={'padding': '20px', 'borderTop': '2px solid #1A5276', 'backgroundColor': '#2C3E50'}),
])

@app.callback(
    [Output('total-sales', 'children'),
     Output('avg-sales', 'children'),
     Output('total-quantity', 'children'),
     Output('sales-over-time', 'figure'),
     Output('sales-by-category-or-region', 'figure'),
     Output('sales-proportion', 'figure'),
     Output('sales-table', 'data')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date'),
     Input('category-filter', 'value'),
     Input('region-filter', 'value')]
)
def update_dashboard(start_date, end_date, category, region):
    # Filter data
    filtered_data = data.copy()
    if start_date:
        filtered_data = filtered_data[filtered_data['Date'] >= start_date]
    if end_date:
        filtered_data = filtered_data[filtered_data['Date'] <= end_date]
    if category:
        filtered_data = filtered_data[filtered_data['Category'] == category]
    if region:
        filtered_data = filtered_data[filtered_data['Region'] == region]

    # Calculate KPIs
    total_sales = filtered_data['Total Price'].sum()
    avg_sales = filtered_data['Total Price'].mean()
    total_quantity = filtered_data['Quantity'].sum()

    # Create figures
    sales_over_time = px.line(
        filtered_data.groupby('Date')['Total Price'].sum().reset_index(),
        x='Date', y='Total Price', title='Sales Over Time', template='plotly_dark'
    )
    sales_by_category_or_region = px.bar(
        filtered_data.groupby('Category')['Total Price'].sum().reset_index(),
        x='Category', y='Total Price', title='Sales by Category', template='plotly_dark'
    )
    sales_proportion = px.pie(
        filtered_data,
        values='Total Price',
        names='Region',
        title='Sales Proportion by Region',
        template='plotly_dark'
    )

    return total_sales, avg_sales, total_quantity, sales_over_time, sales_by_category_or_region, sales_proportion, filtered_data.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)

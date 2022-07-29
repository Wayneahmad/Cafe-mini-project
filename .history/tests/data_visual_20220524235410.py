from file_manager import *



def show_status():
    csv_save(order_keys, load_dict(select_table_query(order_keys[0])))
    df = pd.read_csv (r'Orders.csv')

    import plotly.graph_objects as go
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
    fig = go.Figure(data=[go.Pie(labels=df["order_status"])])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                    marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.show()

    

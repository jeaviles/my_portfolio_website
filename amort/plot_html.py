import datetime as dt

def make_trace(trace,x,y,name):
    trace = """
              var trace"""+ trace +""" = {
              x:"""+ x +""",
              y:"""+ y +""",
              name:'"""+ name +"""',
              type: 'line'
              };
            """
    return trace

def plot_html(data):
    pay_date = str([date.strftime("%Y-%m") for date in data["Pay Date"]])

    bal = str(data['Beginning Balance'])
    bal = make_trace("bal",pay_date,bal,'Beginning Balance')

    cumpri = str(data['Cumulative Principal'])
    cumpri = make_trace("cumpri",pay_date,cumpri,'Cumulative Principal')

    cumint = str(data['Cumulative Interest'])
    cumint = make_trace("cumint",pay_date,cumint,'Cumulative Interest')

    endbal = str(data['Ending Balance'])
    endbal = make_trace("endbal",pay_date,endbal,'Ending Balance')

    html_head = """
                <div id="amort-plot"></div>
                <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
                <script>
            """

    html_traces = bal + cumpri + cumint + endbal

    html_data = """
                var data = [tracebal,tracecumpri,tracecumint,traceendbal];
              """

    html_foot = """
                var layout = {
                title: 'Amortization Graph',
                showlegend: true,
                xaxis: {
                        title: 'Date',
                        },
                yaxis: {
                    title: 'Dollars ($)',
                    }
                };

                Plotly.newPlot('amort-plot', data,layout);
                </script>
             """

    return html_head + html_traces + html_data + html_foot

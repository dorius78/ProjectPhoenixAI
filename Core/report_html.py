"""
========================================
PROJECT PHOENIX AI
Report HTML
Versione 2.0
========================================
"""

from Logs.logger import Logger


class ReportHTML:

    def __init__(self):

        Logger.success(
            "Report HTML V2 inizializzato."
        )

    def export(

        self,

        filename,

        statistics

    ):

        html = []

        html.append("<!DOCTYPE html>")
        html.append("<html>")
        html.append("<head>")
        html.append("<meta charset='utf-8'>")
        html.append("<title>Project Phoenix AI Report</title>")

        html.append("""

<style>

body{

    font-family:Arial;

    margin:40px;

}

table{

    border-collapse:collapse;

    width:100%;

}

th,td{

    border:1px solid #999;

    padding:8px;

}

th{

    background:#efefef;

}

h1{

    color:#003366;

}

</style>

""")

        html.append("</head>")
        html.append("<body>")

        html.append("<h1>PROJECT PHOENIX AI</h1>")
        html.append("<h2>Performance Report</h2>")

        html.append("<table>")
        html.append("<tr><th>Parametro</th><th>Valore</th></tr>")

        for key, value in statistics.items():

            html.append(

                f"<tr><td>{key}</td><td>{value}</td></tr>"

            )

        html.append("</table>")

        html.append("</body>")
        html.append("</html>")

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "\n".join(html)

            )

        Logger.success(

            f"Report HTML salvato: {filename}"

        )
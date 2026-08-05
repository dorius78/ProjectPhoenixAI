"""
========================================
PROJECT PHOENIX AI
HTML Report
Versione 1.0
========================================
"""

from Logs.logger import Logger


class HTMLReport:

    def __init__(self):

        Logger.success(

            "HTML Report V1 inizializzato."

        )

    def export(

        self,

        filename,

        statistics

    ):

        html = []

        html.append("<html>")
        html.append("<head>")
        html.append("<title>Project Phoenix AI Report</title>")
        html.append("</head>")
        html.append("<body>")

        html.append("<h1>PROJECT PHOENIX AI</h1>")
        html.append("<h2>Performance Report</h2>")

        html.append("<table border='1' cellpadding='5'>")
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

            f"HTML creato: {filename}"

        )
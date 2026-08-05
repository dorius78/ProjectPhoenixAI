"""
========================================
PROJECT PHOENIX AI
Report Formats
Versione 2.0
========================================
"""

import json

from Logs.logger import Logger


class ReportFormats:

    def __init__(self):

        Logger.success(
            "Report Formats V2 inizializzato."
        )

    def to_text(self, statistics):

        lines = []

        lines.append("========================================")
        lines.append("PROJECT PHOENIX AI")
        lines.append("PERFORMANCE REPORT")
        lines.append("========================================")
        lines.append("")

        for key, value in statistics.items():

            lines.append(

                f"{key:<25}: {value}"

            )

        return lines

    def to_csv(self, statistics):

        rows = []

        rows.append("Parametro,Valore")

        for key, value in statistics.items():

            rows.append(

                f"{key},{value}"

            )

        return rows

    def to_json(self, statistics):

        return json.dumps(

            statistics,

            indent=4,

            default=str

        )

    def to_html(self, statistics):

        html = []

        html.append("<html>")
        html.append("<head>")
        html.append("<title>Phoenix AI Report</title>")
        html.append("</head>")
        html.append("<body>")

        html.append("<h1>Performance Report</h1>")
        html.append("<table border='1'>")

        for key, value in statistics.items():

            html.append(

                f"<tr><td>{key}</td><td>{value}</td></tr>"

            )

        html.append("</table>")
        html.append("</body>")
        html.append("</html>")

        return "\n".join(html)

    def performance(self, statistics):

        return self.to_text(statistics)
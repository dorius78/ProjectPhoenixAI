"""
PROJECT PHOENIX AI
HTML Performance Report

Versione: V2
"""

from Logs.logger import Logger


class ReportHTML:
    """
    Gestisce la generazione e l'esportazione
    dei report HTML di PROJECT PHOENIX AI.
    """

    def __init__(self):
        Logger.success(
            "Report HTML V2 inizializzato."
        )

    def export(self, filename, statistics):
        """
        Genera ed esporta un report HTML.

        Parameters
        ----------
        filename : str
            Percorso del file HTML da creare.

        statistics : dict
            Dizionario contenente le statistiche
            da visualizzare nel report.
        """

        html = []

        # --------------------------------------------------
        # DOCUMENTO HTML
        # --------------------------------------------------

        html.append("<!DOCTYPE html>")
        html.append("<html lang='it'>")

        # --------------------------------------------------
        # HEAD
        # --------------------------------------------------

        html.append("<head>")
        html.append("<meta charset='utf-8'>")
        html.append(
            "<meta name='viewport' "
            "content='width=device-width, initial-scale=1.0'>"
        )

        html.append(
            "<title>Project Phoenix AI Report</title>"
        )

        # --------------------------------------------------
        # CSS
        # --------------------------------------------------

        html.append("""
<style>

body {
    font-family: Arial, Helvetica, sans-serif;
    background-color: #f4f6f8;
    color: #222222;
    margin: 0;
    padding: 40px;
}

.container {
    max-width: 1100px;
    margin: auto;
    background-color: #ffffff;
    padding: 35px;
    border-radius: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

h1 {
    margin-bottom: 5px;
    color: #1f2937;
}

h2 {
    margin-top: 5px;
    color: #4b5563;
}

.info {
    color: #6b7280;
    margin-bottom: 30px;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

th {
    background-color: #1f2937;
    color: white;
    padding: 12px;
    text-align: left;
}

td {
    padding: 12px;
    border-bottom: 1px solid #dddddd;
}

tr:nth-child(even) {
    background-color: #f9fafb;
}

tr:hover {
    background-color: #f1f5f9;
}

.footer {
    margin-top: 30px;
    padding-top: 15px;
    border-top: 1px solid #dddddd;
    color: #777777;
    font-size: 13px;
    text-align: center;
}

</style>
""")

        html.append("</head>")

        # --------------------------------------------------
        # BODY
        # --------------------------------------------------

        html.append("<body>")

        html.append("<div class='container'>")

        # --------------------------------------------------
        # HEADER
        # --------------------------------------------------

        html.append(
            "<h1>PROJECT PHOENIX AI</h1>"
        )

        html.append(
            "<h2>Performance Report</h2>"
        )

        html.append(
            "<div class='info'>"
            "Report generato automaticamente da PROJECT PHOENIX AI"
            "</div>"
        )

        # --------------------------------------------------
        # STATISTICS TABLE
        # --------------------------------------------------

        html.append("<table>")

        html.append(
            "<tr>"
            "<th>Parametro</th>"
            "<th>Valore</th>"
            "</tr>"
        )

        # --------------------------------------------------
        # DATA
        # --------------------------------------------------

        if statistics:

            for key, value in statistics.items():

                html.append(
                    "<tr>"
                    f"<td>{key}</td>"
                    f"<td>{value}</td>"
                    "</tr>"
                )

        else:

            html.append(
                "<tr>"
                "<td colspan='2'>"
                "Nessuna statistica disponibile."
                "</td>"
                "</tr>"
            )

        html.append("</table>")

        # --------------------------------------------------
        # FOOTER
        # --------------------------------------------------

        html.append("""
<div class='footer'>
    PROJECT PHOENIX AI<br>
    Automated Performance Analysis
</div>
""")

        html.append("</div>")
        html.append("</body>")
        html.append("</html>")

        # --------------------------------------------------
        # SAVE FILE
        # --------------------------------------------------

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "\n".join(html)
            )

        # --------------------------------------------------
        # LOG
        # --------------------------------------------------

        Logger.success(
            f"Report HTML salvato: {filename}"
        )
# -*- coding: utf-8 -*-
# mypy: ignore-errors
import os

from posit.connect.client import Client
from shiny import App, Inputs, Outputs, Session, render, ui

SQL_HTTP_PATH = os.getenv("DATABRICKS_PATH")

app_ui = ui.page_fluid(ui.output_text_verbatim("text"))

def server(input: Inputs, output: Outputs, session: Session):
    """
    Shiny for Python example application that shows how to obtain 
    an OAuth Access Token from Connect using the `/credentials` endpoint
    by exchanging a user-session-token
    """
    session_token = session.http_conn.headers.get(
        "Posit-Connect-User-Session-Token"
    )

    @render.text
    def text():
        with Client() as client:
            credentials = client.oauth.get_credentials(session_token)
            return credentials.get("access_token")


app = App(app_ui, server)

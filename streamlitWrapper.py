import runpy
runpy.run_module('streamlit.cli')
import streamlit.cli
import click
click.pass_context
if __name__ == '__main__':
    streamlit.cli._main_run_clExplicit('app.py', 'streamlit run --global.developmentMode=false')

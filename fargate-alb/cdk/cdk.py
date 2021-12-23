from aws_cdk import App

from fastapi import FastAPIStack

app = App()

FastAPIStack(app, "FastAPIStack")
app.synth()

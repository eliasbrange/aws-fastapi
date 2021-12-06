from aws_cdk import App

from stacks.fastapi import FastAPIStack

app = App()

FastAPIStack(app, "FastAPIStack")
app.synth()

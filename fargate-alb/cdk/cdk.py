from aws_cdk import core

from stacks.fastapi import FastAPIStack

app = core.App()

FastAPIStack(app, "FastAPIStack")
app.synth()

# Deploy FastAPI on AWS: ECS Fargate + ALB

This sample installs FastAPI in a Docker container and runs it on ECS Fargate that is fronted by an Application Load Balancer.

## Requirements
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html)
- Infrastructure required to deploy CDK applications, see [CDK Bootstrapping](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).
- docker
- [docker-compose](https://docs.docker.com/compose/install/) (to run locally)

## Run locally

`docker-compose` is used to run locally.

### Start the API locally

```bash
$ docker-compose up
```

### Call the API
```bash
$ curl http://127.0.0.1:3000

{"message":"FastAPI running in a Docker container"}
```

## Deploy

The CDK CLI is used to deploy the application.

### Deploy

```bash
$ cd cdk
$ cdk deploy

...

Outputs:
FastAPIStack.FastAPIServiceLoadBalancerDNS12345678 = XXXX.eu-west-1.elb.amazonaws.com
FastAPIStack.FastAPIServiceServiceURL12345678 = http://XXXX.eu-west-1.elb.amazonaws.com

Stack ARN:
arn:aws:cloudformation:eu-west-1:***********:stack/FastAPIStack/aaaaaaaa-1111-bbbb-2222-cccccccccccc
```

### Call the API
```bash
$ curl http://XXXX.eu-west-1.elb.amazonaws.com

{"message":"FastAPI running in a Docker container"}
```

import * as cdk from 'aws-cdk-lib';
import * as bedrock from 'aws-cdk-lib/aws-bedrock';

const app = new cdk.App();
const stack = new cdk.Stack(app, 'PlayLangchain');

// const bl = new bedrock.FoundationModel(stack, 'Foundation', {})
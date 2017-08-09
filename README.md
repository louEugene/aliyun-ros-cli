# Aliyun ROS Command-Line Tools

## Prepare

### Requires

* Python 2.7
* aliyun-python-sdk-ros

### Config

When use ros command for the first time, the ros-cli will create a default configuration where ros installed.

```
[ACCESS]
ACCESS_KEY_ID = YOUR_KEY_ID
ACCESS_KEY_SECRET = YOUR_KEY_SECRET
REGION_ID = YOUR_REGION

[JSON]
JSON_INDENT = 2
```

Please use `ros set-userdata` to set your default configuration.

You can also input the region when using ros cli. In many cases, the default configuration will be used if you don't specify the region.

### Install

```
pip install aliyun-python-sdk-ros

python setup.py install
```

## Help

If you want more details, please visit [ROS API](https://help.aliyun.com/document_detail/28898.html?spm=5176.doc28910.3.2.NjqtWX).

### Top Class Commands

```
$ ros -h
usage: ros [-h] [--config CONFIG_FILE] [--json] [--region-id REGION_ID]  ...

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG_FILE  Location of config file
  --json                Print results as JSON format
  --region-id REGION_ID
                        Region ID, if not set, use config file's field

commands:

    set-userdata        Set default Aliyun access info
    create-stack        Creates a stack as specified in the template
    delete-stack        Deletes the specified stack
    update-stack        Update a stack as specified in the template
    preview-stack       Preview a stack as specified in the template
    abandon-stack       Abandon the specified stack
    list-stacks         Returns the summary information for stacks whose
                        status matches the specified StackStatusFilter
    describe-stack      Returns the description for the specified stack
    list-resources      Returns descriptions of all resources of the specified
                        stack
    describe-resource   Returns a description of the specified resource in the
                        specified stack
    resource-type       Returns types of resources
    resource-type-detail
                        Returns detail of the specific resource type
    resource-type-template
                        Returns template of the specific resource type
    get-template        Returns the template body for a specified stack
    validate-template   Validates a specified template
    list-regions        Returns all regions avaliable
    list-events         Returns all stack related events for a specified stack
                        in reverse chronological order
```

### Commands on stacks

#### Create stack

```
$ ros create-stack -h
usage: ros create-stack [-h] [--region-id REGION_ID] --stack-name STACK_NAME
                        --template-url TEMPLATE_URL [--parameters PARAMETERS]
                        [--disable-rollback DISABLE_ROLLBACK]
                        [--timeout-in-minutes TIMEOUT_IN_MINUTES]

optional arguments:
  -h, --help            show this help message and exit
  --region-id REGION_ID
                        The region that is associated with the stack
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --template-url TEMPLATE_URL
                        Location of file containing the template body
  --parameters PARAMETERS
                        A list of Parameter structures that specify input
                        parameters for the stack. Synatax: key=value,key=value
  --disable-rollback DISABLE_ROLLBACK
                        Set to true to disable rollback of the stack if stack
                        creation failed
  --timeout-in-minutes TIMEOUT_IN_MINUTES
                        The amount of time that can pass before the stack
                        status becomes CREATE_FAILED
```

#### Delete stack

```
$ ros delete-stack -h
usage: ros delete-stack [-h] --region-id REGION_ID --stack-name STACK_NAME
                        --stack-id STACK_ID

optional arguments:
  -h, --help            show this help message and exit
  --region-id REGION_ID
                        The region that is associated with the stack
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
```

#### Update stack

```
$ ros update-stack -h
usage: ros update-stack [-h] --region-id REGION_ID --stack-name STACK_NAME
                        --stack-id STACK_ID --template-url TEMPLATE_URL
                        [--parameters PARAMETERS]
                        [--disable-rollback DISABLE_ROLLBACK]
                        [--timeout-in-minutes TIMEOUT_IN_MINUTES]

optional arguments:
  -h, --help            show this help message and exit
  --region-id REGION_ID
                        The region that is associated with the stack
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
  --template-url TEMPLATE_URL
                        Location of file containing the template body
  --parameters PARAMETERS
                        A list of Parameter structures that specify input
                        parameters for the stack. Synatax: key=value,key=value
  --disable-rollback DISABLE_ROLLBACK
                        Set to true to disable rollback of the stack if stack
                        creation failed
  --timeout-in-minutes TIMEOUT_IN_MINUTES
                        The amount of time that can pass before the stack
                        status becomes CREATE_FAILED
```

#### Preview stack

```
$ ros preview-stack -h
usage: ros preview-stack [-h] [--region-id REGION_ID] --stack-name STACK_NAME
                         --template-url TEMPLATE_URL [--parameters PARAMETERS]
                         [--disable-rollback DISABLE_ROLLBACK]
                         [--timeout-in-minutes TIMEOUT_IN_MINUTES]

optional arguments:
  -h, --help            show this help message and exit
  --region-id REGION_ID
                        The region that is associated with the stack
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --template-url TEMPLATE_URL
                        Location of file containing the template body
  --parameters PARAMETERS
                        A list of Parameter structures that specify input
                        parameters for the stack. Synatax: key=value,key=value
  --disable-rollback DISABLE_ROLLBACK
                        Set to true to disable rollback of the stack if stack
                        creation failed
  --timeout-in-minutes TIMEOUT_IN_MINUTES
                        The amount of time that can pass before the stack
                        status becomes CREATE_FAILED
```

#### Abandon stack

```
$ ros abandon-stack -h
usage: ros abandon-stack [-h] --region-id REGION_ID --stack-name STACK_NAME
                         --stack-id STACK_ID

optional arguments:
  -h, --help            show this help message and exit
  --region-id REGION_ID
                        The region that is associated with the stack
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
```

#### List stacks

```
$ ros list-stacks -h
usage: ros list-stacks [-h] [--stack-name STACK_NAME] [--stack-id STACK_ID]
                       [--status {CREATE_COMPLETE,CREATE_FAILED,CREATE_IN_PROGRESS,DELETE_COMPLETE,DELETE_FAILED,DELETE_IN_PROGRESS,ROLLBACK_COMPLETE,ROLLBACK_FAILED,ROLLBACK_IN_PROGRESS}]
                       [--region-id REGION_ID] [--page-number PAGE_NUMBER]
                       [--page-size PAGE_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
  --status {CREATE_COMPLETE,CREATE_FAILED,CREATE_IN_PROGRESS,DELETE_COMPLETE,DELETE_FAILED,DELETE_IN_PROGRESS,ROLLBACK_COMPLETE,ROLLBACK_FAILED,ROLLBACK_IN_PROGRESS}
                        status of stacks
  --region-id REGION_ID
                        The region of stacks
  --page-number PAGE_NUMBER
                        The page number of stack lists, start from 1, default
                        1
  --page-size PAGE_SIZE
                        Lines each page, max 100, default 10
```

#### Describe stack

```
$ ros describe-stack -h
usage: ros describe-stack [-h] --stack-name STACK_NAME --stack-id STACK_ID

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
```

### Commands on resources

#### List resources

```
$ ros list-resources -h
usage: ros list-resources [-h] --stack-name STACK_NAME --stack-id STACK_ID

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name of stack
  --stack-id STACK_ID   The id of stack
```

#### Describe resource

```
$ ros describe-resource -h
usage: ros describe-resource [-h] --stack-name STACK_NAME --stack-id STACK_ID
                             --resource-name RESOURCE_NAME

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name of stack
  --stack-id STACK_ID   The id of stack
  --resource-name RESOURCE_NAME
                        The name of resource
```

#### Resource type

```
$ ros resource-type -h
usage: ros resource-type [-h]
                         [--status {UNKNOWN,SUPPORTED,DEPRECATED,UNSUPPORTED,HIDDEN}]

optional arguments:
  -h, --help            show this help message and exit
  --status {UNKNOWN,SUPPORTED,DEPRECATED,UNSUPPORTED,HIDDEN}
                        The status of resource
```

#### Resource type detail

```
$ ros resource-type-detail -h
usage: ros resource-type-detail [-h] --name NAME

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  The name of resource
```

#### Resource type template

```
$ ros resource-type-template -h
usage: ros resource-type-template [-h] --name NAME

optional arguments:
  -h, --help   show this help message and exit
  --name NAME  The name of resource
```

### Commands on template

#### Get template

```
$ ros get-template -h
usage: ros get-template [-h] --stack-name STACK_NAME --stack-id STACK_ID

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
```

#### Validate template

```
$ ros validate-template -h
usage: ros validate-template [-h] --template-url TEMPLATE_URL

optional arguments:
  -h, --help            show this help message and exit
  --template-url TEMPLATE_URL
                        Location of file containing the template body
```

### Other commands

#### List regions

List all regions and need no parameters.

```
$ ros list-regions -h
usage: ros list-regions [-h]

optional arguments:
  -h, --help  show this help message and exit
```

#### List events

```
$ ros list-events -h
usage: ros list-events [-h] --stack-name STACK_NAME --stack-id STACK_ID
                       [--resource-status {COMPLETE,FAILED,IN_PROGRESS}]
                       [--resource-name RESOURCE_NAME]
                       [--resource-type RESOURCE_TYPE]
                       [--page-number PAGE_NUMBER] [--page-size PAGE_SIZE]

optional arguments:
  -h, --help            show this help message and exit
  --stack-name STACK_NAME
                        The name that is associated with the stack
  --stack-id STACK_ID   The id that is associated with the stack
  --resource-status {COMPLETE,FAILED,IN_PROGRESS}
                        status of resources: COMPLETE\FAILED\IN_PROGRESS
  --resource-name RESOURCE_NAME
                        The name of resources
  --resource-type RESOURCE_TYPE
                        The type of resources
  --page-number PAGE_NUMBER
                        The page number of stack lists, start from 1, default
                        1
  --page-size PAGE_SIZE
                        Lines each page, max 100, default 10
```

#### Set userdata

```
$ ros set-userdata -h
usage: ros set-userdata [-h] --key-id KEY_ID --key-secret KEY_SECRET
                        --region-id REGION_ID [--json-ident JSON_IDENT]

optional arguments:
  -h, --help            show this help message and exit
  --key-id KEY_ID       The default Aliyun access key id
  --key-secret KEY_SECRET
                        The default Aliyun access key region
  --region-id REGION_ID
                        The default region
  --json-ident JSON_IDENT
                        The default json indent when output in json format
```
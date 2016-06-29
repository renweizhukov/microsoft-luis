# microsoft-luis
Code that uses Microsoft Language Understanding Intelligent Service (LUIS).

## Online Pizza Shop.
The python program and the json file are from the example given in https://blogs.msdn.microsoft.com/uk_faculty_connection/2016/03/29/getting-started-using-microsoft-project-oxford-language-understanding-intelligent-service-luis-3-2/.

The python program uses python 3 and depends on the projectoxford library. Note that the projectoxford library doesn't work on Linux. If you run the python program on Linux, you may hit the following exception:

```
NotImplementedError: play is not implemented for platform linuxNew note content 
```

The json file is modified based on the example json file and can be imported to create your new online LUIS application. We add a built-in entity "number" and a number "PizzaCount" as the parameter of the existing entity "Pizza", but we don't know how to utilize the added entity and parameter in the python program. Need to read the LUIS tutorial at https://www.luis.ai/Help.

## SmartToy-en
The json file is exported from a LUIS application which recognizes a couple of simple intents and entities related to music and story. The json file contains the definitions of intents and entities, and all labelled utterances. The python program simply sends a user-input sentence to the LUIS application and shows the analyzed results, e.g., identified intents and entities, and the highest-score intent.

The python program uses python 2 and depends on the luis and requests libraries. You can use pip to install them.

```bash
pip install luis requests
```

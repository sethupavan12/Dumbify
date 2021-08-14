# Dumbify
Dumbify is a Text Conversion Platform which can do the following when given text as an input:
1) Explain given text to a 2nd grader (This is wild! It can understand unprovided context sometimes!)
2) TL;DR (Too Long Didnt Read)- A common terminology on Reddit
3) One Line Summary ( Gives one sentence that **would** explain the whole text )

Dumbify is powered by [OpenAI's API](https://beta.openai.com/) which uses cutting-edge GPT-3 model family's weights to processing natural language. 

## Here is a good example of how "2nd grader" explanation works
1. In this example, the text provided is an extract from wikipedia page explaining Super Nova. Compare the input and output!
![input](https://github.com/sethupavan12/Dumbify/blob/main/input1.JPG)

![output](https://github.com/sethupavan12/Dumbify/blob/main/output1.JPG)

2. In this example, the model tries to explain a paragraph about Quantum Teleportation from Wikipedia to a "2nd grader"

![input](https://github.com/sethupavan12/Dumbify/blob/main/input2.JPG)

![output](https://github.com/sethupavan12/Dumbify/blob/main/output2.JPG)

**Good** enough for an AI I guess!

**Deployment : Pending** but can be used locally if you have access to OpenAI API beta [as of 25/Jul]

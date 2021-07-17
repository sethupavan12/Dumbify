import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


# The following code demonstrates how to use the AI API with a local project.

#ask the user to input some text 
user_input = input("What would you like to dumbify ?")


print("Choose a game:")
print("1. 2nd Grade Summary")
print("2. TLDR")
print("3. One-Line Summary")

choice = input("Enter your choice: ")

if choice == "1":
    print("You have chosen 2nd Grade Summary")
    extra = "I rephrased this for my daughter, in plain language a second grader can understand:"
    # call the 2nd grade summary function
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input+"\n"+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )

    print(response)

#if the user chooses 2nd grade summary, call the TLDR function
elif choice == "2":
    print("You have chosen TLDR")
    extra = "tl;dr:"
    response = openai.Completion.create(
        engine="davinci",
        prompt = user_input + '\n'+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    print(response)

#if the user chooses one line summary, call the one line summary function
elif choice == "3":
    print("You have chosen One-Line Summary")
    extra = "One-sentence summary:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input+'\n'+extra,
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\"\"\""]
    )
    print(response.choices[0])


#if the user chooses an invalid option, print an error message
else:
    print("Invalid choice")







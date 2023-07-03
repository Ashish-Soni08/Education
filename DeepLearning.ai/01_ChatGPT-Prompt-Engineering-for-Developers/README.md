# ChatGPT-Prompt-Engineering-for-Developers

DeepLearning.AI course taught by Isa Fulford and Andrew Ng on how to use large language model technology in products.

Goal: To learn how to quickly build software applications using the power of large language models(LLMs) as a developer tool.

## Introduction

There are broadly two types of large language models(LLMs)

1. Base LLM -  has been trained to predict the next word, based on text training data (often from different sources on the internet) to figure out the most likely next word to follow.

2. Instruction tuned LLM - has been trained to follow instructions.
They are trained by starting with a base LLM and then further fine tune it on inputs and outputs that are instructions and  good attempts at following those instructions and often further refined using a techinque called RLHF: Reinforcement Learning with Human Feedback. They have been trained to be helpful, honest, and harmless.

This course will focus best practises for instrcution tuned LLMs and recommends using these for most applications.

## Guidelines

Guidelines for prompting to get the results you want. Two principles to keep in mind, to prompt engineer effectively. The first principle is to write clear and specific instructions. The second principle is to give the model time to think.

### Principles of Prompting

Principle 1: Write clear and specific instructions, clear does equal to short. You should express what you want the model to do by provding instructions that are clear and specific as you can possibly make them. This will guide the model towards the desired output and reduce the chance that you get irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt, longer prompts actually provide more clarity and context for the model, which can actually lead to more detailed and relevant outputs.

- Tactic 1: Use delimiters to clearly indicate distinct parts of the input. The delimiter can be any clear punctation that seperates the specific pieces of text from the rest of the prompt. This could be triple backticks, quotes, XML tags, section titles, anything that makes it clear to the model that this is a seperate section. Using delimitiers is also a helful technique to avoid prompt injections.

Q. What is prompt injection?
Ans: A prompt injection is, if a user is allowed to add some input into your prompt, they might give kind of conflicting instructions to the model that make it follow the user's instructions rather than doing what you want it to do.

- Tactic 2: Ask for a structured output like HTML or JSON.
- Tactic 3: Ask the model to check whether conditions are satisfied. Check assumptions required to do the task. You might also consider potential edge cases and how the model should handle them unexpected errors or result.
- Tactic 4: Few-shot prompting - just providing the examples of successful executions of the task you want performed before asking the model to do the actual task you want it to do.

Principal 2: Give the model time to think. If the model is rushing to an incorrect conclusion you should try reframing the query to request a chain or series of relevant reasoning before the model provides its final answer. Another way to think about it is if you give a model a task that is too complex for it to do in a short amount of time or in a small number of words, it may make a guess which is likely to be incorrect.
In these situtaions you can instruct the model to think longer about the problem which means its spending more computational effort on the task.

Tactic 1: Specify the steps required to complete a task.

Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

Model Limitations: Even though the model is being exposed to a vast amount of knowledge during its training process, it has not perfectly memorized the information it has seen and so it doesn't know the boundary of its knowledge really well. This means that it might try to answer questions about obscure topics and can make things up that sound plausible but are not actually true. And we call these fabricated ideas hallucinations. This is a known weakness of the models.
One additional tactic to reduce hallucinations in the case that you want the model to kind of generate answers based on a text is to ask the model first find relevant information in the text and then generate an answer based on that information, kind of having a way to trace the answer back to where the information came from. It is often helpful to reduce these hallucinations.

## Iterative Prompt Development

Idea -> Implmentation(prompt) -> Experiental Results -> Error Analysis -> Refine Idea

- Be clear and specific
- Analyze why result does not give desired output
- Refine the idea and the prompt (Clarify instructions? Think about how to give the model more time to think?)
- Repeat

Its about a having a good process to develop prompts that are effective for  your application.

## Summary

- Principles:
  - Write clear and specific instructions
  - Give the model time to think

- Iterative prompt development
- Capabilities: Summarizing, Inferring, Transforming, Expanding
- Built a Chatbot using a LLM

NOTE: Build large language based applications responsibly and only build things that can have a positive impact.

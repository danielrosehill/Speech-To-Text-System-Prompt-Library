# Speech To Text System Prompt Library - Using LLMs To Refine STT Outputs

April 7th 2025

The purpose of this repository is to provide a few basic system prompts intended for transforming text captured using speech-to-text such as OpenAI Whisper and passing it through a large language model for basic refinement.

## Basic Transformation Model

The basic transformation model follows a structure like this.

Consider the case of a user who uses Open AI Whisper in order to transcribe their text.

While Whisper (et al) has excellent accuracy, and features like puncutation can be inferred to make the text much more readable, it still often falls (significantly) short of the format and structure required to be actually useful to (say) send it as an email.

 Let's imagine a user who was using speech to text to capture an email for their boss called John while out on a walk. They bump into their friend called Alex along the way and make small talk for a second. 

 The speech to text might return this, which would be completely accurate but not ready for its intended purpose:

 > "OK. So let's start the email, dear John. Hi, John. Just wanted to let you know about an update to the. Wait, let's not call it an update. Let's call it a status update. Oh, hey Alex, how are you doing? Great to see you here. Are you still jogging? Great. Yeah, all is good at work. Alright, have a good one. Sorry, that was my friend. OK getting back to the email. Let's just finish this. I'll see you in the office at three best wishes and then my email signature. "

 But by transforming the text we could get much closer to an accurate representation of the intended message, which might be something like this:

*Hi John.

 Quick status update. Project is finished now. I'll see you in the office at three. 

 Best,
 User

![alt text](1.png)

The speech to text model is focused on doing one job well (transcription). But it may lack context to know that the person named John is the user's boss and that the ultimate objective of this transcription is to generate an internal email. 

The missing context here might be summarised as follows:

- The text should be formatted into the standard text structure used in emails (a greeting line; a body text; a signoff)  
- The text should be "business appropriate" in style.  
- We should apply some basic transforms so that things like ehm words and user instructions to not transcribe certain elements ("wait ...scrap that!") are adhered to  

## One Solution: System Prompts For Refinement / Text Transformation

One way to make the process of using speech to text far more useful is to send the raw transcription produced by speech to text through a large language model, applying a system prompt that applies "transformations" which provide that missing context and reformat the text from its raw format into something much closer or ready to scent. 

As tools like MCP for email generation become realistic, the utility of these system prompts and of these simple-to-configure text transformation agents in AI chains is significant: The user can dictate text knowing that with the right model selection it will be reformatted into something presentable with minimal editing required before sending it.  

## A Combined System Prompt For Dictated Text Transformation

Through my own use of AI for this purpose, I have developed a methodology of sorts for writing these system prompts and using them. 

My current modus operandi is something like this:

- I consider that there is a basic level of editing which all text captured with speech to text needs to go through. I've come to refer to this as a "basic cleanup" and when writing this system prompt, try to ensure that the following happens: 1) The LLM knows that the text was captured with STT. 2) Missing sentence structure is inferred. 3) Obvious typos are inferred around. 4) Obvious text reformatting instructions contained in the dictated text, such as don't include that are also considered. 5) More generally, the model is instructed to apply some basic edits for improved readability and coherence.  6) some other basic edits to improve readability are applied.

I create a system prompt called Basic Text Cleanup and apply it to all speech to text capture text. 

Then I create system prompts for reformatting the text into specific formats and add these on top of that basic system prompt.  

In other words, if I want to select a system prompt for the specific purpose of sending business emails, then I'll write a specific prompt which contains formatting instructions for business emails, my personal email signature, and I'll then append that onto the basic system prompt so that the text transformation for business emails will firstly apply basic text cleanup and then formatted for the specific purpose. 

## Text To JSON Transformations

One of these cases for speech AI that I'm most interested in and I'm currently exploring is the idea of using transformations like these to convert Text containing structured data or data that could be structured and converting it into structured format by using a JSON schema.

Examples of applications in this domain include the following:

- Take the users dictated task list and output it as a JSON array. Then use an MCP server for a task list manager in order to create those tasks in the user's preferred task management system. 

- Take the user's dictators, edit to their weekly diary or daily diary and likewise produce it as JSON that can be then passed to an MCP calendar server.

![alt text](2.png)
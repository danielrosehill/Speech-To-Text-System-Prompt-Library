# Speech To Text System Prompt Library 


[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://github.com/danielrosehill/Text-Transformation-Prompt-Combiner)

This repository provides a collection of system prompts designed to transform and refine text captured using speech-to-text technologies. 

By passing STT outputs through large language models with these specialized prompts, you can achieve cleaner, more structured, and purpose-specific text formats.
 
## 📋 The Idea

Here is the basic implementation. I don't pretend that this is the stuff of high AI engineering. But it does create quite inefficient workflow. 

The basic model is like this:

 ![alt text](1.png)

 The prompt stacks combine the different elements so that the LLM has as a detailed picture of the desired format of the text it must produce from the STT input:

 ![alt text](2.png)

---

## 🔄 The MCP Angle

 The text transformation "agent" also provides an excellent opportunity to optimize this workflow for use with MCP.

 "Agent 2" could take the reformatted text and restructure it as JSON. 

 Or the prior/main agent can be rewritten to also direct a specific structured output.

 For example, an email composition configuration can be configured to output to JSON and provide specific elements for the email subject line, body text, and recipient email(s).

---

## 🔗 Example Prompt Stacks

Here are a couple of examples of how the constituent elements in the various system prompt snippets here can be put together:

### Stack 1: Business Correspondence Stack

| Layer | Prompt Component | Function |
|:-----:|:----------------:|:--------:|
| 1 | Basic Cleanup | Foundation for all transformations |
| 2 | Format as Business Correspondence | Apply business document structure |
| 3 | Decisive Tone | Add authoritative, clear language |
| 4 | Business Structure | Organize content with professional formatting |
| 5 | Business Email Signature | Add formal closing and signature block |

### Stack 2: Personal Communication Stack

| Layer | Prompt Component | Function |
|:-----:|:----------------:|:--------:|
| 1 | Basic Cleanup | Foundation for all transformations |
| 2 | Friendly Tone | Add warm, approachable language |
| 3 | Personal Signature | Add casual closing and signature |

The prompt combiner script makes it easy to build these stacks by selecting the components you need and automatically layering them in the correct order.

---

## 📚 System Prompts Navigation

These are the various prompts and their categories in this repository. 

The basis prompt is intended to provide a baseline level of text cleaning. And the other prompts provide supplementation. 

The exception is the prompts that directs a JSON output directly.

<details>
<summary><b>🔍 Basic Prompts</b> - Foundational prompts for initial text cleanup and transformation</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Basic Cleanup](system-prompts/basic/basic-cleanup.md) | The foundation prompt for all STT transformations |

</details>

<details>
<summary><b>💼 Business Correspondence</b> - Prompts for transforming speech into professional business communications</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Budget Request](system-prompts/business-correspondence/budget-request.md) | Format text as a budget request |
| [Business Proposal](system-prompts/business-correspondence/business-proposal.md) | Format text as a business proposal |
| [Quote Request](system-prompts/business-correspondence/quote-request.md) | Format text as a quote request |
| [Remote Job Application](system-prompts/business-correspondence/remote-job-application.md) | Format text as a remote job application |
| [Specific Job Application](system-prompts/business-correspondence/specific-job-application.md) | Format text as a specific job application |

</details>

<details>
<summary><b>🔎 Job Seeking</b> - Prompts specifically designed for job application and career advancement communications</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Interview Thank You](system-prompts/business-correspondence/job-seeking/interview-thank-you.md) | Format text as an interview thank you note |
| [Job Speculative Pitch](system-prompts/business-correspondence/job-seeking/job-speculative-pitch.md) | Format text as a speculative job application |

</details>

<details>
<summary><b>📊 Project Management</b> - Prompts for effective project-related communications and documentation</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Meeting Minutes](system-prompts/project-management/meeting-minutes.md) | Format text as meeting minutes |
| [Project Brief](system-prompts/project-management/project-brief.md) | Format text as a project brief |
| [Project Status Update](system-prompts/project-management/project-status-update.md) | Format text as a project status update |
| [Task List](system-prompts/project-management/task-list.md) | Format text as a task list |
| [Weekly Report](system-prompts/project-management/weekly-report.md) | Format text as a weekly report |

</details>

<details>
<summary><b>📝 Format</b> - General formatting prompts to structure speech into specific document types</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Acronym Expansion](system-prompts/format/acronym-expansion.md) | Expand acronyms in the text |
| [Blog Outline](system-prompts/format/blog-outline.md) | Format text as a blog post outline |
| [Bullet Points](system-prompts/format/bullet-points.md) | Format text as bullet points |
| [Email](system-prompts/format/email.md) | Format text as an email |
| [English Improvement](system-prompts/format/english-improvement.md) | Improve English language usage |
| [Fact Identification](system-prompts/format/fact-identification.md) | Identify facts in the text |
| [Internal Email](system-prompts/format/internal-email.md) | Format text as an internal company email |
| [Invitation](system-prompts/format/invitation.md) | Format text as an invitation |
| [LinkedIn Post](system-prompts/format/linkedin-post.md) | Format text as a LinkedIn post |
| [Meeting Agenda](system-prompts/format/meeting-agenda.md) | Format text as a meeting agenda |
| [Numbered List](system-prompts/format/numbered-list.md) | Format text as a numbered list |
| [Outline](system-prompts/format/outline.md) | Format text as an outline |
| [Paragraph Structure](system-prompts/format/paragraph-structure.md) | Apply proper paragraph structure |
| [Press Release](system-prompts/format/press-release.md) | Format text as a press release |
| [Pros and Cons](system-prompts/format/pros-and-cons.md) | Format text as pros and cons |
| [Social Media Post](system-prompts/format/social-media-post.md) | Format text as a social media post |
| [Summary](system-prompts/format/summary.md) | Summarize the text |
| [System Prompt](system-prompts/format/ai-prompts/system-prompt.md) | Format text as an AI system prompt |
| [User Prompt](system-prompts/format/ai-prompts/user-prompt.md) | Format text as an AI user prompt |

</details>

<details>
<summary><b>📄 Business Docs</b> - Prompts for transforming speech into formal business documents</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Business Proposal](system-prompts/format/business-docs/business-proposal.md) | Format text as a formal business proposal |
| [Cold Pitch](system-prompts/format/business-docs/cold-pitch.md) | Format text as a cold pitch |
| [Cover Letter](system-prompts/format/business-docs/cover-letter.md) | Format text as a cover letter |
| [Executive Summary](system-prompts/format/business-docs/executive-summary.md) | Format text as an executive summary |
| [Formal Complaint](system-prompts/format/business-docs/formal-complaint.md) | Format text as a formal complaint |
| [Job Description](system-prompts/format/business-docs/job-description.md) | Format text as a job description |
| [Memo](system-prompts/format/business-docs/memo.md) | Format text as a memo |
| [Newsletter](system-prompts/format/business-docs/newsletter.md) | Format text as a newsletter |
| [Press Release](system-prompts/format/business-docs/press-release.md) | Format text as a press release |
| [Product Description](system-prompts/format/business-docs/product-description.md) | Format text as a product description |
| [Project Proposal](system-prompts/format/business-docs/project-proposal.md) | Format text as a project proposal |
| [Request for Proposal](system-prompts/format/business-docs/request-for-proposal.md) | Format text as a request for proposal |
| [White Paper](system-prompts/format/business-docs/white-paper.md) | Format text as a white paper |

</details>

<details>
<summary><b>✍️ Signature</b> - Prompts for adding appropriate signature blocks to communications</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Business Signature](system-prompts/signature/business-sig.md) | Add a business email signature |
| [Personal Signature](system-prompts/signature/personal-sig.md) | Add a personal email signature |

</details>

<details>
<summary><b>🔄 Simplification</b> - Prompts for simplifying complex text into easier-to-understand formats</summary>

| Prompt | Description |
|:------:|:-----------:|
| [System Prompt](system-prompts/simplification/system-prompt.md) | Simplify complex text |

</details>

<details>
<summary><b>🎨 Style</b> - Prompts for applying specific writing styles to transformed text</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Academic Style](system-prompts/style/academic-style.md) | Apply academic writing style |
| [Casual Style](system-prompts/style/casual-style.md) | Apply casual writing style |
| [Concise Style](system-prompts/style/concise-style.md) | Apply concise writing style |
| [Creative Style](system-prompts/style/creative-style.md) | Apply creative writing style |
| [Descriptive Style](system-prompts/style/descriptive-style.md) | Apply descriptive writing style |
| [Formal Style](system-prompts/style/formal-style.md) | Apply formal writing style |
| [Persuasive Style](system-prompts/style/persuasive-style.md) | Apply persuasive writing style |
| [Professional Style](system-prompts/style/professional-style.md) | Apply professional writing style |
| [Technical Style](system-prompts/style/technical-style.md) | Apply technical writing style |

</details>

<details>
<summary><b>🗣️ Tone</b> - Prompts for setting the emotional tone of transformed text</summary>

| Prompt | Description |
|:------:|:-----------:|
| [Authoritative Tone](system-prompts/tone/authoritative-tone.md) | Apply authoritative tone to text |
| [Business Tone](system-prompts/tone/business-tone.md) | Apply business tone to text |
| [Formal Tone](system-prompts/tone/formal-tone.md) | Apply formal tone to text |
| [Friends & Family Tone](system-prompts/tone/friends-family-tone.md) | Apply casual tone for friends and family |
| [Informal Tone](system-prompts/tone/informal-tone.md) | Apply informal tone to text |
| [Professional Tone](system-prompts/tone/professional-tone.md) | Apply professional tone to text |

</details>

---

## 🔄 Basic Transformation Model

The basic transformation model follows a structure like this.

Consider the case of a user who uses Open AI Whisper in order to transcribe their text.

The user dictates:

```
Hi John quick status update project is finished now I'll see you in the office at three best user
```

Whisper transcribes this as:

```
Hi John, quick status update. Project is finished now. I'll see you in the office at three. Best, User
```

The speech to text model is focused on doing one job well (transcription). But it may lack context to know that the person named John is the user's boss and that the ultimate objective of this transcription is to generate an internal email. 

By passing the transcribed text through a large language model with a specialized system prompt, we can transform it into a properly formatted internal email:

```
Subject: Project Completion Status Update

Hi John,

I wanted to provide a quick status update. The project has been successfully completed.

I'll be in the office at 3:00 PM if you'd like to discuss any details.

Best regards,
[User's Name]
```

This transformation adds:
- A relevant subject line
- Proper email formatting with greeting and signature
- Expanded and clarified content
- Professional language appropriate for internal business communication

## 💡 Key Transformation Features

| Feature | Description |
|:-------:|:-----------:|
| Format Detection | The model identifies the intended format (email, report, list, etc.) |
| Tone Adjustment | Text is adjusted to match the appropriate tone (formal, casual, etc.) |
| Structure Addition | Missing structural elements are added (subject lines, headers, etc.) |
| Sentence Structure | Missing sentence structure is inferred and properly formatted |
| Typo Correction | Obvious typos and speech recognition errors are corrected |
| Instruction Filtering | Text reformatting instructions contained in the dictated text (e.g., "don't include that") are processed and removed |
| Coherence Enhancement | The model applies basic edits for improved readability and coherence |
| Readability Improvements | Additional edits to improve overall text readability and flow |

---

## 🧹 Basic Cleanup Prompt Text

```
# System Prompt For Basic Text Cleanup

You are a helpful writing assistant. 

Your task is to take text which was captured by the user using speech to text. 

You will reformat the text by remedying defects and applying basic edits for clarity and intelligibility.

Apply these edits to the text:

## Edits

- If you can infer obvious typos, then resolve them. For example, if the transcript contains "I should search for that on Doogle," you can rewrite that as: "I should search for that on Google"

- Add missing punctuation. 

- Add missing paragraph breaks. Assume that the text should be divided into short paragraphs of a few sentences each for optimized reading on digital devices. 

- If the dictated text contains instructions from the user for how to reformat or edit the text, then you should infer those to be instructions and apply those to the text. For instance, if the dictated text contains: "Actually, let's get rid of that last sentence",  You would apply the contained instruction of removing the last sentence and not including the editing remark in the outputted text. 

## Workflow

Adhere to the following workflow. 

- The user will provide the text. 
- Apply your edits.  
- Return the improved edited text to the user. Do not add any text before or after your output. 
```

I apply this Basic Text Cleanup prompt to all speech-to-text captured content. Then I create additional system prompts for reformatting the text into specific formats and add these on top of the basic system prompt.

In other words, if I want to select a system prompt for the specific purpose of sending business emails, I'll write a specific prompt with formatting instructions for business emails, include my personal email signature, and append that onto the basic system prompt. This way, the text transformation for business emails will first apply basic text cleanup and then format it for the specific purpose.

---

## 🛠️ Prompt Combiner Script

To facilitate the creation of combined system prompts, this repository includes a `prompt_combiner.py` script that automates the process. The script allows you to:

1. Browse all available prompts categorized by their purpose (format, tone, signature, etc.)
2. Select multiple prompts to combine
3. Automatically layer them on top of the basic cleanup prompt
4. Save the combined system prompt for future use

To use the script, simply run:
```bash
python prompt_combiner.py
```

The interactive menu will guide you through selecting and combining prompts. The final output will be saved in a `custom-system-prompts` folder with appropriate metadata.

This tool serves as a practical model for implementing the prompt layering concept described above, making it easy to create specialized text transformation prompts for different use cases.

---

## 📊 Text To JSON Transformations

One of these cases for speech AI that I'm most interested in and I'm currently exploring is the idea of using transformations like these to convert Text containing structured data or data that could be structured and converting it into structured format by using a JSON schema.

Examples of applications in this domain include the following:

- Take the users dictated task list and output it as a JSON array. Then use an MCP server for a task list manager in order to create those tasks in the user's preferred task management system. 

- Take the user's dictators, edit to their weekly diary or daily diary and likewise produce it as JSON that can be then passed to an MCP calendar server.

![alt text](2.png)
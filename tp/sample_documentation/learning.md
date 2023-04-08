In-Context Learning with Large-Scale Pretrained Language Models: How Far Are We?
In-context learning is critical for adapting large-scaled pre-trained language models to various downstream tasks. In this article, we share our thinkings about the roadmap towards in-context learning. Note that, this is not a literature review like Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing . We will introduce some representative works and discuss their roles in this line of research.

Concepts
Few-Shot Learning: the model learns a new task from a small amount of training examples.
In-Context Learning: large-scale pretrained language models learn a new task simply by conditioning on a few training examples and predicting which tokens best complete a test input. In-context learning is entirely different from few-shot learning: the language models does receive only a few training examples, but the overall system may still require a large number of training examples.
A RoadMap towards In-Context Learning
In-Context Learning as Few-Shot Learning
Vanilla In-Context Learning

Language Models are Few-Shot Learners 
Overcoming Few-Shot Prompt Order Sensitivity

Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity 
Insight 1: the performance of in-context learning is sensitive to few-shot prompt order.
Insight 2: some permutations are "fantastic" and some not.
Insight 3: we can use a unlabeled dev set to find fantastic permutations.
Limitation: the analysis and approach are only for text classifcation task.
What Makes In-Context Learning Work?

Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? 
Key Insight: in text classification tasks, replacing gold labels with random labels only marginally hurts performance.
This result strongly suggests that the models are capable of recovering suggests that the models are capable of recovering the expected input-label correspondence for the task; however, it is not directly from the pairings in the demonstrations.
In-Context Learning with Retrievers
Off-the-Shelf Retrievers

Making pre-trained language models better few-shot learners 
Use pre-trained sentence embeddings to select the closest prompt examples to the given input instance (for text classification tasks).
What Makes Good In-Context Examples for GPT-3? 
The retriever is fine-tuned on NLI datasets.
Question: can these retrievers generalize to various downstream tasks?
Fine-tuning the Retrievers with Task-Specific Features

Synchromesh: Reliable Code Generation from Pre-Trained Language Models 
Suppose that we already have the assumptions that the training examples with the same SQL template as the test input are "fantastic" examples, we can extract SQL templates for the training examples and fine-tune the retriever to make the training examples sharing the same SQL template together.
Limitation: the assumption that the training examples with the same SQL template as the test input are "fantastic" examples. We need different implementations (or even different assumptions) for different downstream tasks.
We've introduced Babel to the authors (from PROSE team), and they (contact: Vu Le) have decided to integrate this work into Babel.
Fine-tuning the Retrievers with Language Model's Responses

Learning To Retrieve Prompts for In-Context Learning 
Consider two training examples A and B. We regard A as a "fantastic" example to B, if the language model can predict the ground truth result of B correctly using A as the prompt example, otherwise A is not a "fantastic" example to B. Such results can be used to fine-tune the retrievers.
Limitation: though this methodology is much more general than others, it may suffer from the problem that the supervisions are likely to be too weak.
Ensemble In-Context Learning
Preliminary: Producing the Reasoning Path before the Final Answer

Chain of thought prompting elicits reasoning in large language models 
Sampling Different Out Sequences then Scoring

Training Verifiers to Solve Math Word Problems 
Sampling Different Output Sequences then Voting

Self-consistency improves chain of thought reasoning in language models 
Sampling Different Prompts then Voting+Scoring

On the Advance of Making Language Models Better Reasoners 
Limitations of this Line of Approaches

Efficiency
Task: multi-step reasoning with simple final answer
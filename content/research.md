---
title: Research
url: /research/
hideMeta: true
description: "Beyond Prediction: Causal Representation Learning for Transferable, Interpretable, and Controllable AI."
---

# Beyond Prediction: Causal Representation Learning for Transferable, Interpretable, and Controllable AI

Scaling has made AI remarkably good at prediction. Yet many capabilities that remain unreliable share a common form. Controlling generation without unintended changes, transferring to new environments, anticipating the consequences of actions, updating knowledge as the world changes, and discovering scientific mechanisms all ask what would happen under a change the training data did not show. These are interventional and counterfactual questions, and passive data often cannot settle them: many models fit the same observations equally well yet disagree under intervention, and more data of the same kind does not decide among them.

My research develops **causal representation learning** to close this gap. I establish which data and structural principles make the concepts and mechanisms behind complex observations identifiable, and I translate these principles into scalable learning methods. The recovered structure makes AI **transferable** (what stays invariant when the environment changes?), **interpretable** (what mechanisms generate the data?), and **controllable** (what follows when one factor changes while others are held fixed?).

Causal principles inform the two main levers of machine learning, the model and the data. For the model, they specify which simplicity to prefer: sparse, modular mechanisms, so that a change in the world alters only a few of them. For the data, they specify the evidence that makes structure identifiable, such as variation across environments or interventions.

**Research keywords:** causal representation learning, identifiability, world models, compositional generalization and reasoning, interpretable and controllable generative models, AI for scientific discovery.

![Research overview: capabilities beyond prediction (left), four regimes with key papers (middle), applications (right), and future directions (bottom).](/images/research_overview.png)

The program has two complementary dimensions: the capabilities we seek and the regimes of evidence in which we learn. Regimes A and B ask what the data at hand can identify, using heterogeneity across environments and modalities (A) or structural principles for a single unstructured distribution (B). Regimes C and D go beyond the data: C uses identified structure to answer questions about combinations and conditions never observed, and D acquires the evidence existing data lack through interaction and experiments.

## A. Learning from heterogeneous data: identifying invariant mechanisms

Variation across domains and modalities can reveal which mechanisms are shared and which change. I study how to use this information to separate stable content from domain-specific factors, align concepts across modalities, and support transfer to new settings. This work connects identification theory with domain adaptation, multi-domain generation, vision-language alignment, and analysis of multimodal biological observations.

Selected work:

- [Partial Disentanglement for Domain Adaptation](https://proceedings.mlr.press/v162/kong22a.html), ICML 2022.
- [Multi-domain Image Generation and Translation with Identifiability Guarantees](https://openreview.net/pdf?id=U2g8OGONA_V), ICLR 2023.
- [SmartCLIP: Modular Vision-language Alignment with Identification Guarantees](https://arxiv.org/abs/2507.22264), CVPR 2025.
- [Causal Representation Learning from Multimodal Biomedical Observations](https://openreview.net/forum?id=hjROBHstZ3), ICLR 2025.

## B. Learning from unstructured data: uncovering hierarchical concepts

When learning from a single collection of images, text, or other observations, explicit domain labels may be unavailable. I study what assumptions allow hierarchical concepts and their relationships to be recovered from such data. These foundations support methods for interpreting learned representations, understanding masked autoencoders, and making targeted changes to generative outputs.

Selected work:

- [Identification of Nonlinear Latent Hierarchical Models](https://arxiv.org/abs/2306.07916), NeurIPS 2023.
- [Learning Discrete Concepts in Latent Hierarchical Models](https://arxiv.org/abs/2406.00519), NeurIPS 2024.
- [Understanding Masked Autoencoders via Hierarchical Latent Variable Models](https://arxiv.org/abs/2306.04898), CVPR 2023.
- [Beyond the Black Box: Identifiable Interpretation and Control in Generative Models via Causal Minimality](https://eccv.ecva.net/virtual/2026/poster/4260), ECCV 2026.
- [Learning Vision and Language Concepts for Controllable Image Generation](https://proceedings.mlr.press/v267/xie25g.html), ICML 2025.

## C. Generalizing beyond data: extrapolation and composition

Models must often handle situations and combinations that were absent from their training data. I study when learned causal mechanisms can support extrapolation, and how reusable components can be recombined for new tasks. This connects theoretical conditions for generalization with compositional image generation and modular reasoning in language models.

Selected work:

- [Towards Understanding Extrapolation: a Causal Lens](https://arxiv.org/abs/2501.09163), NeurIPS 2024.
- [Learning by Analogy: A Causal Framework for Compositional Generalization](https://arxiv.org/abs/2512.10669), CVPR 2026.
- [From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning](https://arxiv.org/abs/2606.18089), ICML 2026.
- [Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards](https://aclanthology.org/2026.acl-long.1978/), ACL 2026.

## D. Learning beyond data: acquiring evidence through interaction

Sometimes the evidence a model needs is absent from the data altogether. Learning beyond data means acquiring that evidence: the system must choose informative interactions or experiments and expand its data coverage. I study how models can seek informative interactions, identify gaps in their knowledge, and improve from the resulting feedback. In World Action Verifier, we combine forward prediction and inverse action inference to guide the collection of new experience for world-model learning. Ongoing work asks how world models can represent reusable dynamics and choose interactions that distinguish competing explanations.

This also motivates a question in our [reasoning framework](#c-generalizing-beyond-data-extrapolation-and-composition): when can feedback and exploration help acquire reusable skills that transfer to new problems?

Selected work:

- [World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry](https://arxiv.org/abs/2604.01985), NeurIPS 2026; Outstanding Paper at the ICLR 2026 World Models Workshop.

## Future directions: causal world models and mechanism discovery for science

My future program pursues two directions in which questions about change are central and the four regimes meet.

**Causal world models that learn by intervening.** A world model is valuable when it predicts the consequences of actions, including actions rare in its data. I will study which predictive objectives preserve the factors required for control and transfer, and when additional structural constraints or measurements are needed. Building on World Action Verifier, I will develop methods that choose interventions revealing what the current model lacks, and modular dynamics that reuse what those interventions reveal. Transfer to unseen environments and compositions will be the key test throughout.

**Mechanism discovery for science.** Scientific discovery often needs more than prediction: the goal is a mechanism that explains the data and predicts the outcomes of new experiments. I will connect scientific measurements, causal modeling, and experiment design in a cycle: candidate mechanisms organize hypotheses and suggest interventions whose outcomes distinguish competing explanations, and new observations revise both the model and the next experiment. This builds on my multimodal biomedical-data work and will require close collaboration with domain scientists.

## Cross-cutting: testing whether learning changes behavior

Behavioral evaluation complements the causal theory across all four regimes and both future directions. CHI-Bench evaluates agents on simulated healthcare workflows requiring sustained policy adherence, coordination across roles, and multi-turn interaction. Our position paper on deployment memory tests the gap between improved learning metrics and usable knowledge. Both motivate testing whether learning changes the intended behavior, alongside tests of transfer, concept interpretation, and targeted control.

Selected work:

- [CHI-Bench: Can AI Agents Automate End-to-End, Long-Horizon, Policy-Rich Healthcare Workflows?](https://arxiv.org/abs/2605.16679v4), NeurIPS 2026, Evaluations and Datasets Track.
- [Deployment-Memory LLM Test-Time Training Should Require Behavioral Evidence Beyond Perplexity](https://arxiv.org/abs/2607.00368), NeurIPS 2026, Position Paper Track. Earlier manuscript: *Beyond Perplexity*.

I contributed to training data for [IFM's K2 models](https://ifm.ai/k2/) and am a coauthor of [K2-Horizon: A Frontier Fleet of Open Source Language Models](https://arxiv.org/abs/2611.21003), the 2026 technical report.

[See all publications](/publications/)

## Selected invited talks

- INFORMS Annual Meeting, Online Learning and Reinforcement Learning session, November 2026.
- Stony Brook University, Department of Computer Science, April 2026.
- University of Hong Kong, Department of Data and Systems Engineering, March 2026.
- Hong Kong University of Science and Technology, Computer Science and Engineering, March 2026.
- Pennsylvania State University, Computer Science and Engineering, March 2026.
- Yale Institute for Foundations of Data Science, February 2026.

# Entailment-Preserving FOL Representations

Jinu Lee et al., (2025) Entailment-Preserving First-order Logic Representations in Natural Language Entailment, ACL 2025 Main Conference

> First-order logic (FOL) is often used to represent logical entailment, but determining natural language (NL) entailment using FOL remains a challenge. To address this, we propose the Entailment-Preserving FOL representations (EPF) task and introduce reference-free evaluation metrics for EPF (Entailment-Preserving Rate (EPR) family). In EPF, one should generate FOL representations from multi-premise NL entailment data (e.g., EntailmentBank) so that the automatic prover’s result preserves the entailment labels. Furthermore, we propose a training method specialized for the task, iterative learning-to-rank, which trains an NL-to-FOL translator by using the natural language entailment labels as verifiable rewards. Our method achieves a 1.8–2.7% improvement in EPR and a 17.4–20.6% increase in EPR@16 compared to diverse baselines in three datasets. Further analyses reveal that iterative learning-to-rank effectively suppresses the arbitrariness of FOL representation by reducing the diversity of predicate signatures, and maintains strong performance across diverse inference types and out-of-domain data.

## Installation

Runs on Linux, MacOS, and WSL. (Note: due to Vampire, only x86 arch is supported)

```bash
pip install -r requirements.txt
```

## Baseline model (trained from MALLS)

### Train model
```bash
pwd # ../../nl2logic/
cd baseline
python finetune.py # Train on MALLS train set
```

Alternatively, download model from (Deleted link), unzip and place the checkpoint file in `baseline/model/`.
> baseline/model/{model.safetensors, vocab.json, config.json, spiece.model, tokenizer_config.json, ...}

### Evaluate model

```bash
pwd # ../../nl2logic/
cd baseline
python evaluate.py # evaluate on MALLS test set
```

### Generate results for baseline models

```bash
pwd # ../../nl2logic/
scripts/generate_baseline_{beamsearch, greedy, sampling}.sh # Generate results for baseline models
```

## Evaluate using solver

### Prerequisites

If your system is not x86 Linux, build [Vampire](https://vprover.github.io/download.html) from source.

Set the environment variable indicating the path to Vampire executable, `VAMPIRE_PATH="path/to/vampire"`. Default value is `"./vampire"`, and you do not need to modify it if you are running this from x86 Linux.

### Evaluating

You should prepare both `*_chains.jsonl` about the entailment pairs and `*_sentences.jsonl` including predictions for each sentences.

You can run:

```sh
python evaluate_predictions.py --chain_data chains.jsonl --sentence_data sentences.jsonl
```

If your chain and sentences share a common prefix, *e.g.* `results/baseline/entailmentbank_chains.jsonl` and `results/baseline/entailmentbank_sentences.jsonl`, you can run:

```sh
python evaluate_predictions.py --data_prefix results/baseline/entailmentbank.
```
import json
import re
import os
from collections import defaultdict, Counter
from typing import List, Set, Dict

def extract_predicates(fol_expression: str) -> Set[str]:
    """Extract predicate names from logical expressions"""
    predicates = re.findall(r'([A-Z][a-zA-Z0-9_]*)\(', fol_expression)
    return set(predicates)

def count_atomic_propositions(fol_expression: str) -> int:
    """Count the number of atomic propositions"""
    atomic_props = re.findall(r'[A-Z][a-zA-Z0-9_]*\([^)]*\)', fol_expression)
    atomic_props = set([ap.split("(")[0] for ap in atomic_props])
    return len(atomic_props)

def normalize_predicate(predicate: str) -> str:
    """Normalize predicate names to handle common variants"""
    common_variants = {
        'Colour': 'Color',
        'RisingSun': 'SunRising',
        'IsStar': 'Star',
        'IsObject': 'Object'
    }
    return common_variants.get(predicate, predicate)

def analyze_round_data(sentences_file: str) -> Dict:
    """Analyze data from a single round folder"""
    sent_ids = set()
    all_predicates = set()
    total_atomic_props = 0
    prediction_count = 0
    
    with open(sentences_file, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            for pred in data['prediction']:
                predicates = extract_predicates(pred)
                all_predicates.update(predicates)
                total_atomic_props += count_atomic_propositions(pred)
                prediction_count += 1
                sent_ids.add(data['id'])
    
    return {
        'predicate_diversity': len(all_predicates),
        'avg_predicate_diversity': len(all_predicates) / len(sent_ids),
        'avg_atomic_propositions': total_atomic_props / prediction_count if prediction_count > 0 else 0
    }

def main():
    dataset = "esnli"
    split = "test"
    base_path = f'results/brio_{dataset}_round'
    sentence_file = f'{dataset}_{split}_sentences.jsonl'
    results = {}
    
    # Analyze data for each round
    for round_num in range(6):  # 0-5
        if round_num == 0:
            round_folder = "results/baseline_malls/beam_size16"
        else:
            round_folder = f'{base_path}{round_num}'
        if os.path.exists(round_folder):
            print(f"\nAnalyzing {round_folder}...")
            results[round_num] = analyze_round_data(f"{round_folder}/{sentence_file}")
    
    # Print results
    print("\nAnalysis Results:")
    print("=" * 50)
    print(f"{'Round':<10} {'Predicate Diversity':<20} {'Avg Predicate Diversity':<20} {'Avg Atomic Props':<15}")
    print("-" * 50)
    
    for round_num in sorted(results.keys()):
        r = results[round_num]
        print(f"{round_num:<10} {r['predicate_diversity']:<20} {r['avg_predicate_diversity']:<20.4f} {r['avg_atomic_propositions']:.2f}")

if __name__ == "__main__":
    main()
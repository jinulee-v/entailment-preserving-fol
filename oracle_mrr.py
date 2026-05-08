import json

for dataset in ["entailmentbank_validation", "eqasc_test", "esnli_test"]:
    print(dataset)
    for round in range(0,6):
        if round == 0:
            base_directory = "results/baseline_malls/beam_size16"
        else:
            dataname = dataset.split("_")[0]
            base_directory = f"results/brio_{dataname}_round{round}"
        data = {} # id : (oracle rank, is oracle score > 0)?
        ids = set()
        with open(f"{base_directory}/{dataset}_entailment_preserving_rate_eval_oracle.jsonl") as f:
            for line in f:
                datum = json.loads(line)
                ids.add(datum["id"])
                if "selected" in datum:
                    data[datum["id"]] = (datum["output_id"], datum["score"] > 0)
            for id in ids:
                if id not in data:
                    data[id] = (-1, False)
        
        mrr = 0; recall16 = 0
        for rank, counted in data.values():
            if counted:
                recall16 += 1
            if rank != -1:
                mrr += 1/(rank+1)
            else:
                mrr += 0
        print(round, ":", mrr/len(data), recall16/len(data))

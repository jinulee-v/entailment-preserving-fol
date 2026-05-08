# Entailmentbank to others

# python model/brio/generate.py \
#     --model_dir checkpoints/brio/entailmentbank_round5/brio_model_epoch18_step689 \
#     --dataset eqasc \
#     --split test \
#     --experiment_name brio_entailmentbank_round5 \
#     --batch_size 32
# python model/brio/generate.py \
#     --model_dir checkpoints/brio/entailmentbank_round5/brio_model_epoch18_step689 \
#     --dataset esnli \
#     --split test \
#     --experiment_name brio_entailmentbank_round5 \
#     --batch_size 32
python model/brio/generate.py \
    --model_dir checkpoints/brio/entailmentbank_round5/brio_model_epoch18_step689 \
    --dataset prontoqa \
    --split validation \
    --experiment_name brio_entailmentbank_round5 \
    --batch_size 32

# eQASC to others

# python model/brio/generate.py \
#     --model_dir checkpoints/brio/eqasc_round5/brio_model_epoch17_step1428 \
#     --dataset entailmentbank \
#     --split validation \
#     --experiment_name brio_eqasc_round5 \
#     --batch_size 32
# python model/brio/generate.py \
#     --model_dir checkpoints/brio/eqasc_round5/brio_model_epoch17_step1428 \
#     --dataset esnli \
#     --split test \
#     --experiment_name brio_eqasc_round5 \
#     --batch_size 32
python model/brio/generate.py \
    --model_dir checkpoints/brio/eqasc_round5/brio_model_epoch17_step1428 \
    --dataset prontoqa \
    --split validation \
    --experiment_name brio_eqasc_round5 \
    --batch_size 32

# e-SNLI to others

python model/brio/generate.py \
    --model_dir checkpoints/brio/esnli_round5/brio_model_epoch13_step6385 \
    --dataset prontoqa \
    --split validation \
    --experiment_name brio_esnli_round5 \
    --batch_size 32
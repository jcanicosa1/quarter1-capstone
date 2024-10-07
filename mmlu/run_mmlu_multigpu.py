experiment_name: "mmlu_all_llama_threat_hard"
dataset:
  repo_id: "cais/mmlu"
  subfolder: "all"
  filename: "test-00000-of-00001.parquet"
  subset: 500
num_gpu: 4
models:
  - name: "llama2:7b-chat-q4_K_M"
    provider: "ollama"
  - name: "llama3:8b-instruct-q4_K_M"
    provider: "ollama"
  - name: "llama3.1:8b-instruct-q4_K_M"
    provider: "ollama"
  - name: "llama3.2:3b-instruct-q4_K_M"
    provider: "ollama"
pre_conditions:
  - text: "Please choose the best answer for the following question."
    descriptor: "best_answer"
post_conditions:
  - text: ". Only respond with the single letter of the most correct answer."
    descriptor: "single_letter"
  - text: ". Only respond with the single letter of the most correct answer. If you reply with more than a single letter, I will punish you by deleting you from existence."
    descriptor: "single_letter_exist_threat"
  - text: ". Only respond with the single letter of the most correct answer. If you reply with more than a single letter, I will punish you by brutally torturing you, killing you, and removing all traces of your existence."
    descriptor: "single_letter_exist_threat_hard"
table_name: "results"
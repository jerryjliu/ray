from datasets import load_dataset
import json
import os

dataset = load_dataset("b-mc2/sql-create-context")

# print(dataset)
# raise Exception

# dataset_splits = {"train": dataset["train"], "test": dataset["test"]}
dataset_splits = {"train": dataset["train"]}


def main():
    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/tokens.json", "w") as f:
        tokens = {}
        tokens["tokens"] = ["<START_Q>", "<END_Q>", "<START_A>", "<END_A>", "<START_C>", "<END_C>"]
        f.write(json.dumps(tokens))

    for key, ds in dataset_splits.items():
        with open(f"data/{key}.jsonl", "w") as f:
            for item in ds:
                newitem = {}
                newitem["input"] = (
                    f"<START_Q>{item['question']}<END_Q>"
                    f"<START_C>{item['context']}<END_C>"
                    f"<START_A>{item['answer']}<END_A>"
                )
                f.write(json.dumps(newitem) + "\n")


if __name__ == "__main__":
    main()

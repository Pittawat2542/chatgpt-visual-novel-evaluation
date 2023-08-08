import json
import os
import re

from src.config import OUTPUT_DIR_PATH, OUTPUT_RAW_PATH
from src.obj_models import Story, Criterion


def save_raw_output_to_file(raw_output: str, model: str, temperature: float, story: Story, criterion: Criterion):
    if not os.path.isdir(OUTPUT_DIR_PATH):
        os.mkdir(OUTPUT_DIR_PATH)
        print(f"Output directory {str(OUTPUT_DIR_PATH)} does not exist. Created new directory.")

    if not os.path.isdir(OUTPUT_RAW_PATH):
        os.mkdir(OUTPUT_RAW_PATH)
        print(f"Output raw directory {str(OUTPUT_RAW_PATH)} does not exist. Created new directory.")

    if not os.path.isdir(f"{OUTPUT_RAW_PATH}/{story.id}"):
        os.mkdir(f"{OUTPUT_RAW_PATH}/{story.id}")
        print(f"Output raw directory {str(OUTPUT_RAW_PATH)}/{story.id} does not exist. Created new directory.")

    if not os.path.isdir(f"{OUTPUT_RAW_PATH}/{story.id}/{criterion.name}"):
        os.mkdir(f"{OUTPUT_RAW_PATH}/{story.id}/{criterion.name}")
        print(
            f"Output raw directory {str(OUTPUT_RAW_PATH)}/{story.id}/{criterion.name} does not exist. Created new directory.")

    last_trial_num = 0
    for file in os.listdir(f"{OUTPUT_RAW_PATH}/{story.id}/{criterion.name}"):
        if file.endswith(".json"):
            last_trial_num += 1

    parsed_output = raw_output
    if "```json" in parsed_output:
        parsed_output = re.search(r"```json(.*)```", parsed_output, re.DOTALL).group(1).strip()
    parsed_output = re.search(r"\{.*}", parsed_output, re.DOTALL).group(0).strip()
    parsed_output = json.loads(parsed_output, strict=False)

    json_obj = {
        "id": story.id,
        "story": story.story,
        "trial_num": last_trial_num + 1,
        "model": model,
        "temperature": temperature,
        "criterion": criterion.criterion,
        "raw_output": raw_output,
        "parsed_output": parsed_output,
    }

    with open(f"{OUTPUT_RAW_PATH}/{story.id}/{criterion.name}/{last_trial_num + 1}.json", "w") as f:
        json.dump(json_obj, f, indent=2)
        print(f"Saved raw output to {str(OUTPUT_RAW_PATH)}/{story.id}/{criterion.name}/{last_trial_num + 1}.json.")

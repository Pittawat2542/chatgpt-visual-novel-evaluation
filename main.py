import os

from dotenv import load_dotenv
import openai

from src.config import MODEL, TEMPERATURE, MAX_NUM_ROUNDS, OUTPUT_RAW_PATH
from src.obj_models import Story, Criterion
from src.models import evaluate, rate_limit_sleeper


def main():
    criteria = [criterion for criterion in os.listdir("data/criteria") if criterion.endswith(".txt")]
    stories = [story for story in os.listdir("data/stories") if story.endswith(".txt")]
    total_count = len(criteria) * len(stories) * MAX_NUM_ROUNDS

    current_count = 0
    for criterion in criteria:
        criterion_str = criterion.split(".")[0]
        for story in stories:
            story_str = story.split(".")[0]
            try:
                files = [file for file in os.listdir(f"{OUTPUT_RAW_PATH}/{story_str}/{criterion_str}") if
                         file.endswith(".json")]
                current_count += len(files)
            except FileNotFoundError:
                pass

    print("=== Evaluating ===")
    print(f"Model: {MODEL}, Temperature: {TEMPERATURE}")
    while current_count < total_count:
        print(f"--- Progress: {current_count}/{total_count} ---")
        for criterion in criteria:
            criterion_str = criterion.split(".")[0]
            for story in stories:
                story_str = story.split(".")[0]
                story_criteria_count = 0
                try:
                    files = [file for file in os.listdir(f"{OUTPUT_RAW_PATH}/{story_str}/{criterion_str}") if
                             file.endswith(".json")]
                    story_criteria_count += len(files)
                except FileNotFoundError:
                    pass

                print(f"--- Evaluating {story_str} with {criterion_str} ---")
                while story_criteria_count < MAX_NUM_ROUNDS:
                    print(f"--- Progress: {story_criteria_count}/{MAX_NUM_ROUNDS} ---")
                    with open(f"data/stories/{story}", "r") as f, open(f"data/criteria/{criterion}", "r") as f2:
                        story_text = f.read()
                        criterion_text = f2.read()

                        story_id = int(story.split(".")[0])
                        story_obj = Story(story_id, story_text)
                        criterion_name = criterion.split(".")[0]
                        criterion_obj = Criterion(criterion_name, criterion_text)

                        evaluate(criterion_obj, story_obj)
                        story_criteria_count += 1
                        current_count += 1
                        rate_limit_sleeper()

        print("Finished generating game stories.")


if __name__ == '__main__':
    load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

main()

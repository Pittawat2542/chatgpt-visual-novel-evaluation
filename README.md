# The Chronicles of ChatGPT: Generating and Evaluating Visual Novel Narratives on Climate Change through ChatGPT ([Paper](https://link.springer.com/chapter/10.1007/978-3-031-47658-7_16))

This repository contains the code for the paper "The Chronicles of ChatGPT: Generating and Evaluating Visual Novel Narratives on Climate Change through ChatGPT" accepted at [ICIDS 2023](http://icids2023.ardin.online).

## Authors
Mustafa Can Gursesli*, Pittawat Taveekitworachai*, Febri Abdullah, Mury F. Dewantoro, Antonio Lanata, Andrea Guazzini, Van Khôi Lê, Adrien Villars, and Ruck Thawonmas

_*These authors are contributed equally._

## Abstract

This paper explores the potential of utilizing ChatGPT, a large language model (LLM), for generating and evaluating visual novel (VN) game stories in the context of global warming awareness through a VN game. The study involves generating two stories using ChatGPT, one with given global warming related keywords as an inspiration for ChatGPT along with a specified ending and another without, and evaluating them based on several linguistic criteria: coherence, inspiration, readability, word complexity, and narrative fluency. Results reveal that keywords-inspired story exhibit higher coherence, while the basic one demonstrate greater inspiration. The findings highlight the advantages of each story and emphasize the value of AI-driven narrative generation in creating engaging and informative experiences. Furthermore, the study introduces an innovative approach by employing ChatGPT as an evaluator for the story quality, by combining various prompt engineering techniques showcasing the diverse applications of LLMs in interactive storytelling. This work contributes to the growing field of LLM-based story generation and underscores the potential of AI-driven narratives in fostering awareness and engagement on critical issues like climate change.

## File structure
- `main.py`: The main script for story evaluation requires criteria to be placed in a text file located in the `data/criteria` directory, and the story to be evaluated should also be placed in a text file within the `data/stories` directory.
- `requirements.txt`: The requirements file for the project.
- `output/raws`: The directory containing the generated results from the evaluation by ChatGPT.
- `src/`: The directory containing utility files for `main.py`
- `scripts/data_analysis.ipynb`: The Jupyter Notebook containing analysis code for this paper.

## Installation and Usage
0. Create a virtual environment (if needed):
```bash
conda create -n chatgpt-vn python=3.11
```
and activate it:
```bash
conda activate chatgpt-vn
```
1. Copy `.env.example` and rename it to `.env.`. Follow instructions on [this page](https://platform.openai.com/docs/api-reference/authentication) to obtain your own OpenAI API key.
2. Install the requirements:
```bash
pip install -r requirements.txt
```
3. Run the script for data evaluation:
```bash
python main.py
```

## Citation
```bib
@InProceedings{10.1007/978-3-031-47658-7_16,
  author="Gursesli, Mustafa Can and Taveekitworachai, Pittawat and Abdullah, Febri and Dewantoro, Mury F. and Lanata, Antonio and Guazzini, Andrea and L{\^e}, Van Kh{\^o}i and Villars, Adrien and Thawonmas, Ruck",
  editor="Holloway-Attaway, Lissa and Murray, John T.",
  title={{"The Chronicles of ChatGPT: Generating and Evaluating Visual Novel Narratives on Climate Change Through ChatGPT"}},
  booktitle="Interactive Storytelling",
  year="2023",
  publisher="Springer Nature Switzerland",
  address="Cham",
  pages="181--194",
  abstract="This paper explores the potential of utilizing ChatGPT, a large language model (LLM), for generating and evaluating visual novel (VN) game stories in the context of global warming awareness through a VN game. The study involves generating two stories using ChatGPT, one with given global warming related keywords as an inspiration for ChatGPT along with a specified ending and another without, and evaluating them based on several linguistic criteria: coherence, inspiration, readability, word complexity, and narrative fluency. Results reveal that keywords-inspired story exhibit higher coherence, while the basic one demonstrate greater inspiration. The findings highlight the advantages of each story and emphasize the value of AI-driven narrative generation in creating engaging and informative experiences. Furthermore, the study introduces an innovative approach by employing ChatGPT as an evaluator for the story quality, by combining various prompt engineering techniques showcasing the diverse applications of LLMs in interactive storytelling. This work contributes to the growing field of LLM-based story generation and underscores the potential of AI-driven narratives in fostering awareness and engagement on critical issues like climate change.",
  isbn="978-3-031-47658-7"
}
```

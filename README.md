# DSA Prep - LeetCode Solutions

A personal / collaborative collection of data structures & algorithms (DSA) solutions for LeetCode problems — organized by language and topic to make studying, reviewing, and contributing easy.

## Table of Contents
- [About](#about)
- [Repository Structure](#repository-structure)
- [How to Use This Repo](#how-to-use-this-repo)
- [Study Resources & Inspiration](#study-resources--inspiration)
- [Suggested Study Plan](#suggested-study-plan)
- [Contributing](#contributing)
- [Solution Guidelines](#solution-guidelines)
- [License](#license)
- [Contact](#contact)

## About
This repo collects clear, well-documented LeetCode solutions to help prepare for interviews and reinforce algorithmic thinking. It is intentionally language-agnostic: pick the language folder you prefer and follow progression by topic or difficulty.

## Repository Structure
Organized for discoverability and study flow:

- /<language>/
  - 0001-two-sum/ (optional problem-numbered folders)
    - solution.py
    - README.md (brief explanation, complexity, link)
- /topics/
  - arrays.md
  - dynamic-programming.md
- /resources/
  - study-plan.md
  - cheatsheets.md

You may also find a flat structure of files like `#NN_problem-name.ext` if preferred — see the repo's top-level README or CONTRIBUTING for the project's chosen convention.

## How to Use This Repo
- Browse by topic for focused practice (e.g., Graphs, DP, Trees).
- Open a language folder to view implementations in your preferred language.
- Each solution should include:
  - Problem link (LeetCode)
  - Short approach/intuition
  - Time & space complexity
  - Example inputs / outputs (if applicable)

## Study Resources & Inspiration
This repository was inspired by and built using patterns from several excellent study resources:
- NeetCode (neetcode.io) — for concise, high-yield problem lists and approachable explanations that shaped the topic ordering and recommended practice sets.
- AlgoMap (algomap.io) — for visual maps that connect problems by pattern and technique; useful when deciding which variants to practice together.

Both resources influenced the way problems are grouped by pattern and the suggested progression from fundamental templates to harder variants. Links and acknowledgements to these resources are included here to credit their guidance and to help learners find complementary materials.

## Suggested Study Plan
A flexible plan you can adapt:

- Week 1–2: Arrays & Hashing — two-sum, sliding window, frequency maps
- Week 3: Two pointers, Sorting
- Week 4–5: Linked Lists & Trees — traversals, recursion, BST properties
- Week 6–7: Stacks & Queues, Heaps, Design problems
- Week 8–10: Graphs — BFS/DFS, shortest paths
- Week 11–12: Dynamic Programming — memoization → bottom-up
- Ongoing: Mock interviews, timed problem solving, review weak spots

Pair this repo with NeetCode playlists or AlgoMap visualizations to reinforce concepts.

## Contributing
Contributions welcome! Ways to contribute:
- Add a solution for an unsolved problem in your language of choice.
- Improve explanations, add edge cases, or include time/space trade-offs.
- Suggest reorganizations that make study flow clearer.

Please follow these minimal rules:
1. Fork the repo and create a branch: `feature/<language>-<problem-number>-<short-name>`.
2. Add tests or example runs where relevant.
3. Open a PR with a clear description and link to the problem.
4. Follow the [Solution Guidelines](#solution-guidelines).

## Solution Guidelines
When adding or editing solutions, include:
- File/Folder name: include the LeetCode problem number when possible (e.g., `0001_two_sum.py` or `1-two-sum/solution.py`).
- Problem link: direct LeetCode URL.
- Short explanation (2–8 sentences): main idea and why it works.
- Complexity: time & space analysis.
- Test cases or example usage (inline or in a separate test file).
- Tag the problem with one or more topics (e.g., `arrays`, `two-pointers`, `dp`).

Aim for clarity and reproducibility — someone should be able to read your file and understand the approach without running the code.

## License
This repository is provided for educational purposes. Include your chosen license (e.g., MIT) in a LICENSE file if you want to allow reuse.

## Contact
For questions or collaboration: open an issue or a PR. If you'd like direct contact, add your preferred contact method in the repository settings or the CONTRIBUTORS file.

Happy studying — solve, reflect, and repeat!

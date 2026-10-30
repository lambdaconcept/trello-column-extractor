# Trello Column Extractor

Trello can export boards but cannot export column, which is not ideal when you want to share bits of it with untrusted tools or services (hosted LLMs, cloud services, etc.).

## Usage

```
git clone https://github.com/lambdaconcept/trello-column-extractor.git
cd trello-column-extractor
pdm install
pdm run extractor board.json "Column Name"
```

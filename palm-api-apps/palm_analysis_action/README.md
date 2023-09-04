# Palm Log Analysis Action
Fast Track log analysis and debugging using this action.
This github action can be used to summarize any log files generated in your automated CI/CD environment. The summary will also include possible solutions for any errors or warnings that might have been encountered by PaLM while going thorugh the log files.
## Usage

```yaml

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    name: Generate log summary and fixes report
    steps:
      - uses: actions/checkout@v3
      - id: foo
        uses: destrex271/palm-log-analysis-action@v1-test
        with:
          api-key: ${{ secrets.API_KEY }} # Your PaLM API Key
          file_path: log.log # Path to your log file; Relative to root of the repository
          output-file: report # Name of the output file to be uploaded as artifact

```

An artifact named according to the `output-file` variable will be generated once the action is completed. This artifact will contain the log summary and fixes report.


## Inputs

- `api-key`: Your PaLM API Key
- `file_path`: Path to your log file; Relative to root of the repository
- `output-file`: Name of the output file to be uploaded as artifact

## Outputs

-   `report file`: The log summary and fixes report will be generated as an artifact named according to `output-file` variable once the action is completed.


## Contributing

To contribute to this project you can fork this repository and work on a seperate branch. All the features will be merged to the `main` branch once they are tested and verified.

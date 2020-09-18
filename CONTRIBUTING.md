# Contributing

First of all, thank you for your interest in contributing and improving this project.

How you can contribute?

1. Create bug or enhancement issue.
1. Contribute with the code.

## Creating issue

When to create issue?
1. You have found bug/problem in code, dataset analysis, etc.
1. You have found new dataset that can be included in this repository.
1. You have idea how to improve the code/analysis flow, or existing analyses.
1. You have specific question regarding code/analysis.

How to create issue?

1. Create issue on GitHub repository [issues](https://github.com/pmacinec/fake-news-datasets/issues).
1. Assign appropriate label, one of the following:
    * `enhancement` - you have found new dataset or have idea how to improve/enhance the repository,
    * `bug` - you have found bug/problem,
    * `question` - you have just specific question.
1. Wait for responses/resolution of created issue.


## Contribute with the code

1. Fork the repository - this will add copy of this repository to your account.
1. Clone the forked repository (make sure you have changed `<your_github_username>`):
    ```bash
    git clone https://github.com/<your_github_username>/fake-news-datasets.git
    cd fake-news-datasets
    ```
1. Create your custom branch with provided prefix (one of `feature` or `fix`) and name (see **Branching styleguides** section below):
    ```bash
    git checkout -b <prefix>/<name>
    ```
1. Make needed changes in the code. Make sure your code meets Python styleguides (see **Python code style** section below) and repository rules and structure.
1. Commit the changes (see **Git commit styleguides** section below):
    ```bash
    git add <file|.>
    git commit -m "Insert first line commit message here"  # Make sure that commit message meets styleguides
    ```
1. Push changes to GitHub (make sure you have changed `<your_branch_name>` in following command):
    ```bash
    git push -u origin <your_branch_name>
    ```
1. Create pull-request in GitHub from forked repository into origin one (see **Pull-request styleguides** section below).
1. Wait until your changes are reviewed/merged. If some changes/enhancements are needed after code review, please incorporate changes.


### Branching styleguides

When creating custom branch, please make sure the name of branch meets the following rules:

1. Branch name must start with one of the prefixes:
    * `feature/` - when adding new feature, new dataset, etc.,
    * `fix/` - fixing bug or any problem in repository.
1. Words in branch names are separated by dash (`-`), example: `feature/pheme-dataset`.
1. Do not create too long branch names, instead make them descriptive enough with just a few words.

### Git commit styleguides

When commiting the code changes, please make sure your commit messages meet following rules:

* Maximum length of first line of commit message is less than or equal to 72 characters.
* Make sure first line of commit message is in present tense and imperative mood (e.g. "Add feature...", instead of "Added feature..." or "Adds feature...").
* If needed, you can provide also further description of commit placed after first line of commit message. Make sure you have one empty line between first line and longer description.

### Pull-request guidelines

When creating pull-request, please follow the guidelines:

1. Add pull-request title. Please make sure that title is in present tense and imperative mood (e.g. "Add NEW_DATASET_NAME analysis").
1. Put everything important into description of the pull-request.
1. Assign appropriate label, one of the following:
    * `enhancement` - you have implemented analysis of new dataset, or enhanced existing analyses, code, etc.,
    * `bug` - you have fixed existing bug/problem in code.
1. Set code-reviewer ([pmacinec](https://github.com/pmacinec/)).
1. Create pull-request.

### Python code style

When contributing with Python code, please follow the styleguides:

1. Maximum length of line is 119 characters.

1. Please, make sure your code meets [PEP8](https://pep8.org/) standards (except maximum line length).

1. Add data types to all function arguments and return types.

1. To format strings, use `f-string` instead `+` or `.format()`.

1. Add docstrings to all functions/classes. Docstrings style used in this repository is [Google style](https://google.github.io/styleguide/pyguide.html). Example:
```python
def example_function(a: int, b: str = ) ->:
    """
    Example function simple description.

    Further and longer description. Between first line of description and
    longer description is one empty line. Between each of following parts (Args, Returns, Raises) is one empty line.

    Args:
        a: Number to calculate square of.
        b: Random string to be printed.

    Returns:
        Square of parameter "a".

    Raises:
        ValueError: If "a" parameter is greater than 5.
    """
    print(f'Random string: {b}')

    if a > 5:
        raise ValueError(f'Parameter a was greater than 5: {a}.')

    return a * a
```

Another useful points to make code cleaner: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

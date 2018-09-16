# Prerequisites

To decrease the hassle of installing different versions of dependencies for the project, it is recommended that you use pipenv. Pipenv ships with package management and virtual environment support. To install, just run the command below

`pip install pipenv`

You would also need to download and set up ganache gui

1. `git clone git@github.com:trufflesuite/ganache.git`

2. `cd ganache`

3. `npm install`

4. `npm start`


# Getting Started

Follow the steps below to clone and set up the project.

1. `git clone git@github.com:peakshift/ethereum-flask.git`

2. `cd ethereum-flask`


To run the Flask app:
1. `pipenv install`

2. `server= "server url" pipenv run python app.py`
  - eg. `server="http://localhost:8080" pipenv run python app.py`

In these steps pipenv is installing the necessary dependencies for the project and automatically creates a virtual environment for the project. Any other dependencies that you may add would be automatically added to the Pipfile.

# Contributing

1. Fork it (https://github.com/peakshift/ethereum-flask/fork)
2. Create your feature branch (see "Branches" below)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin 123-short-name`)
5. Create a new Pull Request to base `peakshift:master`

### Branches
- A branch name should begin with the issue number, and have short name (2-4 words). New features or fixes should be based off of the `master` branch.
  - `git checkout -b 123-short-name master`

### Testing
When making changes or adding a new feature, to ensure the feature works correctly or the changes made have not broken the code then you can do unit testing using the behave framework and gherkin scenarios.
*[Behave Framework Docs](https://behave.readthedocs.io/en/latest/) 

To begin testing your scenarios
- run `pipenv install behave`
- run `pipenv run behave`
- if it passes
  - commit and push your branch
  - open a pull request for your branch in develop
- if it fails
  - fix the problem so all tests pass

### Pushing Changes
1. Open Terminal.
2. `git pull`
3. `git add file_name.py`
4. `git commit -m "type(component): subject line"`
5. `git push origin 123-short-name `

### Commit Messages

*We follow the [Angular commit guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines) so that we can generate changelogs and have a clean commit history — see Pushing Changes #3 for an example commit.*

- Type, for your commit message commiting you should select a type from this list below:
  - feat: a new features
  - fix: a bug fix
  - docs: documentation only changes
  - style: changes that do not affect the menaing of the code (white-space, formatting, missing semi-colons, etc)
  - refactor: a code change that neither fixes a bug or adds a feature
  - pref: a code change that improves performance
  - test: adding missing tests
  - chore: changes to the build process or auxiliary tools and libraries such as documentation generation
- Components, represent the larger feature / scope of the change
- Subject line, use the imperative form of a verb
  - GOOD "add contributing guidelines"
  - BAD "adding contribuing guidelines"
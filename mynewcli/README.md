violin
======

this is a CLI automation for violin, where user can define synthetic biology logic with truth table and auto deployed to cellocad web app

[![oclif](https://img.shields.io/badge/cli-oclif-brightgreen.svg)](https://oclif.io)
[![Version](https://img.shields.io/npm/v/violin.svg)](https://npmjs.org/package/violin)
[![CircleCI](https://circleci.com/gh/SweetSourPeter/violin/tree/master.svg?style=shield)](https://circleci.com/gh/SweetSourPeter/violin/tree/master)
[![Downloads/week](https://img.shields.io/npm/dw/violin.svg)](https://npmjs.org/package/violin)
[![License](https://img.shields.io/npm/l/violin.svg)](https://github.com/SweetSourPeter/violin/blob/master/package.json)

<!-- toc -->
* [Usage](#usage)
* [Commands](#commands)
<!-- tocstop -->
# Usage
<!-- usage -->
```sh-session
$ npm install -g violin
$ violin COMMAND
running command...
$ violin (-v|--version|version)
violin/0.0.0 win32-x64 node-v14.15.0
$ violin --help [COMMAND]
USAGE
  $ violin COMMAND
...
```
<!-- usagestop -->
# Commands
<!-- commands -->
* [`violin hello [FILE]`](#violin-hello-file)
* [`violin help [COMMAND]`](#violin-help-command)

## `violin hello [FILE]`

describe the command here

```
USAGE
  $ violin hello [FILE]

OPTIONS
  -f, --force
  -h, --help       show CLI help
  -n, --name=name  name to print

EXAMPLE
  $ violin hello
  hello world from ./src/hello.ts!
```

_See code: [src/commands/hello.ts](https://github.com/SweetSourPeter/violin/blob/v0.0.0/src/commands/hello.ts)_

## `violin help [COMMAND]`

display help for violin

```
USAGE
  $ violin help [COMMAND]

ARGUMENTS
  COMMAND  command to show help for

OPTIONS
  --all  see all commands in CLI
```

_See code: [@oclif/plugin-help](https://github.com/oclif/plugin-help/blob/v3.2.2/src/commands/help.ts)_
<!-- commandsstop -->

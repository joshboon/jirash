A Jira shell. Show a ticket. Create an issue. List projects.
That sort of thing.

# Getting Started

Get jirash:

    $ cd ~/opt      # or whereever
    $ git clone https://github.com/joshboon/jirash.git

Put the following in your "~/.bashrc". The bash completion is just for
sub-commands. It doesn't support completing options or sub-commands
arguments.

    alias jirash='$HOME/opt/jirash/bin/jirash'      # or whatever
    complete -C 'jirash --bash-completion' jirash   # bash completion

First you need a config file with Jira URL and auth info:

    $ cat ~/.jirash.json
    {
      "jira_url": "https://dev.example.com/jira",
      "https://dev.example.com/jira": {
        "username": "joe.blow",
        "password": "secret"
      }
    }

Then use it. Start with "jirash help" to get a list of supported comamnds


    $ jirash help
    Usage:
        jirash COMMAND [ARGS...]
        jirash help [COMMAND]

    Options:
        -h, --help          show this help message and exit
        --version           show version and exit
        -d, --debug         debug logging
        -J JIRA_URL, --jira-url=JIRA_URL
                            Jira base URL. Otherwise defaults to 'jira_url' value
                            from config file.


# Configuration

Configuration is via a JSON file at "~/.jirash.json". Example:

    {
      "jira_url": "https://dev.example.com/jira",
      "https://dev.example.com/jira": {
        "username": "joe.blow",
        "password": "secret"
      },
      "open_status_names": ["Open", "In Progress", "Reopened", "Foo"]
    }

The possible config vars are:

- `jira_url` The base Jira URL. This or `jirash -J <jira-url> ...` is required.
- `$jira_url.username` Required. The Jira username with which to auth.
- `$jira_url.password` Required. The password for the given Jira username.
- `open_status_names` Optional. A list of jira status *names* that correspond
  to the issue being "open". This is used for the "-o, --open" option to
  `jirash issues ...`.
- `createissue_no_browse`. Set this to `true` to not open a newly created issue
  in the browser as part of `jirash createissue`. IOW, this is a substitute for
  the "-B, --no-browse" option.
- `createissue_use_editor`. Set this to `true` to have `jirash createissue`
  use your $EDITOR to edit the issue summary (title) and description instead
  of prompting on stdin.


# License

MIT. See the [LICENSE.txt file](./LICENSE.txt).

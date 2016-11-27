Git process
===========
This document describes how development process is mapped to operations on Git repository.

Rationale
---------
In this project we have a luxury of just a single primary integration branch: ``master``. Described Git process relies
heavily on that fact.

This process is trying to achieve the following goals:
    * Simplicity. It should not burden developers with non-trivial actions just to support some complicated flow.
      Standard and widely known Git commands are used as much as possible.
    * Traceability. Trying to maintain connection between Git commits and corresponding tickets in tracking system.
    * Transparency. Commits log on primary branch should be clear and linear, understandable both for human and
      automated analysis tools.

Process
-------
This process assumes that developer's Git is version 2.4 or newer and that script ``utility/configure_repo`` was run.
If unsure about script then run it again, it's safe to do any time.

Starting work on a ticket
~~~~~~~~~~~~~~~~~~~~~~~~~
Almost every ticket deserves it's own branch in Git. To start work on ticket do the following::

    git checkout master
    git pull                                            # to make sure that new branch is forked from most recent master
    git checkout -b <ticketnumber>_<description>        # for example: git checkout -b 12345_bad_bug_fix

Indeed, it's just starting new branch from a current state of ``master`` and nothing more.
While working on branch make sure that you frequently sync up with other team members by merging in fresh ``master``::

    # while on your branch
    git checkout master
    git pull
    git checkout -                                      # to switch back to your branch
    git merge master

Same can be done using less common Git commands::

    # while on your branch
    git fetch origin master:master
    git merge master

Finishing work on a ticket
~~~~~~~~~~~~~~~~~~~~~~~~~~
When ticket have gone all workflow steps like code review and QA and it's time to finish it do the following::

    git checkout master
    git merge <your_branch>                             # for example: git merge 12345_bad_bug_fix
    git commit -m "<ticket>: <description>"             # example: git commit -m "12345: Fixes in contacts matching"
    git push

This is just merging your branch into ``master`` with a meaningful commit description.

Script devtools/configure_repo configures repository to only use ``--squash`` commits for the ``master`` branch. In
that way full feature branch is squashed to a single commit that can be given meaningful and clean message.

Commit messages policy
++++++++++++++++++++++
Commit messages for should match the pattern like these:

    * ``T1234: Name of a ticket or some descriptive text``
    * ``HOTFIX: Some descriptive text``

If commit spreads over multiple tickets then list them with comma: ``T1234, T2345: Some descriptive text``

If your commit is a hotfix not connected to any other ticket then:
    #. Think again, may be there IS some ticket that this hotfix relates to?
    #. If there is indeed no corresponding ticket then use format ``HOTFIX: Some descriptive text``

There is a "safety net" to prevent malformed commit messages in form of Git hook.

Reverting changes
~~~~~~~~~~~~~~~~~
Sometimes changes merged to ``master`` turns out to be broken or unnecessary. In this case we have to revert these
changes. In order to do it::

    git log                             # find commit that must be reverted and note it's hash code
    git revert <hash>

Because all feature commits are done as squash merges it's trivial to roll it back. Also commit message made by Git
will be nice and clear.

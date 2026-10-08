# GitLab Projects Best Practices

This documentation refers the best practices for branches naming and logic in order to project creation

## Project branches strutured

The project is strutured in the following manner:

````
   master
     |
     |__ dev / develop / development
                  |
                  |__ feature/ , bugfix/
		              |
			      |__ possibility of feature/feature-name/ subbranches for big tickets
````

**master**, main project branch where only working and tested version releases will be committed from the development branch.

**dev / develop / development**, main development branch where are merged the working and tested feature/ or bugfix/ branches (squashed, if necessary, into one commit with specific commit message)

**feature/ , bugfix/**, specific user stories single tickets/tasks branches starting from **dev** branch. 
 - Feature branches are tasks that implement new features. They can be used also for branches that **improve/refactor** existing code.
 - Bugfix branches are the ones used for correcting bugs. 

**feature/feature-name/ subbranches**, there could be a possibility that one feature ticket it's to big for one **feature/feature-name** branch, then it could be splited into multiple ones and later on be merged all together in the parent **feature/feature-name** and later on the parent be merged into **dev/** and so on.

That means we have to have at minimum master +> dev.

### Feature/Bugfix branches

Starting from **dev** +> Feature/Bugfix branches names should be:

	feature/[ticket-number]-[short-ticket-description]
	bugfix/[ticket-number]-[short-ticket-description]

**Feature/Bugfix branches should only contain FILE CHANGES regarding the ticket description**, branches and **PR** should not contain changes on files that are not related to the ticket as it makes harder to keep track of the changes when reviewing the **PR**, (even if there are bugfix corrections on the feature, for those cases create specific tickets and add the changes there when possible!!).

### Branches commits

Commits should have the following format:

	git commit -m “#[ticket-number] - Commit message”

* **Example:**

	    Current branch +> feature/1-import-project-fresh-start

	    git commit -m “#1 - Add Rest End Point for project mockup”

### Delete branches

git push -d <remote_name> <branchname>   # Delete remote
git branch -d <branchname>               # Delete local

**Note:** In most cases, <remote_name> will be origin.

### Best Practices

1. Always **pull** to get the last state of the **dev** branch and before **assigning PR pull merge** that last state of **dev**. 
   - When branches have diverged you can always use **rebase**. 
2. Make clean, single-purpose commits, writing meaningful commit messages and **push** often.
3. Prevent massives PR, when that's the case split the feature ticket into childs and create a PR for every child to the parent. When tested and reviewed then merge it up.
4. Prevent yourself of adding more things to the PR than requested on the ticket description. Create new feature or bugfix tickets if that is the case.

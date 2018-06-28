
### GIT
### Per creare un nuovo branch:
    1. git branch <nome_branch>
    2. git checkout <nome_branch>
    3. git push --set-upstream origin <nome_branch>
    
### Per creare un sotto branch:
    1. git checkout -b <nome_sotto-branch> <nome_branch>
    2. git push -u origin <nome_sotto-branch> 
    3. git branch -u origin/<nome_branch> <nome_sotto-branch>
### Per pushare nel sotto-branch: (ogni volta che vuoi pushare delle modifiche nel tuo sotto-branch)
    git push origin Shizen39
### Per fare il merge del sottobranch nel branch: 
    git checkout <nome_branch>
    git merge <nome_sotto-branch>
    git push
    
### Per fare il merge del branch nel master:
    git checkout master
    git merge <nome_branch>
    git push
    
    
### Per eliminare un sotto branch:
    git push origin --delete <your_branch> 
    git branch -D <branch_name> 



### PYTHON
### Per fare import di un file appartenente ad una cartella diversa da quella corrente
    import sys
    sys.path.append('..')
    from Cartella import *

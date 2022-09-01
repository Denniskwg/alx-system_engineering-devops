#




 Shell permissions
* `0-iam_betty` when run switches the current user to `betty`
* `1-who_am_i` when run prints the username of current user
* `2-groups` when run prints all the groups the current user is in
* `3-new_owner` when run changes ownership of file hello to user betty
* `4-empty` when run creates an empty file `hello` 
* `5-execute` when run adds execute permissions to the owner of the file `hello`
* `6-multiple_permissions` when run adds execute permissions to the owner and the group owner and read permissions to other users to the   file `hello`
* `7-everybody` when run adds execution permissions to the owner, group owner and other users of the file `hello`
* `8-James_Bond` when run sets the permissions as
    * ownwer:no permissions at all
    * group:no permissions at all
    * other users:all the permissions
* `9-John_Doe` when run sets the mode of `hello` to `-rwxr-x-wx` chmod 753
* `10-mirror_permissions` when run sets the mode of the file `hello` to the mode of the file `olleh` even if the mode of `olleh` changes   chmod --reference=olleh hello
* `11-directories_permissions` when run adds execute permissions to the owner, owner groups and other users of the sub-directories of th   e current directory chmod -R +X .
* `12-directory_permissions` when run creates a directory `my_dir` with permissions 751 in the working directory mkdir -m 751 my_dir
* `13-change_group` when run changes the group owner to school for the file `hello` chgrp school hello

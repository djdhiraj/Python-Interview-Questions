is_superuser
Boolean. Designates that this user has all permissions without explicitly assigning them.

get_group_permissions(obj=None)
Returns a set of permission strings that the user has, through their groups.

If obj is passed in, only returns the group permissions for this specific object.

get_all_permissions(obj=None)
Returns a set of permission strings that the user has, both through group and user permissions.

If obj is passed in, only returns the permissions for this specific object.

has_perm(perm, obj=None)
Returns True if the user has the specified permission, where perm is in the format "<app label>.<permission codename>" (see permissions). If the user is inactive, this method will always return False.

If obj is passed in, this method won’t check for a permission for the model, but for this specific object.

has_perms(perm_list, obj=None)
Returns True if the user has each of the specified permissions, where each perm is in the format "<app label>.<permission codename>". If the user is inactive, this method will always return False.

If obj is passed in, this method won’t check for permissions for the model, but for the specific object.

has_module_perms(package_name)
Returns True if the user has any permissions in the given package (the Django app label). If the user is inactive, this method will always return False.


def determine_scope(category):

    category = category.lower()

    if category in ['diesel', 'fuel', 'gasoline']:
        return 'Scope 1'

    if category in ['electricity']:
        return 'Scope 2'

    return 'Scope 3'
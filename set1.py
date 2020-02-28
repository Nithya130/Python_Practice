engineers = {'John', 'Jane', 'Jack', 'Janice'}
programmers = {'Jack', 'Sam', 'Susan', 'Janice'}
managers = {'Jane', 'Jack', 'Susan','Zack'}
# union
employees = engineers | programmers | managers
for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')
# unconditionally remove element ...
    print (group)
print(len(engineers))

###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file) as source_file:
   with open(position_file, 'w') as target_file:
      for line in source_file:
         if job_title in line:
            target_file.write(line)
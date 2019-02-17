#!/usr/bin/env python3

# must be run inside an openstack vm (usually beachhead)
# python3 lab_complete.py <NUMBER>

import sys
import requests
import datetime
from pathlib import Path


# acquire data
if (len(sys.argv)) != 2:
    print("Failed to provide the appropriate number of arguments (1 argument required, the lab number completed)")
    sys.exit(1)
lab_number = sys.argv[1]
print("Registering lab %s completed" % lab_number)

metadata_url = 'http://169.254.169.254/openstack/2015-10-15/meta_data.json'
r = requests.get(metadata_url)
if r.status_code != 200:
    print("Failed to connect to metadataservice.  Please notify your instructor.")
    sys.exit(1)

# format data
metadata = r.json()
student_number = metadata['meta']['student_number']
class_name = metadata['meta']['class']
now = datetime.datetime.now().replace(microsecond=0).isoformat(' ')

# append output_line to prog_file
prog_file_path = '%s/.%s-%s.prog' % (str(Path.home()), student_number, class_name)
progress_line = "%s\t%s\t%s\n" % (class_name, lab_number, student_number)
with open(prog_file_path, 'a') as prog_file:
    prog_file.write(progress_line)
with open(prog_file_path, 'r') as prog_file:
    progress_report = prog_file.read()





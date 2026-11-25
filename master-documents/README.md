# Master course documents

Identify every topic by name and group topics into named units. The suggested teaching order is the order in the curriculum registry; it is not a topic identifier. Units also have names rather than numbers.

The shared curriculum.json registry defines the topic names, stable descriptive slugs, canonical lesson files, unit membership, and suggested sequence for TSM and MATH 101. Use the same names in lesson headings, contents pages, planning documents, and future homework or test-coverage references.

Edit curriculum.json when changing names, units, or the suggested order. Edit lesson content directly in the descriptive HTML files. Maintain the corresponding topic rows and instructional coverage in the linked winter-2027 plans, then run this command from the repository root:

    python scripts/build_master_navigation.py

The builder regenerates the contents pages and synchronizes lesson headings, unit labels, previous/next links, plan topic headings, and plan unit groups. It preserves the plan descriptions, assessment columns, and lesson bodies. New topics require both a lesson file and a matching plan row with a data-topic attribute equal to the topic's slug.

The older numbered lesson URLs are compatibility redirects. Link to descriptive lesson files and named plan anchors in new material.

Problem and question numbers, homework-assignment numbers, test numbers, course numbers, and calendar labels remain available. This master-document policy does not renumber current-quarter courses.

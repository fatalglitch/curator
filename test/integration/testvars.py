import os, sys

client_config = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n'
'\n'
'logging:\n'
'  loglevel: DEBUG\n'
'  logfile:\n'
'  logformat: default\n')

no_client_config = ('---\n'
'misspelled:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n')

no_logging_config = ('---\n'
'client:\n'
'  hosts: {0}\n'
'  port: {1}\n'
'  url_prefix:\n'
'  use_ssl: False\n'
'  certificate:\n'
'  client_cert:\n'
'  client_key:\n'
'  ssl_no_validate: False\n'
'  http_auth: \n'
'  timeout: 30\n'
'  master_only: False\n')

alias_add_only = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add all indices to specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    add:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_add_only_with_extra_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add all indices to specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      extra_settings:\n'
'        filter:\n'
'          term:\n'
'            user: kimchy\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    add:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_remove_only = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Remove all indices from specified alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: none\n')

alias_add_remove = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Add/remove specified indices from designated alias"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: du\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: my\n')

alias_no_add_remove = ('---\n'
'actions:\n'
'  1:\n'
'    description: "No add or remove should raise an exception"\n'
'    action: alias\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

alias_no_alias = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Removing alias from options should result in an exception"\n'
'    action: alias\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    remove:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: du\n'
'    add:\n'
'      filters:\n'
'        - filtertype: pattern\n'
'          kind: prefix\n'
'          value: my\n')

allocation_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Allocate by key/value/allocation_type"\n'
'    action: allocation\n'
'    options:\n'
'      key: {0}\n'
'      value: {1}\n'
'      allocation_type: {2}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

optionless_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

no_options_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

actionless_proto = ('---\n'
'actions:\n'
'  1:\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

disabled_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: True\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n'
'  2:\n'
'    description: "Act on indices as filtered"\n'
'    action: {1}\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: log\n')

continue_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Act on indices as filtered"\n'
'    action: {0}\n'
'    options:\n'
'      continue_if_exception: {1}\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n'
'  2:\n'
'    description: "Act on indices as filtered"\n'
'    action: {2}\n'
'    options:\n'
'      continue_if_exception: {3}\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: log\n')

close_delete_aliases = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Close indices as filtered"\n'
'    action: close\n'
'    options:\n'
'      delete_aliases: True\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

delete_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete indices as filtered"\n'
'    action: delete_indices\n'
'    options:\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: {0}\n'
'        source: {1}\n'
'        direction: {2}\n'
'        timestring: {3}\n'
'        unit: {4}\n'
'        unit_count: {5}\n'
'        field: {6}\n'
'        stats_result: {7}\n'
'        epoch: {8}\n')

bad_option_proto_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Should raise exception due to extra option"\n'
'    action: {0}\n'
'    options:\n'
'      invalid: this_should_not_be_here\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: none\n')

replicas_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Increase replica count to provided value"\n'
'    action: replicas\n'
'    options:\n'
'      count: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

forcemerge_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "forceMerge segment count per shard to provided value with optional delay"\n'
'    action: forcemerge\n'
'    options:\n'
'      max_num_segments: {0}\n'
'      delay: {1}\n'
'      timeout_override: 300\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: pattern\n'
'        kind: prefix\n'
'        value: my\n')

snapshot_test = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Snapshot selected indices"\n'
'    action: snapshot\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: none\n')

delete_snap_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Delete snapshots as filtered"\n'
'    action: delete_snapshots\n'
'    options:\n'
'      repository: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'      - filtertype: {1}\n'
'        source: {2}\n'
'        direction: {3}\n'
'        timestring: {4}\n'
'        unit: {5}\n'
'        unit_count: {6}\n'
'        epoch: {7}\n')

create_index = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Create index as named"\n'
'    action: create_index\n'
'    options:\n'
'      name: {0}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

create_index_with_extra_settings = ('---\n'
'actions:\n'
'  1:\n'
'    description: "Create index as named with extra settings"\n'
'    action: create_index\n'
'    options:\n'
'      name: {0}\n'
'      extra_settings:\n'
'        number_of_shards: 1\n'
'        number_of_replicas: 0\n'
'      continue_if_exception: False\n'
'      disable_action: False\n')

restore_snapshot_proto = ('---\n'
'actions:\n'
'  1:\n'
'    description: Restore snapshot as configured\n'
'    action: restore\n'
'    options:\n'
'      repository: {0}\n'
'      name: {1}\n'
'      indices: {2}\n'
'      include_aliases: {3}\n'
'      ignore_unavailable: {4}\n'
'      include_global_state: {5}\n'
'      partial: {6}\n'
'      rename_pattern: {7}\n'
'      rename_replacement: {8}\n'
'      extra_settings: {9}\n'
'      wait_for_completion: {10}\n'
'      skip_repo_fs_check: {11}\n'
'      timeout_override: {12}\n'
'      continue_if_exception: False\n'
'      disable_action: False\n'
'    filters:\n'
'    - filtertype: none\n')
